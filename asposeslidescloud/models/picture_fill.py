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

from asposeslidescloud.models.fill_format import FillFormat

class PictureFill(FillFormat):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'type': 'str',
        'crop_bottom': 'float',
        'crop_left': 'float',
        'crop_right': 'float',
        'crop_top': 'float',
        'dpi': 'int',
        'tile_offset_x': 'float',
        'tile_offset_y': 'float',
        'tile_scale_x': 'float',
        'tile_scale_y': 'float',
        'tile_alignment': 'str',
        'tile_flip': 'str',
        'image': 'ResourceUri',
        'base64_data': 'str',
        'svg_data': 'str',
        'delete_picture_cropped_areas': 'bool',
        'resolution': 'float',
        'picture_fill_mode': 'str',
        'image_transform_list': 'list[ImageTransformEffect]'
    }

    attribute_map = {
        'type': 'type',
        'crop_bottom': 'cropBottom',
        'crop_left': 'cropLeft',
        'crop_right': 'cropRight',
        'crop_top': 'cropTop',
        'dpi': 'dpi',
        'tile_offset_x': 'tileOffsetX',
        'tile_offset_y': 'tileOffsetY',
        'tile_scale_x': 'tileScaleX',
        'tile_scale_y': 'tileScaleY',
        'tile_alignment': 'tileAlignment',
        'tile_flip': 'tileFlip',
        'image': 'image',
        'base64_data': 'base64Data',
        'svg_data': 'svgData',
        'delete_picture_cropped_areas': 'deletePictureCroppedAreas',
        'resolution': 'resolution',
        'picture_fill_mode': 'pictureFillMode',
        'image_transform_list': 'imageTransformList'
    }

    type_determiners = {
        'type': 'Picture',
    }

    def __init__(self, type='Picture', crop_bottom=None, crop_left=None, crop_right=None, crop_top=None, dpi=None, tile_offset_x=None, tile_offset_y=None, tile_scale_x=None, tile_scale_y=None, tile_alignment=None, tile_flip=None, image=None, base64_data=None, svg_data=None, delete_picture_cropped_areas=None, resolution=None, picture_fill_mode=None, image_transform_list=None):  # noqa: E501
        """PictureFill - a model defined in Swagger"""  # noqa: E501
        super(PictureFill, self).__init__(type)

        self._crop_bottom = None
        self._crop_left = None
        self._crop_right = None
        self._crop_top = None
        self._dpi = None
        self._tile_offset_x = None
        self._tile_offset_y = None
        self._tile_scale_x = None
        self._tile_scale_y = None
        self._tile_alignment = None
        self._tile_flip = None
        self._image = None
        self._base64_data = None
        self._svg_data = None
        self._delete_picture_cropped_areas = None
        self._resolution = None
        self._picture_fill_mode = None
        self._image_transform_list = None
        self.type = 'Picture'

        self.crop_bottom = crop_bottom
        self.crop_left = crop_left
        self.crop_right = crop_right
        self.crop_top = crop_top
        self.dpi = dpi
        if tile_offset_x is not None:
            self.tile_offset_x = tile_offset_x
        if tile_offset_y is not None:
            self.tile_offset_y = tile_offset_y
        if tile_scale_x is not None:
            self.tile_scale_x = tile_scale_x
        if tile_scale_y is not None:
            self.tile_scale_y = tile_scale_y
        if tile_alignment is not None:
            self.tile_alignment = tile_alignment
        if tile_flip is not None:
            self.tile_flip = tile_flip
        if image is not None:
            self.image = image
        if base64_data is not None:
            self.base64_data = base64_data
        if svg_data is not None:
            self.svg_data = svg_data
        if delete_picture_cropped_areas is not None:
            self.delete_picture_cropped_areas = delete_picture_cropped_areas
        if resolution is not None:
            self.resolution = resolution
        self.picture_fill_mode = picture_fill_mode
        if image_transform_list is not None:
            self.image_transform_list = image_transform_list

    @property
    def crop_bottom(self):
        """Gets the crop_bottom of this PictureFill.  # noqa: E501

        Percentage of image height that is cropped from the bottom.  # noqa: E501

        :return: The crop_bottom of this PictureFill.  # noqa: E501
        :rtype: float
        """
        return self._crop_bottom

    @crop_bottom.setter
    def crop_bottom(self, crop_bottom):
        """Sets the crop_bottom of this PictureFill.

        Percentage of image height that is cropped from the bottom.  # noqa: E501

        :param crop_bottom: The crop_bottom of this PictureFill.  # noqa: E501
        :type: float
        """
        self._crop_bottom = crop_bottom

    @property
    def crop_left(self):
        """Gets the crop_left of this PictureFill.  # noqa: E501

        Percentage of image height that is cropped from the left.  # noqa: E501

        :return: The crop_left of this PictureFill.  # noqa: E501
        :rtype: float
        """
        return self._crop_left

    @crop_left.setter
    def crop_left(self, crop_left):
        """Sets the crop_left of this PictureFill.

        Percentage of image height that is cropped from the left.  # noqa: E501

        :param crop_left: The crop_left of this PictureFill.  # noqa: E501
        :type: float
        """
        self._crop_left = crop_left

    @property
    def crop_right(self):
        """Gets the crop_right of this PictureFill.  # noqa: E501

        Percentage of image height that is cropped from the right.  # noqa: E501

        :return: The crop_right of this PictureFill.  # noqa: E501
        :rtype: float
        """
        return self._crop_right

    @crop_right.setter
    def crop_right(self, crop_right):
        """Sets the crop_right of this PictureFill.

        Percentage of image height that is cropped from the right.  # noqa: E501

        :param crop_right: The crop_right of this PictureFill.  # noqa: E501
        :type: float
        """
        self._crop_right = crop_right

    @property
    def crop_top(self):
        """Gets the crop_top of this PictureFill.  # noqa: E501

        Percentage of image height that is cropped from the top.  # noqa: E501

        :return: The crop_top of this PictureFill.  # noqa: E501
        :rtype: float
        """
        return self._crop_top

    @crop_top.setter
    def crop_top(self, crop_top):
        """Sets the crop_top of this PictureFill.

        Percentage of image height that is cropped from the top.  # noqa: E501

        :param crop_top: The crop_top of this PictureFill.  # noqa: E501
        :type: float
        """
        self._crop_top = crop_top

    @property
    def dpi(self):
        """Gets the dpi of this PictureFill.  # noqa: E501

        Picture resolution.  # noqa: E501

        :return: The dpi of this PictureFill.  # noqa: E501
        :rtype: int
        """
        return self._dpi

    @dpi.setter
    def dpi(self, dpi):
        """Sets the dpi of this PictureFill.

        Picture resolution.  # noqa: E501

        :param dpi: The dpi of this PictureFill.  # noqa: E501
        :type: int
        """
        self._dpi = dpi

    @property
    def tile_offset_x(self):
        """Gets the tile_offset_x of this PictureFill.  # noqa: E501

        The horizontal offset of the texture from the shape's origin in points. A positive value moves the texture to the right, while a negative value moves it to the left.  # noqa: E501

        :return: The tile_offset_x of this PictureFill.  # noqa: E501
        :rtype: float
        """
        return self._tile_offset_x

    @tile_offset_x.setter
    def tile_offset_x(self, tile_offset_x):
        """Sets the tile_offset_x of this PictureFill.

        The horizontal offset of the texture from the shape's origin in points. A positive value moves the texture to the right, while a negative value moves it to the left.  # noqa: E501

        :param tile_offset_x: The tile_offset_x of this PictureFill.  # noqa: E501
        :type: float
        """
        self._tile_offset_x = tile_offset_x

    @property
    def tile_offset_y(self):
        """Gets the tile_offset_y of this PictureFill.  # noqa: E501

        The vertical offset of the texture from the shape's origin in points. A positive value moves the texture down, while a negative value moves it up.  # noqa: E501

        :return: The tile_offset_y of this PictureFill.  # noqa: E501
        :rtype: float
        """
        return self._tile_offset_y

    @tile_offset_y.setter
    def tile_offset_y(self, tile_offset_y):
        """Sets the tile_offset_y of this PictureFill.

        The vertical offset of the texture from the shape's origin in points. A positive value moves the texture down, while a negative value moves it up.  # noqa: E501

        :param tile_offset_y: The tile_offset_y of this PictureFill.  # noqa: E501
        :type: float
        """
        self._tile_offset_y = tile_offset_y

    @property
    def tile_scale_x(self):
        """Gets the tile_scale_x of this PictureFill.  # noqa: E501

        The horizontal scale for the texture fill as a percentage.  # noqa: E501

        :return: The tile_scale_x of this PictureFill.  # noqa: E501
        :rtype: float
        """
        return self._tile_scale_x

    @tile_scale_x.setter
    def tile_scale_x(self, tile_scale_x):
        """Sets the tile_scale_x of this PictureFill.

        The horizontal scale for the texture fill as a percentage.  # noqa: E501

        :param tile_scale_x: The tile_scale_x of this PictureFill.  # noqa: E501
        :type: float
        """
        self._tile_scale_x = tile_scale_x

    @property
    def tile_scale_y(self):
        """Gets the tile_scale_y of this PictureFill.  # noqa: E501

        The vertical scale for the texture fill as a percentage.  # noqa: E501

        :return: The tile_scale_y of this PictureFill.  # noqa: E501
        :rtype: float
        """
        return self._tile_scale_y

    @tile_scale_y.setter
    def tile_scale_y(self, tile_scale_y):
        """Sets the tile_scale_y of this PictureFill.

        The vertical scale for the texture fill as a percentage.  # noqa: E501

        :param tile_scale_y: The tile_scale_y of this PictureFill.  # noqa: E501
        :type: float
        """
        self._tile_scale_y = tile_scale_y

    @property
    def tile_alignment(self):
        """Gets the tile_alignment of this PictureFill.  # noqa: E501

        The way texture is aligned within the shape. This setting controls the starting point of the texture pattern and how it repeats across the shape.  # noqa: E501

        :return: The tile_alignment of this PictureFill.  # noqa: E501
        :rtype: str
        """
        return self._tile_alignment

    @tile_alignment.setter
    def tile_alignment(self, tile_alignment):
        """Sets the tile_alignment of this PictureFill.

        The way texture is aligned within the shape. This setting controls the starting point of the texture pattern and how it repeats across the shape.  # noqa: E501

        :param tile_alignment: The tile_alignment of this PictureFill.  # noqa: E501
        :type: str
        """
        if tile_alignment is not None:
            allowed_values = ["TopLeft", "Top", "TopRight", "Left", "Center", "Right", "BottomLeft", "Bottom", "BottomRight", "NotDefined"]  # noqa: E501
            if tile_alignment.isdigit():
                int_tile_alignment = int(tile_alignment)
                if int_tile_alignment < 0 or int_tile_alignment >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `tile_alignment` ({0}), must be one of {1}"  # noqa: E501
                        .format(tile_alignment, allowed_values)
                    )
                self._tile_alignment = allowed_values[int_tile_alignment]
                return
            if tile_alignment not in allowed_values:
                raise ValueError(
                    "Invalid value for `tile_alignment` ({0}), must be one of {1}"  # noqa: E501
                    .format(tile_alignment, allowed_values)
                )
        self._tile_alignment = tile_alignment

    @property
    def tile_flip(self):
        """Gets the tile_flip of this PictureFill.  # noqa: E501

        Flips the texture tile around its horizontal, vertical or both axis.  # noqa: E501

        :return: The tile_flip of this PictureFill.  # noqa: E501
        :rtype: str
        """
        return self._tile_flip

    @tile_flip.setter
    def tile_flip(self, tile_flip):
        """Sets the tile_flip of this PictureFill.

        Flips the texture tile around its horizontal, vertical or both axis.  # noqa: E501

        :param tile_flip: The tile_flip of this PictureFill.  # noqa: E501
        :type: str
        """
        if tile_flip is not None:
            allowed_values = ["NoFlip", "FlipX", "FlipY", "FlipBoth", "NotDefined"]  # noqa: E501
            if tile_flip.isdigit():
                int_tile_flip = int(tile_flip)
                if int_tile_flip < 0 or int_tile_flip >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `tile_flip` ({0}), must be one of {1}"  # noqa: E501
                        .format(tile_flip, allowed_values)
                    )
                self._tile_flip = allowed_values[int_tile_flip]
                return
            if tile_flip not in allowed_values:
                raise ValueError(
                    "Invalid value for `tile_flip` ({0}), must be one of {1}"  # noqa: E501
                    .format(tile_flip, allowed_values)
                )
        self._tile_flip = tile_flip

    @property
    def image(self):
        """Gets the image of this PictureFill.  # noqa: E501

        Internal image link.  # noqa: E501

        :return: The image of this PictureFill.  # noqa: E501
        :rtype: ResourceUri
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this PictureFill.

        Internal image link.  # noqa: E501

        :param image: The image of this PictureFill.  # noqa: E501
        :type: ResourceUri
        """
        self._image = image

    @property
    def base64_data(self):
        """Gets the base64_data of this PictureFill.  # noqa: E501

        Base 64 image data.  # noqa: E501

        :return: The base64_data of this PictureFill.  # noqa: E501
        :rtype: str
        """
        return self._base64_data

    @base64_data.setter
    def base64_data(self, base64_data):
        """Sets the base64_data of this PictureFill.

        Base 64 image data.  # noqa: E501

        :param base64_data: The base64_data of this PictureFill.  # noqa: E501
        :type: str
        """
        self._base64_data = base64_data

    @property
    def svg_data(self):
        """Gets the svg_data of this PictureFill.  # noqa: E501

        SVG image data.  # noqa: E501

        :return: The svg_data of this PictureFill.  # noqa: E501
        :rtype: str
        """
        return self._svg_data

    @svg_data.setter
    def svg_data(self, svg_data):
        """Sets the svg_data of this PictureFill.

        SVG image data.  # noqa: E501

        :param svg_data: The svg_data of this PictureFill.  # noqa: E501
        :type: str
        """
        self._svg_data = svg_data

    @property
    def delete_picture_cropped_areas(self):
        """Gets the delete_picture_cropped_areas of this PictureFill.  # noqa: E501

        true to delete picture cropped areas on save.  # noqa: E501

        :return: The delete_picture_cropped_areas of this PictureFill.  # noqa: E501
        :rtype: bool
        """
        return self._delete_picture_cropped_areas

    @delete_picture_cropped_areas.setter
    def delete_picture_cropped_areas(self, delete_picture_cropped_areas):
        """Sets the delete_picture_cropped_areas of this PictureFill.

        true to delete picture cropped areas on save.  # noqa: E501

        :param delete_picture_cropped_areas: The delete_picture_cropped_areas of this PictureFill.  # noqa: E501
        :type: bool
        """
        self._delete_picture_cropped_areas = delete_picture_cropped_areas

    @property
    def resolution(self):
        """Gets the resolution of this PictureFill.  # noqa: E501

        true to compress the picture image with the specified resolution (in dpi) on save.  # noqa: E501

        :return: The resolution of this PictureFill.  # noqa: E501
        :rtype: float
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this PictureFill.

        true to compress the picture image with the specified resolution (in dpi) on save.  # noqa: E501

        :param resolution: The resolution of this PictureFill.  # noqa: E501
        :type: float
        """
        self._resolution = resolution

    @property
    def picture_fill_mode(self):
        """Gets the picture_fill_mode of this PictureFill.  # noqa: E501

        Fill mode.  # noqa: E501

        :return: The picture_fill_mode of this PictureFill.  # noqa: E501
        :rtype: str
        """
        return self._picture_fill_mode

    @picture_fill_mode.setter
    def picture_fill_mode(self, picture_fill_mode):
        """Sets the picture_fill_mode of this PictureFill.

        Fill mode.  # noqa: E501

        :param picture_fill_mode: The picture_fill_mode of this PictureFill.  # noqa: E501
        :type: str
        """
        if picture_fill_mode is not None:
            allowed_values = ["Tile", "Stretch"]  # noqa: E501
            if picture_fill_mode.isdigit():
                int_picture_fill_mode = int(picture_fill_mode)
                if int_picture_fill_mode < 0 or int_picture_fill_mode >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `picture_fill_mode` ({0}), must be one of {1}"  # noqa: E501
                        .format(picture_fill_mode, allowed_values)
                    )
                self._picture_fill_mode = allowed_values[int_picture_fill_mode]
                return
            if picture_fill_mode not in allowed_values:
                raise ValueError(
                    "Invalid value for `picture_fill_mode` ({0}), must be one of {1}"  # noqa: E501
                    .format(picture_fill_mode, allowed_values)
                )
        self._picture_fill_mode = picture_fill_mode

    @property
    def image_transform_list(self):
        """Gets the image_transform_list of this PictureFill.  # noqa: E501

        Image transform effects.  # noqa: E501

        :return: The image_transform_list of this PictureFill.  # noqa: E501
        :rtype: list[ImageTransformEffect]
        """
        return self._image_transform_list

    @image_transform_list.setter
    def image_transform_list(self, image_transform_list):
        """Sets the image_transform_list of this PictureFill.

        Image transform effects.  # noqa: E501

        :param image_transform_list: The image_transform_list of this PictureFill.  # noqa: E501
        :type: list[ImageTransformEffect]
        """
        self._image_transform_list = image_transform_list

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
        if not isinstance(other, PictureFill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
