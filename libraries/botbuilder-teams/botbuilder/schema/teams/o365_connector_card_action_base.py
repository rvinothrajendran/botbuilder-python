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


class O365ConnectorCardActionBase(Model):
    """O365 connector card action base.

    :param type: Type of the action. Possible values include: 'ViewAction',
     'OpenUri', 'HttpPOST', 'ActionCard'
    :type type: str or ~teamsapi.models.enum
    :param name: Name of the action that will be used as button title
    :type name: str
    :param id: Action Id
    :type id: str
    """

    _attribute_map = {
        'type': {'key': '@type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': '@id', 'type': 'str'},
    }

    def __init__(self, type=None, name=None, id=None):
        super(O365ConnectorCardActionBase, self).__init__()
        self.type = type
        self.name = name
        self.id = id
