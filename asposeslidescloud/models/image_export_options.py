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

from asposeslidescloud.models.image_export_options_base import ImageExportOptionsBase

class ImageExportOptions(ImageExportOptionsBase):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'default_regular_font': 'str',
        'font_fallback_rules': 'list[FontFallbackRule]',
        'font_subst_rules': 'list[FontSubstRule]',
        'format': 'str',
        'height': 'int',
        'width': 'int',
        'show_hidden_slides': 'bool',
        'slides_layout_options': 'SlidesLayoutOptions'
    }

    attribute_map = {
        'default_regular_font': 'defaultRegularFont',
        'font_fallback_rules': 'fontFallbackRules',
        'font_subst_rules': 'fontSubstRules',
        'format': 'format',
        'height': 'height',
        'width': 'width',
        'show_hidden_slides': 'showHiddenSlides',
        'slides_layout_options': 'slidesLayoutOptions'
    }

    type_determiners = {
        'format': 'image',
    }

    def __init__(self, default_regular_font=None, font_fallback_rules=None, font_subst_rules=None, format='image', height=None, width=None, show_hidden_slides=None, slides_layout_options=None):  # noqa: E501
        """ImageExportOptions - a model defined in Swagger"""  # noqa: E501
        super(ImageExportOptions, self).__init__(default_regular_font, font_fallback_rules, font_subst_rules, format, height, width)

        self._show_hidden_slides = None
        self._slides_layout_options = None
        self.format = 'image'

        if show_hidden_slides is not None:
            self.show_hidden_slides = show_hidden_slides
        if slides_layout_options is not None:
            self.slides_layout_options = slides_layout_options

    @property
    def show_hidden_slides(self):
        """Gets the show_hidden_slides of this ImageExportOptions.  # noqa: E501

        Show hidden slides. If true, hidden are exported.  # noqa: E501

        :return: The show_hidden_slides of this ImageExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._show_hidden_slides

    @show_hidden_slides.setter
    def show_hidden_slides(self, show_hidden_slides):
        """Sets the show_hidden_slides of this ImageExportOptions.

        Show hidden slides. If true, hidden are exported.  # noqa: E501

        :param show_hidden_slides: The show_hidden_slides of this ImageExportOptions.  # noqa: E501
        :type: bool
        """
        self._show_hidden_slides = show_hidden_slides

    @property
    def slides_layout_options(self):
        """Gets the slides_layout_options of this ImageExportOptions.  # noqa: E501

        Slides layouting options  # noqa: E501

        :return: The slides_layout_options of this ImageExportOptions.  # noqa: E501
        :rtype: SlidesLayoutOptions
        """
        return self._slides_layout_options

    @slides_layout_options.setter
    def slides_layout_options(self, slides_layout_options):
        """Sets the slides_layout_options of this ImageExportOptions.

        Slides layouting options  # noqa: E501

        :param slides_layout_options: The slides_layout_options of this ImageExportOptions.  # noqa: E501
        :type: SlidesLayoutOptions
        """
        self._slides_layout_options = slides_layout_options

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
        if not isinstance(other, ImageExportOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
