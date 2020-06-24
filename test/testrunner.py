import unittest

import test.UnitTesting.testcinterop as testcinterop
import test.UnitTesting.testfluids as testfluids

loader = unittest.TestLoader()
suite  = unittest.TestSuite()


suite.addTests(loader.loadTestsFromModule(testcinterop))
suite.addTests(loader.loadTestsFromModule(testfluids))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
