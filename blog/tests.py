from django.test import TestCase
from blog.models import Post


# Create your tests here.
class BlogModelTest(TestCase):
    """Test Blog Model"""

    def setUp(self):
        self.blog = Post.objects.create(
            title="django", author="John", slug="django"
        )

    def test_post_model(self):
        self.assertTrue(isinstance(self.blog, Post))
        self.assertEqual(str(self.blog), "django")
