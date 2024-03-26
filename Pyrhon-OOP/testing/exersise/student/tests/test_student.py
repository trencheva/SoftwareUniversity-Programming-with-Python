from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student('Test')
        self.student_with_courses = Student('Test2', {'math': ['x + y = z']})

    def test_correct_init(self):
        self.assertEqual('Test', self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({'math': ['x + y = z']}, self.student_with_courses.courses)

    def test_enroll_with_existing_course_append_the_notes_returns_correct_string(self):
        result = self.student_with_courses.enroll('math', ['a + b = c', '2 + 4 = 6'])
        self.assertEqual({'math': ['x + y = z', 'a + b = c', '2 + 4 = 6']}, self.student_with_courses.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_without_third_param_expect_appending_notes_returns_correct_string(self):
        result = self.student.enroll('math', ['123', '456'], '')
        self.assertEqual({'math': ['123', '456']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_with_third_param_Y_expect_appending_notes_returns_correct_string(self):
        result = self.student.enroll('math', ['123', '456'], 'Y')
        self.assertEqual({'math': ['123', '456']}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_with_third_param_NO_expect_add_the_course_without_notes_returns_correct_string(self):
        result = self.student.enroll('math', ['123', '456'], 'no')
        self.assertEqual({'math': []}, self.student.courses)
        self.assertEqual('Course has been added.', result)

    def test_add_notes_to_existing_course_expect_success_returns_correct_string(self):
        result = self.student_with_courses.add_notes('math', '123')
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({'math': ['x + y = z', '123']}, self.student_with_courses.courses)

    def test_add_notes_to_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('math', '123')
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_existing_course(self):
        result = self.student_with_courses.leave_course('math')
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student_with_courses.courses)

    def test_leave_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('math')
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()