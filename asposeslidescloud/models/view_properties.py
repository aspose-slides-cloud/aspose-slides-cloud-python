# coding: utf-8

# -----------------------------------------------------------------------------------
# <copyright company="Aspose">
#   Copyright (c) 2018 Aspose.Slides for Cloud
# </copyright>
# <summary>
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# </summary>
# -----------------------------------------------------------------------------------

import pprint
import re  # noqa: F401

import six

from asposeslidescloud.models.resource_base import ResourceBase

class ViewProperties(ResourceBase):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'self_uri': 'ResourceUri',
        'alternate_links': 'list[ResourceUri]',
        'last_view': 'str',
        'horizontal_bar_state': 'str',
        'vertical_bar_state': 'str',
        'prefer_single_view': 'bool',
        'restored_left': 'NormalViewRestoredProperties',
        'restored_top': 'NormalViewRestoredProperties',
        'slide_view_properties': 'CommonSlideViewProperties',
        'notes_view_properties': 'CommonSlideViewProperties',
        'show_comments': 'str',
        'grid_spacing': 'float'
    }

    attribute_map = {
        'self_uri': 'selfUri',
        'alternate_links': 'alternateLinks',
        'last_view': 'lastView',
        'horizontal_bar_state': 'horizontalBarState',
        'vertical_bar_state': 'verticalBarState',
        'prefer_single_view': 'preferSingleView',
        'restored_left': 'restoredLeft',
        'restored_top': 'restoredTop',
        'slide_view_properties': 'slideViewProperties',
        'notes_view_properties': 'notesViewProperties',
        'show_comments': 'showComments',
        'grid_spacing': 'gridSpacing'
    }

    type_determiners = {
    }

    def __init__(self, self_uri=None, alternate_links=None, last_view=None, horizontal_bar_state=None, vertical_bar_state=None, prefer_single_view=None, restored_left=None, restored_top=None, slide_view_properties=None, notes_view_properties=None, show_comments=None, grid_spacing=None):  # noqa: E501
        """ViewProperties - a model defined in Swagger"""  # noqa: E501
        super(ViewProperties, self).__init__(self_uri, alternate_links)

        self._last_view = None
        self._horizontal_bar_state = None
        self._vertical_bar_state = None
        self._prefer_single_view = None
        self._restored_left = None
        self._restored_top = None
        self._slide_view_properties = None
        self._notes_view_properties = None
        self._show_comments = None
        self._grid_spacing = None

        if last_view is not None:
            self.last_view = last_view
        if horizontal_bar_state is not None:
            self.horizontal_bar_state = horizontal_bar_state
        if vertical_bar_state is not None:
            self.vertical_bar_state = vertical_bar_state
        if prefer_single_view is not None:
            self.prefer_single_view = prefer_single_view
        if restored_left is not None:
            self.restored_left = restored_left
        if restored_top is not None:
            self.restored_top = restored_top
        if slide_view_properties is not None:
            self.slide_view_properties = slide_view_properties
        if notes_view_properties is not None:
            self.notes_view_properties = notes_view_properties
        if show_comments is not None:
            self.show_comments = show_comments
        if grid_spacing is not None:
            self.grid_spacing = grid_spacing

    @property
    def last_view(self):
        """Gets the last_view of this ViewProperties.  # noqa: E501

        Last used view mode.  # noqa: E501

        :return: The last_view of this ViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._last_view

    @last_view.setter
    def last_view(self, last_view):
        """Sets the last_view of this ViewProperties.

        Last used view mode.  # noqa: E501

        :param last_view: The last_view of this ViewProperties.  # noqa: E501
        :type: str
        """
        if last_view is not None:
            allowed_values = ["NotDefined", "SlideView", "SlideMasterView", "NotesView", "HandoutView", "NotesMasterView", "OutlineView", "SlideSorterView", "SlideThumbnailView"]  # noqa: E501
            if last_view.isdigit():
                int_last_view = int(last_view)
                if int_last_view < 0 or int_last_view >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `last_view` ({0}), must be one of {1}"  # noqa: E501
                        .format(last_view, allowed_values)
                    )
                self._last_view = allowed_values[int_last_view]
                return
            if last_view not in allowed_values:
                raise ValueError(
                    "Invalid value for `last_view` ({0}), must be one of {1}"  # noqa: E501
                    .format(last_view, allowed_values)
                )
        self._last_view = last_view

    @property
    def horizontal_bar_state(self):
        """Gets the horizontal_bar_state of this ViewProperties.  # noqa: E501

        Horizontal bar state.  # noqa: E501

        :return: The horizontal_bar_state of this ViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._horizontal_bar_state

    @horizontal_bar_state.setter
    def horizontal_bar_state(self, horizontal_bar_state):
        """Sets the horizontal_bar_state of this ViewProperties.

        Horizontal bar state.  # noqa: E501

        :param horizontal_bar_state: The horizontal_bar_state of this ViewProperties.  # noqa: E501
        :type: str
        """
        if horizontal_bar_state is not None:
            allowed_values = ["Minimized", "Restored", "Maximized"]  # noqa: E501
            if horizontal_bar_state.isdigit():
                int_horizontal_bar_state = int(horizontal_bar_state)
                if int_horizontal_bar_state < 0 or int_horizontal_bar_state >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `horizontal_bar_state` ({0}), must be one of {1}"  # noqa: E501
                        .format(horizontal_bar_state, allowed_values)
                    )
                self._horizontal_bar_state = allowed_values[int_horizontal_bar_state]
                return
            if horizontal_bar_state not in allowed_values:
                raise ValueError(
                    "Invalid value for `horizontal_bar_state` ({0}), must be one of {1}"  # noqa: E501
                    .format(horizontal_bar_state, allowed_values)
                )
        self._horizontal_bar_state = horizontal_bar_state

    @property
    def vertical_bar_state(self):
        """Gets the vertical_bar_state of this ViewProperties.  # noqa: E501

        Vertical bar state.  # noqa: E501

        :return: The vertical_bar_state of this ViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._vertical_bar_state

    @vertical_bar_state.setter
    def vertical_bar_state(self, vertical_bar_state):
        """Sets the vertical_bar_state of this ViewProperties.

        Vertical bar state.  # noqa: E501

        :param vertical_bar_state: The vertical_bar_state of this ViewProperties.  # noqa: E501
        :type: str
        """
        if vertical_bar_state is not None:
            allowed_values = ["Minimized", "Restored", "Maximized"]  # noqa: E501
            if vertical_bar_state.isdigit():
                int_vertical_bar_state = int(vertical_bar_state)
                if int_vertical_bar_state < 0 or int_vertical_bar_state >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `vertical_bar_state` ({0}), must be one of {1}"  # noqa: E501
                        .format(vertical_bar_state, allowed_values)
                    )
                self._vertical_bar_state = allowed_values[int_vertical_bar_state]
                return
            if vertical_bar_state not in allowed_values:
                raise ValueError(
                    "Invalid value for `vertical_bar_state` ({0}), must be one of {1}"  # noqa: E501
                    .format(vertical_bar_state, allowed_values)
                )
        self._vertical_bar_state = vertical_bar_state

    @property
    def prefer_single_view(self):
        """Gets the prefer_single_view of this ViewProperties.  # noqa: E501

        True to prefer single view.  # noqa: E501

        :return: The prefer_single_view of this ViewProperties.  # noqa: E501
        :rtype: bool
        """
        return self._prefer_single_view

    @prefer_single_view.setter
    def prefer_single_view(self, prefer_single_view):
        """Sets the prefer_single_view of this ViewProperties.

        True to prefer single view.  # noqa: E501

        :param prefer_single_view: The prefer_single_view of this ViewProperties.  # noqa: E501
        :type: bool
        """
        self._prefer_single_view = prefer_single_view

    @property
    def restored_left(self):
        """Gets the restored_left of this ViewProperties.  # noqa: E501

        The sizing of the side content region of the normal view, when the region is of a variable restored size.  # noqa: E501

        :return: The restored_left of this ViewProperties.  # noqa: E501
        :rtype: NormalViewRestoredProperties
        """
        return self._restored_left

    @restored_left.setter
    def restored_left(self, restored_left):
        """Sets the restored_left of this ViewProperties.

        The sizing of the side content region of the normal view, when the region is of a variable restored size.  # noqa: E501

        :param restored_left: The restored_left of this ViewProperties.  # noqa: E501
        :type: NormalViewRestoredProperties
        """
        self._restored_left = restored_left

    @property
    def restored_top(self):
        """Gets the restored_top of this ViewProperties.  # noqa: E501

        The sizing of the top slide region of the normal view, when the region is of a variable restored size.  # noqa: E501

        :return: The restored_top of this ViewProperties.  # noqa: E501
        :rtype: NormalViewRestoredProperties
        """
        return self._restored_top

    @restored_top.setter
    def restored_top(self, restored_top):
        """Sets the restored_top of this ViewProperties.

        The sizing of the top slide region of the normal view, when the region is of a variable restored size.  # noqa: E501

        :param restored_top: The restored_top of this ViewProperties.  # noqa: E501
        :type: NormalViewRestoredProperties
        """
        self._restored_top = restored_top

    @property
    def slide_view_properties(self):
        """Gets the slide_view_properties of this ViewProperties.  # noqa: E501

        Slide view mode properties.  # noqa: E501

        :return: The slide_view_properties of this ViewProperties.  # noqa: E501
        :rtype: CommonSlideViewProperties
        """
        return self._slide_view_properties

    @slide_view_properties.setter
    def slide_view_properties(self, slide_view_properties):
        """Sets the slide_view_properties of this ViewProperties.

        Slide view mode properties.  # noqa: E501

        :param slide_view_properties: The slide_view_properties of this ViewProperties.  # noqa: E501
        :type: CommonSlideViewProperties
        """
        self._slide_view_properties = slide_view_properties

    @property
    def notes_view_properties(self):
        """Gets the notes_view_properties of this ViewProperties.  # noqa: E501

        Notes view mode properties.  # noqa: E501

        :return: The notes_view_properties of this ViewProperties.  # noqa: E501
        :rtype: CommonSlideViewProperties
        """
        return self._notes_view_properties

    @notes_view_properties.setter
    def notes_view_properties(self, notes_view_properties):
        """Sets the notes_view_properties of this ViewProperties.

        Notes view mode properties.  # noqa: E501

        :param notes_view_properties: The notes_view_properties of this ViewProperties.  # noqa: E501
        :type: CommonSlideViewProperties
        """
        self._notes_view_properties = notes_view_properties

    @property
    def show_comments(self):
        """Gets the show_comments of this ViewProperties.  # noqa: E501

        True if the comments should be shown.  # noqa: E501

        :return: The show_comments of this ViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._show_comments

    @show_comments.setter
    def show_comments(self, show_comments):
        """Sets the show_comments of this ViewProperties.

        True if the comments should be shown.  # noqa: E501

        :param show_comments: The show_comments of this ViewProperties.  # noqa: E501
        :type: str
        """
        if show_comments is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if show_comments.isdigit():
                int_show_comments = int(show_comments)
                if int_show_comments < 0 or int_show_comments >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `show_comments` ({0}), must be one of {1}"  # noqa: E501
                        .format(show_comments, allowed_values)
                    )
                self._show_comments = allowed_values[int_show_comments]
                return
            if show_comments not in allowed_values:
                raise ValueError(
                    "Invalid value for `show_comments` ({0}), must be one of {1}"  # noqa: E501
                    .format(show_comments, allowed_values)
                )
        self._show_comments = show_comments

    @property
    def grid_spacing(self):
        """Gets the grid_spacing of this ViewProperties.  # noqa: E501

        The grid spacing that should be used for the grid underlying the presentation document, in points.  # noqa: E501

        :return: The grid_spacing of this ViewProperties.  # noqa: E501
        :rtype: float
        """
        return self._grid_spacing

    @grid_spacing.setter
    def grid_spacing(self, grid_spacing):
        """Sets the grid_spacing of this ViewProperties.

        The grid spacing that should be used for the grid underlying the presentation document, in points.  # noqa: E501

        :param grid_spacing: The grid_spacing of this ViewProperties.  # noqa: E501
        :type: float
        """
        self._grid_spacing = grid_spacing

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ViewProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
