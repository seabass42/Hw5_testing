# Homework
- Name: Sebastian Ezpeleta-Stewart

## Question 1 Define the following unit, integration, regression tests and when you would use them?
- Unit test: Segments of code designed to test other code segments, you would use typically when you just want to test a function or method
- Integration test: Check the interactions between various parts of the system, valuable when you need to check the synergy between functions / systems
- Regression test: Check new code changes to ensure they havent affected the functionality of existing code, useful when pushing big changes

## Question 2 Briefly explain pytest discovery (file/function naming) and what a fixture is.
Pytest finds test files based on naming conventions automatically such as test_*.py or *_test.py, no manual registration is required.
A fixture is a pre-setup function that provides data to tests to keep tests clean and repeatable. 