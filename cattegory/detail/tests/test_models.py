from django.test import TestCase

from detail.models import Cattegory


class CattegoryModelTest(TestCase):
    def test_save_cattegory(self):
        cattegory = Cattegory()
        cattegory.species = 'scotish'
        cattegory.food = 'tuna'
        cattegory.buy_place = 'facebook'
        cattegory.price = 9000

        cattegory.save()

        cattegory = Cattegory.objects.last()

        self.assertEqual(cattegory.species, 'scotish')
        self.assertEqual(cattegory.price, 9000)
        self.assertEqual(cattegory.food, 'tuna')
        self.assertEqual(cattegory.buy_place, 'facebook')
