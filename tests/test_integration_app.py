import pytest

from quick_calc.app import evaluate_sequence


def test_full_addition_flow():
    # 5 + 3 = 8
    assert evaluate_sequence(["5", "+", "3", "="]) == "8"


def test_clear_resets_after_calculation():
    # 5 + 3 = 8, then C -> 0
    assert evaluate_sequence(["5", "+", "3", "=", "C"]) == "0"


def test_division_by_zero_is_handled_gracefully():
    # Entegrasyon seviyesinde hata fırlatıyor mu kontrol edelim.
    # (core.div ZeroDivisionError fırlatıyor, bu da akışta görünür)
    with pytest.raises(ZeroDivisionError):
        evaluate_sequence(["8", "/", "0", "="])