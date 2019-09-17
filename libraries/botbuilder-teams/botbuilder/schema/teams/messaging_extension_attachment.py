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

from .attachment import Attachment


class MessagingExtensionAttachment(Attachment):
    """Messaging extension attachment.

    :param content_type: mimetype/Contenttype for the file
    :type content_type: str
    :param content_url: Content Url
    :type content_url: str
    :param content: Embedded content
    :type content: object
    :param name: (OPTIONAL) The name of the attachment
    :type name: str
    :param thumbnail_url: (OPTIONAL) Thumbnail associated with attachment
    :type thumbnail_url: str
    :param preview:
    :type preview: ~teamsapi.models.Attachment
    """

    _attribute_map = {
        'content_type': {'key': 'contentType', 'type': 'str'},
        'content_url': {'key': 'contentUrl', 'type': 'str'},
        'content': {'key': 'content', 'type': 'object'},
        'name': {'key': 'name', 'type': 'str'},
        'thumbnail_url': {'key': 'thumbnailUrl', 'type': 'str'},
        'preview': {'key': 'preview', 'type': 'Attachment'},
    }

    def __init__(self, content_type=None, content_url=None, content=None, name=None, thumbnail_url=None, preview=None):
        super(MessagingExtensionAttachment, self).__init__(content_type=content_type, content_url=content_url, content=content, name=name, thumbnail_url=thumbnail_url)
        self.preview = preview
