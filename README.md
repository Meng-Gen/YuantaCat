# YuantaCat
Stock analysis for Taipei market.

Unittest
--------
Before running unittest don't forget to delete .pyc files first: ```find . -name "*.pyc" -exec rm -rf {} \;```
* Test single unit test: ```python -m unittest yuantacat.tests.unit.spider.test_operating_revenue_spider```
* Test all unit tests: ```python -m unittest discover yuantacat/tests/unit/assembler/```
