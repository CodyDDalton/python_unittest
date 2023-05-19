import unittest
from grader import Grader


class TestGrader(unittest.TestCase):
    def test_gradeInfo(self):
        grader = Grader()
        self.assertTrue(grader.gradeInfo())


if __name__ == '__main__':
    unittest.main()