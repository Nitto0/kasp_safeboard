import sqlite3
import sys

from import_data import create_tables
from checker import find_safe_version, find_vulnerabilities


def main():
    args = sys.argv[1:]

    if not args or args[0] in ("--help", "-h"):
        print("Создать базу: python main.py init")
        print('Найти версию: python main.py safe-version "Название продукта"')
        print('Проверить версию: python main.py vulnerabilities "Название продукта" "Версия"')
        return

    try:
        if args[0] == "init" and len(args) == 1:
            create_tables()
            print("База создана, данные из фидов загружены")
        elif args[0] == "safe-version" and len(args) == 2:
            version = find_safe_version(args[1])
            if version is None:
                print("Среди версий в базе нет версии без известных уязвимостей")
            else:
                print(f"Версия без известных уязвимостей по данным фидов: {version}")
        elif args[0] == "vulnerabilities" and len(args) == 3:
            vuln = find_vulnerabilities(args[1], args[2])

            if not vuln:
                print("По данным фидов уязвимости для этой версии не найдены")

            for v in vuln:
                print(f"Статья: {v[0]}")
                print(f"Описание: {v[1]}")
                print(f"Дата публикации: {v[2]}")
                print(f"Первая уязвимая версия: {v[3]}")
                print(f"Первая исправленная версия: {v[4]}")
                print()
        else:
            print("Проверь команду и количество аргументов")
            print("Примеры запуска: python main.py --help")
            sys.exit(1)
    except (sqlite3.Error, OSError, ValueError, KeyError) as error:
        print(f"Ошибка: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
