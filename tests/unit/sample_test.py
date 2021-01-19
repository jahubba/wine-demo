import unittest
import tempfile
import os
import shutil
from pyspark.sql import SparkSession

class SampleJobUnitTest(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory().name
        self.test_config = {
            "output_format": "parquet",
            "output_path": os.path.join(self.test_dir, "output")
        }


    def test_sample(self):

        output_count = 10

        self.assertGreater(output_count, 0)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

if __name__ == "__main__":
    unittest.main()
