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

from .o365_connector_card_input_base import O365ConnectorCardInputBase


class O365ConnectorCardDateInput(O365ConnectorCardInputBase):
    """O365 connector card date input.

    :param type: Input type name. Possible values include: 'textInput',
     'dateInput', 'multichoiceInput'
    :type type: str or ~teamsapi.models.enum
    :param id: Input Id. It must be unique per entire O365 connector card.
    :type id: str
    :param is_required: Define if this input is a required field. Default
     value is false.
    :type is_required: bool
    :param title: Input title that will be shown as the placeholder
    :type title: str
    :param value: Default value for this input field
    :type value: str
    :param include_time: Include time input field. Default value  is false
     (date only).
    :type include_time: bool
    """

    _attribute_map = {
        'type': {'key': '@type', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'is_required': {'key': 'isRequired', 'type': 'bool'},
        'title': {'key': 'title', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'include_time': {'key': 'includeTime', 'type': 'bool'},
    }

    def __init__(self, type=None, id=None, is_required=None, title=None, value=None, include_time=None):
        super(O365ConnectorCardDateInput, self).__init__(type=type, id=id, is_required=is_required, title=title, value=value)
        self.include_time = include_time