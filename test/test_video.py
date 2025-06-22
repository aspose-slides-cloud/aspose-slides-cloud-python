from __future__ import absolute_import

import os
from zipfile import ZipFile

from test.base_test import BaseTest
from asposeslidescloud import VideoFrame
from asposeslidescloud.rest import ApiException

class TestVideo(BaseTest):
    def setUp(self):
        self.slide_index = 1
        self.image_index = 1
        self.image_path = self.test_data_path + "/watermark.png"

    def tearDown(self):
        pass

    def test_caption_tracks(self):
        slide_index = 3
        shape_index = 3
        track1_label = "track1"
        track2_label = "track2"
        track1_data = "WEBVTT\n\n00:00:00.000 --> 00:00:10.000\nCaption 1 text."
        track2_data = "WEBVTT\n\n00:00:00.000 --> 00:00:10.000\nCaption 2 text."
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        dto = VideoFrame()
        dto.base64_data = 'bXAzc2FtcGxl'
        BaseTest.slides_api.create_shape(self.file_name, slide_index, dto, None, None, self.password, self.folder_name)
        captions = BaseTest.slides_api.get_video_caption_tracks(self.file_name, slide_index, shape_index, None, self.password, self.folder_name)
        self.assertEqual(0, len(captions.items))

        BaseTest.slides_api.create_video_caption_track(self.file_name, slide_index, shape_index, track1_label, track1_data, self.password, self.folder_name)
        BaseTest.slides_api.create_video_caption_track(self.file_name, slide_index, shape_index, track2_label, track2_data, self.password, self.folder_name)
        captions = BaseTest.slides_api.get_video_caption_tracks(self.file_name, slide_index, shape_index, True, self.password, self.folder_name)
        self.assertEqual(2, len(captions.items))
        self.assertEqual(track1_label, captions.items[0].label)
        self.assertEqual(track1_data, captions.items[0].data_as_string)
        self.assertEqual(track2_label, captions.items[1].label)
        self.assertEqual(track2_data, captions.items[1].data_as_string)

        BaseTest.slides_api.delete_video_caption_track(self.file_name, slide_index, shape_index, 1, self.password, self.folder_name)
        captions = BaseTest.slides_api.get_video_caption_tracks(self.file_name, slide_index, shape_index, False, self.password, self.folder_name)
        self.assertEqual(1, len(captions.items))
        self.assertEqual(track2_label, captions.items[0].label)
        self.assertIsNone(captions.items[0].data_as_string)

        BaseTest.slides_api.delete_video_caption_tracks(self.file_name, slide_index, shape_index, self.password, self.folder_name)
        captions = BaseTest.slides_api.get_video_caption_tracks(self.file_name, slide_index, shape_index, False, self.password, self.folder_name)
        self.assertEqual(0, len(captions.items))
