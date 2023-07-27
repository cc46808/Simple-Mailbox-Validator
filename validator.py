import http.client
import urllib.parse
import csv
import os
import configparser
import json
from tqdm import tqdm

# Configuration file path
config_file_path = 'config.ini'

# Create a ConfigParser object
config = configparser.ConfigParser()

def get_license_key():
    # If the config file exists and contains the license key, read it
    if os.path.exists(config_file_path):
        config.read(config_file_path)
        if 'MailboxValidator' in config and 'license_key' in config['MailboxValidator']:
            return config['MailboxValidator']['license_key']

    # Otherwise, prompt the user for the license key
    license_key = input('Create an account at https://www.mailboxvalidator.com/api-plan\n Enter your MailboxValidator API key: ')

    # Save the license key in the config file
    config['MailboxValidator'] = {'license_key': license_key}
    with open(config_file_path, 'w') as configfile:
        config.write(configfile)

    return license_key

# Get the license key
license_key = get_license_key()

def validate_email(email):
    params = {
        'key': license_key,
        'format': 'json',
        'email': email,
    }

    conn = http.client.HTTPSConnection("api.mailboxvalidator.com")
    conn.request("GET", "/v1/validation/single?" + urllib.parse.urlencode(params))
    res = conn.getresponse()
    result = res.read().decode()
    return json.loads(result)

# Prompt the user for the CSV file path
csv_file_path = input("Please enter the path to your CSV file: ")

# Create the results file path
base_name = os.path.basename(csv_file_path)
name, ext = os.path.splitext(base_name)
results_file_path = os.path.join(os.path.dirname(csv_file_path), f"{name}_results{ext}")

succeeded = 0
failed = 0

headers = [
    "email_address", "domain", "is_free", "is_syntax", "is_domain", "is_smtp", 
    "is_verified", "is_server_down", "is_greylisted", "is_disposable", "is_suppressed",
    "is_role", "is_high_risk", "is_catchall", "mailboxvalidator_score", "time_taken", 
    "status", "credits_available", "error_code", "error_message"
]

with open(csv_file_path, newline='') as csvfile, open(results_file_path, 'w', newline='') as resultsfile:
    email_reader = csv.reader(csvfile)
    results_writer = csv.writer(resultsfile)

    # Write the headers to the results file
    results_writer.writerow(headers)

    email_list = list(email_reader)  # convert reader object to list to support progress bar
    for row in tqdm(email_list, desc="Validating emails", unit="email"):
        email = row[0]  # assuming email is in the first column
        result = validate_email(email)

        # update the count for succeeded and failed emails based on your success condition
        if result['status'] == 'True':  # replace this with your actual success condition
            succeeded += 1
        else:
            failed += 1

        # Write the email and its result to the results file
        results_writer.writerow([result.get(header, 'UNKNOWN') for header in headers])

print(f"\nSummary:\nSucceeded: {succeeded}\nFailed: {failed}")