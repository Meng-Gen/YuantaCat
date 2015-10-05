# YuantaCat
Stock analysis for Taipei market.

Unittest
--------
Before running unittest don't forget to delete .pyc files first: ```find . -name "*.pyc" -exec rm -rf {} \;```
* Test single unit test: ```python -m unittest yuantacat.tests.unit.assembler.test_profitability_assembler```
* Test all unit tests: ```python -m unittest discover yuantacat/tests/unit/assembler/```

Setup Environment on Mac
------------------------
Step 1. Install Python 2.7.x

Step 2. Install lxml package
```
1. xcode-select --install
2. sudo STATIC_DEPS=true pip install lxml
```

Step 3. Install psycopg2 package
```
1. Search pg_config: find / -name pg_config 2>/dev/null (/Library/PostgreSQL/9.4/bin).  
2. Add one line in ~/.profile: export PATH=${PATH}:/Library/PostgreSQL/9.4/bin
3. Add one line in ~/.profile: export DYLD_LIBRARY_PATH=/Library/PostgreSQL/9.4/lib
4. pip install psycopg2
```

Step 4. Install PostgreSQL 9.4 (or newer)

Step 5. Install Apache

Step 6. Install curl 

Run 
---
Step 1. Git clone: ```git clone https://github.com/Meng-Gen/YuantaCat.git```

Step 2. Run script: ```python main.py```

Step 3. Synchronize site: ```cp -rf report/ ~/Site/yuantacat/```
