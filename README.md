# AWS Profile Switcher Readme

## Overview

The script is a handy tool to help AWS users switch between different AWS CLI profiles quickly. This can be particularly useful if you manage multiple AWS accounts or if you have different roles within an AWS account. After you've switched profiles, the script allows you to set the AWS profile in your environment variables or retrieve user details for that profile.

## Requirements

To run this script, ensure you have the following:

- Python environment
- `boto3`: AWS SDK for Python
- `pyperclip`: Provides a cross-platform Python interface to the clipboard
- `click`: Provides a way to create command-line interfaces
- `psutil`: Allows you to retrieve information on running processes and system utilization
- AWS CLI set up with named profiles (the script reads from `~/.aws/credentials` and `~/.aws/config`).

## Usage

To execute the script, simply run:

```
python <script_name>.py [--profile] [--region REGION_NAME] [PROFILE_NAME]
```

### Options and Arguments:

- `--profile`: Flag to prompt for AWS CLI profile or use the one provided. If this flag is provided, the user will either select a profile from a list or use the profile name provided in `profilename` argument.
- `--region REGION_NAME`: Specify the AWS region. By default, it's set to `cn-north-1`. If the profile contains region information in `~/.aws/config`, it will override this default.
- `profilename`: (Optional) The name of the AWS CLI profile you want to switch to. If not provided and `--profile` flag is set, the script will prompt you to choose from a list of profiles.

### Features:

1. **List AWS CLI Profiles**: Displays a list of AWS CLI profiles stored in `~/.aws/credentials`.
2. **Switch Profile Interactively**: Allows the user to select an AWS profile from a list.
3. **Set Environment Variable**: Once a profile is chosen, the script will generate a command to set the `AWS_PROFILE` environment variable in the user's shell. This command is copied to the clipboard for easy pasting.
4. **Display User Details**: Once a profile is chosen, the script displays the User ID, ARN, Access Key, and Secret Key for the selected profile.

### Notes:

- The script determines the user's operating system to generate the appropriate command to set environment variables. It supports Windows (both cmd and PowerShell), Linux, and macOS.
- If there's an issue connecting to the specified region, the script defaults to connecting to the "us-east-1" region.

## Recommendations:

- Always be cautious about where and how you display AWS Access and Secret keys. Avoid logging these details or exposing them to unintended audiences.
- It's advisable to have a backup of your AWS CLI configuration files (`~/.aws/credentials` and `~/.aws/config`) before using any scripts or tools that modify or interact with them.

## Feedback and Contributions:

Please raise any issues or suggestions on the repository or contact the maintainers directly. Contributions to enhance the script or fix any bugs are always welcome!