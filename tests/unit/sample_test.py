import unittest
import tempfile
import os
import shutil
from pyspark.sql import SparkSession

class SampleJobUnitTest(unittest.TestCase):
    def setUp(self):
        output_count = 10

    def test_sample(self):
        self.assertGreater(output_count, 0)

    def tearDown(self):
        output_count = 0

if __name__ == "__main__":
    unittest.main()
