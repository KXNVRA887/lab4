"""Валидация ввода: проверка типа и диапазона, циклический ввод."""

from constants import M_MIN, M_MAX, T1_MIN, T1_MAX, T2_MIN, T2_MAX
from logger import log_error


def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    """Проверить границы значения через if-elif-else.

    Args:
        value: проверяемое значение.
        low: нижняя граница.
        high: верхняя граница.

    Returns:
        (True, "") если значение допустимо, иначе (False, сообщение).
    """
    if value < low:
        return False, f"Значение {value} меньше минимума {low}."
    elif value > high:
        return False, f"Значение {value} больше максимума {high}."
    else:
        return True, ""


def input_number(prompt: str, low: float, high: float) -> float:
    """Циклический ввод числа до получения корректного значения.

    Args:
        prompt: приглашение к вводу.
        low: нижняя граница.
        high: верхняя граница.

    Returns:
        Корректное число типа float.
    """
    is_valid = False
    value = 0.0
    while not is_valid:
        raw = input(prompt)
        try:
            value = float(raw)
        except ValueError:
            message = f"Ошибка: '{raw}' — не число."
            print(message)
            log_error(message)
            continue
        ok, error = validate_range(value, low, high)
        if ok:
            is_valid = True
        else:
            print("Ошибка: " + error)
            log_error(error)
    return value


def input_mass() -> float:
    """Ввод массы m, кг."""
    return input_number(f"Введите массу m, кг ({M_MIN}..{M_MAX}): ", M_MIN, M_MAX)


def input_t1() -> float:
    """Ввод начальной температуры t1, °C."""
    return input_number(
        f"Введите начальную температуру t1, °C ({T1_MIN}..{T1_MAX}): ", T1_MIN, T1_MAX
    )


def input_t2(t1: float) -> float:
    """Ввод конечной температуры t2, °C; цикл, пока не выполнено t2 > t1.

    Args:
        t1: начальная температура.
    """
    is_valid = False
    t2 = 0.0
    while not is_valid:
        t2 = input_number(
            f"Введите конечную температуру t2, °C ({T2_MIN}..{T2_MAX}): ", T2_MIN, T2_MAX
        )
        if t2 > t1:
            is_valid = True
        else:
            message = f"Значение t2={t2} должно быть больше t1={t1}."
            print("Ошибка: " + message)
            log_error(message)
    return t2
