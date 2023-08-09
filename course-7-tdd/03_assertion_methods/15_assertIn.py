import unittest


class TestClass(unittest.TestCase):

    def test_case_1(self):
        self.assertIn("@", "sample@email.com")

    def test_case_2(self):
        tech_stacks = ["python", "django", "javascript"]
        self.assertIn("python", tech_stacks)

    def test_case_3(self):
        tech_stacks = ["python", "django", "javascript"]
        self.assertIn("c++", tech_stacks)

    def test_case_4(self):
        tech_stacks = {"python": "mid", "django": "senior", "javascript": "junior"}
        self.assertIn("mid", tech_stacks)

    def test_case_5(self):
        tech_stacks = {"python": "mid", "django": "senior", "javascript": "junior"}
        self.assertNotIn("mid", tech_stacks)


if __name__ == "__main__":
    unittest.main(verbosity=2)
