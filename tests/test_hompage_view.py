from django.test import TestCase
from IPython import embed

class TestHomepageView(TestCase):
    def test_homepage_exists_at_root(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<p id=\'welcome\'>Welcome To<br>Dragons and Dungeons</p>", response.content)
