"""Точка входа: расчёт теплоты на нагрев технологической среды (вариант 3)."""

from validators import input_mass, input_t1, input_t2
from menu import select_mode, mode_name
from operations import heat_amount, heating_class


def main() -> None:
    """Главный цикл программы."""
    while True:
        c = select_mode()
        if c is None:
            print("Работа завершена.")
            break
        m = input_mass()
        t1 = input_t1()
        t2 = input_t2(t1)
        q = heat_amount(m, c, t1, t2)
        cls = heating_class(t2 - t1)
        print(f"\nСреда: {mode_name(c)} (c = {c:.0f})")
        print(f"Q = {q:.2f} Дж")
        print(f"Класс нагрева: {cls}")


if __name__ == "__main__":
    main()
