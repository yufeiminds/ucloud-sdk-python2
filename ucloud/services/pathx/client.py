# -*- coding: utf-8 -*-

""" Code is generated by ucloud-model, DO NOT EDIT IT. """
from ucloud.core.client import Client
from ucloud.services.pathx.schemas import apis


class PathXClient(Client):
    def __init__(self, config, transport=None, middleware=None, logger=None):
        super(PathXClient, self).__init__(config, transport, middleware, logger)

    def create_global_ssh_instance(self, req=None, **kwargs):
        """ CreateGlobalSSHInstance - 创建GlobalSSH实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID,如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Area** (str) - (Required) 填写支持SSH访问IP的地区名称，如“洛杉矶”，“新加坡”，“香港”，“东京”，“华盛顿”，“法兰克福”。Area和AreaCode两者必填一个
        - **AreaCode** (str) - (Required) AreaCode, 区域航空港国际通用代码。Area和AreaCode两者必填一个
        - **Port** (int) - (Required) SSH端口，1-65535且不能使用80，443端口
        - **TargetIP** (str) - (Required) 被SSH访问的IP
        - **ChargeType** (str) - 支付方式，如按月、按年、按时
        - **CouponId** (str) - 使用代金券可冲抵部分费用
        - **Quantity** (int) - 购买数量
        - **Remark** (str) - 备注信息
        
        **Response**

        - **AcceleratingDomain** (str) - 加速域名，访问该域名可就近接入
        - **InstanceId** (str) - 实例ID，资源唯一标识
        - **Message** (str) - 提示信息
        
        """
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.CreateGlobalSSHInstanceRequestSchema().dumps(d)
        kwargs["max_retries"] = 0
        resp = self.invoke("CreateGlobalSSHInstance", d, **kwargs)
        return apis.CreateGlobalSSHInstanceResponseSchema().loads(resp)

    def delete_global_ssh_instance(self, req=None, **kwargs):
        """ DeleteGlobalSSHInstance - 删除GlobalSSH实例

        **Request**

        - **ProjectId** (str) - (Config) 项目ID,如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **InstanceId** (str) - (Required) 实例Id,资源的唯一标识
        
        **Response**

        - **Message** (str) - 提示信息
        
        """
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.DeleteGlobalSSHInstanceRequestSchema().dumps(d)
        resp = self.invoke("DeleteGlobalSSHInstance", d, **kwargs)
        return apis.DeleteGlobalSSHInstanceResponseSchema().loads(resp)

    def describe_global_ssh_area(self, req=None, **kwargs):
        """ DescribeGlobalSSHArea - 获取GlobalSSH覆盖的地区列表 用于控制显示哪些机房地域可以使用SSH特性

        **Request**

        - **ProjectId** (str) - (Config) 项目ID,如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 机房地域代号，如hk、 us-ca、 us-ws等。不填默认为空，返回所有支持地区。
        
        **Response**

        - **AreaSet** (list) - 见 **GlobalSSHArea** 模型定义
        - **Message** (str) - 提示信息
        
        **Response Model**
        
        **GlobalSSHArea** 
        
        - **Area** (str) - GlobalSSH覆盖的地区,如香港、东京、洛杉矶等
        - **AreaCode** (str) - 地区代号,以地区AirPort Code
        - **RegionSet** (list) - ucloud机房代号构成的数组，如["hk","us-ca"]

        """
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeGlobalSSHAreaRequestSchema().dumps(d)
        resp = self.invoke("DescribeGlobalSSHArea", d, **kwargs)
        return apis.DescribeGlobalSSHAreaResponseSchema().loads(resp)

    def describe_global_ssh_instance(self, req=None, **kwargs):
        """ DescribeGlobalSSHInstance - 获取GlobalSSH实例列表（传实例ID获取单个实例信息，不传获取项目下全部实例）

        **Request**

        - **ProjectId** (str) - (Config) 项目ID，如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **InstanceId** (str) - 实例ID，资源唯一标识
        
        **Response**

        - **InstanceSet** (list) - 见 **GlobalSSHInfo** 模型定义
        
        **Response Model**
        
        **GlobalSSHInfo** 
        
        - **AcceleratingDomain** (str) - 加速域名
        - **Area** (str) - 被SSH访问的IP所在地区
        - **ChargeType** (str) - 支付周期，如Month,Year等
        - **CreateTime** (int) - 资源创建时间戳
        - **ExpireTime** (int) - 资源过期时间戳
        - **InstanceId** (str) - 实例ID，资源唯一标识
        - **Port** (int) - SSH登陆端口
        - **Remark** (str) - 备注信息
        - **TargetIP** (str) - 被SSH访问的EIP

        """
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.DescribeGlobalSSHInstanceRequestSchema().dumps(d)
        resp = self.invoke("DescribeGlobalSSHInstance", d, **kwargs)
        return apis.DescribeGlobalSSHInstanceResponseSchema().loads(resp)

    def modify_global_ssh_port(self, req=None, **kwargs):
        """ ModifyGlobalSSHPort - 修改GlobalSSH端口

        **Request**

        - **ProjectId** (str) - (Config) 项目ID，如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **InstanceId** (str) - (Required) 实例ID,资源唯一标识
        - **Port** (int) - (Required) 调整后的SSH登陆端口
        
        **Response**

        - **Message** (str) - 提示信息
        
        """
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.ModifyGlobalSSHPortRequestSchema().dumps(d)
        resp = self.invoke("ModifyGlobalSSHPort", d, **kwargs)
        return apis.ModifyGlobalSSHPortResponseSchema().loads(resp)

    def modify_global_ssh_remark(self, req=None, **kwargs):
        """ ModifyGlobalSSHRemark - 修改GlobalSSH备注

        **Request**

        - **ProjectId** (str) - (Config) 项目ID，如org-xxxx。请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **InstanceId** (str) - (Required) 实例ID,资源唯一标识
        - **Remark** (str) - 备注信息，不填默认为空字符串
        
        **Response**

        - **Message** (str) - 接口返回消息
        
        """
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.ModifyGlobalSSHRemarkRequestSchema().dumps(d)
        resp = self.invoke("ModifyGlobalSSHRemark", d, **kwargs)
        return apis.ModifyGlobalSSHRemarkResponseSchema().loads(resp)
