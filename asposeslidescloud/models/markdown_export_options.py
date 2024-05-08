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

class MarkdownExportOptions(ExportOptions):


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
        'export_type': 'str',
        'flavor': 'str',
        'new_line_type': 'str',
        'images_save_folder_name': 'str',
        'show_slide_number': 'bool',
        'show_comments': 'bool',
        'show_hidden_slides': 'bool'
    }

    attribute_map = {
        'default_regular_font': 'defaultRegularFont',
        'font_fallback_rules': 'fontFallbackRules',
        'font_subst_rules': 'fontSubstRules',
        'format': 'format',
        'export_type': 'exportType',
        'flavor': 'flavor',
        'new_line_type': 'newLineType',
        'images_save_folder_name': 'imagesSaveFolderName',
        'show_slide_number': 'showSlideNumber',
        'show_comments': 'showComments',
        'show_hidden_slides': 'showHiddenSlides'
    }

    type_determiners = {
        'format': 'md',
    }

    def __init__(self, default_regular_font=None, font_fallback_rules=None, font_subst_rules=None, format='md', export_type=None, flavor=None, new_line_type=None, images_save_folder_name=None, show_slide_number=None, show_comments=None, show_hidden_slides=None):  # noqa: E501
        """MarkdownExportOptions - a model defined in Swagger"""  # noqa: E501
        super(MarkdownExportOptions, self).__init__(default_regular_font, font_fallback_rules, font_subst_rules, format)

        self._export_type = None
        self._flavor = None
        self._new_line_type = None
        self._images_save_folder_name = None
        self._show_slide_number = None
        self._show_comments = None
        self._show_hidden_slides = None
        self.format = 'md'

        if export_type is not None:
            self.export_type = export_type
        if flavor is not None:
            self.flavor = flavor
        if new_line_type is not None:
            self.new_line_type = new_line_type
        if images_save_folder_name is not None:
            self.images_save_folder_name = images_save_folder_name
        if show_slide_number is not None:
            self.show_slide_number = show_slide_number
        if show_comments is not None:
            self.show_comments = show_comments
        if show_hidden_slides is not None:
            self.show_hidden_slides = show_hidden_slides

    @property
    def export_type(self):
        """Gets the export_type of this MarkdownExportOptions.  # noqa: E501

        Specifies markdown specification to convert presentation. Default is TextOnly.  # noqa: E501

        :return: The export_type of this MarkdownExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._export_type

    @export_type.setter
    def export_type(self, export_type):
        """Sets the export_type of this MarkdownExportOptions.

        Specifies markdown specification to convert presentation. Default is TextOnly.  # noqa: E501

        :param export_type: The export_type of this MarkdownExportOptions.  # noqa: E501
        :type: str
        """
        if export_type is not None:
            allowed_values = ["Sequential", "TextOnly", "Visual"]  # noqa: E501
            if export_type.isdigit():
                int_export_type = int(export_type)
                if int_export_type < 0 or int_export_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `export_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(export_type, allowed_values)
                    )
                self._export_type = allowed_values[int_export_type]
                return
            if export_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `export_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(export_type, allowed_values)
                )
        self._export_type = export_type

    @property
    def flavor(self):
        """Gets the flavor of this MarkdownExportOptions.  # noqa: E501

        Specifies markdown specification to convert presentation. Default is MultiMarkdown.  # noqa: E501

        :return: The flavor of this MarkdownExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this MarkdownExportOptions.

        Specifies markdown specification to convert presentation. Default is MultiMarkdown.  # noqa: E501

        :param flavor: The flavor of this MarkdownExportOptions.  # noqa: E501
        :type: str
        """
        if flavor is not None:
            allowed_values = ["Github", "Gruber", "MultiMarkdown", "CommonMark", "MarkdownExtra", "Pandoc", "Kramdown", "Markua", "Maruku", "Markdown2", "Remarkable", "Showdown", "Ghost", "GitLab", "Haroopad", "IaWriter", "Redcarpet", "ScholarlyMarkdown", "Taiga", "Trello", "S9ETextFormatter", "XWiki", "StackOverflow", "Default"]  # noqa: E501
            if flavor.isdigit():
                int_flavor = int(flavor)
                if int_flavor < 0 or int_flavor >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `flavor` ({0}), must be one of {1}"  # noqa: E501
                        .format(flavor, allowed_values)
                    )
                self._flavor = allowed_values[int_flavor]
                return
            if flavor not in allowed_values:
                raise ValueError(
                    "Invalid value for `flavor` ({0}), must be one of {1}"  # noqa: E501
                    .format(flavor, allowed_values)
                )
        self._flavor = flavor

    @property
    def new_line_type(self):
        """Gets the new_line_type of this MarkdownExportOptions.  # noqa: E501

        Specifies whether the generated document should have new lines of \\\\r(Macintosh), \\\\n(Unix) or \\\\r\\\\n(Windows). Default is Unix.  # noqa: E501

        :return: The new_line_type of this MarkdownExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._new_line_type

    @new_line_type.setter
    def new_line_type(self, new_line_type):
        """Sets the new_line_type of this MarkdownExportOptions.

        Specifies whether the generated document should have new lines of \\\\r(Macintosh), \\\\n(Unix) or \\\\r\\\\n(Windows). Default is Unix.  # noqa: E501

        :param new_line_type: The new_line_type of this MarkdownExportOptions.  # noqa: E501
        :type: str
        """
        if new_line_type is not None:
            allowed_values = ["Windows", "Unix", "Mac"]  # noqa: E501
            if new_line_type.isdigit():
                int_new_line_type = int(new_line_type)
                if int_new_line_type < 0 or int_new_line_type >= len(allowed_values):
                    raise ValueError(
                        "Invalid value for `new_line_type` ({0}), must be one of {1}"  # noqa: E501
                        .format(new_line_type, allowed_values)
                    )
                self._new_line_type = allowed_values[int_new_line_type]
                return
            if new_line_type not in allowed_values:
                raise ValueError(
                    "Invalid value for `new_line_type` ({0}), must be one of {1}"  # noqa: E501
                    .format(new_line_type, allowed_values)
                )
        self._new_line_type = new_line_type

    @property
    def images_save_folder_name(self):
        """Gets the images_save_folder_name of this MarkdownExportOptions.  # noqa: E501

        Specifies folder name to save images. Default is Images.   # noqa: E501

        :return: The images_save_folder_name of this MarkdownExportOptions.  # noqa: E501
        :rtype: str
        """
        return self._images_save_folder_name

    @images_save_folder_name.setter
    def images_save_folder_name(self, images_save_folder_name):
        """Sets the images_save_folder_name of this MarkdownExportOptions.

        Specifies folder name to save images. Default is Images.   # noqa: E501

        :param images_save_folder_name: The images_save_folder_name of this MarkdownExportOptions.  # noqa: E501
        :type: str
        """
        self._images_save_folder_name = images_save_folder_name

    @property
    def show_slide_number(self):
        """Gets the show_slide_number of this MarkdownExportOptions.  # noqa: E501

        Specifies whether the generated document should include slide number. Default is false.   # noqa: E501

        :return: The show_slide_number of this MarkdownExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._show_slide_number

    @show_slide_number.setter
    def show_slide_number(self, show_slide_number):
        """Sets the show_slide_number of this MarkdownExportOptions.

        Specifies whether the generated document should include slide number. Default is false.   # noqa: E501

        :param show_slide_number: The show_slide_number of this MarkdownExportOptions.  # noqa: E501
        :type: bool
        """
        self._show_slide_number = show_slide_number

    @property
    def show_comments(self):
        """Gets the show_comments of this MarkdownExportOptions.  # noqa: E501

        Specifies whether the generated document should include comments. Default is false.   # noqa: E501

        :return: The show_comments of this MarkdownExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._show_comments

    @show_comments.setter
    def show_comments(self, show_comments):
        """Sets the show_comments of this MarkdownExportOptions.

        Specifies whether the generated document should include comments. Default is false.   # noqa: E501

        :param show_comments: The show_comments of this MarkdownExportOptions.  # noqa: E501
        :type: bool
        """
        self._show_comments = show_comments

    @property
    def show_hidden_slides(self):
        """Gets the show_hidden_slides of this MarkdownExportOptions.  # noqa: E501

        Specifies whether the generated document should include hidden slides. Default is false.   # noqa: E501

        :return: The show_hidden_slides of this MarkdownExportOptions.  # noqa: E501
        :rtype: bool
        """
        return self._show_hidden_slides

    @show_hidden_slides.setter
    def show_hidden_slides(self, show_hidden_slides):
        """Sets the show_hidden_slides of this MarkdownExportOptions.

        Specifies whether the generated document should include hidden slides. Default is false.   # noqa: E501

        :param show_hidden_slides: The show_hidden_slides of this MarkdownExportOptions.  # noqa: E501
        :type: bool
        """
        self._show_hidden_slides = show_hidden_slides

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
        if not isinstance(other, MarkdownExportOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
