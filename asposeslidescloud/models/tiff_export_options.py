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

class TiffExportOptions(ImageExportOptionsBase):


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
        'compression': 'str',
        'dpi_x': 'int',
        'dpi_y': 'int',
        'show_hidden_slides': 'bool',
        'pixel_format': 'str',
        'slides_layout_options': 'SlidesLayoutOptions',
        'bw_conversion_mode': 'str'
    }

    attribute_map = {
        'default_regular_font': 'defaultRegularFont',
        'font_fallback_rules': 'fontFallbackRules',
        'font_subst_rules': 'fontSubstRules',
        'format': 'format',
        'height': 'height',
        'width': 'width',
        'compression': 'compression',
        'dpi_x': 'dpiX',
        'dpi_y': 'dpiY',
        'show_hidden_slides': 'showHiddenSlides',
        'pixel_format': 'pixelFormat',
        'slides_layout_options': 'slidesLayoutOptions',
        'bw_conversion_mode': 'bwConversionMode'
    }

    type_determiners = {
        'format': 'tiff',
    }

    def __init__(self, default_regular_font=None, font_fallback_rules=None, font_subst_rules=None, format='tiff', height=None, width=None, compression=None, dpi_x=None, dpi_y=None, show_hidden_slides=None, pixel_format=None, slides_layout_options=None, bw_conversion_mode=None):  # noqa: E501
        """TiffExportOptions - a model defined in Swagger"""  # noqa: E501
        super(TiffExportOptions, self).__init__(default_regular_font, font_fallback_rules, font_subst_rules, format, height, width)

        self._compression = None
        self._dpi_x = None
        self._dpi_y = None
        self._show_hidden_slides = None
        self._pixel_format = None
        self._slides_layout_options = None
        self._bw_conversion_mode = None
        self.format = 'tiff'

        if compression is not None:
            self.compression = compression
        if dpi_x is not None:
            self.dpi_x = dpi_x
        if dpi_y is not None:
            self.dpi_y = dpi_y
        if show_hidden_slides is not None:
            self.show_hidden_slides = show_hidden_slides
        if pixel_format is not None:
            self.pixel_format = pixel_format
        if slides_layout_options is not None:
            self.slides_layout_options = slides_layout_options
        if bw_conversion_mode is not None:
            self.bw_conversion_mode = bw_conversion_mode

    @property
    def compression(self):
        """Gets the compression of this TiffExportOptions.  # noqa: E501

        Compression type.  # noqa: E501

        :return: The compression of this TiffExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._compression

    @compression.setter
    def compression(self, compression):
        """Sets the compression of this TiffExportOptions.

        Compression type.  # noqa: E501

        :param compression: The compression of this TiffExportOptions.  # noqa: E501
        :type: str
        """
        if compression is not None:
            allowed_values = ["Default", "None", "CCITT3", "CCITT4", "LZW", "RLE"]  # noqa: E501
            if compression.isdigit():
                int_compression = int(compression)
                if int_compression < 0 or int_compression >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `compression` ({0}), must be one of {1}"  # noqa: E501
                        .format(compression, allowed_values)
                    )
                self._compression = allowed_values[int_compression]
                return
            if compression not in allowed_values:
                raise ValueError(
                    "Invalid value for `compression` ({0}), must be one of {1}"  # noqa: E501
                    .format(compression, allowed_values)
                )
        self._compression = compression

    @property
    def dpi_x(self):
        """Gets the dpi_x of this TiffExportOptions.  # noqa: E501

        Horizontal resolution, in dots per inch.  # noqa: E501

        :return: The dpi_x of this TiffExportOptions.  # noqa: E501
        :rtype: int
        """
        return self._dpi_x

    @dpi_x.setter
    def dpi_x(self, dpi_x):
        """Sets the dpi_x of this TiffExportOptions.

        Horizontal resolution, in dots per inch.  # noqa: E501

        :param dpi_x: The dpi_x of this TiffExportOptions.  # noqa: E501
        :type: int
        """
        self._dpi_x = dpi_x

    @property
    def dpi_y(self):
        """Gets the dpi_y of this TiffExportOptions.  # noqa: E501

        Vertical resolution, in dots per inch.  # noqa: E501

        :return: The dpi_y of this TiffExportOptions.  # noqa: E501
        :rtype: int
        """
        return self._dpi_y

    @dpi_y.setter
    def dpi_y(self, dpi_y):
        """Sets the dpi_y of this TiffExportOptions.

        Vertical resolution, in dots per inch.  # noqa: E501

        :param dpi_y: The dpi_y of this TiffExportOptions.  # noqa: E501
        :type: int
        """
        self._dpi_y = dpi_y

    @property
    def show_hidden_slides(self):
        """Gets the show_hidden_slides of this TiffExportOptions.  # noqa: E501

        Specifies whether the generated document should include hidden slides or not. Default is false.   # noqa: E501

        :return: The show_hidden_slides of this TiffExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._show_hidden_slides

    @show_hidden_slides.setter
    def show_hidden_slides(self, show_hidden_slides):
        """Sets the show_hidden_slides of this TiffExportOptions.

        Specifies whether the generated document should include hidden slides or not. Default is false.   # noqa: E501

        :param show_hidden_slides: The show_hidden_slides of this TiffExportOptions.  # noqa: E501
        :type: bool
        """
        self._show_hidden_slides = show_hidden_slides

    @property
    def pixel_format(self):
        """Gets the pixel_format of this TiffExportOptions.  # noqa: E501

        Specifies the pixel format for the generated images. Read/write ImagePixelFormat.  # noqa: E501

        :return: The pixel_format of this TiffExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._pixel_format

    @pixel_format.setter
    def pixel_format(self, pixel_format):
        """Sets the pixel_format of this TiffExportOptions.

        Specifies the pixel format for the generated images. Read/write ImagePixelFormat.  # noqa: E501

        :param pixel_format: The pixel_format of this TiffExportOptions.  # noqa: E501
        :type: str
        """
        if pixel_format is not None:
            allowed_values = ["Format1bppIndexed", "Format4bppIndexed", "Format8bppIndexed", "Format24bppRgb", "Format32bppArgb"]  # noqa: E501
            if pixel_format.isdigit():
                int_pixel_format = int(pixel_format)
                if int_pixel_format < 0 or int_pixel_format >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `pixel_format` ({0}), must be one of {1}"  # noqa: E501
                        .format(pixel_format, allowed_values)
                    )
                self._pixel_format = allowed_values[int_pixel_format]
                return
            if pixel_format not in allowed_values:
                raise ValueError(
                    "Invalid value for `pixel_format` ({0}), must be one of {1}"  # noqa: E501
                    .format(pixel_format, allowed_values)
                )
        self._pixel_format = pixel_format

    @property
    def slides_layout_options(self):
        """Gets the slides_layout_options of this TiffExportOptions.  # noqa: E501

        Slides layouting options  # noqa: E501

        :return: The slides_layout_options of this TiffExportOptions.  # noqa: E501
        :rtype: SlidesLayoutOptions
        """
        return self._slides_layout_options

    @slides_layout_options.setter
    def slides_layout_options(self, slides_layout_options):
        """Sets the slides_layout_options of this TiffExportOptions.

        Slides layouting options  # noqa: E501

        :param slides_layout_options: The slides_layout_options of this TiffExportOptions.  # noqa: E501
        :type: SlidesLayoutOptions
        """
        self._slides_layout_options = slides_layout_options

    @property
    def bw_conversion_mode(self):
        """Gets the bw_conversion_mode of this TiffExportOptions.  # noqa: E501

        Specifies the algorithm for converting a color image into a black and white image. This option will applied only if Aspose.Slides.Export.TiffOptions.CompressionType is set to Aspose.Slides.Export.TiffCompressionTypes.CCITT4 or Aspose.Slides.Export.TiffCompressionTypes.CCITT3.  # noqa: E501

        :return: The bw_conversion_mode of this TiffExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._bw_conversion_mode

    @bw_conversion_mode.setter
    def bw_conversion_mode(self, bw_conversion_mode):
        """Sets the bw_conversion_mode of this TiffExportOptions.

        Specifies the algorithm for converting a color image into a black and white image. This option will applied only if Aspose.Slides.Export.TiffOptions.CompressionType is set to Aspose.Slides.Export.TiffCompressionTypes.CCITT4 or Aspose.Slides.Export.TiffCompressionTypes.CCITT3.  # noqa: E501

        :param bw_conversion_mode: The bw_conversion_mode of this TiffExportOptions.  # noqa: E501
        :type: str
        """
        if bw_conversion_mode is not None:
            allowed_values = ["Default", "Dithering", "DitheringFloydSteinberg", "Auto", "AutoOtsu", "Threshold25", "Threshold50", "Threshold75"]  # noqa: E501
            if bw_conversion_mode.isdigit():
                int_bw_conversion_mode = int(bw_conversion_mode)
                if int_bw_conversion_mode < 0 or int_bw_conversion_mode >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `bw_conversion_mode` ({0}), must be one of {1}"  # noqa: E501
                        .format(bw_conversion_mode, allowed_values)
                    )
                self._bw_conversion_mode = allowed_values[int_bw_conversion_mode]
                return
            if bw_conversion_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `bw_conversion_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(bw_conversion_mode, allowed_values)
                )
        self._bw_conversion_mode = bw_conversion_mode

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
        if not isinstance(other, TiffExportOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
