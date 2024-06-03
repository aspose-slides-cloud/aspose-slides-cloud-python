from __future__ import absolute_import

from asposeslidescloud import Configuration
from asposeslidescloud.rest import ApiException
from test.base_test import BaseTest
import asposeslidescloud

class TestAuth(BaseTest):
    def setUp(self):
        self.api = asposeslidescloud.apis.slides_api.SlidesApi(self.slides_api_configuration)  # noqa: E501

    def tearDown(self):
        pass

    def test_good_auth(self):
        config = Configuration()
        config.app_sid = self.slides_api_configuration.app_sid
        config.app_key = self.slides_api_configuration.app_key
        config.base_url = self.slides_api_configuration.base_url
        config.auth_base_url = self.slides_api_configuration.auth_base_url
        config.debug = self.slides_api_configuration.debug
        config.verify_ssl = self.slides_api_configuration.verify_ssl
        api = asposeslidescloud.apis.slides_api.SlidesApi(config)
        api.get_api_info()

    def test_bad_auth(self):
        config = Configuration()
        config.app_sid = "invalid"
        config.app_key = self.slides_api_configuration.app_key
        config.base_url = self.slides_api_configuration.base_url
        config.auth_base_url = self.slides_api_configuration.auth_base_url
        config.verify_ssl = self.slides_api_configuration.verify_ssl
        config.debug = self.slides_api_configuration.debug
        try:
            api = asposeslidescloud.apis.slides_api.SlidesApi(config)
            api.get_api_info()
            self.fail("Must have failed")
        except ApiException as ex:
            self.assertEqual(401, ex.status)

    def test_good_token(self):
        config = Configuration()
        config.app_sid = self.slides_api_configuration.app_sid
        config.app_key = self.slides_api_configuration.app_key
        config.base_url = self.slides_api_configuration.base_url
        config.auth_base_url = self.slides_api_configuration.auth_base_url
        config.debug = self.slides_api_configuration.debug
        config.verify_ssl = self.slides_api_configuration.verify_ssl
        api = asposeslidescloud.apis.slides_api.SlidesApi(config)
        api.get_api_info()
        config.app_sid = "invalid"
        api = asposeslidescloud.apis.slides_api.SlidesApi(config)
        api.get_api_info()

    def test_bad_token(self):
        config = Configuration()
        config.app_sid = self.slides_api_configuration.app_sid
        config.app_key = self.slides_api_configuration.app_key
        config.base_url = self.slides_api_configuration.base_url
        config.auth_base_url = self.slides_api_configuration.auth_base_url
        config.debug = self.slides_api_configuration.debug
        config.verify_ssl = self.slides_api_configuration.verify_ssl
        config.access_token = "invalid"
        api = asposeslidescloud.apis.slides_api.SlidesApi(config)
        api.get_api_info()

    def test_expired_token(self):
        config = Configuration()
        config.app_sid = self.slides_api_configuration.app_sid
        config.app_key = self.slides_api_configuration.app_key
        config.base_url = self.slides_api_configuration.base_url
        config.auth_base_url = self.slides_api_configuration.auth_base_url
        config.debug = self.slides_api_configuration.debug
        config.verify_ssl = self.slides_api_configuration.verify_ssl
        config.access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE2ODYzMzI5ODAsImV4cCI6MTY4NjQxOTM4MCwiaXNzIjoiaHR0cHM6Ly9hcGkuYXNwb3NlLmNsb3VkIiwiYXVkIjpbImh0dHBzOi8vYXBpLmFzcG9zZS5jbG91ZC9yZXNvdXJjZXMiLCJhcGkuYmlsbGluZyIsImFwaS5pZGVudGl0eSIsImFwaS5wcm9kdWN0cyIsImFwaS5zdG9yYWdlIl0sImNsaWVudF9pZCI6ImVhMTFkNzAwLWE3YjAtNDgwMi05YjFjLWRmYWVhNGI2OTA0YSIsImNsaWVudF9kZWZhdWx0X3N0b3JhZ2UiOiIyNDc5NjRmYy04MjIyLTQ4M2EtYmZmMS1kNTYxYzM5MjQ3ZWIiLCJjbGllbnRfaWRlbnRpdHlfdXNlcl9pZCI6Ijc2MjY4MiIsInNjb3BlIjpbImFwaS5iaWxsaW5nIiwiYXBpLmlkZW50aXR5IiwiYXBpLnByb2R1Y3RzIiwiYXBpLnN0b3JhZ2UiXX0.qGRwbpVQNJ7k09FF81bfknBd_9bERkProMukobxkAEzwIhIRSwCDvzgVhhUcA-OMr8s-49XLYtFb6ZtuDT2r3xDsYXWxwjYekFk4MZhEFKeIqLyI9-kSxanL7w4WoKkE_OAXHquChRJcsqz5vhKOOJ9swu4PS0TSRYHfkLFsLpZLXIV4X53Ear8vDosOfeZONq9QPCfikCi1ruSMa3OddD2WE17_V3FzzyuC7d3FQxRznFJhyWoKI2jvOw7a92KatWVt3I78fOl9M-3MkkHR1ip5CXp3arnn139i73D-TfXeRNcAU5UpAGfuYPbIDpTkJ-DirqYWO6I5S7JmchPl1A"
        api = asposeslidescloud.apis.slides_api.SlidesApi(config)
        api.get_api_info()