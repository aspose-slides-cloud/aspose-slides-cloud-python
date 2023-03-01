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


class TextFrameFormat(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'three_d_format': 'ThreeDFormat',
        'transform': 'str',
        'margin_left': 'float',
        'margin_right': 'float',
        'margin_top': 'float',
        'margin_bottom': 'float',
        'wrap_text': 'str',
        'anchoring_type': 'str',
        'center_text': 'str',
        'text_vertical_type': 'str',
        'autofit_type': 'str',
        'column_count': 'int',
        'column_spacing': 'float',
        'keep_text_flat': 'bool',
        'rotation_angle': 'float',
        'default_paragraph_format': 'ParagraphFormat'
    }

    attribute_map = {
        'three_d_format': 'threeDFormat',
        'transform': 'transform',
        'margin_left': 'marginLeft',
        'margin_right': 'marginRight',
        'margin_top': 'marginTop',
        'margin_bottom': 'marginBottom',
        'wrap_text': 'wrapText',
        'anchoring_type': 'anchoringType',
        'center_text': 'centerText',
        'text_vertical_type': 'textVerticalType',
        'autofit_type': 'autofitType',
        'column_count': 'columnCount',
        'column_spacing': 'columnSpacing',
        'keep_text_flat': 'keepTextFlat',
        'rotation_angle': 'rotationAngle',
        'default_paragraph_format': 'defaultParagraphFormat'
    }

    type_determiners = {
    }

    def __init__(self, three_d_format=None, transform=None, margin_left=None, margin_right=None, margin_top=None, margin_bottom=None, wrap_text=None, anchoring_type=None, center_text=None, text_vertical_type=None, autofit_type=None, column_count=None, column_spacing=None, keep_text_flat=None, rotation_angle=None, default_paragraph_format=None):  # noqa: E501
        """TextFrameFormat - a model defined in Swagger"""  # noqa: E501

        self._three_d_format = None
        self._transform = None
        self._margin_left = None
        self._margin_right = None
        self._margin_top = None
        self._margin_bottom = None
        self._wrap_text = None
        self._anchoring_type = None
        self._center_text = None
        self._text_vertical_type = None
        self._autofit_type = None
        self._column_count = None
        self._column_spacing = None
        self._keep_text_flat = None
        self._rotation_angle = None
        self._default_paragraph_format = None

        if three_d_format is not None:
            self.three_d_format = three_d_format
        if transform is not None:
            self.transform = transform
        if margin_left is not None:
            self.margin_left = margin_left
        if margin_right is not None:
            self.margin_right = margin_right
        if margin_top is not None:
            self.margin_top = margin_top
        if margin_bottom is not None:
            self.margin_bottom = margin_bottom
        if wrap_text is not None:
            self.wrap_text = wrap_text
        if anchoring_type is not None:
            self.anchoring_type = anchoring_type
        if center_text is not None:
            self.center_text = center_text
        if text_vertical_type is not None:
            self.text_vertical_type = text_vertical_type
        if autofit_type is not None:
            self.autofit_type = autofit_type
        if column_count is not None:
            self.column_count = column_count
        if column_spacing is not None:
            self.column_spacing = column_spacing
        if keep_text_flat is not None:
            self.keep_text_flat = keep_text_flat
        if rotation_angle is not None:
            self.rotation_angle = rotation_angle
        if default_paragraph_format is not None:
            self.default_paragraph_format = default_paragraph_format

    @property
    def three_d_format(self):
        """Gets the three_d_format of this TextFrameFormat.  # noqa: E501

        Represents 3d effect properties for a text.  # noqa: E501

        :return: The three_d_format of this TextFrameFormat.  # noqa: E501
        :rtype: ThreeDFormat
        """
        return self._three_d_format

    @three_d_format.setter
    def three_d_format(self, three_d_format):
        """Sets the three_d_format of this TextFrameFormat.

        Represents 3d effect properties for a text.  # noqa: E501

        :param three_d_format: The three_d_format of this TextFrameFormat.  # noqa: E501
        :type: ThreeDFormat
        """
        self._three_d_format = three_d_format

    @property
    def transform(self):
        """Gets the transform of this TextFrameFormat.  # noqa: E501

        Gets or sets text wrapping shape.  # noqa: E501

        :return: The transform of this TextFrameFormat.  # noqa: E501
        :rtype: str
        """
        return self._transform

    @transform.setter
    def transform(self, transform):
        """Sets the transform of this TextFrameFormat.

        Gets or sets text wrapping shape.  # noqa: E501

        :param transform: The transform of this TextFrameFormat.  # noqa: E501
        :type: str
        """
        if transform is not None:
            allowed_values = ["None", "Plain", "Stop", "Triangle", "TriangleInverted", "Chevron", "ChevronInverted", "RingInside", "RingOutside", "ArchUp", "ArchDown", "Circle", "Button", "ArchUpPour", "ArchDownPour", "CirclePour", "ButtonPour", "CurveUp", "CurveDown", "CanUp", "CanDown", "Wave1", "Wave2", "DoubleWave1", "Wave4", "Inflate", "Deflate", "InflateBottom", "DeflateBottom", "InflateTop", "DeflateTop", "DeflateInflate", "DeflateInflateDeflate", "FadeRight", "FadeLeft", "FadeUp", "FadeDown", "SlantUp", "SlantDown", "CascadeUp", "CascadeDown", "Custom", "NotDefined"]  # noqa: E501
            if transform.isdigit():
                int_transform = int(transform)
                if int_transform < 0 or int_transform >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `transform` ({0}), must be one of {1}"  # noqa: E501
                        .format(transform, allowed_values)
                    )
                self._transform = allowed_values[int_transform]
                return
            if transform not in allowed_values:
                raise ValueError(
                    "Invalid value for `transform` ({0}), must be one of {1}"  # noqa: E501
                    .format(transform, allowed_values)
                )
        self._transform = transform

    @property
    def margin_left(self):
        """Gets the margin_left of this TextFrameFormat.  # noqa: E501

        Left margin. Left margin.  # noqa: E501

        :return: The margin_left of this TextFrameFormat.  # noqa: E501
        :rtype: float
        """
        return self._margin_left

    @margin_left.setter
    def margin_left(self, margin_left):
        """Sets the margin_left of this TextFrameFormat.

        Left margin. Left margin.  # noqa: E501

        :param margin_left: The margin_left of this TextFrameFormat.  # noqa: E501
        :type: float
        """
        self._margin_left = margin_left

    @property
    def margin_right(self):
        """Gets the margin_right of this TextFrameFormat.  # noqa: E501

        Right margin.  # noqa: E501

        :return: The margin_right of this TextFrameFormat.  # noqa: E501
        :rtype: float
        """
        return self._margin_right

    @margin_right.setter
    def margin_right(self, margin_right):
        """Sets the margin_right of this TextFrameFormat.

        Right margin.  # noqa: E501

        :param margin_right: The margin_right of this TextFrameFormat.  # noqa: E501
        :type: float
        """
        self._margin_right = margin_right

    @property
    def margin_top(self):
        """Gets the margin_top of this TextFrameFormat.  # noqa: E501

        Top margin.  # noqa: E501

        :return: The margin_top of this TextFrameFormat.  # noqa: E501
        :rtype: float
        """
        return self._margin_top

    @margin_top.setter
    def margin_top(self, margin_top):
        """Sets the margin_top of this TextFrameFormat.

        Top margin.  # noqa: E501

        :param margin_top: The margin_top of this TextFrameFormat.  # noqa: E501
        :type: float
        """
        self._margin_top = margin_top

    @property
    def margin_bottom(self):
        """Gets the margin_bottom of this TextFrameFormat.  # noqa: E501

        Bottom margin.  # noqa: E501

        :return: The margin_bottom of this TextFrameFormat.  # noqa: E501
        :rtype: float
        """
        return self._margin_bottom

    @margin_bottom.setter
    def margin_bottom(self, margin_bottom):
        """Sets the margin_bottom of this TextFrameFormat.

        Bottom margin.  # noqa: E501

        :param margin_bottom: The margin_bottom of this TextFrameFormat.  # noqa: E501
        :type: float
        """
        self._margin_bottom = margin_bottom

    @property
    def wrap_text(self):
        """Gets the wrap_text of this TextFrameFormat.  # noqa: E501

        True if text is wrapped at TextFrame's margins.  # noqa: E501

        :return: The wrap_text of this TextFrameFormat.  # noqa: E501
        :rtype: str
        """
        return self._wrap_text

    @wrap_text.setter
    def wrap_text(self, wrap_text):
        """Sets the wrap_text of this TextFrameFormat.

        True if text is wrapped at TextFrame's margins.  # noqa: E501

        :param wrap_text: The wrap_text of this TextFrameFormat.  # noqa: E501
        :type: str
        """
        if wrap_text is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if wrap_text.isdigit():
                int_wrap_text = int(wrap_text)
                if int_wrap_text < 0 or int_wrap_text >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `wrap_text` ({0}), must be one of {1}"  # noqa: E501
                        .format(wrap_text, allowed_values)
                    )
                self._wrap_text = allowed_values[int_wrap_text]
                return
            if wrap_text not in allowed_values:
                raise ValueError(
                    "Invalid value for `wrap_text` ({0}), must be one of {1}"  # noqa: E501
                    .format(wrap_text, allowed_values)
                )
        self._wrap_text = wrap_text

    @property
    def anchoring_type(self):
        """Gets the anchoring_type of this TextFrameFormat.  # noqa: E501

        Returns or sets vertical anchor text in a TextFrame.  # noqa: E501

        :return: The anchoring_type of this TextFrameFormat.  # noqa: E501
        :rtype: str
        """
        return self._anchoring_type

    @anchoring_type.setter
    def anchoring_type(self, anchoring_type):
        """Sets the anchoring_type of this TextFrameFormat.

        Returns or sets vertical anchor text in a TextFrame.  # noqa: E501

        :param anchoring_type: The anchoring_type of this TextFrameFormat.  # noqa: E501
        :type: str
        """
        if anchoring_type is not None:
            allowed_values = ["Top", "Center", "Bottom", "Justified", "Distributed", "NotDefined"]  # noqa: E501
            if anchoring_type.isdigit():
                int_anchoring_type = int(anchoring_type)
                if int_anchoring_type < 0 or int_anchoring_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `anchoring_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(anchoring_type, allowed_values)
                    )
                self._anchoring_type = allowed_values[int_anchoring_type]
                return
            if anchoring_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `anchoring_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(anchoring_type, allowed_values)
                )
        self._anchoring_type = anchoring_type

    @property
    def center_text(self):
        """Gets the center_text of this TextFrameFormat.  # noqa: E501

        If True then text should be centered in box horizontally.  # noqa: E501

        :return: The center_text of this TextFrameFormat.  # noqa: E501
        :rtype: str
        """
        return self._center_text

    @center_text.setter
    def center_text(self, center_text):
        """Sets the center_text of this TextFrameFormat.

        If True then text should be centered in box horizontally.  # noqa: E501

        :param center_text: The center_text of this TextFrameFormat.  # noqa: E501
        :type: str
        """
        if center_text is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if center_text.isdigit():
                int_center_text = int(center_text)
                if int_center_text < 0 or int_center_text >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `center_text` ({0}), must be one of {1}"  # noqa: E501
                        .format(center_text, allowed_values)
                    )
                self._center_text = allowed_values[int_center_text]
                return
            if center_text not in allowed_values:
                raise ValueError(
                    "Invalid value for `center_text` ({0}), must be one of {1}"  # noqa: E501
                    .format(center_text, allowed_values)
                )
        self._center_text = center_text

    @property
    def text_vertical_type(self):
        """Gets the text_vertical_type of this TextFrameFormat.  # noqa: E501

        Determines text orientation. The resulted value of visual text rotation summarized from this property and custom angle in property RotationAngle.  # noqa: E501

        :return: The text_vertical_type of this TextFrameFormat.  # noqa: E501
        :rtype: str
        """
        return self._text_vertical_type

    @text_vertical_type.setter
    def text_vertical_type(self, text_vertical_type):
        """Sets the text_vertical_type of this TextFrameFormat.

        Determines text orientation. The resulted value of visual text rotation summarized from this property and custom angle in property RotationAngle.  # noqa: E501

        :param text_vertical_type: The text_vertical_type of this TextFrameFormat.  # noqa: E501
        :type: str
        """
        if text_vertical_type is not None:
            allowed_values = ["Horizontal", "Vertical", "Vertical270", "WordArtVertical", "EastAsianVertical", "MongolianVertical", "WordArtVerticalRightToLeft", "NotDefined"]  # noqa: E501
            if text_vertical_type.isdigit():
                int_text_vertical_type = int(text_vertical_type)
                if int_text_vertical_type < 0 or int_text_vertical_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `text_vertical_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(text_vertical_type, allowed_values)
                    )
                self._text_vertical_type = allowed_values[int_text_vertical_type]
                return
            if text_vertical_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `text_vertical_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(text_vertical_type, allowed_values)
                )
        self._text_vertical_type = text_vertical_type

    @property
    def autofit_type(self):
        """Gets the autofit_type of this TextFrameFormat.  # noqa: E501

        Returns or sets text's auto-fit mode.  # noqa: E501

        :return: The autofit_type of this TextFrameFormat.  # noqa: E501
        :rtype: str
        """
        return self._autofit_type

    @autofit_type.setter
    def autofit_type(self, autofit_type):
        """Sets the autofit_type of this TextFrameFormat.

        Returns or sets text's auto-fit mode.  # noqa: E501

        :param autofit_type: The autofit_type of this TextFrameFormat.  # noqa: E501
        :type: str
        """
        if autofit_type is not None:
            allowed_values = ["None", "Normal", "Shape", "NotDefined"]  # noqa: E501
            if autofit_type.isdigit():
                int_autofit_type = int(autofit_type)
                if int_autofit_type < 0 or int_autofit_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `autofit_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(autofit_type, allowed_values)
                    )
                self._autofit_type = allowed_values[int_autofit_type]
                return
            if autofit_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `autofit_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(autofit_type, allowed_values)
                )
        self._autofit_type = autofit_type

    @property
    def column_count(self):
        """Gets the column_count of this TextFrameFormat.  # noqa: E501

        Returns or sets number of columns in the text area. This value must be a positive number. Otherwise, the value will be set to zero.  Value 0 means undefined value.  # noqa: E501

        :return: The column_count of this TextFrameFormat.  # noqa: E501
        :rtype: int
        """
        return self._column_count

    @column_count.setter
    def column_count(self, column_count):
        """Sets the column_count of this TextFrameFormat.

        Returns or sets number of columns in the text area. This value must be a positive number. Otherwise, the value will be set to zero.  Value 0 means undefined value.  # noqa: E501

        :param column_count: The column_count of this TextFrameFormat.  # noqa: E501
        :type: int
        """
        self._column_count = column_count

    @property
    def column_spacing(self):
        """Gets the column_spacing of this TextFrameFormat.  # noqa: E501

        Returns or sets the space between text columns in the text area (in points). This should only apply  when there is more than 1 column present. This value must be a positive number. Otherwise, the value will be set to zero.   # noqa: E501

        :return: The column_spacing of this TextFrameFormat.  # noqa: E501
        :rtype: float
        """
        return self._column_spacing

    @column_spacing.setter
    def column_spacing(self, column_spacing):
        """Sets the column_spacing of this TextFrameFormat.

        Returns or sets the space between text columns in the text area (in points). This should only apply  when there is more than 1 column present. This value must be a positive number. Otherwise, the value will be set to zero.   # noqa: E501

        :param column_spacing: The column_spacing of this TextFrameFormat.  # noqa: E501
        :type: float
        """
        self._column_spacing = column_spacing

    @property
    def keep_text_flat(self):
        """Gets the keep_text_flat of this TextFrameFormat.  # noqa: E501

        Returns or set keeping text out of 3D scene entirely.  # noqa: E501

        :return: The keep_text_flat of this TextFrameFormat.  # noqa: E501
        :rtype: bool
        """
        return self._keep_text_flat

    @keep_text_flat.setter
    def keep_text_flat(self, keep_text_flat):
        """Sets the keep_text_flat of this TextFrameFormat.

        Returns or set keeping text out of 3D scene entirely.  # noqa: E501

        :param keep_text_flat: The keep_text_flat of this TextFrameFormat.  # noqa: E501
        :type: bool
        """
        self._keep_text_flat = keep_text_flat

    @property
    def rotation_angle(self):
        """Gets the rotation_angle of this TextFrameFormat.  # noqa: E501

        Specifies the custom rotation that is being applied to the text within the bounding box.  # noqa: E501

        :return: The rotation_angle of this TextFrameFormat.  # noqa: E501
        :rtype: float
        """
        return self._rotation_angle

    @rotation_angle.setter
    def rotation_angle(self, rotation_angle):
        """Sets the rotation_angle of this TextFrameFormat.

        Specifies the custom rotation that is being applied to the text within the bounding box.  # noqa: E501

        :param rotation_angle: The rotation_angle of this TextFrameFormat.  # noqa: E501
        :type: float
        """
        self._rotation_angle = rotation_angle

    @property
    def default_paragraph_format(self):
        """Gets the default_paragraph_format of this TextFrameFormat.  # noqa: E501

        Default portion format.  # noqa: E501

        :return: The default_paragraph_format of this TextFrameFormat.  # noqa: E501
        :rtype: ParagraphFormat
        """
        return self._default_paragraph_format

    @default_paragraph_format.setter
    def default_paragraph_format(self, default_paragraph_format):
        """Sets the default_paragraph_format of this TextFrameFormat.

        Default portion format.  # noqa: E501

        :param default_paragraph_format: The default_paragraph_format of this TextFrameFormat.  # noqa: E501
        :type: ParagraphFormat
        """
        self._default_paragraph_format = default_paragraph_format

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
        if not isinstance(other, TextFrameFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
