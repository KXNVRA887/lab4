"""Расчёты: теплота на нагрев и классификация нагрева."""

from constants import DT_SMALL_LIMIT, DT_LARGE_LIMIT


def heat_amount(m: float, c: float, t1: float, t2: float) -> float:
    """Рассчитать теплоту Q = m · c · (t2 - t1), Дж.

    Args:
        m: масса, кг.
        c: удельная теплоёмкость, Дж/(кг·°C).
        t1: начальная температура, °C.
        t2: конечная температура, °C.
    """
    return m * c * (t2 - t1)


def heating_class(dt: float) -> str:
    """Классифицировать нагрев по Δt через if-elif-else.

    Args:
        dt: разность температур t2 - t1, °C.
    """
    if dt < DT_SMALL_LIMIT:
        return "малый нагрев"
    elif dt <= DT_LARGE_LIMIT:
        return "нормальный нагрев"
    else:
        return "интенсивный нагрев"
