"""Меню и маршрутизация выбора среды через match-case."""

from constants import C_WATER, C_OIL, C_STEEL


def show_menu() -> None:
    """Вывести пункты меню."""
    print("\nВыберите среду:")
    print(f"1 — вода,  c = {C_WATER:.0f} Дж/(кг·°C)")
    print(f"2 — масло, c = {C_OIL:.0f} Дж/(кг·°C)")
    print(f"3 — сталь, c = {C_STEEL:.0f} Дж/(кг·°C)")
    print("0 — выход")


def select_mode() -> float | None:
    """Циклический выбор среды; вернуть c или None при выходе."""
    while True:
        show_menu()
        choice = input("Ваш выбор: ").strip()
        match choice:
            case "1":
                return C_WATER
            case "2":
                return C_OIL
            case "3":
                return C_STEEL
            case "0":
                return None
            case _:
                print("Ошибка: неверный пункт меню.")


def mode_name(c: float) -> str:
    """Вернуть название среды по теплоёмкости c."""
    match c:
        case 4200.0:
            return "вода"
        case 2000.0:
            return "масло"
        case 500.0:
            return "сталь"
        case _:
            return "неизвестная среда"
