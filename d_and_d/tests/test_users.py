from django.test import TestCase
from django.contrib.auth.models import User

class TestCreateModels(TestCase):
    def setUp(self):
        User.objects.create_user('joe', 'joe@joemail.joe', 'hidden')
        User.objects.create_user('bob', 'bob@bobmail.bob', 'secret')

    def test_users(self):
        joe = User.objects.get(username="joe")
        bob = User.objects.get(username="bob")
        self.assertEqual(joe.username, 'joe')
        self.assertEqual(joe.email, 'joe@joemail.joe')
        self.assertEqual(bob.username, 'bob')
        self.assertEqual(bob.email, 'bob@bobmail.bob')
