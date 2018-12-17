from django.test import TestCase
from .models import Post

class IndexViewTests(TestCase):
    def test_displays_title(self):
        """
        Displays the title of all posts
        """

        Post.objects.create(title="Test")
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test')

# Create your tests here.
