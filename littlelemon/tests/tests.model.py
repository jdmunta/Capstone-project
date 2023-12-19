from django.tests import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='TestItem1', price=10.99, inventory=10)
        self.assertEquals(item, 'TestItem1 : 10.99')