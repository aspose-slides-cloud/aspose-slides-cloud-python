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

class CaptionTrack(ResourceBase):


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
        'caption_id': 'str',
        'label': 'str',
        'data_as_string': 'str'
    }

    attribute_map = {
        'self_uri': 'selfUri',
        'alternate_links': 'alternateLinks',
        'caption_id': 'captionId',
        'label': 'label',
        'data_as_string': 'dataAsString'
    }

    type_determiners = {
    }

    def __init__(self, self_uri=None, alternate_links=None, caption_id=None, label=None, data_as_string=None):  # noqa: E501
        """CaptionTrack - a model defined in Swagger"""  # noqa: E501
        super(CaptionTrack, self).__init__(self_uri, alternate_links)

        self._caption_id = None
        self._label = None
        self._data_as_string = None

        self.caption_id = caption_id
        if label is not None:
            self.label = label
        if data_as_string is not None:
            self.data_as_string = data_as_string

    @property
    def caption_id(self):
        """Gets the caption_id of this CaptionTrack.  # noqa: E501

        Caption ID.  # noqa: E501

        :return: The caption_id of this CaptionTrack.  # noqa: E501
        :rtype: str
        """
        return self._caption_id

    @caption_id.setter
    def caption_id(self, caption_id):
        """Sets the caption_id of this CaptionTrack.

        Caption ID.  # noqa: E501

        :param caption_id: The caption_id of this CaptionTrack.  # noqa: E501
        :type: str
        """
        self._caption_id = caption_id

    @property
    def label(self):
        """Gets the label of this CaptionTrack.  # noqa: E501

        Label.  # noqa: E501

        :return: The label of this CaptionTrack.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CaptionTrack.

        Label.  # noqa: E501

        :param label: The label of this CaptionTrack.  # noqa: E501
        :type: str
        """
        self._label = label

    @property
    def data_as_string(self):
        """Gets the data_as_string of this CaptionTrack.  # noqa: E501

        Caption track data as string.  # noqa: E501

        :return: The data_as_string of this CaptionTrack.  # noqa: E501
        :rtype: str
        """
        return self._data_as_string

    @data_as_string.setter
    def data_as_string(self, data_as_string):
        """Sets the data_as_string of this CaptionTrack.

        Caption track data as string.  # noqa: E501

        :param data_as_string: The data_as_string of this CaptionTrack.  # noqa: E501
        :type: str
        """
        self._data_as_string = data_as_string

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
        if not isinstance(other, CaptionTrack):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
