# coding: utf-8

# flake8: noqa

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

from __future__ import absolute_import

# import apis into sdk package
from asposeslidescloud.apis.document_api import DocumentApi
from asposeslidescloud.apis.images_api import ImagesApi
from asposeslidescloud.apis.layout_slides_api import LayoutSlidesApi
from asposeslidescloud.apis.master_slides_api import MasterSlidesApi
from asposeslidescloud.apis.merge_document_api import MergeDocumentApi
from asposeslidescloud.apis.notes_slide_api import NotesSlideApi
from asposeslidescloud.apis.notes_slide_shapes_api import NotesSlideShapesApi
from asposeslidescloud.apis.placeholders_api import PlaceholdersApi
from asposeslidescloud.apis.properties_api import PropertiesApi
from asposeslidescloud.apis.shapes_api import ShapesApi
from asposeslidescloud.apis.slides_api import SlidesApi
from asposeslidescloud.apis.text_api import TextApi
from asposeslidescloud.apis.theme_api import ThemeApi

# import ApiClient
from asposeslidescloud.api_client import ApiClient
from asposeslidescloud.configuration import Configuration
# import models into sdk package
from asposeslidescloud.models.arrow_head_properties import ArrowHeadProperties
from asposeslidescloud.models.audio_play_mode_preset import AudioPlayModePreset
from asposeslidescloud.models.audio_volume_mode import AudioVolumeMode
from asposeslidescloud.models.axes import Axes
from asposeslidescloud.models.axis import Axis
from asposeslidescloud.models.axis_position_type import AxisPositionType
from asposeslidescloud.models.blur_effect import BlurEffect
from asposeslidescloud.models.bullet_type import BulletType
from asposeslidescloud.models.category_axis_type import CategoryAxisType
from asposeslidescloud.models.chart_data_point_type import ChartDataPointType
from asposeslidescloud.models.chart_title import ChartTitle
from asposeslidescloud.models.chart_type import ChartType
from asposeslidescloud.models.chart_wall import ChartWall
from asposeslidescloud.models.combined_shape_type import CombinedShapeType
from asposeslidescloud.models.comments_positions import CommentsPositions
from asposeslidescloud.models.crosses_type import CrossesType
from asposeslidescloud.models.custom_dash_pattern import CustomDashPattern
from asposeslidescloud.models.display_unit_type import DisplayUnitType
from asposeslidescloud.models.effect_format import EffectFormat
from asposeslidescloud.models.export_format import ExportFormat
from asposeslidescloud.models.export_options import ExportOptions
from asposeslidescloud.models.external_fonts_handling import ExternalFontsHandling
from asposeslidescloud.models.fill_blend_mode import FillBlendMode
from asposeslidescloud.models.fill_format import FillFormat
from asposeslidescloud.models.fill_overlay_effect import FillOverlayEffect
from asposeslidescloud.models.fill_type import FillType
from asposeslidescloud.models.font_alignment import FontAlignment
from asposeslidescloud.models.font_set import FontSet
from asposeslidescloud.models.geometry_shape_type import GeometryShapeType
from asposeslidescloud.models.glow_effect import GlowEffect
from asposeslidescloud.models.gradient_direction import GradientDirection
from asposeslidescloud.models.gradient_fill_stop import GradientFillStop
from asposeslidescloud.models.gradient_shape_type import GradientShapeType
from asposeslidescloud.models.gradient_tile_flip import GradientTileFlip
from asposeslidescloud.models.http_status_code import HttpStatusCode
from asposeslidescloud.models.i_shape_export_options import IShapeExportOptions
from asposeslidescloud.models.image_export_format import ImageExportFormat
from asposeslidescloud.models.image_pixel_format import ImagePixelFormat
from asposeslidescloud.models.inner_shadow_effect import InnerShadowEffect
from asposeslidescloud.models.input import Input
from asposeslidescloud.models.input_file import InputFile
from asposeslidescloud.models.input_file_type import InputFileType
from asposeslidescloud.models.layout_slide_type import LayoutSlideType
from asposeslidescloud.models.legend import Legend
from asposeslidescloud.models.legend_position_type import LegendPositionType
from asposeslidescloud.models.line_alignment import LineAlignment
from asposeslidescloud.models.line_arrowhead_length import LineArrowheadLength
from asposeslidescloud.models.line_arrowhead_style import LineArrowheadStyle
from asposeslidescloud.models.line_arrowhead_width import LineArrowheadWidth
from asposeslidescloud.models.line_cap_style import LineCapStyle
from asposeslidescloud.models.line_dash_style import LineDashStyle
from asposeslidescloud.models.line_format import LineFormat
from asposeslidescloud.models.line_join_style import LineJoinStyle
from asposeslidescloud.models.line_style import LineStyle
from asposeslidescloud.models.marker_style_type import MarkerStyleType
from asposeslidescloud.models.marshal_by_ref_object import MarshalByRefObject
from asposeslidescloud.models.merging_source import MergingSource
from asposeslidescloud.models.notes_positions import NotesPositions
from asposeslidescloud.models.notes_slide_export_format import NotesSlideExportFormat
from asposeslidescloud.models.nullable_bool import NullableBool
from asposeslidescloud.models.numbered_bullet_style import NumberedBulletStyle
from asposeslidescloud.models.one_value_chart_data_point import OneValueChartDataPoint
from asposeslidescloud.models.ordered_merge_request import OrderedMergeRequest
from asposeslidescloud.models.organization_chart_layout_type import OrganizationChartLayoutType
from asposeslidescloud.models.outer_shadow_effect import OuterShadowEffect
from asposeslidescloud.models.output_file import OutputFile
from asposeslidescloud.models.output_file_type import OutputFileType
from asposeslidescloud.models.pattern_style import PatternStyle
from asposeslidescloud.models.pdf_compliance import PdfCompliance
from asposeslidescloud.models.pdf_text_compression import PdfTextCompression
from asposeslidescloud.models.picture_fill_mode import PictureFillMode
from asposeslidescloud.models.picture_type import PictureType
from asposeslidescloud.models.pictures_compression import PicturesCompression
from asposeslidescloud.models.pipeline import Pipeline
from asposeslidescloud.models.placeholder_orientation import PlaceholderOrientation
from asposeslidescloud.models.placeholder_size import PlaceholderSize
from asposeslidescloud.models.placeholder_type import PlaceholderType
from asposeslidescloud.models.plot_area import PlotArea
from asposeslidescloud.models.presentation_to_merge import PresentationToMerge
from asposeslidescloud.models.presentations_merge_request import PresentationsMergeRequest
from asposeslidescloud.models.preset_shadow_effect import PresetShadowEffect
from asposeslidescloud.models.preset_shadow_type import PresetShadowType
from asposeslidescloud.models.rectangle_alignment import RectangleAlignment
from asposeslidescloud.models.reflection_effect import ReflectionEffect
from asposeslidescloud.models.resource_base import ResourceBase
from asposeslidescloud.models.resource_uri import ResourceUri
from asposeslidescloud.models.resource_uri_element import ResourceUriElement
from asposeslidescloud.models.saa_spose_response import SaaSposeResponse
from asposeslidescloud.models.scale_type import ScaleType
from asposeslidescloud.models.scatter_chart_data_point import ScatterChartDataPoint
from asposeslidescloud.models.series import Series
from asposeslidescloud.models.series_marker import SeriesMarker
from asposeslidescloud.models.shape_export_format import ShapeExportFormat
from asposeslidescloud.models.shape_image_export_options import ShapeImageExportOptions
from asposeslidescloud.models.shape_thumbnail_bounds import ShapeThumbnailBounds
from asposeslidescloud.models.shape_type import ShapeType
from asposeslidescloud.models.size_type import SizeType
from asposeslidescloud.models.slide_comment import SlideComment
from asposeslidescloud.models.slide_export_format import SlideExportFormat
from asposeslidescloud.models.smart_art_color_type import SmartArtColorType
from asposeslidescloud.models.smart_art_layout_type import SmartArtLayoutType
from asposeslidescloud.models.smart_art_node import SmartArtNode
from asposeslidescloud.models.smart_art_quick_style_type import SmartArtQuickStyleType
from asposeslidescloud.models.soft_edge_effect import SoftEdgeEffect
from asposeslidescloud.models.table_cell import TableCell
from asposeslidescloud.models.table_column import TableColumn
from asposeslidescloud.models.table_row import TableRow
from asposeslidescloud.models.table_style_preset import TableStylePreset
from asposeslidescloud.models.task import Task
from asposeslidescloud.models.task_type import TaskType
from asposeslidescloud.models.text_alignment import TextAlignment
from asposeslidescloud.models.text_anchor_type import TextAnchorType
from asposeslidescloud.models.text_cap_type import TextCapType
from asposeslidescloud.models.text_item import TextItem
from asposeslidescloud.models.text_strikethrough_type import TextStrikethroughType
from asposeslidescloud.models.text_underline_type import TextUnderlineType
from asposeslidescloud.models.text_vertical_type import TextVerticalType
from asposeslidescloud.models.tick_label_position_type import TickLabelPositionType
from asposeslidescloud.models.tick_mark_type import TickMarkType
from asposeslidescloud.models.tiff_compression_type import TiffCompressionType
from asposeslidescloud.models.time_unit_type import TimeUnitType
from asposeslidescloud.models.video_play_mode_preset import VideoPlayModePreset
from asposeslidescloud.models.add_layout_slide import AddLayoutSlide
from asposeslidescloud.models.add_master_slide import AddMasterSlide
from asposeslidescloud.models.add_shape import AddShape
from asposeslidescloud.models.add_slide import AddSlide
from asposeslidescloud.models.api_info_response import ApiInfoResponse
from asposeslidescloud.models.base64_input_file import Base64InputFile
from asposeslidescloud.models.bubble_chart_data_point import BubbleChartDataPoint
from asposeslidescloud.models.bubble_series import BubbleSeries
from asposeslidescloud.models.color_scheme import ColorScheme
from asposeslidescloud.models.color_scheme_response import ColorSchemeResponse
from asposeslidescloud.models.document import Document
from asposeslidescloud.models.document_properties import DocumentProperties
from asposeslidescloud.models.document_properties_response import DocumentPropertiesResponse
from asposeslidescloud.models.document_property import DocumentProperty
from asposeslidescloud.models.document_property_response import DocumentPropertyResponse
from asposeslidescloud.models.document_response import DocumentResponse
from asposeslidescloud.models.font_scheme import FontScheme
from asposeslidescloud.models.font_scheme_response import FontSchemeResponse
from asposeslidescloud.models.format_scheme import FormatScheme
from asposeslidescloud.models.format_scheme_response import FormatSchemeResponse
from asposeslidescloud.models.gradient_fill import GradientFill
from asposeslidescloud.models.html_export_options import HtmlExportOptions
from asposeslidescloud.models.image import Image
from asposeslidescloud.models.image_export_options import ImageExportOptions
from asposeslidescloud.models.images import Images
from asposeslidescloud.models.images_response import ImagesResponse
from asposeslidescloud.models.layout_slide import LayoutSlide
from asposeslidescloud.models.layout_slide_list_response import LayoutSlideListResponse
from asposeslidescloud.models.layout_slide_response import LayoutSlideResponse
from asposeslidescloud.models.layout_slides import LayoutSlides
from asposeslidescloud.models.master_slide import MasterSlide
from asposeslidescloud.models.master_slide_list_response import MasterSlideListResponse
from asposeslidescloud.models.master_slide_response import MasterSlideResponse
from asposeslidescloud.models.master_slides import MasterSlides
from asposeslidescloud.models.merge import Merge
from asposeslidescloud.models.no_fill import NoFill
from asposeslidescloud.models.notes_slide import NotesSlide
from asposeslidescloud.models.notes_slide_response import NotesSlideResponse
from asposeslidescloud.models.one_value_series import OneValueSeries
from asposeslidescloud.models.paragraph import Paragraph
from asposeslidescloud.models.paragraph_list import ParagraphList
from asposeslidescloud.models.paragraph_list_response import ParagraphListResponse
from asposeslidescloud.models.paragraph_response import ParagraphResponse
from asposeslidescloud.models.path_input_file import PathInputFile
from asposeslidescloud.models.path_output_file import PathOutputFile
from asposeslidescloud.models.pattern_fill import PatternFill
from asposeslidescloud.models.pdf_export_options import PdfExportOptions
from asposeslidescloud.models.picture_fill import PictureFill
from asposeslidescloud.models.placeholder import Placeholder
from asposeslidescloud.models.placeholder_response import PlaceholderResponse
from asposeslidescloud.models.placeholders import Placeholders
from asposeslidescloud.models.placeholders_response import PlaceholdersResponse
from asposeslidescloud.models.portion import Portion
from asposeslidescloud.models.portion_list import PortionList
from asposeslidescloud.models.portion_list_response import PortionListResponse
from asposeslidescloud.models.portion_response import PortionResponse
from asposeslidescloud.models.remove_shape import RemoveShape
from asposeslidescloud.models.remove_slide import RemoveSlide
from asposeslidescloud.models.reorder_slide import ReorderSlide
from asposeslidescloud.models.replace_text import ReplaceText
from asposeslidescloud.models.request_input_file import RequestInputFile
from asposeslidescloud.models.reset_slide import ResetSlide
from asposeslidescloud.models.response_output_file import ResponseOutputFile
from asposeslidescloud.models.save import Save
from asposeslidescloud.models.save_shape import SaveShape
from asposeslidescloud.models.save_slide import SaveSlide
from asposeslidescloud.models.scatter_series import ScatterSeries
from asposeslidescloud.models.shape_base import ShapeBase
from asposeslidescloud.models.shape_list_response import ShapeListResponse
from asposeslidescloud.models.shape_response import ShapeResponse
from asposeslidescloud.models.shapes import Shapes
from asposeslidescloud.models.slide import Slide
from asposeslidescloud.models.slide_background import SlideBackground
from asposeslidescloud.models.slide_background_response import SlideBackgroundResponse
from asposeslidescloud.models.slide_comments import SlideComments
from asposeslidescloud.models.slide_comments_response import SlideCommentsResponse
from asposeslidescloud.models.slide_list_response import SlideListResponse
from asposeslidescloud.models.slide_response import SlideResponse
from asposeslidescloud.models.slides import Slides
from asposeslidescloud.models.solid_fill import SolidFill
from asposeslidescloud.models.split_document_response import SplitDocumentResponse
from asposeslidescloud.models.split_document_result import SplitDocumentResult
from asposeslidescloud.models.stream import Stream
from asposeslidescloud.models.string_replace_response import StringReplaceResponse
from asposeslidescloud.models.svg_export_options import SvgExportOptions
from asposeslidescloud.models.swf_export_options import SwfExportOptions
from asposeslidescloud.models.text_items import TextItems
from asposeslidescloud.models.text_items_response import TextItemsResponse
from asposeslidescloud.models.theme import Theme
from asposeslidescloud.models.theme_response import ThemeResponse
from asposeslidescloud.models.tiff_export_options import TiffExportOptions
from asposeslidescloud.models.update_background import UpdateBackground
from asposeslidescloud.models.update_shape import UpdateShape
from asposeslidescloud.models.xps_export_options import XpsExportOptions
from asposeslidescloud.models.chart import Chart
from asposeslidescloud.models.geometry_shape import GeometryShape
from asposeslidescloud.models.graphical_object import GraphicalObject
from asposeslidescloud.models.group_shape import GroupShape
from asposeslidescloud.models.ole_object_frame import OleObjectFrame
from asposeslidescloud.models.presentation_string_replace_response import PresentationStringReplaceResponse
from asposeslidescloud.models.slide_string_replace_response import SlideStringReplaceResponse
from asposeslidescloud.models.smart_art import SmartArt
from asposeslidescloud.models.smart_art_shape import SmartArtShape
from asposeslidescloud.models.table import Table
from asposeslidescloud.models.audio_frame import AudioFrame
from asposeslidescloud.models.connector import Connector
from asposeslidescloud.models.picture_frame import PictureFrame
from asposeslidescloud.models.shape import Shape
from asposeslidescloud.models.video_frame import VideoFrame



