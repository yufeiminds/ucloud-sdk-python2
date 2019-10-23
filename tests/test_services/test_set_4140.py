# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
import pytest
import logging
from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)
scenario = utest.Scenario(4140)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_4140(client, variables):
    scenario.initial(variables)
    scenario.variables["BucketName_test"] = funcs.concat(
        "ucdntest-", funcs.get_timestamp(10)
    )
    scenario.variables["time_granule_type"] = 1
    scenario.run(client)


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "CreateBucketResponse"),
    ],
    action="CreateBucket",
)
def create_bucket_00(client, variables):
    d = {
        "Region": variables.get("Region"),
        "BucketName": variables.get("BucketName_test"),
    }
    try:
        resp = client.invoke("CreateBucket", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "StartUcdnTestDomainResponse"),
    ],
    action="StartUcdnTestDomain",
)
def start_ucdn_test_domain_01(client, variables):
    d = {
        "Region": variables.get("Region"),
        "BucketName": variables.get("BucketName_test"),
    }
    try:
        resp = client.invoke("StartUcdnTestDomain", d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["domainId"] = utest.value_at_path(resp, "DomainId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=3,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeUcdnDomainResponse"),
        ("str_eq", "DomainSet.0.ChannelType", "ucdn"),
        (
            "str_eq",
            "DomainSet.0.Domain",
            funcs.concat(
                variables.get("BucketName_test"), ".ufile.ucloud.com.cn"
            ),
        ),
        ("str_eq", "DomainSet.0.DomainId", variables.get("domainId")),
        ("str_eq", "DomainSet.0.Status", "check"),
    ],
    action="DescribeUcdnDomain",
)
def describe_ucdn_domain_02(client, variables):
    d = {"DomainId": [variables.get("domainId")]}
    try:
        resp = client.invoke("DescribeUcdnDomain", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=30,
    retry_interval=10,
    startup_delay=200,
    fast_fail=True,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeUcdnDomainResponse"),
        ("str_eq", "DomainSet.0.ChannelType", "ucdn"),
        (
            "str_eq",
            "DomainSet.0.Domain",
            funcs.concat(
                variables.get("BucketName_test"), ".ufile.ucloud.com.cn"
            ),
        ),
        ("str_eq", "DomainSet.0.DomainId", variables.get("domainId")),
        ("str_eq", "DomainSet.0.Status", "enable"),
    ],
    action="DescribeUcdnDomain",
)
def describe_ucdn_domain_03(client, variables):
    d = {"DomainId": [variables.get("domainId")]}
    try:
        resp = client.invoke("DescribeUcdnDomain", d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["domain"] = utest.value_at_path(resp, "DomainSet.0.Domain")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "BatchDescribeNewUcdnDomainResponse"),
    ],
    action="BatchDescribeNewUcdnDomain",
)
def batch_describe_new_ucdn_domain_04(client, variables):
    d = {}
    try:
        resp = client.ucdn().batch_describe_new_ucdn_domain(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "GetNewUcdnDomainHttpCodeV2Response"),
    ],
    action="GetNewUcdnDomainHttpCodeV2",
)
def get_new_ucdn_domain_http_code_v2_05(client, variables):
    d = {
        "Type": variables.get("time_granule_type"),
        "EndTime": funcs.get_timestamp(10),
        "BeginTime": funcs.get_timestamp(10) - 10000,
    }
    try:
        resp = client.ucdn().get_new_ucdn_domain_http_code_v2(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "GetNewUcdnDomainHitRateResponse"),
    ],
    action="GetNewUcdnDomainHitRate",
)
def get_new_ucdn_domain_hit_rate_06(client, variables):
    d = {
        "Type": variables.get("time_granule_type"),
        "EndTime": funcs.get_timestamp(10),
        "BeginTime": funcs.get_timestamp(10) - 1000,
    }
    try:
        resp = client.ucdn().get_new_ucdn_domain_hit_rate(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "GetNewUcdnDomainHttpCodeResponse"),
    ],
    action="GetNewUcdnDomainHttpCode",
)
def get_new_ucdn_domain_http_code_07(client, variables):
    d = {
        "Type": variables.get("time_granule_type"),
        "EndTime": funcs.get_timestamp(10),
        "BeginTime": funcs.get_timestamp(10) - 10000,
    }
    try:
        resp = client.ucdn().get_new_ucdn_domain_http_code(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "PrefetchNewUcdnDomainCacheResponse"),
    ],
    action="PrefetchNewUcdnDomainCache",
)
def prefetch_new_ucdn_domain_cache_08(client, variables):
    d = {"UrlList": [funcs.concat("http://", variables.get("domain"), "/")]}
    try:
        resp = client.ucdn().prefetch_new_ucdn_domain_cache(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["PrefetchCache_TaskId"] = utest.value_at_path(resp, "TaskId")
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeNewUcdnPrefetchCacheTaskResponse"),
    ],
    action="DescribeNewUcdnPrefetchCacheTask",
)
def describe_new_ucdn_prefetch_cache_task_09(client, variables):
    d = {"TaskId": [variables.get("PrefetchCache_TaskId")]}
    try:
        resp = client.ucdn().describe_new_ucdn_prefetch_cache_task(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeNewUcdnRefreshCacheTaskResponse"),
    ],
    action="DescribeNewUcdnRefreshCacheTask",
)
def describe_new_ucdn_refresh_cache_task_10(client, variables):
    d = {"TaskId": [variables.get("PrefetchCache_TaskId")]}
    try:
        resp = client.ucdn().describe_new_ucdn_refresh_cache_task(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "RefreshNewUcdnDomainCacheResponse"),
    ],
    action="RefreshNewUcdnDomainCache",
)
def refresh_new_ucdn_domain_cache_11(client, variables):
    d = {
        "UrlList": [funcs.concat("http://", variables.get("domain"), "/")],
        "Type": "file",
    }
    try:
        resp = client.ucdn().refresh_new_ucdn_domain_cache(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "GetNewUcdnDomainBandwidthResponse"),
    ],
    action="GetNewUcdnDomainBandwidth",
)
def get_new_ucdn_domain_bandwidth_12(client, variables):
    d = {"Type": variables.get("time_granule_type")}
    try:
        resp = client.ucdn().get_new_ucdn_domain_bandwidth(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "GetUcdnPassBandwidthResponse"),
    ],
    action="GetUcdnPassBandwidth",
)
def get_ucdn_pass_bandwidth_13(client, variables):
    d = {"Type": variables.get("time_granule_type")}
    try:
        resp = client.ucdn().get_ucdn_pass_bandwidth(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "GetUcdnDomainRequestNumV2Response"),
    ],
    action="GetUcdnDomainRequestNumV2",
)
def get_ucdn_domain_request_num_v2_14(client, variables):
    d = {
        "Type": variables.get("time_granule_type"),
        "EndTime": funcs.get_timestamp(10),
        "DomainId": [variables.get("domainId")],
        "BeginTime": funcs.get_timestamp(10) - 1000,
    }
    try:
        resp = client.ucdn().get_ucdn_domain_request_num_v2(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "GetUcdnDomainLogResponse"),
    ],
    action="GetUcdnDomainLog",
)
def get_ucdn_domain_log_15(client, variables):
    d = {
        "Type": variables.get("time_granule_type"),
        "DomainId": [variables.get("domainId")],
    }
    try:
        resp = client.ucdn().get_ucdn_domain_log(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "GetUcdnTrafficResponse"),
    ],
    action="GetUcdnTraffic",
)
def get_ucdn_traffic_16(client, variables):
    d = {}
    try:
        resp = client.ucdn().get_ucdn_traffic(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "GetUcdnDomainTrafficResponse"),
    ],
    action="GetUcdnDomainTraffic",
)
def get_ucdn_domain_traffic_17(client, variables):
    d = {"AccountType": "top"}
    try:
        resp = client.ucdn().get_ucdn_domain_traffic(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "GetUcdnDomainPrefetchEnableResponse"),
        ("str_eq", "Enable", 1),
    ],
    action="GetUcdnDomainPrefetchEnable",
)
def get_ucdn_domain_prefetch_enable_18(client, variables):
    d = {"DomainId": variables.get("domainId")}
    try:
        resp = client.ucdn().get_ucdn_domain_prefetch_enable(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "SwitchUcdnChargeTypeResponse"),
    ],
    action="SwitchUcdnChargeType",
)
def switch_ucdn_charge_type_19(client, variables):
    d = {"ChargeType": "traffic"}
    try:
        resp = client.ucdn().switch_ucdn_charge_type(d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "StopUcdnTestDomainResponse"),
    ],
    action="StopUcdnTestDomain",
)
def stop_ucdn_test_domain_20(client, variables):
    d = {
        "Region": variables.get("Region"),
        "BucketName": variables.get("BucketName_test"),
    }
    try:
        resp = client.invoke("StopUcdnTestDomain", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=3,
    retry_interval=1,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DescribeUcdnDomainResponse"),
        ("str_eq", "DomainSet.0.ChannelType", "ucdn"),
        (
            "str_eq",
            "DomainSet.0.Domain",
            funcs.concat(
                variables.get("BucketName_test"), ".ufile.ucloud.com.cn"
            ),
        ),
        ("str_eq", "DomainSet.0.DomainId", variables.get("domainId")),
        ("str_eq", "DomainSet.0.Status", "deleteing"),
    ],
    action="DescribeUcdnDomain",
)
def describe_ucdn_domain_21(client, variables):
    d = {"DomainId": [variables.get("domainId")]}
    try:
        resp = client.invoke("DescribeUcdnDomain", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=10,
    retry_interval=10,
    startup_delay=120,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "Action", "DeleteBucketResponse"),
    ],
    action="DeleteBucket",
)
def delete_bucket_22(client, variables):
    d = {"BucketName": variables.get("BucketName_test")}
    try:
        resp = client.invoke("DeleteBucket", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp
