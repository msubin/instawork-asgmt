from django.test import TestCase
from ..forms import MemberForm


class MemberFormTests(TestCase):
    def test_valid_form_submission(self):
        form_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'isAdmin': 'True',
            'phoneNumber': '+12345678901',
            'email': 'john.doe@example.com',
        }
        form = MemberForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_submission(self):
        form_data = {
            'first_name': 'John',
            'last_name': '',
            'isAdmin': 'True',
            'phoneNumber': '+12345678901',
            'email': 'john.doe@example.com',
        }
        form = MemberForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)
        self.assertEqual(form.errors['last_name'], ['This field is required.'])
