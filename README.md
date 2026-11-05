# SafeBoard

Консольная программа на Python и SQLite. Находит самую новую версию продукта
без известных уязвимостей и показывает уязвимости конкретной версии по данным фидов.

Для запуска нужен Python. Команды выполняются из папки проекта.

Создать базу и загрузить фиды. При повторном запуске данные загружаются заново:

```bash
python main.py init
```

Найти версию без известных уязвимостей:

```bash
python main.py safe-version "VLC media player (MSI installer)"
```

Проверить указанную версию:

```bash
python main.py vulnerabilities "PostgreSQL" "15.3"
```

Показать команды:

```bash
python main.py --help
```