class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort

    def test_student_has_name(self, name):
        return self.name

    def test_student_has_cohort(self, cohort):
        return self.cohort

    def test_student_can_update_name(self, name):
        self.name = name

    def test_student_can_update_chort(self, cohort):
        self.cohort = cohort

    def talk(self):
        return ("I can talk!")

    def say_favourite_language(self, fave):
        return "I love " + fave
