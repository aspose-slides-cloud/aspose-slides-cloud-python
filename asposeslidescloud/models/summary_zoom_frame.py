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

from asposeslidescloud.models.shape_base import ShapeBase

class SummaryZoomFrame(ShapeBase):


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
        'name': 'str',
        'width': 'float',
        'height': 'float',
        'alternative_text': 'str',
        'alternative_text_title': 'str',
        'hidden': 'bool',
        'is_decorative': 'bool',
        'x': 'float',
        'y': 'float',
        'z_order_position': 'int',
        'fill_format': 'FillFormat',
        'effect_format': 'EffectFormat',
        'three_d_format': 'ThreeDFormat',
        'line_format': 'LineFormat',
        'hyperlink_click': 'Hyperlink',
        'hyperlink_mouse_over': 'Hyperlink',
        'type': 'str',
        'zoom_layout': 'str',
        'sections': 'list[SummaryZoomSection]'
    }

    attribute_map = {
        'self_uri': 'selfUri',
        'alternate_links': 'alternateLinks',
        'name': 'name',
        'width': 'width',
        'height': 'height',
        'alternative_text': 'alternativeText',
        'alternative_text_title': 'alternativeTextTitle',
        'hidden': 'hidden',
        'is_decorative': 'isDecorative',
        'x': 'x',
        'y': 'y',
        'z_order_position': 'zOrderPosition',
        'fill_format': 'fillFormat',
        'effect_format': 'effectFormat',
        'three_d_format': 'threeDFormat',
        'line_format': 'lineFormat',
        'hyperlink_click': 'hyperlinkClick',
        'hyperlink_mouse_over': 'hyperlinkMouseOver',
        'type': 'type',
        'zoom_layout': 'zoomLayout',
        'sections': 'sections'
    }

    type_determiners = {
        'type': 'SummaryZoomFrame',
    }

    def __init__(self, self_uri=None, alternate_links=None, name=None, width=None, height=None, alternative_text=None, alternative_text_title=None, hidden=None, is_decorative=None, x=None, y=None, z_order_position=None, fill_format=None, effect_format=None, three_d_format=None, line_format=None, hyperlink_click=None, hyperlink_mouse_over=None, type='SummaryZoomFrame', zoom_layout=None, sections=None):  # noqa: E501
        """SummaryZoomFrame - a model defined in Swagger"""  # noqa: E501
        super(SummaryZoomFrame, self).__init__(self_uri, alternate_links, name, width, height, alternative_text, alternative_text_title, hidden, is_decorative, x, y, z_order_position, fill_format, effect_format, three_d_format, line_format, hyperlink_click, hyperlink_mouse_over, type)

        self._zoom_layout = None
        self._sections = None
        self.type = 'SummaryZoomFrame'

        if zoom_layout is not None:
            self.zoom_layout = zoom_layout
        if sections is not None:
            self.sections = sections

    @property
    def zoom_layout(self):
        """Gets the zoom_layout of this SummaryZoomFrame.  # noqa: E501

        Zoom layout type  # noqa: E501

        :return: The zoom_layout of this SummaryZoomFrame.  # noqa: E501
        :rtype: str
        """
        return self._zoom_layout

    @zoom_layout.setter
    def zoom_layout(self, zoom_layout):
        """Sets the zoom_layout of this SummaryZoomFrame.

        Zoom layout type  # noqa: E501

        :param zoom_layout: The zoom_layout of this SummaryZoomFrame.  # noqa: E501
        :type: str
        """
        if zoom_layout is not None:
            allowed_values = ["GridLayout", "FixedLayout"]  # noqa: E501
            if zoom_layout.isdigit():
                int_zoom_layout = int(zoom_layout)
                if int_zoom_layout < 0 or int_zoom_layout >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `zoom_layout` ({0}), must be one of {1}"  # noqa: E501
                        .format(zoom_layout, allowed_values)
                    )
                self._zoom_layout = allowed_values[int_zoom_layout]
                return
            if zoom_layout not in allowed_values:
                raise ValueError(
                    "Invalid value for `zoom_layout` ({0}), must be one of {1}"  # noqa: E501
                    .format(zoom_layout, allowed_values)
                )
        self._zoom_layout = zoom_layout

    @property
    def sections(self):
        """Gets the sections of this SummaryZoomFrame.  # noqa: E501

        Zoom frame sections  # noqa: E501

        :return: The sections of this SummaryZoomFrame.  # noqa: E501
        :rtype: list[SummaryZoomSection]
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this SummaryZoomFrame.

        Zoom frame sections  # noqa: E501

        :param sections: The sections of this SummaryZoomFrame.  # noqa: E501
        :type: list[SummaryZoomSection]
        """
        self._sections = sections

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
        if not isinstance(other, SummaryZoomFrame):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
