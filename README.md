# Test Project
[![Run Unit Testing](https://github.com/safo-bora/tests_demo/actions/workflows/ci-configuration.yaml/badge.svg?branch=main)](https://github.com/safo-bora/tests_demo/actions/workflows/ci-configuration.yaml)
![Badge](https://gist.githubusercontent.com/safo-bora/fba1dd06d94a6c3166f557a425fc1c5c/raw/tests-badge.svg)
![Badge](https://gist.githubusercontent.com/safo-bora/fba1dd06d94a6c3166f557a425fc1c5c/raw/coverage-badge.svg)
![Badge](https://gist.githubusercontent.com/safo-bora/fba1dd06d94a6c3166f557a425fc1c5c/raw/api-tests-badge.svg)

## About

This is a test demo project for experiments with CI integration, test reports, and metrics from testing.

QA Community - https://t.me/AutomationUA (Tests are written by people)

## CI/CD Integrations Example (We took 2 CI systems just to compare)

### Jenkins:
   - URL: http://13.43.86.245:8080/
   - Login/Password: TestAreWrittenByPeople
<img src="https://github.com/safo-bora/tests_demo/raw/main/screens/photo_2024-04-09_10-23-24.jpg" width="600">


### GitHub Action:
   - URL: https://github.com/safo-bora/tests_demo/actions
<img src="https://github.com/safo-bora/tests_demo/raw/main/screens/photo_2024-04-10_10-31-17.jpg" width="600">



_____________

## Unit Testing
#### Unit Testing Best Practices:

1️⃣ **Coverage:**
   - The main metric for unit tests. (How many percent of the code is covered by tests.)
   - It should always be calculated and visible.
   - In my case, coverage is 96.49%.
   - Please add a badge to the repository if possible. It's very important to see coverage WITHOUT diving into build logs 🙏

2️⃣ **Mocks:**
   - Mocks are often used in unit tests. To check the interaction with an external service without actually calling that service.
   - I added an example. ([Example Mocked Service Test](https://github.com/safo-bora/tests_demo/blob/main/unit_tests/tests_mocked_service.py))

3️⃣ **Very important:**
   - Break the code and check that the test fails. Because if you've covered the code with a test, broken the code, and the test is green, then you're doing something wrong.

## API Testing (Example with Trello API)
#### API Testing Best Practices

- Always consider NOT updating ALL tests with the slightest changes in the code.
- Avoid making requests directly in the tests to prevent duplicate code (noise).
- Instead of returning just a JSON response in the test, parse it into an object.

Example: 🙏

**Here we created a separate class responsible for sending requests. And all the logic of the Trellо API
<img src="https://github.com/safo-bora/tests_demo/raw/main/screens/photo_2024-04-30_19-39-14.jpg" width="700">
<img src="https://github.com/safo-bora/tests_demo/raw/main/screens/photo_2024-04-30_19-39-15.jpg" width="700">

_______

# Grafana For Metrics from Testing (In Progress)

- URL: http://35.176.58.38:3000/d/edneb78dskzcwn/demo-project-test-metrics-influxdb-2b-grafana?orgId=1&refresh=5s&from=now-2M&to=now
- Login/password TestsAreWrittenByPeople/TestsAreWrittenByPeople

Of course, when a project is small and the team is small, metrics may not be needed. But when the team is large and there are many tests, we need to understand how long each test takes, which tests are flaky, and which errors occur in which tests.

I really love DataDog, and we had it in our company, so it was easy to set up there. 
https://safo-bora-katerina.blogspot.com/2024/02/datadoggrafana-and-metrics.html

Now I took Grafana as an example to experiment with it.

#### What were we interested in?

- We were interested in which tests were the longest.
- How often do we run tests per day (since we knew how much an hour of CI costs and it was important for us to understand the time).
- How long do we wait for the build (and all tests).
- The number of tests at each level (unit, API, end-to-end, etc.)
- PASSED/FAILED/SKIPPED.
- Whether there are flaky tests? Which ones specifically?
- Whether we rerun tests, and how many times?
