# -*- coding: utf-8 -*-

from ucloud.core.typesystem import schema, fields
from ucloud.services.unet.schemas import models

""" UNet API Schema
"""
"""
API: ReleaseVIP

释放VIP资源
"""


class ReleaseVIPRequestSchema(schema.RequestSchema):
    """ ReleaseVIP - 释放VIP资源
    """

    fields = {
        "VIPId": fields.Str(required=True, dump_to="VIPId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class ReleaseVIPResponseSchema(schema.ResponseSchema):
    """ ReleaseVIP - 释放VIP资源
    """

    fields = {}


"""
API: SetEIPPayMode

设置弹性IP计费模式, 切换时会涉及付费/退费.
"""


class SetEIPPayModeRequestSchema(schema.RequestSchema):
    """ SetEIPPayMode - 设置弹性IP计费模式, 切换时会涉及付费/退费.
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "PayMode": fields.Str(required=True, dump_to="PayMode"),
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
    }


class SetEIPPayModeResponseSchema(schema.ResponseSchema):
    """ SetEIPPayMode - 设置弹性IP计费模式, 切换时会涉及付费/退费.
    """

    fields = {}


"""
API: DeleteBandwidthPackage

删除弹性IP上已附加带宽包
"""


class DeleteBandwidthPackageRequestSchema(schema.RequestSchema):
    """ DeleteBandwidthPackage - 删除弹性IP上已附加带宽包
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "BandwidthPackageId": fields.Str(required=True, dump_to="BandwidthPackageId"),
    }


class DeleteBandwidthPackageResponseSchema(schema.ResponseSchema):
    """ DeleteBandwidthPackage - 删除弹性IP上已附加带宽包
    """

    fields = {}


"""
API: DescribeEIP

获取弹性IP信息
"""


class DescribeEIPRequestSchema(schema.RequestSchema):
    """ DescribeEIP - 获取弹性IP信息
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "EIPIds": fields.List(fields.Str()),
    }


class DescribeEIPResponseSchema(schema.ResponseSchema):
    """ DescribeEIP - 获取弹性IP信息
    """

    fields = {
        "TotalBandwidth": fields.Int(required=False, load_from="TotalBandwidth"),
        "EIPSet": fields.List(
            models.UnetEIPSetSchema(), required=False, load_from="EIPSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: GetEIPPayMode

获取弹性IP计费模式
"""


class GetEIPPayModeRequestSchema(schema.RequestSchema):
    """ GetEIPPayMode - 获取弹性IP计费模式
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "EIPId": fields.List(fields.Str()),
    }


class GetEIPPayModeResponseSchema(schema.ResponseSchema):
    """ GetEIPPayMode - 获取弹性IP计费模式
    """

    fields = {
        "EIPPayMode": fields.List(
            models.EIPPayModeSetSchema(), required=False, load_from="EIPPayMode"
        )
    }


"""
API: ResizeShareBandwidth

调整共享带宽的带宽值
"""


class ResizeShareBandwidthRequestSchema(schema.RequestSchema):
    """ ResizeShareBandwidth - 调整共享带宽的带宽值
    """

    fields = {
        "ShareBandwidth": fields.Int(required=True, dump_to="ShareBandwidth"),
        "ShareBandwidthId": fields.Str(required=True, dump_to="ShareBandwidthId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class ResizeShareBandwidthResponseSchema(schema.ResponseSchema):
    """ ResizeShareBandwidth - 调整共享带宽的带宽值
    """

    fields = {}


"""
API: AllocateVIP

根据提供信息，申请内网VIP(Virtual IP），多用于高可用程序作为漂移IP。
"""


class AllocateVIPRequestSchema(schema.RequestSchema):
    """ AllocateVIP - 根据提供信息，申请内网VIP(Virtual IP），多用于高可用程序作为漂移IP。
    """

    fields = {
        "SubnetId": fields.Str(required=True, dump_to="SubnetId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "VPCId": fields.Str(required=True, dump_to="VPCId"),
        "Count": fields.Int(required=False, dump_to="Count"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "BusinessId": fields.Str(required=False, dump_to="BusinessId"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class AllocateVIPResponseSchema(schema.ResponseSchema):
    """ AllocateVIP - 根据提供信息，申请内网VIP(Virtual IP），多用于高可用程序作为漂移IP。
    """

    fields = {
        "VIPSet": fields.List(
            models.VIPSetSchema(), required=False, load_from="VIPSet"
        ),
        "DataSet": fields.List(fields.Str(), required=False, load_from="DataSet"),
    }


"""
API: CreateBandwidthPackage

为非共享带宽模式下, 已绑定资源实例的带宽计费弹性IP附加临时带宽包
"""


class CreateBandwidthPackageRequestSchema(schema.RequestSchema):
    """ CreateBandwidthPackage - 为非共享带宽模式下, 已绑定资源实例的带宽计费弹性IP附加临时带宽包
    """

    fields = {
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "TimeRange": fields.Int(required=True, dump_to="TimeRange"),
        "EnableTime": fields.Int(required=False, dump_to="EnableTime"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
    }


class CreateBandwidthPackageResponseSchema(schema.ResponseSchema):
    """ CreateBandwidthPackage - 为非共享带宽模式下, 已绑定资源实例的带宽计费弹性IP附加临时带宽包
    """

    fields = {
        "BandwidthPackageId": fields.Str(required=False, load_from="BandwidthPackageId")
    }


"""
API: UnBindEIP

将弹性IP从资源上解绑
"""


class UnBindEIPRequestSchema(schema.RequestSchema):
    """ UnBindEIP - 将弹性IP从资源上解绑
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "ResourceType": fields.Str(required=True, dump_to="ResourceType"),
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
    }


class UnBindEIPResponseSchema(schema.ResponseSchema):
    """ UnBindEIP - 将弹性IP从资源上解绑
    """

    fields = {}


"""
API: DescribeFirewallResource

获取防火墙组所绑定资源的外网IP
"""


class DescribeFirewallResourceRequestSchema(schema.RequestSchema):
    """ DescribeFirewallResource - 获取防火墙组所绑定资源的外网IP
    """

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "FWId": fields.Str(required=True, dump_to="FWId"),
    }


class DescribeFirewallResourceResponseSchema(schema.ResponseSchema):
    """ DescribeFirewallResource - 获取防火墙组所绑定资源的外网IP
    """

    fields = {
        "ResourceSet": fields.List(
            models.ResourceSetSchema(), required=False, load_from="ResourceSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: ModifyEIPBandwidth

调整弹性IP的外网带宽
"""


class ModifyEIPBandwidthRequestSchema(schema.RequestSchema):
    """ ModifyEIPBandwidth - 调整弹性IP的外网带宽
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
    }


class ModifyEIPBandwidthResponseSchema(schema.ResponseSchema):
    """ ModifyEIPBandwidth - 调整弹性IP的外网带宽
    """

    fields = {}


"""
API: UpdateFirewall

更新防火墙规则
"""


class UpdateFirewallRequestSchema(schema.RequestSchema):
    """ UpdateFirewall - 更新防火墙规则
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "FWId": fields.Str(required=True, dump_to="FWId"),
        "Rule": fields.List(fields.Str()),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class UpdateFirewallResponseSchema(schema.ResponseSchema):
    """ UpdateFirewall - 更新防火墙规则
    """

    fields = {"FWId": fields.Str(required=False, load_from="FWId")}


"""
API: UpdateFirewallAttribute

更新防火墙规则
"""


class UpdateFirewallAttributeRequestSchema(schema.RequestSchema):
    """ UpdateFirewallAttribute - 更新防火墙规则
    """

    fields = {
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "FWId": fields.Str(required=True, dump_to="FWId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Region": fields.Str(required=True, dump_to="Region"),
    }


class UpdateFirewallAttributeResponseSchema(schema.ResponseSchema):
    """ UpdateFirewallAttribute - 更新防火墙规则
    """

    fields = {}


"""
API: DeleteFirewall

删除防火墙
"""


class DeleteFirewallRequestSchema(schema.RequestSchema):
    """ DeleteFirewall - 删除防火墙
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "FWId": fields.Str(required=True, dump_to="FWId"),
    }


class DeleteFirewallResponseSchema(schema.ResponseSchema):
    """ DeleteFirewall - 删除防火墙
    """

    fields = {}


"""
API: GrantFirewall

将防火墙应用到资源上
"""


class GrantFirewallRequestSchema(schema.RequestSchema):
    """ GrantFirewall - 将防火墙应用到资源上
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "FWId": fields.Str(required=True, dump_to="FWId"),
        "ResourceType": fields.Str(required=True, dump_to="ResourceType"),
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
    }


class GrantFirewallResponseSchema(schema.ResponseSchema):
    """ GrantFirewall - 将防火墙应用到资源上
    """

    fields = {}


"""
API: DescribeVIP

获取内网VIP详细信息
"""


class DescribeVIPRequestSchema(schema.RequestSchema):
    """ DescribeVIP - 获取内网VIP详细信息
    """

    fields = {
        "BusinessId": fields.Str(required=False, dump_to="BusinessId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "Zone": fields.Str(required=False, dump_to="Zone"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "VPCId": fields.Str(required=False, dump_to="VPCId"),
        "SubnetId": fields.Str(required=False, dump_to="SubnetId"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
    }


class DescribeVIPResponseSchema(schema.ResponseSchema):
    """ DescribeVIP - 获取内网VIP详细信息
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "VIPSet": fields.List(
            models.VIPDetailSetSchema(), required=False, load_from="VIPSet"
        ),
        "DataSet": fields.List(fields.Str(), required=False, load_from="DataSet"),
    }


"""
API: DisassociateEIPWithShareBandwidth

将EIP移出共享带宽
"""


class DisassociateEIPWithShareBandwidthRequestSchema(schema.RequestSchema):
    """ DisassociateEIPWithShareBandwidth - 将EIP移出共享带宽
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ShareBandwidthId": fields.Str(required=True, dump_to="ShareBandwidthId"),
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "PayMode": fields.Str(required=False, dump_to="PayMode"),
        "EIPIds": fields.List(fields.Str()),
    }


class DisassociateEIPWithShareBandwidthResponseSchema(schema.ResponseSchema):
    """ DisassociateEIPWithShareBandwidth - 将EIP移出共享带宽
    """

    fields = {}


"""
API: AssociateEIPWithShareBandwidth

将EIP加入共享带宽
"""


class AssociateEIPWithShareBandwidthRequestSchema(schema.RequestSchema):
    """ AssociateEIPWithShareBandwidth - 将EIP加入共享带宽
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ShareBandwidthId": fields.Str(required=True, dump_to="ShareBandwidthId"),
        "EIPIds": fields.List(fields.Str()),
    }


