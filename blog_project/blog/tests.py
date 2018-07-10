from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Author, Post


# Create your tests here.
class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )

        self.author = Author.objects.create(
            user=self.user,
            phone_number='+919422312223'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Nice Body Content',
            author=self.author
        )

    def test_string_representation(self):
        author = Author(user=get_user_model()(
            username='testuser',
            email='test@email.com',
            password='secret',
        ))

        post = Post(title='A sample title', author=author)
        self.assertEqual(f'{str(post)}', f'{post.title} - {author}')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice Body Content')

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice Body Content')
        self.assertTemplateUsed(response, 'blog/index.html')

    def test_post_detail_view(self):
        response = self.client.get('/1/details/')
        no_response = self.client.get('/1000000/details/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'blog/detail.html')
