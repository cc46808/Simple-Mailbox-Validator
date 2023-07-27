
# Email Validation Script

This script uses the MailboxValidator API to validate email addresses from a CSV file. The validation results are written to a new CSV file. The script also displays a progress bar during the validation process, and prints a summary of how many emails were successfully validated and how many failed.

## Prerequisites

- Python 3.6 or higher
- Python libraries: `http.client`, `urllib.parse`, `csv`, `os`, `configparser`, `json`, `tqdm`

You also need a MailboxValidator API key. You can get it by creating an account at [https://www.mailboxvalidator.com/api-plan](https://www.mailboxvalidator.com/api-plan).

## Installation

1. Clone the repository or download the ZIP file and extract it.

2. Open your terminal and navigate to the directory containing the script.

3. Run the following command to install the required libraries:

    ```shell
    pip install -r requirements.txt
    ```

## Usage

To run the script, use the following command in your terminal:

```shell
python validator.py
```

When you run the script for the first time, it will prompt you for your MailboxValidator API key. The key will be saved in a configuration file (`config.ini`) in the same directory as the script, and will be used for subsequent runs. If you need to change the API key, you can edit the configuration file.

The script will then prompt you to enter the path to your CSV file. The CSV file should contain the email addresses to be validated in the
****FIRST COLUMN ONLY****, with one email address per line.

The script will validate each email in the CSV file, displaying a progress bar in the terminal. The validation results will be written to a new CSV file in the same directory as the original file. The new file will have the same name as the original file, but with `_results` appended before the file extension. Each row in the results file will contain the validation result for one email.

After validating all the emails, the script will print a summary of how many emails were successfully validated and how many failed.

## Output

The results CSV file will contain the following columns:

- `email_address`
- `domain`
- `is_free`
- `is_syntax`
- `is_domain`
- `is_smtp`
- `is_verified`
- `is_server_down`
- `is_greylisted`
- `is_disposable`
- `is_suppressed`
- `is_role`
- `is_high_risk`
- `is_catchall`
- `mailboxvalidator_score`
- `time_taken`
- `status`
- `credits_available`
- `error_code`
- `error_message`

If a field is not present in the validation result for an email, the corresponding cell in the results file will contain `'UNKNOWN'`.
