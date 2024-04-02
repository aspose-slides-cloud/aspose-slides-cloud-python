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

from asposeslidescloud.models.slides_layout_options import SlidesLayoutOptions

class HandoutLayoutingOptions(SlidesLayoutOptions):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'layout_type': 'str',
        'handout': 'str',
        'print_slide_numbers': 'bool',
        'print_comments': 'bool',
        'print_frame_slide': 'bool'
    }

    attribute_map = {
        'layout_type': 'layoutType',
        'handout': 'handout',
        'print_slide_numbers': 'printSlideNumbers',
        'print_comments': 'printComments',
        'print_frame_slide': 'printFrameSlide'
    }

    type_determiners = {
        'layoutType': 'Handout',
    }

    def __init__(self, layout_type='Handout', handout=None, print_slide_numbers=None, print_comments=None, print_frame_slide=None):  # noqa: E501
        """HandoutLayoutingOptions - a model defined in Swagger"""  # noqa: E501
        super(HandoutLayoutingOptions, self).__init__(layout_type)

        self._handout = None
        self._print_slide_numbers = None
        self._print_comments = None
        self._print_frame_slide = None
        self.layout_type = 'Handout'

        if handout is not None:
            self.handout = handout
        if print_slide_numbers is not None:
            self.print_slide_numbers = print_slide_numbers
        if print_comments is not None:
            self.print_comments = print_comments
        if print_frame_slide is not None:
            self.print_frame_slide = print_frame_slide

    @property
    def handout(self):
        """Gets the handout of this HandoutLayoutingOptions.  # noqa: E501

        Specified how many pages and in what sequence will be placed on the page.  # noqa: E501

        :return: The handout of this HandoutLayoutingOptions.  # noqa: E501
        :rtype: str
        """
        return self._handout

    @handout.setter
    def handout(self, handout):
        """Sets the handout of this HandoutLayoutingOptions.

        Specified how many pages and in what sequence will be placed on the page.  # noqa: E501

        :param handout: The handout of this HandoutLayoutingOptions.  # noqa: E501
        :type: str
        """
        if handout is not None:
            allowed_values = ["Handouts1", "Handouts2", "Handouts3", "Handouts4Horizontal", "Handouts4Vertical", "Handouts6Horizontal", "Handouts6Vertical", "Handouts9Horizontal", "Handouts9Vertical"]  # noqa: E501
            if handout.isdigit():
                int_handout = int(handout)
                if int_handout < 0 or int_handout >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `handout` ({0}), must be one of {1}"  # noqa: E501
                        .format(handout, allowed_values)
                    )
                self._handout = allowed_values[int_handout]
                return
            if handout not in allowed_values:
                raise ValueError(
                    "Invalid value for `handout` ({0}), must be one of {1}"  # noqa: E501
                    .format(handout, allowed_values)
                )
        self._handout = handout

    @property
    def print_slide_numbers(self):
        """Gets the print_slide_numbers of this HandoutLayoutingOptions.  # noqa: E501

        True to print the displayed slide numbers.  # noqa: E501

        :return: The print_slide_numbers of this HandoutLayoutingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._print_slide_numbers

    @print_slide_numbers.setter
    def print_slide_numbers(self, print_slide_numbers):
        """Sets the print_slide_numbers of this HandoutLayoutingOptions.

        True to print the displayed slide numbers.  # noqa: E501

        :param print_slide_numbers: The print_slide_numbers of this HandoutLayoutingOptions.  # noqa: E501
        :type: bool
        """
        self._print_slide_numbers = print_slide_numbers

    @property
    def print_comments(self):
        """Gets the print_comments of this HandoutLayoutingOptions.  # noqa: E501

        True to display comments on slide.  # noqa: E501

        :return: The print_comments of this HandoutLayoutingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._print_comments

    @print_comments.setter
    def print_comments(self, print_comments):
        """Sets the print_comments of this HandoutLayoutingOptions.

        True to display comments on slide.  # noqa: E501

        :param print_comments: The print_comments of this HandoutLayoutingOptions.  # noqa: E501
        :type: bool
        """
        self._print_comments = print_comments

    @property
    def print_frame_slide(self):
        """Gets the print_frame_slide of this HandoutLayoutingOptions.  # noqa: E501

        True to draw frames around the displayed slides.  # noqa: E501

        :return: The print_frame_slide of this HandoutLayoutingOptions.  # noqa: E501
        :rtype: bool
        """
        return self._print_frame_slide

    @print_frame_slide.setter
    def print_frame_slide(self, print_frame_slide):
        """Sets the print_frame_slide of this HandoutLayoutingOptions.

        True to draw frames around the displayed slides.  # noqa: E501

        :param print_frame_slide: The print_frame_slide of this HandoutLayoutingOptions.  # noqa: E501
        :type: bool
        """
        self._print_frame_slide = print_frame_slide

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
        if not isinstance(other, HandoutLayoutingOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
