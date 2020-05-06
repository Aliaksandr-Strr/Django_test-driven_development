from django.test import TestCase
from . import views


class HomePageTest(TestCase):
    """тест домашней страницы"""

    def test_uses_home_template(self):
        """Тест: используется домашний шаблон"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
