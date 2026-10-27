# Отчёт по практической работе: окружения и зависимости Python

## 1. Среда выполнения

- **Python:** 3.12.7
- **Poetry:** lock-файл версии 2.1. Версию можно уточнить командой `poetry --version`.
- **Операционная система:** Windows.

## 2. Пути к интерпретаторам

### pip_project

C:\Users\Admin\Desktop\practice_2_result\pip_project.venv\scripts\python.exe

### Проверка

python --version
# Python 3.12.7

python -c "import sys; print(sys.executable)"
# C:\Users\Admin\Desktop\practice_2_result\pip_project.venv\scripts\python.exe


### poetry_project

C:\Users\Admin\Desktop\practice_2_result\poetry_project.venv\Scripts\python.exe

poetry run python --version
# Python 3.12.7

poetry run python -c "import sys; print(sys.executable)"
# C:\Users\Admin\Desktop\practice_2_result\poetry_project.venv\Scripts\python.exe


## 3. Прямые зависимости и их назначение

| Пакет | Группа | Назначение |
|-------|--------|------------|
| `requests` | основная | HTTP-запросы к Open-Meteo для получения почасовой температуры. |
| `pandas` | основная | Преобразование списков времени и температуры в `DataFrame`, сохранение CSV. |
| `matplotlib` | основная | Построение и сохранение графика температуры в PNG. |
| `pytest` | `test` | Автоматическая проверка функции преобразования данных. |
| `ruff` | `dev` | Линтинг и статический анализ кода. |

Модуль `numpy` не добавлен как прямая зависимость, потому что исходный скрипт `plt_temp.py` явно его не импортирует. `numpy` появляется в окружении как транзитивная зависимость `pandas` и `matplotlib`.


## 4. Примеры транзитивных зависимостей

Для каждого основного пакета можно привести хотя бы одну транзитивную зависимость:

| Основной пакет | Пример транзитивной зависимости |
|----------------|--------------------------------|
| `requests` | `urllib3` |
| `pandas` | `numpy` |
| `matplotlib` | `contourpy` |

Фрагмент дерева зависимостей из `poetry show --tree`:

```text
matplotlib 3.11.2
├── contourpy >=1.0.1
│   └── numpy >=2.0
├── cycler >=0.10
├── fonttools >=4.28.2
├── kiwisolver >=1.3.1
├── numpy >=1.25
├── packaging >=20.0
├── pillow >=9
├── pyparsing >=3
└── python-dateutil >=2.7
    └── six >=1.5

pandas 3.0.6
├── numpy >=1.26.0
├── python-dateutil >=2.8.2
│   └── six >=1.5
└── tzdata *

requests 2.34.2
├── certifi >=2023.5.7
├── charset-normalizer >=2,<4
├── idna >=2.5,<4
└── urllib3 >=1.26,<3
```

## 5. Результат восстановления окружения `pip_project`

После удаления только директории `pip_project/.venv` было создано новое пустое окружение с тем же именем. Зависимости восстановлены из `requirements.txt`.

Проверка работы проекта:

# python plt_temp.py

Сохранено в temperature_24h.csv и temperature_24h.png

Проверка CSV:

# python -c "import pandas as pd; df=pd.read_csv('temperature_24h.csv'); print(df.shape, df.columns.tolist())"
(24, 2) ['time', 'temperature_c']

## 6. Результат проверки групп Poetry

Проверены три варианта установки зависимостей.

| Выбранные группы | Доступен `pytest` | Доступен `ruff` | Можно запустить основной скрипт | Причина |
|---|---|---|---|---|
| Только основная группа | Нет | Нет | Да | Установлены `requests`, `pandas`, `matplotlib`; инструменты разработки и тестирования не входят в основную группу. |
| Только группа `test` | Да | Нет | Нет | Установлен `pytest`, но отсутствуют основные библиотеки, необходимые скрипту. |
| Полное окружение: основная + `test` + `dev` | Да | Да | Да | Установлены все группы, поэтому доступны и скрипт, и инструменты разработки. |

После эксперимента восстановлено полное окружение проекта.


# 7. Точечное обновление зависимости

Исходное ограничение для requests в pyproject.toml:

# requests = "^2.34.2"
Изменено на:

# requests = ">=2.31,<3.0"
Результат git diff:

в pyproject.toml изменилось ограничение прямой зависимости;

в poetry.lock изменился content-hash;

установленная версия requests осталась 2.34.2;

транзитивные зависимости не изменились.

Объяснение: более новой совместимой версии requests в диапазоне >=2.31,<3.0 не появилось, поэтому poetry update requests не привёл к смене версии. Обновление не выходит за диапазон, так как верхняя граница <3.0 запрещает переход на следующую мажорную версию.

# 8. Результат чистого восстановления Poetry-проекта

После удаления poetry_project/.venv и восстановления окружения по pyproject.toml и poetry.lock:

# poetry install --with test,dev
Операции с пакетами: 24 установки, 0 обновлений, 0 удалений

# poetry run pytest -q .
1 passed in 4.17s

# poetry run python plt_temp.py
Сохранено в temperature_24h.csv и temperature_24h.png

ls temperature_24h.*
# -a---- 16.10.2026 18:06 637 temperature_24h.csv
# -a---- 16.10.2026 18:06 32752 temperature_24h.png
Проверка CSV:

# poetry run python -c "import pandas as pd; df=pd.read_csv('temperature_24h.csv'); print(df.shape, df.columns.tolist())"
(24, 2) ['time', 'temperature_c']
Окружение восстанавливается без ручного добавления пакетов; тесты проходят; скрипт создаёт CSV и PNG; в CSV 24 строки данных.


## 9. Сравнение подходов `venv + pip` и Poetry

| Критерий | `venv + pip` | Poetry |
|---|---|---|
| Изоляция окружения | Да, через `python -m venv` | Да, Poetry создаёт `.venv` автоматически |
| Фиксация прямых зависимостей | Вручную в `requirements.txt` или через `pip install` | В `pyproject.toml` с указанием диапазонов |
| Фиксация транзитивных зависимостей | Только через `pip freeze` (плоский список без иерархии) | Автоматически в `poetry.lock` с деревом зависимостей |
| Разделение на группы (`test`, `dev`) | Нет штатного механизма (можно `requirements-dev.txt`) | Встроенные группы `[tool.poetry.group.*]` |
| Разрешение конфликтов версий | `pip` разрешает последовательно, может ломаться при обновлении | Полноценный SAT-резолвер, учитывает все ограничения |
| Воспроизводимость | Обеспечивается точными версиями (`==`) в `requirements.txt` из `pip freeze` | Обеспечивается совместно `pyproject.toml` (диапазоны) и `poetry.lock` (точные версии) |
| Обновление зависимостей | Ручное: правка `requirements.txt` + `pip install -U` | `poetry update <пакет>` с учётом lock-файла |



Итог:
В venv + pip воспроизводимость держится на точных версиях, зафиксированных через pip freeze. Если файл потерян, восстановить окружение «как было» невозможно.
В Poetry воспроизводимость обеспечивается двумя файлами: pyproject.toml описывает допустимые версии, а poetry.lock фиксирует конкретные разрешённые версии для всей иерархии. Это позволяет как точно восстановить окружение, так и осознанно обновлять отдельные зависимости.