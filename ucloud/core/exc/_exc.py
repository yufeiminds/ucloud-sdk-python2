# -*- coding: utf-8 -*-

import collections
from ucloud.core.utils import compact


class UCloudException(Exception):
    @property
    def retryable(self):
        return False


MAX_COMMON_RET_CODE = 2000


class RetCodeException(UCloudException):
    def __init__(self, action, code, message):
        self.action = action
        self.code = code
        self.message = message

    @property
    def retryable(self):
        return self.code > MAX_COMMON_RET_CODE

    def __str__(self):
        return "{self.action} - {self.code}: {self.message}".format(self=self)


class RetryTimeoutException(UCloudException):
    pass


class ValidationException(UCloudException):
    def __init__(self, e=None):
        if isinstance(e, compact.string_types):
            self.errors = [e]
        elif isinstance(e, collections.Iterable):
            self.errors = e or []
        else:
            self.errors = [e]

    @property
    def retryable(self):
        return False

    def __str__(self):
        return str([str(e) for e in self.errors])
