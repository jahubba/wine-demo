import unittest
import tempfile
import os
import shutil
from pyspark.sql import SparkSession

class SampleJobUnitTest(unittest.TestCase):
    def setUp(self):
        # initialze stuff here
        println("setup")

    def test_sample(self):
        output_count = 10
        self.assertGreater(output_count, 0)

    def tearDown(self):
        # uninitialize here
        println("tearDown")

if __name__ == "__main__":
    unittest.main()
