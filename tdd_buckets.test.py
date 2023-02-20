import unittest

import tdd_buckets as tddb
import tdd_buckets_constants as tddbc


class TypewiseTest(unittest.TestCase):

  def test_check_and_alert(self):
    self.assertEqual(
      tddb.check_ranges_on_array(
        [4,5]
      ), [["4-5", 2]]
    )


if __name__ == '__main__':
  unittest.main()