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

class Section(ResourceBase):


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
        'first_slide_index': 'int',
        'slide_list': 'list[ResourceUriElement]'
    }

    attribute_map = {
        'self_uri': 'selfUri',
        'alternate_links': 'alternateLinks',
        'name': 'name',
        'first_slide_index': 'firstSlideIndex',
        'slide_list': 'slideList'
    }

    type_determiners = {
    }

    def __init__(self, self_uri=None, alternate_links=None, name=None, first_slide_index=None, slide_list=None):  # noqa: E501
        """Section - a model defined in Swagger"""  # noqa: E501
        super(Section, self).__init__(self_uri, alternate_links)

        self._name = None
        self._first_slide_index = None
        self._slide_list = None

        if name is not None:
            self.name = name
        self.first_slide_index = first_slide_index
        if slide_list is not None:
            self.slide_list = slide_list

    @property
    def name(self):
        """Gets the name of this Section.  # noqa: E501

        Name.  # noqa: E501

        :return: The name of this Section.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Section.

        Name.  # noqa: E501

        :param name: The name of this Section.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def first_slide_index(self):
        """Gets the first_slide_index of this Section.  # noqa: E501

        One-based index of slide with which the section starts.  # noqa: E501

        :return: The first_slide_index of this Section.  # noqa: E501
        :rtype: int
        """
        return self._first_slide_index

    @first_slide_index.setter
    def first_slide_index(self, first_slide_index):
        """Sets the first_slide_index of this Section.

        One-based index of slide with which the section starts.  # noqa: E501

        :param first_slide_index: The first_slide_index of this Section.  # noqa: E501
        :type: int
        """
        self._first_slide_index = first_slide_index

    @property
    def slide_list(self):
        """Gets the slide_list of this Section.  # noqa: E501

        Links to the shapes contained in the section.  # noqa: E501

        :return: The slide_list of this Section.  # noqa: E501
        :rtype: list[ResourceUriElement]
        """
        return self._slide_list

    @slide_list.setter
    def slide_list(self, slide_list):
        """Sets the slide_list of this Section.

        Links to the shapes contained in the section.  # noqa: E501

        :param slide_list: The slide_list of this Section.  # noqa: E501
        :type: list[ResourceUriElement]
        """
        self._slide_list = slide_list

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
        if not isinstance(other, Section):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
