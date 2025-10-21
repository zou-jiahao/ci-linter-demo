# tests/test_calculator.py
import pytest
from calculator import add


# ✅ 正常情况
def test_add_normal():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -1) == -2


def test_add_zero():
    assert add(0, 0) == 0


# ⚠️ 边界情况
def test_add_floats():
    result = add(0.1, 0.2)
    assert abs(result - 0.3) < 1e-9  # 处理浮点精度


def test_add_large_numbers():
    assert add(1_000_000, 2_000_000) == 3_000_000


def test_add_mixed_types():
    assert add(1, 2.5) == 3.5


# ❌ 异常情况
def test_add_with_string_raises_type_error():
    with pytest.raises(TypeError):
        add(1, "2")


def test_add_with_none_raises_type_error():
    with pytest.raises(TypeError):
        add(None, 5)


def test_add_with_list_raises_type_error():
    with pytest.raises(TypeError):
        add([1], [2])


# ⚙️ 减法测试
def test_subtract_normal():
    assert subtract(5, 3) == 2


def test_subtract_negative():
    assert subtract(-1, -1) == 0


def test_subtract_zero():
    assert subtract(0, 0) == 0


def test_subtract_floats():
    result = subtract(0.3, 0.1)
    assert abs(result - 0.2) < 1e-9


def test_subtract_large_numbers():
    assert subtract(2_000_000, 1_000_000) == 1_000_000


def test_subtract_mixed_types():
    assert subtract(2, 1.5) == 0.5


def test_subtract_with_string_raises_type_error():
    with pytest.raises(TypeError):
        subtract(1, "2")


def test_subtract_with_none_raises_type_error():
    with pytest.raises(TypeError):
        subtract(None, 5)


def test_subtract_with_list_raises_type_error():
    with pytest.raises(TypeError):
        subtract([1], [2])

