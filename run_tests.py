
import unittest

def run():
    loader = unittest.TestLoader()
    tests = loader.discover('.')
    testRunner = unittest.TextTestRunner()
    testRunner.run(tests)

if __name__ == '__main__':
    run()