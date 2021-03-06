from unittest import TestCase

from parameterized import parameterized

from solutions import summultiples


class TestSumMultiples(TestCase):
    @parameterized.expand([
        (0, 0),
        (8, 5),
        (33, 10)
    ])
    def test_should_return_sum_of_all_number_divisible_by_three_and_five(self, expected, number):
        self.assertEqual(expected, summultiples.sum_multiples(number))
