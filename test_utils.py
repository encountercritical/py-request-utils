import unittest
from unittest.mock import patch, MagicMock
import utils


class TestUtils(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_get(self, mock_urlopen):
        # Mock response
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"status": "ok"}'
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        result = utils.get('http://example.com')
        self.assertEqual(result, '{"status": "ok"}')

    @patch('urllib.request.urlopen')
    def test_post(self, mock_urlopen):
        # Mock response
        mock_response = MagicMock()
        mock_response.read.return_value = b'{"success": true}'
        mock_response.__enter__.return_value = mock_response
        mock_urlopen.return_value = mock_response

        data = {"key": "value"}
        result = utils.post('http://example.com', data)
        self.assertEqual(result, '{"success": true}')

    def test_build_url(self):
        base = 'http://example.com/api'
        result = utils.build_url(base, key1='val1', key2='val2')
        self.assertEqual(result, 'http://example.com/api?key1=val1&key2=val2')

    def test_build_url_with_existing_params(self):
        base = 'http://example.com/api?a=b'
        result = utils.build_url(base, c='d')
        self.assertEqual(result, 'http://example.com/api?a=b&c=d')

    def test_build_url_preserves_multiple_values(self):
        base = 'http://example.com/api?a=1&a=2'
        result = utils.build_url(base, c='3')
        self.assertEqual(result, 'http://example.com/api?a=1&a=2&c=3')

    def test_build_url_updates_existing_value(self):
        base = 'http://example.com/api?a=1&b=2'
        result = utils.build_url(base, a='3')
        self.assertEqual(result, 'http://example.com/api?a=3&b=2')


if __name__ == '__main__':
    unittest.main()
