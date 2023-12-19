from django.test import TestCase
from .models import Menu

class MenuTest(TestCase):

    def setup():
        Menu.objects.create(id=20,title='TestItem1', price=11.99, inventory=10)
        Menu.objects.create(id=21,title='TestItem2', price=12.99, inventory=20)
        Menu.objects.create(id=22,title='TestItem3', price=13.99, inventory=30)
    
    def test_all(self):
        items = Menu.objects.all()
        self.assertEquals(len(items),3)

    def test_get_item(self):
        item = Menu.objects.create(id=27,title='TestItem1', price=10.99, inventory=10)
        self.assertEquals(str(item), 'TestItem1 : 10.99')