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


class ParagraphFormat(object):


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'depth': 'int',
        'alignment': 'str',
        'margin_left': 'float',
        'margin_right': 'float',
        'space_before': 'float',
        'space_after': 'float',
        'space_within': 'float',
        'font_alignment': 'str',
        'indent': 'float',
        'right_to_left': 'str',
        'east_asian_line_break': 'str',
        'latin_line_break': 'str',
        'hanging_punctuation': 'str',
        'default_tab_size': 'float',
        'default_portion_format': 'PortionFormat',
        'bullet_char': 'str',
        'bullet_height': 'float',
        'bullet_type': 'str',
        'numbered_bullet_start_with': 'int',
        'numbered_bullet_style': 'str',
        'bullet_fill_format': 'FillFormat'
    }

    attribute_map = {
        'depth': 'depth',
        'alignment': 'alignment',
        'margin_left': 'marginLeft',
        'margin_right': 'marginRight',
        'space_before': 'spaceBefore',
        'space_after': 'spaceAfter',
        'space_within': 'spaceWithin',
        'font_alignment': 'fontAlignment',
        'indent': 'indent',
        'right_to_left': 'rightToLeft',
        'east_asian_line_break': 'eastAsianLineBreak',
        'latin_line_break': 'latinLineBreak',
        'hanging_punctuation': 'hangingPunctuation',
        'default_tab_size': 'defaultTabSize',
        'default_portion_format': 'defaultPortionFormat',
        'bullet_char': 'bulletChar',
        'bullet_height': 'bulletHeight',
        'bullet_type': 'bulletType',
        'numbered_bullet_start_with': 'numberedBulletStartWith',
        'numbered_bullet_style': 'numberedBulletStyle',
        'bullet_fill_format': 'bulletFillFormat'
    }

    type_determiners = {
    }

    def __init__(self, depth=None, alignment=None, margin_left=None, margin_right=None, space_before=None, space_after=None, space_within=None, font_alignment=None, indent=None, right_to_left=None, east_asian_line_break=None, latin_line_break=None, hanging_punctuation=None, default_tab_size=None, default_portion_format=None, bullet_char=None, bullet_height=None, bullet_type=None, numbered_bullet_start_with=None, numbered_bullet_style=None, bullet_fill_format=None):  # noqa: E501
        """ParagraphFormat - a model defined in Swagger"""  # noqa: E501

        self._depth = None
        self._alignment = None
        self._margin_left = None
        self._margin_right = None
        self._space_before = None
        self._space_after = None
        self._space_within = None
        self._font_alignment = None
        self._indent = None
        self._right_to_left = None
        self._east_asian_line_break = None
        self._latin_line_break = None
        self._hanging_punctuation = None
        self._default_tab_size = None
        self._default_portion_format = None
        self._bullet_char = None
        self._bullet_height = None
        self._bullet_type = None
        self._numbered_bullet_start_with = None
        self._numbered_bullet_style = None
        self._bullet_fill_format = None

        if depth is not None:
            self.depth = depth
        if alignment is not None:
            self.alignment = alignment
        if margin_left is not None:
            self.margin_left = margin_left
        if margin_right is not None:
            self.margin_right = margin_right
        if space_before is not None:
            self.space_before = space_before
        if space_after is not None:
            self.space_after = space_after
        if space_within is not None:
            self.space_within = space_within
        if font_alignment is not None:
            self.font_alignment = font_alignment
        if indent is not None:
            self.indent = indent
        if right_to_left is not None:
            self.right_to_left = right_to_left
        if east_asian_line_break is not None:
            self.east_asian_line_break = east_asian_line_break
        if latin_line_break is not None:
            self.latin_line_break = latin_line_break
        if hanging_punctuation is not None:
            self.hanging_punctuation = hanging_punctuation
        if default_tab_size is not None:
            self.default_tab_size = default_tab_size
        if default_portion_format is not None:
            self.default_portion_format = default_portion_format
        if bullet_char is not None:
            self.bullet_char = bullet_char
        if bullet_height is not None:
            self.bullet_height = bullet_height
        if bullet_type is not None:
            self.bullet_type = bullet_type
        if numbered_bullet_start_with is not None:
            self.numbered_bullet_start_with = numbered_bullet_start_with
        if numbered_bullet_style is not None:
            self.numbered_bullet_style = numbered_bullet_style
        if bullet_fill_format is not None:
            self.bullet_fill_format = bullet_fill_format

    @property
    def depth(self):
        """Gets the depth of this ParagraphFormat.  # noqa: E501

        Depth.  # noqa: E501

        :return: The depth of this ParagraphFormat.  # noqa: E501
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this ParagraphFormat.

        Depth.  # noqa: E501

        :param depth: The depth of this ParagraphFormat.  # noqa: E501
        :type: int
        """
        self._depth = depth

    @property
    def alignment(self):
        """Gets the alignment of this ParagraphFormat.  # noqa: E501

        Text alignment.  # noqa: E501

        :return: The alignment of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._alignment

    @alignment.setter
    def alignment(self, alignment):
        """Sets the alignment of this ParagraphFormat.

        Text alignment.  # noqa: E501

        :param alignment: The alignment of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        if alignment is not None:
            allowed_values = ["Left", "Center", "Right", "Justify", "JustifyLow", "Distributed", "NotDefined"]  # noqa: E501
            if alignment.isdigit():
                int_alignment = int(alignment)
                if int_alignment < 0 or int_alignment >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `alignment` ({0}), must be one of {1}"  # noqa: E501
                        .format(alignment, allowed_values)
                    )
                self._alignment = allowed_values[int_alignment]
                return
            if alignment not in allowed_values:
                raise ValueError(
                    "Invalid value for `alignment` ({0}), must be one of {1}"  # noqa: E501
                    .format(alignment, allowed_values)
                )
        self._alignment = alignment

    @property
    def margin_left(self):
        """Gets the margin_left of this ParagraphFormat.  # noqa: E501

        Left margin.  # noqa: E501

        :return: The margin_left of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._margin_left

    @margin_left.setter
    def margin_left(self, margin_left):
        """Sets the margin_left of this ParagraphFormat.

        Left margin.  # noqa: E501

        :param margin_left: The margin_left of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._margin_left = margin_left

    @property
    def margin_right(self):
        """Gets the margin_right of this ParagraphFormat.  # noqa: E501

        Right margin.  # noqa: E501

        :return: The margin_right of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._margin_right

    @margin_right.setter
    def margin_right(self, margin_right):
        """Sets the margin_right of this ParagraphFormat.

        Right margin.  # noqa: E501

        :param margin_right: The margin_right of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._margin_right = margin_right

    @property
    def space_before(self):
        """Gets the space_before of this ParagraphFormat.  # noqa: E501

        Left spacing.  # noqa: E501

        :return: The space_before of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._space_before

    @space_before.setter
    def space_before(self, space_before):
        """Sets the space_before of this ParagraphFormat.

        Left spacing.  # noqa: E501

        :param space_before: The space_before of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._space_before = space_before

    @property
    def space_after(self):
        """Gets the space_after of this ParagraphFormat.  # noqa: E501

        Right spacing.  # noqa: E501

        :return: The space_after of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._space_after

    @space_after.setter
    def space_after(self, space_after):
        """Sets the space_after of this ParagraphFormat.

        Right spacing.  # noqa: E501

        :param space_after: The space_after of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._space_after = space_after

    @property
    def space_within(self):
        """Gets the space_within of this ParagraphFormat.  # noqa: E501

        Spacing between lines.  # noqa: E501

        :return: The space_within of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._space_within

    @space_within.setter
    def space_within(self, space_within):
        """Sets the space_within of this ParagraphFormat.

        Spacing between lines.  # noqa: E501

        :param space_within: The space_within of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._space_within = space_within

    @property
    def font_alignment(self):
        """Gets the font_alignment of this ParagraphFormat.  # noqa: E501

        Font alignment.  # noqa: E501

        :return: The font_alignment of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._font_alignment

    @font_alignment.setter
    def font_alignment(self, font_alignment):
        """Sets the font_alignment of this ParagraphFormat.

        Font alignment.  # noqa: E501

        :param font_alignment: The font_alignment of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        if font_alignment is not None:
            allowed_values = ["Automatic", "Top", "Center", "Bottom", "Baseline", "Default"]  # noqa: E501
            if font_alignment.isdigit():
                int_font_alignment = int(font_alignment)
                if int_font_alignment < 0 or int_font_alignment >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `font_alignment` ({0}), must be one of {1}"  # noqa: E501
                        .format(font_alignment, allowed_values)
                    )
                self._font_alignment = allowed_values[int_font_alignment]
                return
            if font_alignment not in allowed_values:
                raise ValueError(
                    "Invalid value for `font_alignment` ({0}), must be one of {1}"  # noqa: E501
                    .format(font_alignment, allowed_values)
                )
        self._font_alignment = font_alignment

    @property
    def indent(self):
        """Gets the indent of this ParagraphFormat.  # noqa: E501

        First line indent.  # noqa: E501

        :return: The indent of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._indent

    @indent.setter
    def indent(self, indent):
        """Sets the indent of this ParagraphFormat.

        First line indent.  # noqa: E501

        :param indent: The indent of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._indent = indent

    @property
    def right_to_left(self):
        """Gets the right_to_left of this ParagraphFormat.  # noqa: E501

        Determines whether the Right to Left writing is used in a paragraph. No inheritance applied.  # noqa: E501

        :return: The right_to_left of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._right_to_left

    @right_to_left.setter
    def right_to_left(self, right_to_left):
        """Sets the right_to_left of this ParagraphFormat.

        Determines whether the Right to Left writing is used in a paragraph. No inheritance applied.  # noqa: E501

        :param right_to_left: The right_to_left of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        if right_to_left is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if right_to_left.isdigit():
                int_right_to_left = int(right_to_left)
                if int_right_to_left < 0 or int_right_to_left >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `right_to_left` ({0}), must be one of {1}"  # noqa: E501
                        .format(right_to_left, allowed_values)
                    )
                self._right_to_left = allowed_values[int_right_to_left]
                return
            if right_to_left not in allowed_values:
                raise ValueError(
                    "Invalid value for `right_to_left` ({0}), must be one of {1}"  # noqa: E501
                    .format(right_to_left, allowed_values)
                )
        self._right_to_left = right_to_left

    @property
    def east_asian_line_break(self):
        """Gets the east_asian_line_break of this ParagraphFormat.  # noqa: E501

        Determines whether the East Asian line break is used in a paragraph. No inheritance applied.  # noqa: E501

        :return: The east_asian_line_break of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._east_asian_line_break

    @east_asian_line_break.setter
    def east_asian_line_break(self, east_asian_line_break):
        """Sets the east_asian_line_break of this ParagraphFormat.

        Determines whether the East Asian line break is used in a paragraph. No inheritance applied.  # noqa: E501

        :param east_asian_line_break: The east_asian_line_break of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        if east_asian_line_break is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if east_asian_line_break.isdigit():
                int_east_asian_line_break = int(east_asian_line_break)
                if int_east_asian_line_break < 0 or int_east_asian_line_break >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `east_asian_line_break` ({0}), must be one of {1}"  # noqa: E501
                        .format(east_asian_line_break, allowed_values)
                    )
                self._east_asian_line_break = allowed_values[int_east_asian_line_break]
                return
            if east_asian_line_break not in allowed_values:
                raise ValueError(
                    "Invalid value for `east_asian_line_break` ({0}), must be one of {1}"  # noqa: E501
                    .format(east_asian_line_break, allowed_values)
                )
        self._east_asian_line_break = east_asian_line_break

    @property
    def latin_line_break(self):
        """Gets the latin_line_break of this ParagraphFormat.  # noqa: E501

        Determines whether the Latin line break is used in a paragraph. No inheritance applied.  # noqa: E501

        :return: The latin_line_break of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._latin_line_break

    @latin_line_break.setter
    def latin_line_break(self, latin_line_break):
        """Sets the latin_line_break of this ParagraphFormat.

        Determines whether the Latin line break is used in a paragraph. No inheritance applied.  # noqa: E501

        :param latin_line_break: The latin_line_break of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        if latin_line_break is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if latin_line_break.isdigit():
                int_latin_line_break = int(latin_line_break)
                if int_latin_line_break < 0 or int_latin_line_break >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `latin_line_break` ({0}), must be one of {1}"  # noqa: E501
                        .format(latin_line_break, allowed_values)
                    )
                self._latin_line_break = allowed_values[int_latin_line_break]
                return
            if latin_line_break not in allowed_values:
                raise ValueError(
                    "Invalid value for `latin_line_break` ({0}), must be one of {1}"  # noqa: E501
                    .format(latin_line_break, allowed_values)
                )
        self._latin_line_break = latin_line_break

    @property
    def hanging_punctuation(self):
        """Gets the hanging_punctuation of this ParagraphFormat.  # noqa: E501

        Determines whether the hanging punctuation is used in a paragraph. No inheritance applied.  # noqa: E501

        :return: The hanging_punctuation of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._hanging_punctuation

    @hanging_punctuation.setter
    def hanging_punctuation(self, hanging_punctuation):
        """Sets the hanging_punctuation of this ParagraphFormat.

        Determines whether the hanging punctuation is used in a paragraph. No inheritance applied.  # noqa: E501

        :param hanging_punctuation: The hanging_punctuation of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        if hanging_punctuation is not None:
            allowed_values = ["False", "True", "NotDefined"]  # noqa: E501
            if hanging_punctuation.isdigit():
                int_hanging_punctuation = int(hanging_punctuation)
                if int_hanging_punctuation < 0 or int_hanging_punctuation >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `hanging_punctuation` ({0}), must be one of {1}"  # noqa: E501
                        .format(hanging_punctuation, allowed_values)
                    )
                self._hanging_punctuation = allowed_values[int_hanging_punctuation]
                return
            if hanging_punctuation not in allowed_values:
                raise ValueError(
                    "Invalid value for `hanging_punctuation` ({0}), must be one of {1}"  # noqa: E501
                    .format(hanging_punctuation, allowed_values)
                )
        self._hanging_punctuation = hanging_punctuation

    @property
    def default_tab_size(self):
        """Gets the default_tab_size of this ParagraphFormat.  # noqa: E501

        Returns or sets default tabulation size with no inheritance.  # noqa: E501

        :return: The default_tab_size of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._default_tab_size

    @default_tab_size.setter
    def default_tab_size(self, default_tab_size):
        """Sets the default_tab_size of this ParagraphFormat.

        Returns or sets default tabulation size with no inheritance.  # noqa: E501

        :param default_tab_size: The default_tab_size of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._default_tab_size = default_tab_size

    @property
    def default_portion_format(self):
        """Gets the default_portion_format of this ParagraphFormat.  # noqa: E501

        Default portion format.  # noqa: E501

        :return: The default_portion_format of this ParagraphFormat.  # noqa: E501
        :rtype: PortionFormat
        """
        return self._default_portion_format

    @default_portion_format.setter
    def default_portion_format(self, default_portion_format):
        """Sets the default_portion_format of this ParagraphFormat.

        Default portion format.  # noqa: E501

        :param default_portion_format: The default_portion_format of this ParagraphFormat.  # noqa: E501
        :type: PortionFormat
        """
        self._default_portion_format = default_portion_format

    @property
    def bullet_char(self):
        """Gets the bullet_char of this ParagraphFormat.  # noqa: E501

        Bullet char.  # noqa: E501

        :return: The bullet_char of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._bullet_char

    @bullet_char.setter
    def bullet_char(self, bullet_char):
        """Sets the bullet_char of this ParagraphFormat.

        Bullet char.  # noqa: E501

        :param bullet_char: The bullet_char of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        self._bullet_char = bullet_char

    @property
    def bullet_height(self):
        """Gets the bullet_height of this ParagraphFormat.  # noqa: E501

        Bullet height.  # noqa: E501

        :return: The bullet_height of this ParagraphFormat.  # noqa: E501
        :rtype: float
        """
        return self._bullet_height

    @bullet_height.setter
    def bullet_height(self, bullet_height):
        """Sets the bullet_height of this ParagraphFormat.

        Bullet height.  # noqa: E501

        :param bullet_height: The bullet_height of this ParagraphFormat.  # noqa: E501
        :type: float
        """
        self._bullet_height = bullet_height

    @property
    def bullet_type(self):
        """Gets the bullet_type of this ParagraphFormat.  # noqa: E501

        Bullet type.  # noqa: E501

        :return: The bullet_type of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._bullet_type

    @bullet_type.setter
    def bullet_type(self, bullet_type):
        """Sets the bullet_type of this ParagraphFormat.

        Bullet type.  # noqa: E501

        :param bullet_type: The bullet_type of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        if bullet_type is not None:
            allowed_values = ["None", "Symbol", "Numbered", "Picture", "NotDefined"]  # noqa: E501
            if bullet_type.isdigit():
                int_bullet_type = int(bullet_type)
                if int_bullet_type < 0 or int_bullet_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `bullet_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(bullet_type, allowed_values)
                    )
                self._bullet_type = allowed_values[int_bullet_type]
                return
            if bullet_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `bullet_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(bullet_type, allowed_values)
                )
        self._bullet_type = bullet_type

    @property
    def numbered_bullet_start_with(self):
        """Gets the numbered_bullet_start_with of this ParagraphFormat.  # noqa: E501

        Starting number for a numbered bullet.  # noqa: E501

        :return: The numbered_bullet_start_with of this ParagraphFormat.  # noqa: E501
        :rtype: int
        """
        return self._numbered_bullet_start_with

    @numbered_bullet_start_with.setter
    def numbered_bullet_start_with(self, numbered_bullet_start_with):
        """Sets the numbered_bullet_start_with of this ParagraphFormat.

        Starting number for a numbered bullet.  # noqa: E501

        :param numbered_bullet_start_with: The numbered_bullet_start_with of this ParagraphFormat.  # noqa: E501
        :type: int
        """
        self._numbered_bullet_start_with = numbered_bullet_start_with

    @property
    def numbered_bullet_style(self):
        """Gets the numbered_bullet_style of this ParagraphFormat.  # noqa: E501

        Numbered bullet style.  # noqa: E501

        :return: The numbered_bullet_style of this ParagraphFormat.  # noqa: E501
        :rtype: str
        """
        return self._numbered_bullet_style

    @numbered_bullet_style.setter
    def numbered_bullet_style(self, numbered_bullet_style):
        """Sets the numbered_bullet_style of this ParagraphFormat.

        Numbered bullet style.  # noqa: E501

        :param numbered_bullet_style: The numbered_bullet_style of this ParagraphFormat.  # noqa: E501
        :type: str
        """
        if numbered_bullet_style is not None:
            allowed_values = ["BulletAlphaLCPeriod", "BulletAlphaUCPeriod", "BulletArabicParenRight", "BulletArabicPeriod", "BulletRomanLCParenBoth", "BulletRomanLCParenRight", "BulletRomanLCPeriod", "BulletRomanUCPeriod", "BulletAlphaLCParenBoth", "BulletAlphaLCParenRight", "BulletAlphaUCParenBoth", "BulletAlphaUCParenRight", "BulletArabicParenBoth", "BulletArabicPlain", "BulletRomanUCParenBoth", "BulletRomanUCParenRight", "BulletSimpChinPlain", "BulletSimpChinPeriod", "BulletCircleNumDBPlain", "BulletCircleNumWDWhitePlain", "BulletCircleNumWDBlackPlain", "BulletTradChinPlain", "BulletTradChinPeriod", "BulletArabicAlphaDash", "BulletArabicAbjadDash", "BulletHebrewAlphaDash", "BulletKanjiKoreanPlain", "BulletKanjiKoreanPeriod", "BulletArabicDBPlain", "BulletArabicDBPeriod", "BulletThaiAlphaPeriod", "BulletThaiAlphaParenRight", "BulletThaiAlphaParenBoth", "BulletThaiNumPeriod", "BulletThaiNumParenRight", "BulletThaiNumParenBoth", "BulletHindiAlphaPeriod", "BulletHindiNumPeriod", "BulletKanjiSimpChinDBPeriod", "BulletHindiNumParenRight", "BulletHindiAlpha1Period", "NotDefined"]  # noqa: E501
            if numbered_bullet_style.isdigit():
                int_numbered_bullet_style = int(numbered_bullet_style)
                if int_numbered_bullet_style < 0 or int_numbered_bullet_style >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `numbered_bullet_style` ({0}), must be one of {1}"  # noqa: E501
                        .format(numbered_bullet_style, allowed_values)
                    )
                self._numbered_bullet_style = allowed_values[int_numbered_bullet_style]
                return
            if numbered_bullet_style not in allowed_values:
                raise ValueError(
                    "Invalid value for `numbered_bullet_style` ({0}), must be one of {1}"  # noqa: E501
                    .format(numbered_bullet_style, allowed_values)
                )
        self._numbered_bullet_style = numbered_bullet_style

    @property
    def bullet_fill_format(self):
        """Gets the bullet_fill_format of this ParagraphFormat.  # noqa: E501

        Bullet fill format.  # noqa: E501

        :return: The bullet_fill_format of this ParagraphFormat.  # noqa: E501
        :rtype: FillFormat
        """
        return self._bullet_fill_format

    @bullet_fill_format.setter
    def bullet_fill_format(self, bullet_fill_format):
        """Sets the bullet_fill_format of this ParagraphFormat.

        Bullet fill format.  # noqa: E501

        :param bullet_fill_format: The bullet_fill_format of this ParagraphFormat.  # noqa: E501
        :type: FillFormat
        """
        self._bullet_fill_format = bullet_fill_format

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
        if not isinstance(other, ParagraphFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
