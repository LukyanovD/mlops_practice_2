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


