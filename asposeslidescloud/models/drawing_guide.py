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


class DrawingGuide(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'orientation': 'str',
        'position': 'float'
    }

    attribute_map = {
        'orientation': 'orientation',
        'position': 'position'
    }

    type_determiners = {
    }

    def __init__(self, orientation=None, position=None):  # noqa: E501
        """DrawingGuide - a model defined in Swagger"""  # noqa: E501

        self._orientation = None
        self._position = None

        self.orientation = orientation
        self.position = position

    @property
    def orientation(self):
        """Gets the orientation of this DrawingGuide.  # noqa: E501

        Last used view mode.  # noqa: E501

        :return: The orientation of this DrawingGuide.  # noqa: E501
        :rtype: str
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this DrawingGuide.

        Last used view mode.  # noqa: E501

        :param orientation: The orientation of this DrawingGuide.  # noqa: E501
        :type: str
        """
        if orientation is not None:
            allowed_values = ["Horizontal", "Vertical"]  # noqa: E501
            if orientation.isdigit():
                int_orientation = int(orientation)
                if int_orientation < 0 or int_orientation >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `orientation` ({0}), must be one of {1}"  # noqa: E501
                        .format(orientation, allowed_values)
                    )
                self._orientation = allowed_values[int_orientation]
                return
            if orientation not in allowed_values:
                raise ValueError(
                    "Invalid value for `orientation` ({0}), must be one of {1}"  # noqa: E501
                    .format(orientation, allowed_values)
                )
        self._orientation = orientation

    @property
    def position(self):
        """Gets the position of this DrawingGuide.  # noqa: E501

        Horizontal bar state.  # noqa: E501

        :return: The position of this DrawingGuide.  # noqa: E501
        :rtype: float
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this DrawingGuide.

        Horizontal bar state.  # noqa: E501

        :param position: The position of this DrawingGuide.  # noqa: E501
        :type: float
        """
        self._position = position

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
        if not isinstance(other, DrawingGuide):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
