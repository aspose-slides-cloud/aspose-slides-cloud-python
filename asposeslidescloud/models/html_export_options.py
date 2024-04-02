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

class HtmlExportOptions(ExportOptions):


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
        'save_as_zip': 'bool',
        'sub_directory_name': 'str',
        'show_hidden_slides': 'bool',
        'svg_responsive_layout': 'bool',
        'jpeg_quality': 'int',
        'pictures_compression': 'str',
        'delete_pictures_cropped_areas': 'bool',
        'slides_layout_options': 'SlidesLayoutOptions'
    }

    attribute_map = {
        'default_regular_font': 'defaultRegularFont',
        'font_fallback_rules': 'fontFallbackRules',
        'font_subst_rules': 'fontSubstRules',
        'format': 'format',
        'save_as_zip': 'saveAsZip',
        'sub_directory_name': 'subDirectoryName',
        'show_hidden_slides': 'showHiddenSlides',
        'svg_responsive_layout': 'svgResponsiveLayout',
        'jpeg_quality': 'jpegQuality',
        'pictures_compression': 'picturesCompression',
        'delete_pictures_cropped_areas': 'deletePicturesCroppedAreas',
        'slides_layout_options': 'slidesLayoutOptions'
    }

    type_determiners = {
        'format': 'html',
    }

    def __init__(self, default_regular_font=None, font_fallback_rules=None, font_subst_rules=None, format='html', save_as_zip=None, sub_directory_name=None, show_hidden_slides=None, svg_responsive_layout=None, jpeg_quality=None, pictures_compression=None, delete_pictures_cropped_areas=None, slides_layout_options=None):  # noqa: E501
        """HtmlExportOptions - a model defined in Swagger"""  # noqa: E501
        super(HtmlExportOptions, self).__init__(default_regular_font, font_fallback_rules, font_subst_rules, format)

        self._save_as_zip = None
        self._sub_directory_name = None
        self._show_hidden_slides = None
        self._svg_responsive_layout = None
        self._jpeg_quality = None
        self._pictures_compression = None
        self._delete_pictures_cropped_areas = None
        self._slides_layout_options = None
        self.format = 'html'

        if save_as_zip is not None:
            self.save_as_zip = save_as_zip
        if sub_directory_name is not None:
            self.sub_directory_name = sub_directory_name
        if show_hidden_slides is not None:
            self.show_hidden_slides = show_hidden_slides
        if svg_responsive_layout is not None:
            self.svg_responsive_layout = svg_responsive_layout
        if jpeg_quality is not None:
            self.jpeg_quality = jpeg_quality
        if pictures_compression is not None:
            self.pictures_compression = pictures_compression
        if delete_pictures_cropped_areas is not None:
            self.delete_pictures_cropped_areas = delete_pictures_cropped_areas
        if slides_layout_options is not None:
            self.slides_layout_options = slides_layout_options

    @property
    def save_as_zip(self):
        """Gets the save_as_zip of this HtmlExportOptions.  # noqa: E501

        Get or sets flag for save presentation as zip file  # noqa: E501

        :return: The save_as_zip of this HtmlExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._save_as_zip

    @save_as_zip.setter
    def save_as_zip(self, save_as_zip):
        """Sets the save_as_zip of this HtmlExportOptions.

        Get or sets flag for save presentation as zip file  # noqa: E501

        :param save_as_zip: The save_as_zip of this HtmlExportOptions.  # noqa: E501
        :type: bool
        """
        self._save_as_zip = save_as_zip

    @property
    def sub_directory_name(self):
        """Gets the sub_directory_name of this HtmlExportOptions.  # noqa: E501

        Get or set name of subdirectory in zip-file for store external files  # noqa: E501

        :return: The sub_directory_name of this HtmlExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._sub_directory_name

    @sub_directory_name.setter
    def sub_directory_name(self, sub_directory_name):
        """Sets the sub_directory_name of this HtmlExportOptions.

        Get or set name of subdirectory in zip-file for store external files  # noqa: E501

        :param sub_directory_name: The sub_directory_name of this HtmlExportOptions.  # noqa: E501
        :type: str
        """
        self._sub_directory_name = sub_directory_name

    @property
    def show_hidden_slides(self):
        """Gets the show_hidden_slides of this HtmlExportOptions.  # noqa: E501

        Specifies whether the generated document should include hidden slides or not. Default is false.   # noqa: E501

        :return: The show_hidden_slides of this HtmlExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._show_hidden_slides

    @show_hidden_slides.setter
    def show_hidden_slides(self, show_hidden_slides):
        """Sets the show_hidden_slides of this HtmlExportOptions.

        Specifies whether the generated document should include hidden slides or not. Default is false.   # noqa: E501

        :param show_hidden_slides: The show_hidden_slides of this HtmlExportOptions.  # noqa: E501
        :type: bool
        """
        self._show_hidden_slides = show_hidden_slides

    @property
    def svg_responsive_layout(self):
        """Gets the svg_responsive_layout of this HtmlExportOptions.  # noqa: E501

        True to make layout responsive by excluding width and height attributes from svg container.  # noqa: E501

        :return: The svg_responsive_layout of this HtmlExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._svg_responsive_layout

    @svg_responsive_layout.setter
    def svg_responsive_layout(self, svg_responsive_layout):
        """Sets the svg_responsive_layout of this HtmlExportOptions.

        True to make layout responsive by excluding width and height attributes from svg container.  # noqa: E501

        :param svg_responsive_layout: The svg_responsive_layout of this HtmlExportOptions.  # noqa: E501
        :type: bool
        """
        self._svg_responsive_layout = svg_responsive_layout

    @property
    def jpeg_quality(self):
        """Gets the jpeg_quality of this HtmlExportOptions.  # noqa: E501

        Returns or sets a value determining the quality of the JPEG images inside PDF document.  # noqa: E501

        :return: The jpeg_quality of this HtmlExportOptions.  # noqa: E501
        :rtype: int
        """
        return self._jpeg_quality

    @jpeg_quality.setter
    def jpeg_quality(self, jpeg_quality):
        """Sets the jpeg_quality of this HtmlExportOptions.

        Returns or sets a value determining the quality of the JPEG images inside PDF document.  # noqa: E501

        :param jpeg_quality: The jpeg_quality of this HtmlExportOptions.  # noqa: E501
        :type: int
        """
        self._jpeg_quality = jpeg_quality

    @property
    def pictures_compression(self):
        """Gets the pictures_compression of this HtmlExportOptions.  # noqa: E501

        Represents the pictures compression level  # noqa: E501

        :return: The pictures_compression of this HtmlExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._pictures_compression

    @pictures_compression.setter
    def pictures_compression(self, pictures_compression):
        """Sets the pictures_compression of this HtmlExportOptions.

        Represents the pictures compression level  # noqa: E501

        :param pictures_compression: The pictures_compression of this HtmlExportOptions.  # noqa: E501
        :type: str
        """
        if pictures_compression is not None:
            allowed_values = ["Dpi330", "Dpi220", "Dpi150", "Dpi96", "Dpi72", "DocumentResolution"]  # noqa: E501
            if pictures_compression.isdigit():
                int_pictures_compression = int(pictures_compression)
                if int_pictures_compression < 0 or int_pictures_compression >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `pictures_compression` ({0}), must be one of {1}"  # noqa: E501
                        .format(pictures_compression, allowed_values)
                    )
                self._pictures_compression = allowed_values[int_pictures_compression]
                return
            if pictures_compression not in allowed_values:
                raise ValueError(
                    "Invalid value for `pictures_compression` ({0}), must be one of {1}"  # noqa: E501
                    .format(pictures_compression, allowed_values)
                )
        self._pictures_compression = pictures_compression

    @property
    def delete_pictures_cropped_areas(self):
        """Gets the delete_pictures_cropped_areas of this HtmlExportOptions.  # noqa: E501

        A boolean flag indicates if the cropped parts remain as part of the document. If true the cropped  parts will removed, if false they will be serialized in the document (which can possible lead to a  larger file)  # noqa: E501

        :return: The delete_pictures_cropped_areas of this HtmlExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._delete_pictures_cropped_areas

    @delete_pictures_cropped_areas.setter
    def delete_pictures_cropped_areas(self, delete_pictures_cropped_areas):
        """Sets the delete_pictures_cropped_areas of this HtmlExportOptions.

        A boolean flag indicates if the cropped parts remain as part of the document. If true the cropped  parts will removed, if false they will be serialized in the document (which can possible lead to a  larger file)  # noqa: E501

        :param delete_pictures_cropped_areas: The delete_pictures_cropped_areas of this HtmlExportOptions.  # noqa: E501
        :type: bool
        """
        self._delete_pictures_cropped_areas = delete_pictures_cropped_areas

    @property
    def slides_layout_options(self):
        """Gets the slides_layout_options of this HtmlExportOptions.  # noqa: E501

        Slides layouting options  # noqa: E501

        :return: The slides_layout_options of this HtmlExportOptions.  # noqa: E501
        :rtype: SlidesLayoutOptions
        """
        return self._slides_layout_options

    @slides_layout_options.setter
    def slides_layout_options(self, slides_layout_options):
        """Sets the slides_layout_options of this HtmlExportOptions.

        Slides layouting options  # noqa: E501

        :param slides_layout_options: The slides_layout_options of this HtmlExportOptions.  # noqa: E501
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
        if not isinstance(other, HtmlExportOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
