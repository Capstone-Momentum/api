
import unittest

def run(filename_pattern):
    loader = unittest.TestLoader()
    tests = loader.discover('.', pattern=filename_pattern)
    testRunner = unittest.TextTestRunner()
    testRunner.run(tests)

if __name__ == '__main__':
    run('test_logic*.py')
    run('test_api*.py')
