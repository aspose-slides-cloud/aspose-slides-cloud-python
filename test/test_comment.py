from __future__ import absolute_import

from asposeslidescloud import SlideComment, SlideModernComment, CommentAuthors
from test.base_test import BaseTest

class TestComment(BaseTest):
    def setUp(self):
        self.slide_index = 3
        self.comment_text = "Comment text"
        self.child_comment_text = "Child comment text"
        self.comment_author = "Test author"

    def tearDown(self):
        pass

    def test_create_comment(self):
        dto = SlideComment()
        dto.text = self.comment_text
        dto.author = self.comment_author
        child_comment = SlideComment()
        child_comment.text = self.child_comment_text
        child_comment.author = self.comment_author
        dto.child_comments = [child_comment]

        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.create_comment(self.file_name, self.slide_index, dto, None, self.password, self.folder_name)
        self.assertEqual(1, len(response.list))
        self.assertEqual(self.comment_author, response.list[0].author)
        self.assertEqual(self.comment_text, response.list[0].text)
        self.assertEqual(self.child_comment_text, response.list[0].child_comments[0].text)
        self.assertEqual(self.comment_author, response.list[0].child_comments[0].author)

    def test_create_comment_online(self):
        dto = SlideComment()
        dto.text = self.comment_text
        dto.author = self.comment_author
        child_comment = SlideComment()
        child_comment.text = self.child_comment_text
        child_comment.author = self.comment_author
        dto.child_comments = [child_comment]

        with open(self.local_path, 'rb') as f:
            document = f.read()
        output_document = BaseTest.slides_api.create_comment_online(document, self.slide_index, dto, None, self.password)
        self.assertIsNotNone(output_document)

    def test_get_slide_comments(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_slide_comments(self.file_name, 1, self.password, self.folder_name)
        self.assertEqual(2, len(response.list))
        self.assertEqual(1, len(response.list[0].child_comments))

    def test_delete_comments(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        BaseTest.slides_api.delete_comments(self.file_name, None, self.password, self.folder_name)
        response = BaseTest.slides_api.get_slide_comments(self.file_name, 1, self.password, self.folder_name)
        self.assertEqual(0, len(response.list))

    def test_delete_comments_online(self):
        with open(self.local_path, 'rb') as f:
            document = f.read()
        output_document = BaseTest.slides_api.delete_comments_online(document, None, self.password)
        self.assertIsNotNone(output_document)

    def test_delete_slides_comments(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        slide_index = 1
        BaseTest.slides_api.delete_slide_comments(self.file_name, slide_index, None, self.password, self.folder_name)
        response = BaseTest.slides_api.get_slide_comments(self.file_name, slide_index, self.password, self.folder_name)
        self.assertEqual(0, len(response.list))

    def test_delete_slide_comments_online(self):
        with open(self.local_path, 'rb') as f:
            document = f.read()
        outputDocument = BaseTest.slides_api.delete_slide_comments_online(document, 1, None, self.password)
        self.assertIsNotNone(outputDocument)

    def test_create_modern_comment(self):
        text_selection_start_index = 1
        text_selection_length = 5

        child_comment = SlideModernComment()
        child_comment.text = self.child_comment_text
        child_comment.author = self.comment_author
        child_comment.status = "Resolved"

        comment = SlideModernComment()
        comment.text = self.comment_text
        comment.author = self.comment_author
        comment.status = "Active"
        comment.text_selection_start = text_selection_start_index
        comment.text_selection_length = text_selection_length
        comment.child_comments = [child_comment]

        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.create_comment(self.file_name, self.slide_index, comment, None, self.password, self.folder_name)
        self.assertEqual(1, len(response.list))
        self.assertEqual("Modern", response.list[0].type)

    def test_create_modern_comment_shape(self):
        text_selection_start_index = 1
        text_selection_length = 5

        child_comment = SlideModernComment()
        child_comment.text = self.child_comment_text
        child_comment.author = self.comment_author
        child_comment.status = "Resolved"

        comment = SlideModernComment()
        comment.text = self.comment_text
        comment.author = self.comment_author
        comment.status = "Active"
        comment.text_selection_start = text_selection_start_index
        comment.text_selection_length = text_selection_length
        comment.child_comments = [child_comment]

        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.create_comment(self.file_name, self.slide_index, comment, 1, self.password, self.folder_name)
        self.assertEqual(1, len(response.list))
        self.assertEqual("Modern", response.list[0].type)

    def test_get_comment_authors(self):
        BaseTest.slides_api.copy_file(self.temp_path, self.path)
        response = BaseTest.slides_api.get_comment_authors(self.file_name, self.password, self.folder_name)
        self.assertEqual(1, len(response.list))