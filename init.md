# GildedRose Project Initialization

## 1. Create a Python Virtual Environment
python -m venv venv

## 2. Allow PowerShell scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

## 3. Activate the Virtual Environment
.\venv\Scripts\Activate.ps1

## 4. Install Dependencies
pip install --upgrade pip
pip install -r python\requirements.txt

## 5. Set Python Path
$env:PYTHONPATH="python"

## 6. Run TextTest Fixture to Create Golden Master
python texttest_fixture.py > ../golden_master.txt

- This creates `golden_master.txt` as the reference output before refactoring.  
- Now refactoring starts






python python\tests\test_gilded_rose.py
"“The GildedRoseRefactoring Kata contains failing tests as a starting point. Your task is to make the code pass while refactoring.”"


...

deactivate