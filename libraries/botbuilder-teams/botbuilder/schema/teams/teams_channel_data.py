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


class TeamsChannelData(Model):
    """Channel data specific to messages received in Microsoft Teams.

    :param channel: Information about the channel in which the message was
     sent
    :type channel: ~teamsapi.models.ChannelInfo
    :param event_type: Type of event.
    :type event_type: str
    :param team: Information about the team in which the message was sent
    :type team: ~teamsapi.models.TeamInfo
    :param notification: Notification settings for the message
    :type notification: ~teamsapi.models.NotificationInfo
    :param tenant: Information about the tenant in which the message was sent
    :type tenant: ~teamsapi.models.TenantInfo
    """

    _attribute_map = {
        'channel': {'key': 'channel', 'type': 'ChannelInfo'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'team': {'key': 'team', 'type': 'TeamInfo'},
        'notification': {'key': 'notification', 'type': 'NotificationInfo'},
        'tenant': {'key': 'tenant', 'type': 'TenantInfo'},
    }

    def __init__(self, channel=None, event_type=None, team=None, notification=None, tenant=None):
        super(TeamsChannelData, self).__init__()
        self.channel = channel
        self.event_type = event_type
        self.team = team
        self.notification = notification
        self.tenant = tenant
