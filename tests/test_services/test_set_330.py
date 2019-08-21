# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
import pytest
import logging
from ucloud.core import exc
from ucloud.testing import env, funcs, op, utest

logger = logging.getLogger(__name__)
scenario = utest.Scenario(330)


@pytest.mark.skipif(env.is_ut(), reason=env.get_skip_reason())
def test_set_330(client, variables):
    scenario.initial(variables)
    scenario.variables["Region"] = "cn-bj2"
    scenario.variables["Zone"] = "cn-bj2-02"
    scenario.run(client)


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateUMemcacheGroup",
)
def create_umem_cache_group_00(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Size": 1,
        "Region": variables.get("Region"),
        "Quantity": 1,
        "Name": "umem_charge",
        "ChargeType": "Month",
    }
    try:
        resp = client.umem().create_umem_cache_group(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["group_id"] = utest.value_at_path(resp, "GroupId")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=30,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUMem",
)
def describe_umem_01(client, variables):
    d = {
        "ResourceId": variables.get("group_id"),
        "Region": variables.get("Region"),
        "Protocol": "memcache",
        "Offset": 0,
        "Limit": 1000,
    }
    try:
        resp = client.invoke("DescribeUMem", d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["CreateTime"] = utest.value_at_path(resp, "DataSet.0.CreateTime")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUMemcachePrice",
)
def describe_umem_cache_price_02(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "Size": 1,
        "Region": variables.get("Region"),
        "Quantity": 1,
        "ChargeType": "Month",
    }
    try:
        resp = client.umem().describe_umem_cache_price(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["GetPrice"] = utest.value_at_path(resp, "DataSet.0.Price")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=60,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("float_eq", "OrderInfos.0.Amount", variables.get("GetPrice") / 100),
    ],
    action="DescribeOrderDetailInfo",
)
def describe_order_detail_info_03(client, variables):
    d = {
        "ResourceIds": [variables.get("group_id")],
        "QueryAll": True,
        "OrderTypes": ["OT_BUY"],
        "OrderStates": ["OS_FINISHED"],
        "EndTime": funcs.get_timestamp(10),
        "ChargeTypes": ["Month"],
        "BeginTime": funcs.get_timestamp(10) - 1200,
    }
    try:
        resp = client.invoke("DescribeOrderDetailInfo", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="DescribeUMemcacheUpgradePrice",
)
def describe_umem_cache_upgrade_price_04(client, variables):
    d = {
        "Size": 2,
        "Region": variables.get("Region"),
        "GroupId": variables.get("group_id"),
    }
    try:
        resp = client.umem().describe_umem_cache_upgrade_price(d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["UpgradePrice"] = utest.value_at_path(resp, "Price")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="ResizeUMemcacheGroup",
)
def resize_umem_cache_group_05(client, variables):
    d = {
        "Size": 2,
        "Region": variables.get("Region"),
        "GroupId": variables.get("group_id"),
    }
    try:
        resp = client.invoke("ResizeUMemcacheGroup", d)
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
        ("float_eq", "OrderInfos.0.Amount", variables.get("GetPrice") / 100),
    ],
    action="DescribeOrderDetailInfo",
)
def describe_order_detail_info_06(client, variables):
    d = {
        "ResourceIds": [variables.get("group_id")],
        "QueryAll": True,
        "OrderTypes": ["OT_BUY"],
        "OrderStates": ["OS_FINISHED"],
        "EndTime": funcs.get_timestamp(10),
        "ChargeTypes": ["Month"],
        "BeginTime": funcs.get_timestamp(10) - 1200,
    }
    try:
        resp = client.invoke("DescribeOrderDetailInfo", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=0,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="GetResourceRenewPrice",
)
def get_resource_renew_price_07(client, variables):
    d = {
        "ResourceIds": [variables.get("group_id")],
        "Quantity": 1,
        "ChargeType": "Month",
    }
    try:
        resp = client.invoke("GetResourceRenewPrice", d)
    except exc.RetCodeException as e:
        resp = e.json()
    variables["ReNewPrice"] = utest.value_at_path(resp, "RenewPriceSet.0.Price")
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=2,
    fast_fail=False,
    validators=lambda variables: [("str_eq", "RetCode", 0)],
    action="CreateRenew",
)
def create_renew_08(client, variables):
    d = {
        "ResourceId": variables.get("group_id"),
        "Quantity": 1,
        "ChargeType": "Month",
    }
    try:
        resp = client.invoke("CreateRenew", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=60,
    fast_fail=False,
    validators=lambda variables: [
        ("str_eq", "RetCode", 0),
        ("str_eq", "OrderInfos.0.Amount", variables.get("ReNewPrice")),
    ],
    action="DescribeOrderDetailInfo",
)
def describe_order_detail_info_09(client, variables):
    d = {
        "ResourceIds": [variables.get("group_id")],
        "QueryAll": True,
        "OrderTypes": ["OT_RENEW"],
        "OrderStates": ["OS_FINISHED"],
        "EndTime": funcs.get_timestamp(10),
        "ChargeTypes": ["Month"],
        "BeginTime": funcs.get_timestamp(10) - 1200,
    }
    try:
        resp = client.invoke("DescribeOrderDetailInfo", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp


@scenario.step(
    max_retries=0,
    retry_interval=0,
    startup_delay=2,
    fast_fail=False,
    action="DeleteUMem",
)
def delete_umem_10(client, variables):
    d = {
        "Zone": variables.get("Zone"),
        "ResourceType": "single",
        "ResourceId": variables.get("group_id"),
        "Region": variables.get("Region"),
    }
    try:
        resp = client.invoke("DeleteUMem", d)
    except exc.RetCodeException as e:
        resp = e.json()
    return resp
