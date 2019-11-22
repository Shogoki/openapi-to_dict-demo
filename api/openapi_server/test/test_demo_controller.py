# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.my_model import MyModel  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDemoController(BaseTestCase):
    """DemoController integration test stubs"""

    def test_get_demo(self):
        """Test case for get_demo

        
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/demo',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
