from django.urls import reverse

from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from detail.models import Cattegory


class ListCattegoryTest(APITestCase):
    def setUp(self):
        self.cattegory = mommy.make(
            Cattegory,
            species='scottish',
            price=9000,
            food='fish',
            buy_place='facebook'
        )

    def test_list_cattegory_should_return_all_cattegory(self):
        response = self.client.get(reverse('cattegory_list'))

        expected = [{
            'species': 'scottish',
            'price': 9000,
            'food': 'fish',
            'buy_place': 'facebook'
        }]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)

    def test_filter_by_species_should_return_species(self):
        mommy.make(
            Cattegory,
            species='british shorthair',
            price=30000,
            food='cat food',
            buy_place='farm'
        )

        response = self.client.get(reverse('cattegory_list'), {'species': self.cattegory.species})

        expected = [{
            'species': 'scottish',
            'price': 9000,
            'food': 'fish',
            'buy_place': 'facebook'
        }]

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)
