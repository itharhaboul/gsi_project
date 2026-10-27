from academicElemnt import AcademicElement


class Unit(AcademicElement):
    """Represents a teaching unit containing multiple modules."""

    def __init__(self, name, title, modules=None):
        super().__init__(name, title)
        self._modules = []          # avoid the mutable default argument bug (modules=[])
        for m in (modules or []):
            self.add_module(m)

    def add_module(self, module):
        self._modules.append(module)
        # unit coef / credits / hours = sum of its modules
        self.coef += module.coef
        self.credit += module.credit
        self.hours_lecture += module.hours_lecture
        self.hours_td += module.hours_td
        self.hours_tp += module.hours_tp

    def get_modules(self):
        return list(self._modules)

    def calculate_average(self):
        """Aggregation: weighted average of module averages."""
        if not self._modules:
            return 0
        total = sum(m.calculate_average() * m.coef for m in self._modules)
        coef_sum = sum(m.coef for m in self._modules)
        return total / coef_sum

    def calculate_credits(self):
        """If unit average >= 10, all credits are acquired (compensation),
        otherwise only the modules that passed give credits."""
        if not self._modules:
            return 0
        if self.calculate_average() >= 10:
            return sum(m.credit for m in self._modules)
        return sum(m.calculate_credits() for m in self._modules)