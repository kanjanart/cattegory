from django.contrib.auth.models import User
from django.test import TestCase

from model_mommy import mommy


class CattegoryAdminTest(TestCase):
    def setUp(self):
        User.objects.create_superuser('admin', 'kwang@prontomarketing.com', 'admin')
        self.client.login(username='admin', password='admin')

        mommy.make(
            'Cattegory',
            species='scotish',
            price=9000,
            food='tuna',
            buy_place='facebook'
        )

        self.url = 'http://127.0.0.1:8000/admin/detail/cattegory/'

    def test_access_cattegory_admin(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
