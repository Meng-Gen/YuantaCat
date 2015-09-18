# YuantaCat
Stock analysis for Taipei market.

Unittest
--------
Before running unittest don't forget to delete .pyc files first: ```find . -name "*.pyc" -exec rm -rf {} \;```
* Test single unit test: ```python -m unittest yuantacat.tests.unit.assembler.test_profitability_assembler```
* Test all unit tests: ```python -m unittest discover yuantacat/tests/unit/assembler/```
