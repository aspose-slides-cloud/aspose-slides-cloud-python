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

class VbaModule(ResourceBase):


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
        'source_code': 'str',
        'references': 'list[VbaReference]'
    }

    attribute_map = {
        'self_uri': 'selfUri',
        'alternate_links': 'alternateLinks',
        'name': 'name',
        'source_code': 'sourceCode',
        'references': 'references'
    }

    type_determiners = {
    }

    def __init__(self, self_uri=None, alternate_links=None, name=None, source_code=None, references=None):  # noqa: E501
        """VbaModule - a model defined in Swagger"""  # noqa: E501
        super(VbaModule, self).__init__(self_uri, alternate_links)

        self._name = None
        self._source_code = None
        self._references = None

        if name is not None:
            self.name = name
        if source_code is not None:
            self.source_code = source_code
        if references is not None:
            self.references = references

    @property
    def name(self):
        """Gets the name of this VbaModule.  # noqa: E501

        VBA module name.   # noqa: E501

        :return: The name of this VbaModule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VbaModule.

        VBA module name.   # noqa: E501

        :param name: The name of this VbaModule.  # noqa: E501
        :type: str
        """
        self._name = name

    @property
    def source_code(self):
        """Gets the source_code of this VbaModule.  # noqa: E501

        VBA module source code.  # noqa: E501

        :return: The source_code of this VbaModule.  # noqa: E501
        :rtype: str
        """
        return self._source_code

    @source_code.setter
    def source_code(self, source_code):
        """Sets the source_code of this VbaModule.

        VBA module source code.  # noqa: E501

        :param source_code: The source_code of this VbaModule.  # noqa: E501
        :type: str
        """
        self._source_code = source_code

    @property
    def references(self):
        """Gets the references of this VbaModule.  # noqa: E501

        List of references.   # noqa: E501

        :return: The references of this VbaModule.  # noqa: E501
        :rtype: list[VbaReference]
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this VbaModule.

        List of references.   # noqa: E501

        :param references: The references of this VbaModule.  # noqa: E501
        :type: list[VbaReference]
        """
        self._references = references

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
        if not isinstance(other, VbaModule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
