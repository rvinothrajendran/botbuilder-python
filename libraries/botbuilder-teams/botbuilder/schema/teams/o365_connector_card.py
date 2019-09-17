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


class O365ConnectorCard(Model):
    """O365 connector card.

    :param title: Title of the item
    :type title: str
    :param text: Text for the card
    :type text: str
    :param summary: Summary for the card
    :type summary: str
    :param theme_color: Theme color for the card
    :type theme_color: str
    :param sections: Set of sections for the current card
    :type sections: list[~teamsapi.models.O365ConnectorCardSection]
    :param potential_action: Set of actions for the current card
    :type potential_action: list[~teamsapi.models.O365ConnectorCardActionBase]
    """

    _attribute_map = {
        'title': {'key': 'title', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'summary': {'key': 'summary', 'type': 'str'},
        'theme_color': {'key': 'themeColor', 'type': 'str'},
        'sections': {'key': 'sections', 'type': '[O365ConnectorCardSection]'},
        'potential_action': {'key': 'potentialAction', 'type': '[O365ConnectorCardActionBase]'},
    }

    def __init__(self, title=None, text=None, summary=None, theme_color=None, sections=None, potential_action=None):
        super(O365ConnectorCard, self).__init__()
        self.title = title
        self.text = text
        self.summary = summary
        self.theme_color = theme_color
        self.sections = sections
        self.potential_action = potential_action