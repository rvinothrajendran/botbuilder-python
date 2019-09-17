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


class TaskModuleTaskInfo(Model):
    """Metadata for a Task Module.

    :param title: Appears below the app name and to the right of the app icon.
    :type title: str
    :param height: This can be a number, representing the task module's height
     in pixels, or a string, one of: small, medium, large.
    :type height: object
    :param width: This can be a number, representing the task module's width
     in pixels, or a string, one of: small, medium, large.
    :type width: object
    :param url: The URL of what is loaded as an iframe inside the task module.
     One of url or card is required.
    :type url: str
    :param card: The JSON for the Adaptive card to appear in the task module.
    :type card: ~teamsapi.models.Attachment
    :param fallback_url: If a client does not support the task module feature,
     this URL is opened in a browser tab.
    :type fallback_url: str
    :param completion_bot_id: If a client does not support the task module
     feature, this URL is opened in a browser tab.
    :type completion_bot_id: str
    """

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'height': {'key': 'height', 'type': 'object'},
        'width': {'key': 'width', 'type': 'object'},
        'url': {'key': 'url', 'type': 'str'},
        'card': {'key': 'card', 'type': 'Attachment'},
        'fallback_url': {'key': 'fallbackUrl', 'type': 'str'},
        'completion_bot_id': {'key': 'completionBotId', 'type': 'str'},
    }

    def __init__(self, title=None, height=None, width=None, url=None, card=None, fallback_url=None, completion_bot_id=None):
        super(TaskModuleTaskInfo, self).__init__()
        self.title = title
        self.height = height
        self.width = width
        self.url = url
        self.card = card
        self.fallback_url = fallback_url
        self.completion_bot_id = completion_bot_id