from django.contrib.auth import get_user_model
from django.test import TestCase

from catalog.models import LiteraryFormat, Book


class ModelsTest(TestCase):
    def test_literary_format_str(self):
        format_ = LiteraryFormat.objects.create(name="test")

        self.assertEqual(str(format_), format_.name)

    def test_author_str(self):
        author = get_user_model().objects.create_user(
            username="t_sheva",
            password="shevataras1234567",
            first_name="Taras",
            last_name="Shevchenko",
        )

        self.assertEqual(str(author), "t_sheva (Taras Shevchenko)")

    def test_book_str(self):
        format_ = LiteraryFormat.objects.create(name="test")
        book = Book.objects.create(
            title="Kobzar",
            price=100,
            format=format_
        )

        self.assertEqual(str(book), "Kobzar (price: 100, format: test)")

    def test_create_author_with_pseudonym(self):
        username = "user"
        password = "useruser9876543221"
        pseudonym = "Tets pseudo"
        author = get_user_model().objects.create_user(
            username=username,
            password=password,
            pseudonym=pseudonym
        )

        self.assertEqual(author.username, username)
        self.assertTrue(author.check_password(password))
        self.assertEqual(author.pseudonym, pseudonym)
