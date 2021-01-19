import unittest
import tempfile
import os
import shutil
from pyspark.sql import SparkSession

class SampleJobUnitTest(unittest.TestCase):
    def setUp(self):
        # initialze stuff here

    def test_sample(self):
        output_count = 10
        self.assertGreater(output_count, 0)

    def tearDown(self):
        # uninitialize here

if __name__ == "__main__":
    unittest.main()
