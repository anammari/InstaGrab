from instagrab import media_pic
import unittest
from unittest import mock

class TestMediaPic(unittest.TestCase):

    def test_get_image_url(self):
        url = "https://www.instagram.com/p/CxApz_9NID5/"
        image_url = media_pic.get_image_url(url)
        self.assertTrue(image_url.startswith("http"))

    def test_download_image(self):
        url = "https://www.instagram.com/p/CxApz_9NID5/"
        image_url = media_pic.get_image_url(url)
        image_data = media_pic.download_image(image_url)
        self.assertGreater(len(image_data), 0)
        
    @mock.patch("builtins.open", new_callable=mock.mock_open)
    def test_save_image(self, mock_open):
        image_data = b"test image data"
        file_name = "test.jpg"
        media_pic.save_image(image_data, file_name)
        mock_open.assert_called_once_with(file_name, "wb")
        handle = mock_open()
        handle.write.assert_called_once_with(image_data)

if __name__ == '__main__':
    unittest.main()

