# -*- coding: utf-8 -*-

from ucloud.core.typesystem import schema, fields
from ucloud.services.uaccount.schemas import models

""" UAccount API Schema
"""
"""
API: ModifyProject

修改项目
"""


class ModifyProjectRequestSchema(schema.RequestSchema):
    """ ModifyProject - 修改项目
    """

    fields = {
        "ProjectId": fields.Str(required=True, dump_to="ProjectId"),
        "ProjectName": fields.Str(required=True, dump_to="ProjectName"),
    }


class ModifyProjectResponseSchema(schema.ResponseSchema):
    """ ModifyProject - 修改项目
    """

    fields = {}


"""
API: TerminateProject

删除项目
"""


class TerminateProjectRequestSchema(schema.RequestSchema):
    """ TerminateProject - 删除项目
    """

    fields = {"ProjectId": fields.Str(required=False, dump_to="ProjectId")}


class TerminateProjectResponseSchema(schema.ResponseSchema):
    """ TerminateProject - 删除项目
    """

    fields = {}


"""
API: CreateProject

创建项目
"""


class CreateProjectRequestSchema(schema.RequestSchema):
    """ CreateProject - 创建项目
    """

    fields = {"ProjectName": fields.Str(required=True, dump_to="ProjectName")}


class CreateProjectResponseSchema(schema.ResponseSchema):
    """ CreateProject - 创建项目
    """

    fields = {"ProjectId": fields.Str(required=True, load_from="ProjectId")}


"""
API: GetProjectList

获取项目列表
"""


class GetProjectListRequestSchema(schema.RequestSchema):
    """ GetProjectList - 获取项目列表
    """

    fields = {"IsFinance": fields.Str(required=False, dump_to="IsFinance")}


class GetProjectListResponseSchema(schema.ResponseSchema):
    """ GetProjectList - 获取项目列表
    """

    fields = {
        "ProjectCount": fields.Int(required=True, load_from="ProjectCount"),
        "ProjectSet": fields.List(
            models.ProjectListInfoSchema(), required=True, load_from="ProjectSet"
        ),
    }


"""
API: GetRegion

获取用户在各数据中心的权限等信息
"""


class GetRegionRequestSchema(schema.RequestSchema):
    """ GetRegion - 获取用户在各数据中心的权限等信息
    """

    fields = {}


class GetRegionResponseSchema(schema.ResponseSchema):
    """ GetRegion - 获取用户在各数据中心的权限等信息
    """

    fields = {
        "Regions": fields.List(
            models.RegionInfoSchema(), required=False, load_from="Regions"
        )
    }


"""
API: GetUserInfo

获取用户信息
"""


class GetUserInfoRequestSchema(schema.RequestSchema):
    """ GetUserInfo - 获取用户信息
    """

    fields = {}


class GetUserInfoResponseSchema(schema.ResponseSchema):
    """ GetUserInfo - 获取用户信息
    """

    fields = {
        "DataSet": fields.List(
            models.UserInfoSchema(), required=True, load_from="DataSet"
        )
    }
