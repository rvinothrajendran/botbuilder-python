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


class FileConsentCardResponse(Model):
    """Represents the value of the invoke activity sent when the user acts on a
    file consent card.

    :param action: The action the user took. Possible values include:
     'accept', 'decline'
    :type action: str or ~teamsapi.models.enum
    :param context: The context associated with the action.
    :type context: object
    :param upload_info: If the user accepted the file, contains information
     about the file to be uploaded.
    :type upload_info: ~teamsapi.models.FileUploadInfo
    """

    _attribute_map = {
        'action': {'key': 'action', 'type': 'str'},
        'context': {'key': 'context', 'type': 'object'},
        'upload_info': {'key': 'uploadInfo', 'type': 'FileUploadInfo'},
    }

    def __init__(self, action=None, context=None, upload_info=None):
        super(FileConsentCardResponse, self).__init__()
        self.action = action
        self.context = context
        self.upload_info = upload_info