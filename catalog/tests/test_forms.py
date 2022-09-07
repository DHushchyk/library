from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from catalog.forms import AuthorCreationForm


class FormsTest(TestCase):
    def test_author_creation_form_with_pseudonym_first_name_last_name_is_valid(self):
        form_data = {
            "username": "new_user",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test first",
            "last_name": "Test last",
            "pseudonym": "Tst pseudo"
        }
        form = AuthorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class PrivateAuthorTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test",
            "password123"
        )
        self.client.force_login(self.user)

    def test_create_author(self):
        form_data = {
            "username": "new_user",
            "password1": "user123test",
            "password2": "user123test",
            "first_name": "Test first",
            "last_name": "Test last",
            "pseudonym": "Tst pseudo"
        }
        self.client.post(reverse("catalog:author-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.pseudonym, form_data["pseudonym"])
