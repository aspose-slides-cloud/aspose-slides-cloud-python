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


class CommonSlideViewProperties(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'scale': 'int',
        'variable_scale': 'bool',
        'drawing_guides': 'list[DrawingGuide]'
    }

    attribute_map = {
        'scale': 'scale',
        'variable_scale': 'variableScale',
        'drawing_guides': 'drawingGuides'
    }

    type_determiners = {
    }

    def __init__(self, scale=None, variable_scale=None, drawing_guides=None):  # noqa: E501
        """CommonSlideViewProperties - a model defined in Swagger"""  # noqa: E501

        self._scale = None
        self._variable_scale = None
        self._drawing_guides = None

        if scale is not None:
            self.scale = scale
        if variable_scale is not None:
            self.variable_scale = variable_scale
        if drawing_guides is not None:
            self.drawing_guides = drawing_guides

    @property
    def scale(self):
        """Gets the scale of this CommonSlideViewProperties.  # noqa: E501

        The view scaling ratio (percentage).  # noqa: E501

        :return: The scale of this CommonSlideViewProperties.  # noqa: E501
        :rtype: int
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this CommonSlideViewProperties.

        The view scaling ratio (percentage).  # noqa: E501

        :param scale: The scale of this CommonSlideViewProperties.  # noqa: E501
        :type: int
        """
        self._scale = scale

    @property
    def variable_scale(self):
        """Gets the variable_scale of this CommonSlideViewProperties.  # noqa: E501

        True if the view content should automatically scale to best fit the current window size.  # noqa: E501

        :return: The variable_scale of this CommonSlideViewProperties.  # noqa: E501
        :rtype: bool
        """
        return self._variable_scale

    @variable_scale.setter
    def variable_scale(self, variable_scale):
        """Sets the variable_scale of this CommonSlideViewProperties.

        True if the view content should automatically scale to best fit the current window size.  # noqa: E501

        :param variable_scale: The variable_scale of this CommonSlideViewProperties.  # noqa: E501
        :type: bool
        """
        self._variable_scale = variable_scale

    @property
    def drawing_guides(self):
        """Gets the drawing_guides of this CommonSlideViewProperties.  # noqa: E501

        Drawing guides  # noqa: E501

        :return: The drawing_guides of this CommonSlideViewProperties.  # noqa: E501
        :rtype: list[DrawingGuide]
        """
        return self._drawing_guides

    @drawing_guides.setter
    def drawing_guides(self, drawing_guides):
        """Sets the drawing_guides of this CommonSlideViewProperties.

        Drawing guides  # noqa: E501

        :param drawing_guides: The drawing_guides of this CommonSlideViewProperties.  # noqa: E501
        :type: list[DrawingGuide]
        """
        self._drawing_guides = drawing_guides

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
        if not isinstance(other, CommonSlideViewProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