from asposeslidescloud.models.requests.document_api_requests import GetSlidesDocumentRequest
from asposeslidescloud.models.requests.document_api_requests import GetSlidesDocumentWithFormatRequest
from asposeslidescloud.models.requests.document_api_requests import PostSlidesDocumentRequest
from asposeslidescloud.models.requests.document_api_requests import PostSlidesPipelineRequest
from asposeslidescloud.models.requests.document_api_requests import PostSlidesSaveAsRequest
from asposeslidescloud.models.requests.document_api_requests import PostSlidesSplitRequest
from asposeslidescloud.models.requests.document_api_requests import PutNewPresentationRequest
from asposeslidescloud.models.requests.document_api_requests import PutSlidesConvertRequest
from asposeslidescloud.models.requests.document_api_requests import PutSlidesDocumentFromHtmlRequest
from asposeslidescloud.models.requests.document_api_requests import PutSlidesSlideSizeRequest
from asposeslidescloud.models.requests.images_api_requests import GetSlidesImageWithFormatRequest
from asposeslidescloud.models.requests.images_api_requests import GetSlidesImagesRequest
from asposeslidescloud.models.requests.images_api_requests import GetSlidesSlideImagesRequest
from asposeslidescloud.models.requests.layout_slides_api_requests import GetLayoutSlideRequest
from asposeslidescloud.models.requests.layout_slides_api_requests import GetLayoutSlidesListRequest
from asposeslidescloud.models.requests.layout_slides_api_requests import PostCopyLayoutSlideFromSourcePresentationRequest
from asposeslidescloud.models.requests.layout_slides_api_requests import PutLayoutSlideRequest
from asposeslidescloud.models.requests.master_slides_api_requests import GetMasterSlideRequest
from asposeslidescloud.models.requests.master_slides_api_requests import GetMasterSlidesListRequest
from asposeslidescloud.models.requests.master_slides_api_requests import PostCopyMasterSlideFromSourcePresentationRequest
from asposeslidescloud.models.requests.merge_document_api_requests import PostPresentationMergeRequest
from asposeslidescloud.models.requests.merge_document_api_requests import PutPresentationMergeRequest
from asposeslidescloud.models.requests.notes_slide_api_requests import DeleteNotesSlideRequest
from asposeslidescloud.models.requests.notes_slide_api_requests import GetNotesSlideRequest
from asposeslidescloud.models.requests.notes_slide_api_requests import GetNotesSlideWithFormatRequest
from asposeslidescloud.models.requests.notes_slide_api_requests import PostAddNotesSlideRequest
from asposeslidescloud.models.requests.notes_slide_api_requests import PutUpdateNotesSlideRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import DeleteNotesSlideParagraphRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import DeleteNotesSlideParagraphsRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import DeleteNotesSlidePortionRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import DeleteNotesSlidePortionsRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import DeleteNotesSlideShapeRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import DeleteNotesSlideShapesRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import GetNotesSlideShapeRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import GetNotesSlideShapeParagraphRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import GetNotesSlideShapeParagraphsRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import GetNotesSlideShapePortionRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import GetNotesSlideShapePortionsRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import GetNotesSlideShapeWithFormatRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import GetNotesSlideShapesRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import PostNotesSlideAddNewParagraphRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import PostNotesSlideAddNewPortionRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import PostNotesSlideAddNewShapeRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import PostNotesSlideShapeSaveAsRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import PutUpdateNotesSlideShapeRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import PutUpdateNotesSlideShapeParagraphRequest
from asposeslidescloud.models.requests.notes_slide_shapes_api_requests import PutUpdateNotesSlideShapePortionRequest
from asposeslidescloud.models.requests.placeholders_api_requests import GetSlidesPlaceholderRequest
from asposeslidescloud.models.requests.placeholders_api_requests import GetSlidesPlaceholdersRequest
from asposeslidescloud.models.requests.properties_api_requests import DeleteSlidesDocumentPropertiesRequest
from asposeslidescloud.models.requests.properties_api_requests import DeleteSlidesDocumentPropertyRequest
from asposeslidescloud.models.requests.properties_api_requests import GetSlidesDocumentPropertiesRequest
from asposeslidescloud.models.requests.properties_api_requests import GetSlidesDocumentPropertyRequest
from asposeslidescloud.models.requests.properties_api_requests import PostSlidesSetDocumentPropertiesRequest
from asposeslidescloud.models.requests.properties_api_requests import PutSlidesSetDocumentPropertyRequest
from asposeslidescloud.models.requests.shapes_api_requests import DeleteParagraphRequest
from asposeslidescloud.models.requests.shapes_api_requests import DeleteParagraphsRequest
from asposeslidescloud.models.requests.shapes_api_requests import DeletePortionRequest
from asposeslidescloud.models.requests.shapes_api_requests import DeletePortionsRequest
from asposeslidescloud.models.requests.shapes_api_requests import DeleteSlideShapeRequest
from asposeslidescloud.models.requests.shapes_api_requests import DeleteSlideShapesRequest
from asposeslidescloud.models.requests.shapes_api_requests import GetParagraphPortionRequest
from asposeslidescloud.models.requests.shapes_api_requests import GetParagraphPortionsRequest
from asposeslidescloud.models.requests.shapes_api_requests import GetShapeParagraphRequest
from asposeslidescloud.models.requests.shapes_api_requests import GetShapeWithFormatRequest
from asposeslidescloud.models.requests.shapes_api_requests import GetSlideShapeRequest
from asposeslidescloud.models.requests.shapes_api_requests import GetSlideShapeParagraphsRequest
from asposeslidescloud.models.requests.shapes_api_requests import GetSlideShapesRequest
from asposeslidescloud.models.requests.shapes_api_requests import PostAddNewParagraphRequest
from asposeslidescloud.models.requests.shapes_api_requests import PostAddNewPortionRequest
from asposeslidescloud.models.requests.shapes_api_requests import PostAddNewShapeRequest
from asposeslidescloud.models.requests.shapes_api_requests import PostShapeSaveAsRequest
from asposeslidescloud.models.requests.shapes_api_requests import PutSetParagraphPortionPropertiesRequest
from asposeslidescloud.models.requests.shapes_api_requests import PutSetParagraphPropertiesRequest
from asposeslidescloud.models.requests.shapes_api_requests import PutSlideShapeInfoRequest
from asposeslidescloud.models.requests.slides_api_requests import DeleteSlideByIndexRequest
from asposeslidescloud.models.requests.slides_api_requests import DeleteSlidesCleanSlidesListRequest
from asposeslidescloud.models.requests.slides_api_requests import DeleteSlidesSlideBackgroundRequest
from asposeslidescloud.models.requests.slides_api_requests import GetSlideWithFormatRequest
from asposeslidescloud.models.requests.slides_api_requests import GetSlidesSlideRequest
from asposeslidescloud.models.requests.slides_api_requests import GetSlidesSlideBackgroundRequest
from asposeslidescloud.models.requests.slides_api_requests import GetSlidesSlideCommentsRequest
from asposeslidescloud.models.requests.slides_api_requests import GetSlidesSlidesListRequest
from asposeslidescloud.models.requests.slides_api_requests import PostSlideSaveAsRequest
from asposeslidescloud.models.requests.slides_api_requests import PostSlidesAddRequest
from asposeslidescloud.models.requests.slides_api_requests import PostSlidesCopyRequest
from asposeslidescloud.models.requests.slides_api_requests import PostSlidesReorderRequest
from asposeslidescloud.models.requests.slides_api_requests import PostSlidesReorderManyRequest
from asposeslidescloud.models.requests.slides_api_requests import PostSlidesReorderPositionRequest
from asposeslidescloud.models.requests.slides_api_requests import PutSlidesSlideRequest
from asposeslidescloud.models.requests.slides_api_requests import PutSlidesSlideBackgroundRequest
from asposeslidescloud.models.requests.text_api_requests import GetSlidesPresentationTextItemsRequest
from asposeslidescloud.models.requests.text_api_requests import GetSlidesSlideTextItemsRequest
from asposeslidescloud.models.requests.text_api_requests import PostSlidesPresentationReplaceTextRequest
from asposeslidescloud.models.requests.text_api_requests import PostSlidesSlideReplaceTextRequest
from asposeslidescloud.models.requests.theme_api_requests import GetSlidesThemeRequest
from asposeslidescloud.models.requests.theme_api_requests import GetSlidesThemeColorSchemeRequest
from asposeslidescloud.models.requests.theme_api_requests import GetSlidesThemeFontSchemeRequest
from asposeslidescloud.models.requests.theme_api_requests import GetSlidesThemeFormatSchemeRequest
