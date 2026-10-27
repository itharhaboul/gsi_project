import random
from module import Module
from unit import Unit
from semester import Semester


def build_semester1():
    # Module(code, title, coef, credit, C, TD, TP, mode, continu%, exam%)
    f111 = Module("F111", "Réseaux des couches basses", 3, 6, 1.5, 1.5, 1.5)
    f112 = Module("F112", "Algorithmique Avancée et Complexité", 2, 4, 1.5, 0, 1.5)
    f121 = Module("F121", "Système d'exploitation", 2, 4, 1.5, 1.5, 0)
    f122 = Module("F122", "Architectures Modernes des SI", 2, 4, 1.5, 0, 1.5)
    m111 = Module("M111", "Architecture et administration des BD", 2, 4, 1.5, 0, 1.5)
    m112 = Module("M112", "Méthodes et Technologies d'Implémentation", 3, 5, 1.5, 0, 1.5)
    d111 = Module("D111", "Systèmes de Communication Vocaux et Vidéos", 2, 2, 1.5, 0, 1.5)
    t111 = Module("T111", "Cloud Computing", 1, 1, 1.5, 0, 0, "Distance", 0, 100)

    return Semester("S1", "Semestre 1", [
        Unit("UEF11", "UE Fondamentale 11", [f111, f112]),
        Unit("UEF12", "UE Fondamentale 12", [f121, f122]),
        Unit("UEM11", "UE Méthodologie 11", [m111, m112]),
        Unit("UED11", "UE Découverte 11", [d111]),
        Unit("UET11", "UE Transversale 11", [t111]),
    ])


def build_semester2():
    f211 = Module("F211", "Les Middlewares pour les systèmes répartis", 3, 6, 1.5, 1.5, 1.5)
    f212 = Module("F212", "Modélisation et Architectures logicielles", 2, 4, 1.5, 0, 1.5)
    uf221 = Module("UF221", "Réseaux de la couche IP", 3, 6, 1.5, 0, 1.5)
    uf222 = Module("UF222", "Introduction au Machine Learning", 2, 4, 1.5, 0, 1.5)
    m211 = Module("M211", "Infographie", 2, 3, 1.5, 0, 1.5)
    m212 = Module("M212", "Gestion de l'incertain", 2, 3, 1.5, 1.5, 0)
    d211 = Module("D211", "Internet of Things", 2, 3, 1.5, 0, 1.5)
    t211 = Module("T211", "Cybercriminalité", 1, 1, 1.5, 0, 0, "Distance", 0, 100)

    return Semester("S2", "Semestre 2", [
        Unit("UEF21", "UE Fondamentale 21", [f211, f212]),
        Unit("UF22", "UE Fondamentale 22", [uf221, uf222]),
        Unit("UEM21", "UE Méthodologie 21", [m211, m212]),
        Unit("UED21", "UE Découverte 21", [d211]),
        Unit("UET21", "UE Transversale 21", [t211]),
    ])


def fill_random_grades(semester):
    """Demo: random grades (replace by real student grades)."""
    for unit in semester.get_units():
        for m in unit.get_modules():
            m.set_grade(
                tp=random.randint(6, 18) if m.hours_tp else None,
                td=random.randint(6, 18) if m.hours_td else None,
                exam=random.randint(5, 18),
            )


def report(semester):
    print(f"\n===== {semester.title} =====")
    for unit in semester.get_units():
        print(f"\n{unit.name} - {unit.title}")
        for m in unit.get_modules():
            print(f"   {m.name:6} avg={m.calculate_average():5.2f}  "
                  f"credits={m.calculate_credits()}/{m.credit}")
        print(f"   >> Unit average = {unit.calculate_average():.2f}, "
              f"credits = {unit.calculate_credits()}/{unit.credit}")
    print(f"\nSEMESTER average = {semester.calculate_average():.2f}")
    print(f"SEMESTER credits = {semester.calculate_credits()}/{semester.credit}")


if __name__ == "__main__":
    random.seed(1)
    s1, s2 = build_semester1(), build_semester2()
    for s in (s1, s2):
        fill_random_grades(s)
        report(s)

    total = s1.calculate_credits() + s2.calculate_credits()
    print(f"\nTotal credits Master 1: {total}/60")