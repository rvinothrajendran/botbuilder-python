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

from msrest.serialization import Model


class TaskModuleRequestContext(Model):
    """Current user context, i.e., the current theme.

    :param theme:
    :type theme: str
    """

    _attribute_map = {
        'theme': {'key': 'theme', 'type': 'str'},
    }

    def __init__(self, theme=None):
        super(TaskModuleRequestContext, self).__init__()
        self.theme = theme
