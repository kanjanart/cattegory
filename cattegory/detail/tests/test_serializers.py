from django.test import TestCase

from model_mommy import mommy

from detail.models import Cattegory
from detail.serializers import CattegorySerializer


class ListCattegorySerializerTest(TestCase):
    def test_serializer_should_return_field(self):
        cattegorys = mommy.make(
            Cattegory,
            species='scottish',
            price=9000,
            food='fish',
            buy_place='facebook'
        )

        actual = CattegorySerializer(cattegorys).data

        expected = {
            'species': 'scottish',
            'price': 9000,
            'food': 'fish',
            'buy_place': 'facebook'
        }
        self.assertEqual(actual, expected)

    # def test_require_field(self):
    #     expected = {
    #         'species': ['This field is required.'],
    #         'price': ['This field is required.'],
    #         'food': ['This field is required.'],
    #         'buy_place': ['This field is required.']
    #     }

    #     actual = CattegorySerializer(data={})

    #     self.assertFalse(actual.is_valid())
    #     self.assertEqual(actual.errors, expected)

    # def test_fields_should_not_be_blank(self):
    #     cattegorys = {
    #         'price': ''
    #     }

    #     actual = CattegorySerializer(data=cattegorys)

    #     expected = {
    #         'price': ['This field may not be blank.']
    #     }

    #     self.assertFalse(actual.is_valid())
    #     self.assertEqual(actual.errors, expected)