class AssociateEIPWithShareBandwidthResponseSchema(schema.ResponseSchema):
    """ AssociateEIPWithShareBandwidth - 将EIP加入共享带宽
    """

    fields = {}


"""
API: DescribeBandwidthPackage

获取某地域下的带宽包信息
"""


class DescribeBandwidthPackageRequestSchema(schema.RequestSchema):
    """ DescribeBandwidthPackage - 获取某地域下的带宽包信息
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
    }


class DescribeBandwidthPackageResponseSchema(schema.ResponseSchema):
    """ DescribeBandwidthPackage - 获取某地域下的带宽包信息
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "DataSets": fields.List(
            models.UnetBandwidthPackageSetSchema(), required=False, load_from="DataSets"
        ),
    }


"""
API: DescribeFirewall

获取防火墙组信息
"""


class DescribeFirewallRequestSchema(schema.RequestSchema):
    """ DescribeFirewall - 获取防火墙组信息
    """

    fields = {
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "Offset": fields.Int(required=False, dump_to="Offset"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "FWId": fields.Str(required=False, dump_to="FWId"),
        "ResourceType": fields.Str(required=False, dump_to="ResourceType"),
        "ResourceId": fields.Str(required=False, dump_to="ResourceId"),
    }


class DescribeFirewallResponseSchema(schema.ResponseSchema):
    """ DescribeFirewall - 获取防火墙组信息
    """

    fields = {
        "DataSet": fields.List(
            models.FirewallDataSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: GetEIPPrice

获取弹性IP价格
"""


class GetEIPPriceRequestSchema(schema.RequestSchema):
    """ GetEIPPrice - 获取弹性IP价格
    """

    fields = {
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "PayMode": fields.Str(required=False, dump_to="PayMode"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "OperatorName": fields.Str(required=True, dump_to="OperatorName"),
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
    }


class GetEIPPriceResponseSchema(schema.ResponseSchema):
    """ GetEIPPrice - 获取弹性IP价格
    """

    fields = {
        "PriceSet": fields.List(
            models.EIPPriceDetailSetSchema(), required=False, load_from="PriceSet"
        )
    }


"""
API: GetEIPUpgradePrice

获取弹性IP带宽改动价格
"""


class GetEIPUpgradePriceRequestSchema(schema.RequestSchema):
    """ GetEIPUpgradePrice - 获取弹性IP带宽改动价格
    """

    fields = {
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class GetEIPUpgradePriceResponseSchema(schema.ResponseSchema):
    """ GetEIPUpgradePrice - 获取弹性IP带宽改动价格
    """

    fields = {"Price": fields.Float(required=False, load_from="Price")}


"""
API: BindEIP

将尚未使用的弹性IP绑定到指定的资源
"""


class BindEIPRequestSchema(schema.RequestSchema):
    """ BindEIP - 将尚未使用的弹性IP绑定到指定的资源
    """

    fields = {
        "ResourceType": fields.Str(required=True, dump_to="ResourceType"),
        "ResourceId": fields.Str(required=True, dump_to="ResourceId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
    }


class BindEIPResponseSchema(schema.ResponseSchema):
    """ BindEIP - 将尚未使用的弹性IP绑定到指定的资源
    """

    fields = {}


"""
API: CreateFirewall

创建防火墙
"""


class CreateFirewallRequestSchema(schema.RequestSchema):
    """ CreateFirewall - 创建防火墙
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "Rule": fields.List(fields.Str()),
    }


class CreateFirewallResponseSchema(schema.ResponseSchema):
    """ CreateFirewall - 创建防火墙
    """

    fields = {"FWId": fields.Str(required=False, load_from="FWId")}


"""
API: DescribeShareBandwidth

获取共享带宽信息
"""


class DescribeShareBandwidthRequestSchema(schema.RequestSchema):
    """ DescribeShareBandwidth - 获取共享带宽信息
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ShareBandwidthIds": fields.List(fields.Str()),
    }


class DescribeShareBandwidthResponseSchema(schema.ResponseSchema):
    """ DescribeShareBandwidth - 获取共享带宽信息
    """

    fields = {
        "DataSet": fields.List(
            models.UnetShareBandwidthSetSchema(), required=False, load_from="DataSet"
        ),
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
    }


"""
API: ModifyEIPWeight

修改弹性IP的外网出口权重
"""


class ModifyEIPWeightRequestSchema(schema.RequestSchema):
    """ ModifyEIPWeight - 修改弹性IP的外网出口权重
    """

    fields = {
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "Weight": fields.Int(required=True, dump_to="Weight"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class ModifyEIPWeightResponseSchema(schema.ResponseSchema):
    """ ModifyEIPWeight - 修改弹性IP的外网出口权重
    """

    fields = {}


"""
API: DescribeBandwidthUsage

获取带宽用量信息
"""


class DescribeBandwidthUsageRequestSchema(schema.RequestSchema):
    """ DescribeBandwidthUsage - 获取带宽用量信息
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Limit": fields.Int(required=False, dump_to="Limit"),
        "OffSet": fields.Int(required=False, dump_to="OffSet"),
        "EIPIds": fields.List(fields.Str()),
    }


class DescribeBandwidthUsageResponseSchema(schema.ResponseSchema):
    """ DescribeBandwidthUsage - 获取带宽用量信息
    """

    fields = {
        "TotalCount": fields.Int(required=False, load_from="TotalCount"),
        "EIPSet": fields.List(
            models.UnetBandwidthUsageEIPSetSchema(), required=False, load_from="EIPSet"
        ),
    }


"""
API: ReleaseEIP

释放弹性IP资源, 所释放弹性IP必须为非绑定状态.
"""


class ReleaseEIPRequestSchema(schema.RequestSchema):
    """ ReleaseEIP - 释放弹性IP资源, 所释放弹性IP必须为非绑定状态.
    """

    fields = {
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
    }


class ReleaseEIPResponseSchema(schema.ResponseSchema):
    """ ReleaseEIP - 释放弹性IP资源, 所释放弹性IP必须为非绑定状态.
    """

    fields = {}


"""
API: ReleaseShareBandwidth

关闭共享带宽
"""


class ReleaseShareBandwidthRequestSchema(schema.RequestSchema):
    """ ReleaseShareBandwidth - 关闭共享带宽
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "ShareBandwidthId": fields.Str(required=True, dump_to="ShareBandwidthId"),
        "EIPBandwidth": fields.Int(required=True, dump_to="EIPBandwidth"),
        "PayMode": fields.Str(required=False, dump_to="PayMode"),
    }


class ReleaseShareBandwidthResponseSchema(schema.ResponseSchema):
    """ ReleaseShareBandwidth - 关闭共享带宽
    """

    fields = {}


"""
API: UpdateEIPAttribute

更新弹性IP名称，业务组，备注等属性字段
"""


class UpdateEIPAttributeRequestSchema(schema.RequestSchema):
    """ UpdateEIPAttribute - 更新弹性IP名称，业务组，备注等属性字段
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "EIPId": fields.Str(required=True, dump_to="EIPId"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
    }


class UpdateEIPAttributeResponseSchema(schema.ResponseSchema):
    """ UpdateEIPAttribute - 更新弹性IP名称，业务组，备注等属性字段
    """

    fields = {}


"""
API: AllocateEIP

根据提供信息, 申请弹性IP
"""


class AllocateEIPRequestSchema(schema.RequestSchema):
    """ AllocateEIP - 根据提供信息, 申请弹性IP
    """

    fields = {
        "PayMode": fields.Str(required=False, dump_to="PayMode"),
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Bandwidth": fields.Int(required=True, dump_to="Bandwidth"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "Name": fields.Str(required=False, dump_to="Name"),
        "Remark": fields.Str(required=False, dump_to="Remark"),
        "CouponId": fields.Str(required=False, dump_to="CouponId"),
        "OperatorName": fields.Str(required=True, dump_to="OperatorName"),
        "Tag": fields.Str(required=False, dump_to="Tag"),
        "ChargeType": fields.Str(required=False, dump_to="ChargeType"),
        "ShareBandwidthId": fields.Str(required=False, dump_to="ShareBandwidthId"),
    }


class AllocateEIPResponseSchema(schema.ResponseSchema):
    """ AllocateEIP - 根据提供信息, 申请弹性IP
    """

    fields = {
        "EIPSet": fields.List(
            models.UnetAllocateEIPSetSchema(), required=False, load_from="EIPSet"
        )
    }


"""
API: AllocateShareBandwidth

开通共享带宽
"""


class AllocateShareBandwidthRequestSchema(schema.RequestSchema):
    """ AllocateShareBandwidth - 开通共享带宽
    """

    fields = {
        "Region": fields.Str(required=True, dump_to="Region"),
        "ProjectId": fields.Str(required=False, dump_to="ProjectId"),
        "Name": fields.Str(required=True, dump_to="Name"),
        "ChargeType": fields.Str(required=True, dump_to="ChargeType"),
        "ShareBandwidth": fields.Int(required=True, dump_to="ShareBandwidth"),
        "Quantity": fields.Int(required=False, dump_to="Quantity"),
        "ShareBandwidthGuarantee": fields.Int(
            required=False, dump_to="ShareBandwidthGuarantee"
        ),
    }


class AllocateShareBandwidthResponseSchema(schema.ResponseSchema):
    """ AllocateShareBandwidth - 开通共享带宽
    """

    fields = {
        "ShareBandwidthId": fields.Str(required=False, load_from="ShareBandwidthId")
    }
