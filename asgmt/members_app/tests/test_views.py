from django.test import Client, TestCase
from ..models import Member
from ..forms import MemberForm


class MemberViewTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        self.client = Client()
        self.client = Client()
        self.member_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'isAdmin': 'False',
            'phoneNumber': '1234567890',
            'email': 'johndoe@example.com'
        }
        self.member = Member.objects.create(**self.member_data)

    def test_get_member_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'members_app/member_list.html')

    def test_create_member(self):
        response = self.client.post('/add/', data=self.member_data)
        self.assertTemplateUsed(response, 'members_app/new_member.html')

    def test_update_member(self):
        response = self.client.post(f'/update/{self.member.pk}/', data=self.member_data)
        self.assertRedirects(response, '/', status_code=302, target_status_code=200)

    def test_delete_member(self):
        response = self.client.post(f'/delete/{self.member.pk}/')
        self.assertRedirects(response, '/', status_code=302, target_status_code=200)
