import unittest
from photo_album import retrieve_photos, display_photos

class TestPhotoAlbum(unittest.TestCase):

    def test_retrieve_photos(self):
        # Test that the function does not raise an exception
        try:
            retrieve_photos(2)
        except Exception as e:
            self.fail(f"retrieve_photos raised an exception: {e}")

    def test_display_photos(self):
        # Test that the function does not raise an exception
        try:
            display_photos(retrieve_photos(2))  # Pass a single JSON entry object
        except Exception as e:
            self.fail(f"display_photos raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
