# -*- coding: utf-8 -*-

import logging
import sys
from ucloud import version
from ucloud.core.client._cfg import Config
from ucloud.core.transport import Transport, RequestsTransport, Request, Response
from ucloud.core.utils import log
from ucloud.core.utils.middleware import Middleware
from ucloud.core import auth, exc

default_transport = RequestsTransport()


class Client(object):
    def __init__(self, config, transport=None, middleware=None, logger=None):
        cfg, cred = self._parse_dict_config(config)
        self.config = cfg
        self.credential = cred
        self.transport = transport or default_transport
        self.logger = logger or log.default_logger
        if middleware is None:
            middleware = Middleware()
            middleware.response(self.logged_response_handler)
            middleware.request(self.logged_request_handler)
        self._middleware = middleware

    def invoke(self, action, args=None, **options):
        """ invoke will invoke the action with arguments data and options

        :param str action: the api action, like `CreateUHostInstance`
        :param dict args: arguments of api(action), see doc: `UCloud API Documentation <https://docs.ucloud.cn/api>`__
        :return:
        """
        retries = 0
        max_retries = options.get("max_retries") or self.config.max_retries
        while retries <= max_retries:
            try:
                return self._send(action, args or {}, **options)
            except exc.UCloudException as e:
                if e.retryable and retries != max_retries:
                    logging.info(
                        "Retrying {action}: {args}".format(action=action, args=args)
                    )
                    retries += 1
                    continue
                raise e
            except Exception as e:
                raise e
        raise exc.RetryTimeoutException("max retries is reached")

    @property
    def middleware(self):
        return self._middleware

    def logged_request_handler(self, req):
        self.logger.info("[request] {} {}".format(req.get("Action", ""), req))
        return req

    def logged_response_handler(self, resp):
        self.logger.info("[response] {} {}".format(resp.get("Action", ""), resp))
        return resp

    def __enter__(self):
        yield self

    @staticmethod
    def _parse_dict_config(config):
        return Config.from_dict(config), auth.Credential.from_dict(config)

    def _send(self, action, args, **options):
        args["Action"] = action
        for handler in self.middleware.request_handlers:
            args = handler(args)
        req = self._build_http_request(args)
        max_retries = options.get("max_retries") or self.config.max_retries
        timeout = options.get("timeout") or self.config.timeout
        resp = self.transport.send(req, timeout=timeout, max_retries=max_retries).json()
        for handler in self.middleware.response_handlers:
            resp = handler(resp)
        if int(resp.get("RetCode", -1)) != 0:
            raise exc.RetCodeException(
                action=req.json.get("Action"),
                code=int(resp.get("RetCode")),
                message=resp.get("Message"),
            )
        return resp

    def _build_http_request(self, args):
        payload = {"Region": self.config.region, "ProjectId": self.config.project_id}
        payload.update({k: v for k, v in args.items() if v is not None})
        payload["Signature"] = self.credential.verify_ac(payload)
        return Request(
            url=self.config.base_url,
            method="post",
            json=payload,
            headers={
                "User-Agent": self._build_user_agent(),
                "Content-Type": "application/json",
            },
        )

    def _build_user_agent(self):
        python_version = "{v[0]}.{v[1]}.{v[2]}".format(v=sys.version_info)
        user_agent = "Python/{python_version} Python-SDK/{sdk_version}".format(
            python_version=python_version, sdk_version=version.version
        ) + (self.config.user_agent or "")
        return user_agent
