import pytest
from module import Module


def test_module_creation():
    m = Module("MTI", "Methods and Technologies", coef=3, credit=5)

    assert m.name == "MTI"
    assert m.title == "Methods and Technologies"
    assert m.coef == 3
    assert m.credit == 5


def test_total_hours():
    m = Module(
        "MTI",
        "Methods and Technologies",
        hours_lecture=1.5,
        hours_td=1,
        hours_tp=1.5
    )

    assert m.total_hours == m._WEEKS * 4


def test_set_grade():
    m = Module("MTI", "Methods and Technologies")

    m.set_grade(tp=12, td=14, exam=16)

    assert m.get_grades() == {
        "tp": 12,
        "td": 14,
        "exam": 16
    }


def test_invalid_grade():
    m = Module("MTI", "Methods and Technologies")

    with pytest.raises(ValueError):
        m.set_grade(exam=21)


def test_calculate_average():
    m = Module(
        "MTI",
        "Methods and Technologies",
        hours_lecture=1.5,
        hours_tp=1.5,
        continous_percent=40,
        exam_percent=60
    )

    m.set_grade(tp=10, exam=12)

    assert m.calculate_average() == pytest.approx(11.2)



def test_calculate_credits_pass():
    m = Module(
        "MTI",
        "Methods and Technologies",
        credit=5,
        exam_percent=100,
        continous_percent=0
    )
    m.set_grade(exam=12)
    assert m.calculate_credits() == 5


def test_calculate_credits_fail():
    m = Module("MTI", "Methods and Technologies", credit=5)

    m.set_grade(exam=8)

    assert m.calculate_credits() == 0


def test_get_grades_returns_copy():
    m = Module("MTI", "Methods and Technologies")

    grades = m.get_grades()
    grades["exam"] = 20

    assert m.get_grades()["exam"] == 0

