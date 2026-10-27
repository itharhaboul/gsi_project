from academicElemnt import AcademicElement


class Module(AcademicElement):
    """Represents a teaching module with pedagogical and evaluation attributes."""

    def __init__(
        self,
        name: str = "",            # module code
        title: str = "",
        coef: int = 1,
        credit: int = 1,
        hours_lecture: float = 1.5,
        hours_td: float = 0,
        hours_tp: float = 0,
        teaching_mode: str = "In-person",   # "Distance" or "In-person"
        continous_percent: int = 40,
        exam_percent: int = 60,
    ):
        super().__init__(name, title)
        self.coef = coef
        self.credit = credit

        self.hours_lecture = hours_lecture
        self.hours_td = hours_td
        self.hours_tp = hours_tp

        self.teaching_mode = teaching_mode
        self.evaluation_continous_percent = continous_percent
        self.evaluation_exam_percent = exam_percent

        # Total hours x semester
        self.total_hours = self._WEEKS * (self.hours_lecture + self.hours_td + self.hours_tp)

        # Private grades (encapsulation)
        self._grades = {"tp": 0, "td": 0, "exam": 0}

    # Encapsulation: controlled access to grades
    def set_grade(self, tp=None, td=None, exam=None):
        for key, value in (("tp", tp), ("td", td), ("exam", exam)):
            if value is not None:
                if not 0 <= value <= 20:
                    raise ValueError(f"Invalid grade for {key}: {value} (must be 0..20)")
                self._grades[key] = value

    def get_grades(self):
        """Read-only copy of the grades."""
        return dict(self._grades)

    def summary(self):
        """Return a short textual description of the module."""
        return (
            f"Module: {self.title} ({self.name})\n"
            f"Coefficient: {self.coef}, Credits: {self.credit}\n"
            f"Hours: total {self.total_hours}, {self.hours_lecture} Lecture, "
            f"{self.hours_td} TD, {self.hours_tp} TP\n"
            f"Teaching mode: {self.teaching_mode}, "
            f"Evaluation mode: Continous: {self.evaluation_continous_percent}% "
            f"Exam: {self.evaluation_exam_percent}%"
        )

    # Q9: weights are an internal detail -> private helper
    def _weights(self):
        """Return (percent_tp, percent_td, percent_exam)."""
        percent_exam = self.evaluation_exam_percent
        percent_tp = percent_td = 0
        cont = self.evaluation_continous_percent
        if self.hours_tp and self.hours_td:
            percent_tp = percent_td = cont / 2
        elif self.hours_td:
            percent_td = cont
        elif self.hours_tp:
            percent_tp = cont
        return percent_tp, percent_td, percent_exam

    def calculate_average(self):
        """Polymorphism: different modules could override this behavior."""
        p_tp, p_td, p_exam = self._weights()
        g = self._grades
        return (g["tp"] * p_tp + g["td"] * p_td + g["exam"] * p_exam) / 100

    def calculate_credits(self):
        """Credits are acquired only if average >= 10."""
        return self.credit if self.calculate_average() >= 10 else 0


# Example usage
if __name__ == "__main__":
    mti = Module("MTI", "Methods and Technologies of Implementation",
                 coef=3, credit=5, hours_lecture=1.5, hours_tp=1.5)
    print(mti.summary())
    mti.set_grade(tp=10, exam=12)
    print("Module average:", mti.name, mti.calculate_average())
    print("Credits:", mti.calculate_credits())