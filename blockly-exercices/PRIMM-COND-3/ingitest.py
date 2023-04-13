#!/bin/python3
# pylint: disable=C0103
"""INGInious test library with feedback
This framework is inspired by python's unittest library
"""

from typing import Any

from inginious import feedback  # pylint: disable=E0401,


class TestCase:
    """Test cases wrapper. Inginious adaptation from unittest"""

    FAIL = 0
    SUCCESS = 1

    def __init__(self) -> None:
        self.feedback = []
        self.grade = 0

    def run(self):
        """Collect and run tests"""
        tests = [attr for attr in dir(self) if attr.startswith("test")]

        setUp = getattr(self, 'setUp') if hasattr(
            self, 'setUP') else lambda: ""
        tearDown = getattr(self, 'tearDown') if hasattr(
            self, 'tearDown') else lambda: ""

        if hasattr(self, 'setUpClass'):
            getattr(self, 'setUpClass')()

        for test in tests:
            setUp()
            getattr(self, test)()
            tearDown()

        if hasattr(self, 'tearDownClass'):
            getattr(self, 'tearDownClass')()

        if len(tests) > 0:
            passed = len(
                tuple(filter(lambda f: f[0] == self.SUCCESS, self.feedback)))
            self.grade = passed / len(self.feedback) * 100
        return self

    def getFeedback(self) -> str:
        """Collect test feedback as one string"""
        return "\n".join(map(lambda f: f[1], self.feedback))

    def setFeedback(self, pass_grade: int = 50) -> None:
        """Set feedback on INGInious"""
        feedback.set_grade(self.grade)
        feedback.set_global_result(
            "success" if self.grade >= pass_grade else "failure")
        feedback.set_global_feedback(self.getFeedback())

    def fail(self, msg: Any = None) -> None:
        """Force fail a test"""
        self.feedback.append((self.FAIL, msg))

    def success(self, msg: Any = None) -> None:
        """Force succed a test"""
        self.feedback.append((self.SUCCESS, msg))

    def assertEqual(
            self,
            first: Any,
            second: Any,
            msg: Any = None,
            success_msg: Any = None
    ) -> None:
        """Test == operator"""
        if first == second:
            self.feedback.append((self.SUCCESS, success_msg))
        else:
            self.feedback.append((self.FAIL, msg))

    def assertNotEqual(
            self,
            first: Any,
            second: Any,
            msg: Any = None,
            success_msg: Any = None
    ) -> None:
        """Test != operator"""
        if first != second:
            self.feedback.append((self.SUCCESS, success_msg))
        else:
            self.feedback.append((self.FAIL, msg))
