# -*- coding: utf-8 -*-

import os

ACC_ENV_KEY = "USDK_ACC"
ACC_SKIP_REASON = "skip test for non-acc environment"


def get_skip_reason():
    return ACC_SKIP_REASON


def is_acc():
    """ check test env is acceptance testing or not """
    return os.getenv(ACC_ENV_KEY)


def is_ut():
    """ check test env is unit testing or not """
    return not is_acc()


def pre_check_env():
    """ pre check environment for testing

    NOTE: system environment variables credential is required for test environment
    """
    assert os.getenv("UCLOUD_PUBLIC_KEY"), "invalid public key"
    assert os.getenv("UCLOUD_PRIVATE_KEY"), "invalid private key"
    assert os.getenv("UCLOUD_REGION"), "invalid region"
