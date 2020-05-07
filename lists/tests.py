from django.test import TestCase
from . import models

from . import views


class HomePageTest(TestCase):
    """тест домашней страницы"""

    def test_uses_home_template(self):
        """Тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        """Тест: Можно сохранить post-запрос"""
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        # self.assertTempLateYsed(response, 'home.html')


class ItemModelTest(TestCase):
    """тест модели элемента списка"""

    def test_saving_and_retrieving_items(self):
        """Тест сохранения и получения элементов списка"""
        first_item = models.Item()
        first_item.text = "The first (ever) list item"
        first_item.save()

        second_item = models.Item()
        second_item.text = 'Item the second'
        second_item.save()
        saved_items = models.Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        fitst_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(fitst_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
