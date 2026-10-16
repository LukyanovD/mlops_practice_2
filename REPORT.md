python --version
Python 3.12.7

python -c "import sys; print(sys.executable)"
C:\Users\Admin\Desktop\practice_2_result\pip_project\.venv\scripts\python.exe

certifi==2026.7.22
charset-normalizer==3.5.2
contourpy==1.4.0
cycler==0.12.1
fonttools==4.67.0
idna==3.20
kiwisolver==1.5.1
matplotlib==3.11.2
numpy==2.5.4
packaging==26.3
pandas==3.0.6
pillow==12.3.0
pyparsing==3.3.3
python-dateutil==2.9.0.post0
requests==2.34.2
six==1.17.0
tzdata==2026.5
urllib3==2.8.0


poetry env info --path
C:\Users\Admin\Desktop\practice_2_result\poetry_project\.venv

poetry run python --version
Python 3.12.7

poetry run python -c "import sys; print(sys.executable)"
C:\Users\Admin\Desktop\practice_2_result\poetry_project\.venv\Scripts\python.exe

poetry show --tree

matplotlib 3.11.2 Python plotting package
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
pandas 3.0.6 Powerful data structures for data analysis, time series, and statistics
├── numpy >=1.26.0
├── python-dateutil >=2.8.2
│   └── six >=1.5 
└── tzdata *
pytest 9.1.1 pytest: simple powerful testing with Python
├── colorama >=0.4
├── iniconfig >=1.0.1
├── packaging >=22
├── pluggy >=1.5,<2
└── pygments >=2.7.2
requests 2.34.2 Python HTTP for Humans.
├── certifi >=2023.5.7
├── charset-normalizer >=2,<4
├── idna >=2.5,<4
└── urllib3 >=1.26,<3

ls temperature_24h.*

Mode                 LastWriteTime         Length Name                                    
----                 -------------         ------ ----                                    
-a----        16.10.2026     17:28            637 temperature_24h.csv                     
-a----        16.10.2026     17:28          32752 temperature_24h.png                     


PS C:\Users\Admin\Desktop\practice_2_result\poetry_project> poetry show --outdated
PS C:\Users\Admin\Desktop\practice_2_result\poetry_project> poetry show --latest
certifi            2026.7.22   2026.7.22   Python package for providing Mozilla's ...
charset-normalizer 3.5.2       3.5.2       The Real First Universal Charset Detect...
colorama           0.4.6       0.4.6       Cross-platform colored terminal text.
contourpy          1.4.0       1.4.0       Python library for calculating contours...
cycler             0.12.1      0.12.1      Composable style cycles
fonttools          4.67.0      4.67.0      Tools to manipulate font files
idna               3.20        3.20        Internationalized Domain Names in Appli...
iniconfig          2.3.1       2.3.1       brain-dead simple config-ini parsing
kiwisolver         1.5.1       1.5.1       A fast implementation of the Cassowary ...
matplotlib         3.11.2      3.11.2      Python plotting package
numpy              2.5.4       2.5.4       Fundamental package for array computing...
packaging          26.3        26.3        Core utilities for Python packages
pandas             3.0.6       3.0.6       Powerful data structures for data analy...
pillow             12.3.0      12.3.0      Python Imaging Library (fork)
pluggy             1.7.0       1.7.0       plugin and hook calling mechanisms for ...
pygments           2.21.0      2.21.0      Pygments is a syntax highlighting packa...
pyparsing          3.3.3       3.3.3       pyparsing - Classes and methods to defi...
pytest             9.1.1       9.1.1       pytest: simple powerful testing with Py...
python-dateutil    2.9.0.post0 2.9.0.post0 Extensions to the standard Python datet...
requests           2.34.2      2.34.2      Python HTTP for Humans.
ruff               0.17.1      0.17.1      An extremely fast Python linter and cod...
six                1.17.0      1.17.0      Python 2 and 3 compatibility utilities
tzdata             2026.5      2026.5      Provider of IANA time zone data
urllib3            2.8.0       2.8.0       HTTP library with thread-safe connectio...


Select-String -Path pyproject.toml -Pattern "requests"

pyproject.toml:10:requests = "^2.34.2"


S C:\Users\Admin\Desktop\practice_2_result> git --no-pager diff poetry_project/pyproject.toml poetry_project/poetry.lock
diff --git a/poetry_project/poetry.lock b/poetry_project/poetry.lock
index 98b3e7e..0af5691 100644
--- a/poetry_project/poetry.lock
+++ b/poetry_project/poetry.lock
@@ -1113,4 +1113,4 @@ zstd = ["backports-zstd (>=1.0.0) ; python_version < \"3.14\""]
 [metadata]
 lock-version = "2.1"
 python-versions = ">=3.12,<3.13"
