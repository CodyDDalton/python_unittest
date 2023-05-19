import unittest
from grader import Grader

gr = Grader()

class Test(unittest.TestCase):

    def test_gradeInfo(self):
        name=input("Enter your name here: ")
        assignment=input("Enter your assignment name: ")
        grade=float(input("Enter the grade number for that assignment: "))
        if grade <=100 and grade >=90:
            msg="Hello %s\nYour letter grade for %s assignment is as follows: A\nAssignment details:\nYou have met most or all of the assignment's requirements." % (name, assignment)
            self.assertEqual(msg, "Hello %s\nYour letter grade for %s assignment is as follows: A\nAssignment details:\nYou have met most or all of the assignment's requirements." % (name, assignment))
            self.assertNotEqual(msg, "You did not entered a grade number between 0 and 100.")
        elif grade <=90 and grade >=80:
            msg="Hello %s\nYour letter grade for %s assignment is as follows: B\nAssignment details:\nYou have met most of the assignment's requirements." % (name, assignment)
            self.assertEqual(msg, "Hello %s\nYour letter grade for %s assignment is as follows: B\nAssignment details:\nYou have met most of the assignment's requirements." % (name, assignment))
        elif grade <=80 and grade >=70:
            msg="Hello %s\nYour letter grade for %s assignment is as follows: C\nAssignment details:\nYou have met many of the assignment's requirements." % (name, assignment)
            self.assertEqual(msg, "Hello %s\nYour letter grade for %s assignment is as follows: C\nAssignment details:\nYou have met many of the assignment's requirements." % (name, assignment))
        elif grade <=70 and grade >=60:
            msg="Hello %s\nYour letter grade for %s assignment is as follows: D\nAssignment details:\nYou have met some of the assignment's requirements." % (name, assignment)
            self.assertEqual(msg, "Hello %s\nYour letter grade for %s assignment is as follows: D\nAssignment details:\nYou have met some of the assignment's requirements." % (name, assignment))
        elif grade <=60 and grade >=0:
            msg=grade
            self.assertEqual(msg, grade)
        else:
            msg="You did not entered a grade number between 0 and 100."
            self.assertEqual(msg, "You did not entered a grade number between 0 and 100.")

class Test(unittest.TestCase):

    def test_gradeInfo(self):
        grader = Grader()
        self.assertTrue(grader.gradeInfo())


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
