from django.test import TestCase
from django.urls import reverse

from model_mommy import mommy


class HomeTest(TestCase):
    def test_get_species_should_return_all_species(self):
        mommy.make(
            'Cattegory',
            species='scotish',
            price=9000,
            food='tuna',
            buy_place='facebook'
        )

        mommy.make(
            'Cattegory',
            species='british shorthair',
            price=40000,
            food='tuna',
            buy_place='farm'
        )

        response = self.client.get(reverse('home'))

        expected_scotish = '<li>scotish</li>'
        self.assertContains(response, expected_scotish, status_code=200)

        expected_british = '<li>british shorthair</li>'
        self.assertContains(response, expected_british, status_code=200)