-content-hash = "99385f89a2668ffae6e7e56b4b01c2b458e8c37fd2931a26ff17745f2c229ea0"
+content-hash = "05c09f27342c375bd6442409f42dbb3f083f97931539194878b6750eb7d6a5f9"
diff --git a/poetry_project/pyproject.toml b/poetry_project/pyproject.toml
index c1cd963..86e155c 100644
--- a/poetry_project/pyproject.toml
+++ b/poetry_project/pyproject.toml
@@ -7,7 +7,7 @@ package-mode = false
 
 [tool.poetry.dependencies]
 python = ">=3.12,<3.13"
-requests = "^2.34.2"
+requests = ">=2.31,<3.0"
 matplotlib = "^3.11.2"
 pandas = "^3.0.6"
 

Get-Content requirements.txt | Select-Object -First 15

certifi==2026.7.22 ; python_version == "3.12"
charset-normalizer==3.5.2 ; python_version == "3.12"
contourpy==1.4.0 ; python_version == "3.12"
cycler==0.12.1 ; python_version == "3.12"
fonttools==4.67.0 ; python_version == "3.12"
idna==3.20 ; python_version == "3.12"
kiwisolver==1.5.1 ; python_version == "3.12"
matplotlib==3.11.2 ; python_version == "3.12"
numpy==2.5.4 ; python_version == "3.12"
packaging==26.3 ; python_version == "3.12"
pandas==3.0.6 ; python_version == "3.12"
pillow==12.3.0 ; python_version == "3.12"
pyparsing==3.3.3 ; python_version == "3.12"
python-dateutil==2.9.0.post0 ; python_version == "3.12"
requests==2.34.2 ; python_version == "3.12"


poetry install --with test,dev

Creating virtualenv poetry-project in C:\Users\Admin\Desktop\practice_2_result\poetry_project\.venv
Installing dependencies from lock file

Package operations: 24 installs, 0 updates, 0 removals

  - Installing certifi (2026.7.22): Pending...
  - Installing charset-normalizer (3.5.2): Pending...
  - Installing colorama (0.4.6): Pending...
  - Installing contourpy (1.4.0): Pending...
  - Installing charset-normalizer (3.5.2): Pending...
  - Installing colorama (0.4.6): Pending...
  - Installing contourpy (1.4.0): Pending...
  - Installing certifi (2026.7.22): Installing...
  - Installing charset-normalizer (3.5.2): Pending...
  - Installing colorama (0.4.6): Pending...
  - Installing contourpy (1.4.0): Pending...


  poetry run pytest -q
.                                                                              [100%]
1 passed in 4.17s

poetry run python plt_temp.py
Сохранено в temperature_24h.csv и temperature_24h.png


ls temperature_24h.*


    Каталог: C:\Users\Admin\Desktop\practice_2_result\poetry_project


Mode                 LastWriteTime         Length Name                               
----                 -------------         ------ ----                               
-a----        16.10.2026     18:06            637 temperature_24h.csv                
-a----        16.10.2026     18:06          32752 temperature_24h.png                


poetry run python -c "import pandas as pd; df=pd.read_csv('temperature_24h.csv'); print(df.shape, df.columns.tolist())"

(24, 2) ['time', 'temperature_c']


Сравнение подходов `venv + pip` и Poetry

| Критерий | `venv + pip` | Poetry |
|---|---|---|
| Изоляция окружения | Да, через `python -m venv` | Да, Poetry создаёт `.venv` автоматически |
| Фиксация прямых зависимостей | Вручную в `requirements.txt` или через `pip install` | В `pyproject.toml` с указанием диапазонов |
| Фиксация транзитивных зависимостей | Только если сделать `pip freeze` (плоский список без иерархии) | Автоматически в `poetry.lock` с деревом зависимостей |
| Разделение на группы (test, dev) | Нет штатного механизма (можно `requirements-dev.txt`) | Встроенные группы `[tool.poetry.group.*]` |
| Разрешение конфликтов версий | `pip` разрешает последовательно, может ломаться при обновлении | Полноценный SAT-резолвер, учитывает все ограничения |
| Воспроизводимость | Обеспечивается точными версиями (`==`) в `requirements.txt` из `pip freeze` | Обеспечивается совместно `pyproject.toml` (диапазоны) и `poetry.lock` (точные версии) |
| Обновление зависимости | Ручное: правка `requirements.txt` + `pip install -U` | `poetry update <пакет>` с учётом lock-файла |

Итог:

- В `venv + pip` воспроизводимость держится на **точных версиях**, зафиксированных
  через `pip freeze`. Если файл потерян, воспроизвести окружение «как было»
  невозможно.
- В Poetry воспроизводимость обеспечивается **двумя файлами**: `pyproject.toml`
  описывает, какие версии допустимы, а `poetry.lock` фиксирует конкретные
  разрешённые версии всей иерархии. Это позволяет как точно восстанавливать
  окружение, так и осознанно обновлять отдельные зависимости.