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


class ImageTransformEffect(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str'
    }

    attribute_map = {
        'type': 'type'
    }

    type_determiners = {
    }

    def __init__(self, type=None):  # noqa: E501
        """ImageTransformEffect - a model defined in Swagger"""  # noqa: E501

        self._type = None

        if type is not None:
            self.type = type

    @property
    def type(self):
        """Gets the type of this ImageTransformEffect.  # noqa: E501


        :return: The type of this ImageTransformEffect.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImageTransformEffect.


        :param type: The type of this ImageTransformEffect.  # noqa: E501
        :type: str
        """
        if type is not None:
            allowed_values = ["AlphaBiLevel", "AlphaCeiling", "AlphaFloor", "AlphaInverse", "AlphaModulate", "AlphaModulateFixed", "AlphaReplace", "BiLevel", "Blur", "ColorChange", "ColorReplace", "Duotone", "FillOverlay", "GrayScale", "Hsl", "Luminance", "Tint"]  # noqa: E501
            if type.isdigit():
                int_type = int(type)
                if int_type < 0 or int_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                        .format(type, allowed_values)
                    )
                self._type = allowed_values[int_type]
                return
            if type not in allowed_values:
                raise ValueError(
                    "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                    .format(type, allowed_values)
                )
        self._type = type

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
        if not isinstance(other, ImageTransformEffect):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
