from leap_year.main import MyYear


def test_save_year():
    assert MyYear(1000).year == 1000
