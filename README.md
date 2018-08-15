# Selenium_with_python

This is an automation framework used to test two main functionality on a website, ability to add a new user and the ability to search for that user. This framework is also coupled with an api testing functionality that allows a user to make request and perform assertion on the results.

## Setting up

Firstly you need to ensure that python is installed, with pytest
Then clone this repo, and then run the following commands

### Navigate to the test_scripts and run this commnand.

```shell
pytest -v -s test_case_01_add_and_search_user.py
```


### API Testing

Navigate to the api_testing folder and run this commnand.

```shell
pytest -v  test_api_with_dogbreed.py 
```
