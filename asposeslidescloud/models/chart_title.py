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


class ChartTitle(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'text': 'str',
        'x': 'float',
        'y': 'float',
        'width': 'float',
        'height': 'float',
        'overlay': 'bool',
        'fill_format': 'FillFormat',
        'effect_format': 'EffectFormat',
        'line_format': 'LineFormat'
    }

    attribute_map = {
        'text': 'text',
        'x': 'x',
        'y': 'y',
        'width': 'width',
        'height': 'height',
        'overlay': 'overlay',
        'fill_format': 'fillFormat',
        'effect_format': 'effectFormat',
        'line_format': 'lineFormat'
    }

    type_determiners = {
    }

    def __init__(self, text=None, x=None, y=None, width=None, height=None, overlay=None, fill_format=None, effect_format=None, line_format=None):  # noqa: E501
        """ChartTitle - a model defined in Swagger"""  # noqa: E501

        self._text = None
        self._x = None
        self._y = None
        self._width = None
        self._height = None
        self._overlay = None
        self._fill_format = None
        self._effect_format = None
        self._line_format = None

        if text is not None:
            self.text = text
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if overlay is not None:
            self.overlay = overlay
        if fill_format is not None:
            self.fill_format = fill_format
        if effect_format is not None:
            self.effect_format = effect_format
        if line_format is not None:
            self.line_format = line_format

    @property
    def text(self):
        """Gets the text of this ChartTitle.  # noqa: E501

        Get or sets the text.  # noqa: E501

        :return: The text of this ChartTitle.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ChartTitle.

        Get or sets the text.  # noqa: E501

        :param text: The text of this ChartTitle.  # noqa: E501
        :type: str
        """
        self._text = text

    @property
    def x(self):
        """Gets the x of this ChartTitle.  # noqa: E501

        the X location  # noqa: E501

        :return: The x of this ChartTitle.  # noqa: E501
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this ChartTitle.

        the X location  # noqa: E501

        :param x: The x of this ChartTitle.  # noqa: E501
        :type: float
        """
        self._x = x

    @property
    def y(self):
        """Gets the y of this ChartTitle.  # noqa: E501

        the Y location  # noqa: E501

        :return: The y of this ChartTitle.  # noqa: E501
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this ChartTitle.

        the Y location  # noqa: E501

        :param y: The y of this ChartTitle.  # noqa: E501
        :type: float
        """
        self._y = y

    @property
    def width(self):
        """Gets the width of this ChartTitle.  # noqa: E501

        Width  # noqa: E501

        :return: The width of this ChartTitle.  # noqa: E501
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ChartTitle.

        Width  # noqa: E501

        :param width: The width of this ChartTitle.  # noqa: E501
        :type: float
        """
        self._width = width

    @property
    def height(self):
        """Gets the height of this ChartTitle.  # noqa: E501

        Height  # noqa: E501

        :return: The height of this ChartTitle.  # noqa: E501
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ChartTitle.

        Height  # noqa: E501

        :param height: The height of this ChartTitle.  # noqa: E501
        :type: float
        """
        self._height = height

    @property
    def overlay(self):
        """Gets the overlay of this ChartTitle.  # noqa: E501

        true if other elements are allowed to overlay the legend  # noqa: E501

        :return: The overlay of this ChartTitle.  # noqa: E501
        :rtype: bool
        """
        return self._overlay

    @overlay.setter
    def overlay(self, overlay):
        """Sets the overlay of this ChartTitle.

        true if other elements are allowed to overlay the legend  # noqa: E501

        :param overlay: The overlay of this ChartTitle.  # noqa: E501
        :type: bool
        """
        self._overlay = overlay

    @property
    def fill_format(self):
        """Gets the fill_format of this ChartTitle.  # noqa: E501

        Get or sets the fill format.  # noqa: E501

        :return: The fill_format of this ChartTitle.  # noqa: E501
        :rtype: FillFormat
        """
        return self._fill_format

    @fill_format.setter
    def fill_format(self, fill_format):
        """Sets the fill_format of this ChartTitle.

        Get or sets the fill format.  # noqa: E501

        :param fill_format: The fill_format of this ChartTitle.  # noqa: E501
        :type: FillFormat
        """
        self._fill_format = fill_format

    @property
    def effect_format(self):
        """Gets the effect_format of this ChartTitle.  # noqa: E501

        Get or sets the effect format.  # noqa: E501

        :return: The effect_format of this ChartTitle.  # noqa: E501
        :rtype: EffectFormat
        """
        return self._effect_format

    @effect_format.setter
    def effect_format(self, effect_format):
        """Sets the effect_format of this ChartTitle.

        Get or sets the effect format.  # noqa: E501

        :param effect_format: The effect_format of this ChartTitle.  # noqa: E501
        :type: EffectFormat
        """
        self._effect_format = effect_format

    @property
    def line_format(self):
        """Gets the line_format of this ChartTitle.  # noqa: E501

        Get or sets the line format.  # noqa: E501

        :return: The line_format of this ChartTitle.  # noqa: E501
        :rtype: LineFormat
        """
        return self._line_format

    @line_format.setter
    def line_format(self, line_format):
        """Sets the line_format of this ChartTitle.

        Get or sets the line format.  # noqa: E501

        :param line_format: The line_format of this ChartTitle.  # noqa: E501
        :type: LineFormat
        """
        self._line_format = line_format

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
        if not isinstance(other, ChartTitle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
