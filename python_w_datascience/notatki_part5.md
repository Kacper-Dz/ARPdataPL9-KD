# Python w Data Science - part 4

## markdown reminders
**Bold text**

*itali text*

> blockquote

---
`code`

# folder venv

- wirtualne środowisko, które może być osobne dla każdego projektu
- venv nie wrzuca się na gita
- pip - program do zarzadzania modułami w pythonie:
- strona pypi.org
- komenda `pip install 'nazwamodulu'==wersja`
- najczesciej tworzymy requirements z lista wymaganych modułów: 
```
numpy==1.x.x
matplotslib=3.x.x
```
- instalacja opcji za pomoca requirements: 'pip install -r .\requirements.txt' 
- Jako nazwę należy podać nazwę pliku razem z scieżką.
- Odinstalowanie modułów `pip uninstall 'nazwa modułu'`
- Moduły pod datascience:
  - pandas
  - numpy
  - seaborn
  - matplotlib

# Projekt

---
- Aplikacja do zarządzania fakturami
- moduł `datetime` - moduł do zarzadzania czasem: https://www.w3schools.com/python/python_datetime.asp
- optymalizacja - wątkowanie, 
