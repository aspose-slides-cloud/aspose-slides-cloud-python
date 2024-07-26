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

from asposeslidescloud.models.export_options import ExportOptions

class PptxExportOptions(ExportOptions):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_regular_font': 'str',
        'gradient_style': 'str',
        'font_fallback_rules': 'list[FontFallbackRule]',
        'font_subst_rules': 'list[FontSubstRule]',
        'format': 'str',
        'conformance': 'str',
        'zip64_mode': 'str'
    }

    attribute_map = {
        'default_regular_font': 'defaultRegularFont',
        'gradient_style': 'gradientStyle',
        'font_fallback_rules': 'fontFallbackRules',
        'font_subst_rules': 'fontSubstRules',
        'format': 'format',
        'conformance': 'conformance',
        'zip64_mode': 'zip64Mode'
    }

    type_determiners = {
        'format': 'pptx',
    }

    def __init__(self, default_regular_font=None, gradient_style=None, font_fallback_rules=None, font_subst_rules=None, format='pptx', conformance=None, zip64_mode=None):  # noqa: E501
        """PptxExportOptions - a model defined in Swagger"""  # noqa: E501
        super(PptxExportOptions, self).__init__(default_regular_font, gradient_style, font_fallback_rules, font_subst_rules, format)

        self._conformance = None
        self._zip64_mode = None
        self.format = 'pptx'

        if conformance is not None:
            self.conformance = conformance
        if zip64_mode is not None:
            self.zip64_mode = zip64_mode

    @property
    def conformance(self):
        """Gets the conformance of this PptxExportOptions.  # noqa: E501

        The conformance class to which the PresentationML document conforms.  # noqa: E501

        :return: The conformance of this PptxExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._conformance

    @conformance.setter
    def conformance(self, conformance):
        """Sets the conformance of this PptxExportOptions.

        The conformance class to which the PresentationML document conforms.  # noqa: E501

        :param conformance: The conformance of this PptxExportOptions.  # noqa: E501
        :type: str
        """
        if conformance is not None:
            allowed_values = ["Ecma376", "Iso29500Transitional", "Iso29500Strict"]  # noqa: E501
            if conformance.isdigit():
                int_conformance = int(conformance)
                if int_conformance < 0 or int_conformance >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `conformance` ({0}), must be one of {1}"  # noqa: E501
                        .format(conformance, allowed_values)
                    )
                self._conformance = allowed_values[int_conformance]
                return
            if conformance not in allowed_values:
                raise ValueError(
                    "Invalid value for `conformance` ({0}), must be one of {1}"  # noqa: E501
                    .format(conformance, allowed_values)
                )
        self._conformance = conformance

    @property
    def zip64_mode(self):
        """Gets the zip64_mode of this PptxExportOptions.  # noqa: E501

        Specifies whether the ZIP64 format is used for the Presentation document. The default value is Zip64Mode.IfNecessary.  # noqa: E501

        :return: The zip64_mode of this PptxExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._zip64_mode

    @zip64_mode.setter
    def zip64_mode(self, zip64_mode):
        """Sets the zip64_mode of this PptxExportOptions.

        Specifies whether the ZIP64 format is used for the Presentation document. The default value is Zip64Mode.IfNecessary.  # noqa: E501

        :param zip64_mode: The zip64_mode of this PptxExportOptions.  # noqa: E501
        :type: str
        """
        if zip64_mode is not None:
            allowed_values = ["Never", "IfNecessary", "Always"]  # noqa: E501
            if zip64_mode.isdigit():
                int_zip64_mode = int(zip64_mode)
                if int_zip64_mode < 0 or int_zip64_mode >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `zip64_mode` ({0}), must be one of {1}"  # noqa: E501
                        .format(zip64_mode, allowed_values)
                    )
                self._zip64_mode = allowed_values[int_zip64_mode]
                return
            if zip64_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `zip64_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(zip64_mode, allowed_values)
                )
        self._zip64_mode = zip64_mode

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
        if not isinstance(other, PptxExportOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
