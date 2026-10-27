from academicElemnt import AcademicElement


class Semester(AcademicElement):
    """A semester contains several teaching units."""

    def __init__(self, name, title, units=None):
        super().__init__(name, title)
        self._units = []
        for u in (units or []):
            self.add_unit(u)

    def add_unit(self, unit):
        self._units.append(unit)
        self.coef += unit.coef
        self.credit += unit.credit
        self.hours_lecture += unit.hours_lecture
        self.hours_td += unit.hours_td
        self.hours_tp += unit.hours_tp

    def get_units(self):
        return list(self._units)

    def calculate_average(self):
        """Weighted average of the units (weight = unit coef)."""
        if not self._units:
            return 0
        total = sum(u.calculate_average() * u.coef for u in self._units)
        return total / sum(u.coef for u in self._units)

    def calculate_credits(self):
        """Semester >= 10 => all 30 credits (compensation between units),
        otherwise sum of credits acquired by each unit."""
        if not self._units:
            return 0
        if self.calculate_average() >= 10:
            return sum(u.credit for u in self._units)
        return sum(u.calculate_credits() for u in self._units)