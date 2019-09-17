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


class AppBasedLinkQuery(Model):
    """Invoke request body type for app-based link query.

    :param url: Url queried by user
    :type url: str
    """

    _attribute_map = {
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, url=None):
        super(AppBasedLinkQuery, self).__init__()
        self.url = url
