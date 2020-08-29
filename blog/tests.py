
from django.test import TestCase
from .models import Post
from .models import CV 

class CVPageTest(TestCase):
    '''

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'homepage.html')

    def test_can_save_a_POST_request(self):
        self.client.post('/', data={'title': 'TDD Approach'})

        self.assertEqual(Post.objects.count(), 1)
        new_post = Post.objects.first()
        self.assertEqual(new_post.title, 'TDD Approach')


    def test_redirects_after_POST(self):
        response = self.client.post('/', data={'title': 'TDD Approach'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_displays_all_posts(self):
        Post.objects.create(text='Post 1')
        Post.objects.create(text='Post 2')

        response = self.client.get('/')

        self.assertIn('Post 1', response.content.decode())
        self.assertIn('Post 2', response.content.decode())
    '''
class CVModelTest(TestCase):
    '''

     def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
        '''
