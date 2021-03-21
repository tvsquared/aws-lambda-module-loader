import unittest
from aws_lambda_module_loader import import_submodules, SubModuleImporterExpection

class TestAwsLambdaModuleLoader(unittest.TestCase):

    def test_loader_no_package(self):
        with self.assertRaises(SubModuleImporterExpection):
            import_submodules('tests.tvsquared.main')

    def test_loader_missing_package(self):
        with self.assertRaises(SubModuleImporterExpection):
            import_submodules('tests.some')

    def test_loader(self):
        import_submodules('tests')
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()