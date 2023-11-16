from django.test import TestCase
from ..models import Tag, Task
from datetime import date, timedelta

# Unit Tests
class TagTestCase(TestCase):
    def setUp(self):
        Tag.objects.create(user="user", title="Red", color="#cc0000")
        Tag.objects.create(user="user", title="Green", color="#6aa84f")
        Tag.objects.create(user="user", title="Blue", color="#2986cc")
        
class TaskTestCase(TestCase):
    today = date.today()
    threedays = today + timedelta(3)
    sevendays = today + timedelta(7)
    thirtydays = today + timedelta(30)
    sixtydays = today + timedelta(60)
    
    def setUp(self):
        Task.objects.create(user="user", title="Red 1", description="Test", tag="Red", complete=False, due=self.today)
        Task.objects.create(user="user", title="Blue 1", description="Test", tag="Blue", complete=False, due=self.today)
        Task.objects.create(user="user", title="Green 1", description="Test", tag="Green", complete=False, due=self.today)
        
        Task.objects.create(user="user", title="Red 2", description="Test", tag="Red", complete=False, due=self.sevendays)
        Task.objects.create(user="user", title="Blue 2", description="Test", tag="Blue", complete=False, due=self.sevendays)
        Task.objects.create(user="user", title="Green 2", description="Test", tag="Green", complete=False, due=self.sevendays)
        
        Task.objects.create(user="user", title="Blue 3", description="Test", tag="Blue", complete=False, due=self.thirtydays)
        Task.objects.create(user="user", title="Green 3", description="Test", tag="Green", complete=False, due=self.thirtydays)
        
        Task.objects.create(user="user", title="Green 4", description="Test", tag="Green", complete=False, due=self.sixtydays)