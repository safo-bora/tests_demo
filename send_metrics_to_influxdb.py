import os
import argparse

from datetime import datetime
import xml.etree.ElementTree as ET
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

"""
The script sets up an InfluxDB client using the retrieved environment variables. 
It initializes a synchronous write API for writing data points to the database.

For each test result extracted from the JUnit report, 
the code creates an InfluxDB data point. 

Each point includes tags and fields like test name, commit, author, test class, test level, 
test status, test duration, and error message.

The created data points are written to the specified InfluxDB bucket using the write API.

The send_report function is called to process the JUnit report and send the data to InfluxDB. 

URL: http://35.176.58.38:3000/d/edneb78dskzcwn/demo-project-test-metrics-influxdb-2b-grafana?orgId=1&refresh=5s&from=now-1M&to=now
Login/password: 
TestsAreWrittenByPeople/TestsAreWrittenByPeople

"""


def get_env_var(name):
    """Retrieve an environment variable and raise an exception if it is not found."""
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"{name} environment variable is not set!")
    return value


INFLUXDB_TOKEN = get_env_var("INFLUXDB_TOKEN")
BUCKET_NAME = get_env_var("BUCKET_NAME")
ORGANIZATION = get_env_var("ORGANIZATION")
DB_URL = get_env_var("INFLUX_DB_URL")


def send_report(level, reports, author, commit):
    print("Current working directory:", os.getcwd())
    tree = ET.parse(reports)
    root = tree.getroot()

    tests = []

    for testsuite in root.iter('testsuite'):
        for testcase in testsuite.iter('testcase'):
            test_name = testcase.get('name')
            test_class = testcase.get('classname')
            test_time = testcase.get('time')

            # Ensure test_time is stored as a float
            try:
                test_time = float(test_time)
            except ValueError:
                test_time = 0.0  # Default to 0.0 if conversion fails

            test_status = 'PASSED'
            error_message = None

            if testcase.find('failure') is not None:
                test_status = 'FAILED'
                error_message = testcase.find('failure').text
            elif testcase.find('error') is not None:
                test_status = 'ERROR'
                error_message = testcase.find('error').text
            elif testcase.find('skipped') is not None:
                test_status = 'SKIPPED'

            tests.append((test_name, test_class, error_message, test_time, test_status))

    for test_name, test_class, error_message, test_time, test_status in tests:
        point = Point("tests") \
            .tag("test_name", test_name) \
            .tag("commit", commit) \
            .tag("author", author) \
            .tag("test_class", test_class) \
            .tag("test_level", level) \
            .tag("test_status", test_status) \
            .field("test_duration", test_time) \
            .field("error_message", error_message if error_message else "") \
            .time(datetime.utcnow(), WritePrecision.NS)
        write_api.write(bucket=BUCKET_NAME, org=ORGANIZATION, record=point)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script to send test reports to Grafana / InfluxDB')

    parser.add_argument('--commit', required=True, help='Commit message')
    parser.add_argument('--author', required=True, help='Commit author')
    parser.add_argument('--path_to_junit_reports', required=True, help='Path to JUnit reports')
    parser.add_argument('--test_level', required=True, help='Test level (api/unit/contract/end2end etc.)')

    args = parser.parse_args()

    print("DEBUG:", args.commit, args.author, args.path_to_junit_reports, args.test_level)

    client = InfluxDBClient(url=DB_URL, token=INFLUXDB_TOKEN, org=ORGANIZATION)
    try:
        write_api = client.write_api(write_options=SYNCHRONOUS)

        print("=========================")
        print("Reports:")
        print(os.listdir("./reports"))
        print("=========================")
        send_report(level=args.test_level,
                    reports=args.path_to_junit_reports,
                    author=args.author, commit=args.commit)
    except Exception as e:
        print("------------- ERROR---------------------")
        raise Exception(f"An error occurred: {e}")
    finally:
        client.close()
