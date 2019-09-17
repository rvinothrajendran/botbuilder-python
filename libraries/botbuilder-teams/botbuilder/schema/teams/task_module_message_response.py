# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .task_module_response_base import TaskModuleResponseBase


class TaskModuleMessageResponse(TaskModuleResponseBase):
    """Task Module response with message action.

    :param type: Choice of action options when responding to the task/submit
     message. Possible values include: 'message', 'continue'
    :type type: str or ~teamsapi.models.enum
    :param value: Teams will display the value of value in a popup message
     box.
    :type value: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(self, type=None, value=None):
        super(TaskModuleMessageResponse, self).__init__(type=type)
        self.value = value