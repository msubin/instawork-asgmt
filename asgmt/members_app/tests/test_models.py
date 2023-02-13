from django.test import TestCase
from ..models import Member


class MemberModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Member.objects.create(first_name="John", last_name="Doe", email="jane@instawork.com", phoneNumber="1234567890")

    def test_first_name_label(self):
        member = Member.objects.get(id=1)
        field_label = member._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name_label(self):
        member = Member.objects.get(id=1)
        field_label = member._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_email_label(self):
        member = Member.objects.get(id=1)
        field_label = member._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_phoneNumber_label(self):
        member = Member.objects.get(id=1)
        field_label = member._meta.get_field('phoneNumber').verbose_name
        self.assertEquals(field_label, 'phoneNumber')

    def test_isAdmin_label(self):
        member = Member.objects.get(id=1)
        field_label = member._meta.get_field('isAdmin').verbose_name
        self.assertEquals(field_label, 'isAdmin')

    def test_first_name_max_length(self):
        member = Member.objects.get(id=1)
        max_length = member._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_last_name_max_length(self):
        member = Member.objects.get(id=1)
        max_length = member._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_full_name(self):
        member = Member.objects.get(id=1)
        expected_output = f"{member.first_name} {member.last_name}"
        self.assertEquals(expected_output, str(member))

    def test_default_isAdmin(self):
        member = Member.objects.get(id=1)
        self.assertFalse(member.isAdmin)

    def test_phoneNum_max_length(self):
        member = Member.objects.get(id=1)
        max_length = member._meta.get_field('phoneNumber').max_length
        self.assertEquals(max_length, 16)
