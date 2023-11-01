# AWS Profile Switcher Readme

## Overview

The script is a handy tool to help AWS users switch between different AWS CLI profiles quickly. This can be particularly useful if you manage multiple AWS accounts or if you have different roles within an AWS account. After you've switched profiles, the script allows you to set the AWS profile in your environment variables or retrieve user details for that profile.

### Features:

1. **List AWS CLI Profiles**: Displays a list of AWS CLI profiles stored in `~/.aws/credentials`.
2. **Switch Profile Interactively**: Allows the user to select an AWS profile from a list.
3. **Set Environment Variable**: Once a profile is chosen, the script will generate a command to set the `AWS_PROFILE` environment variable in the user's shell. This command is copied to the clipboard for easy pasting.
4. **Display User Details**: Once a profile is chosen, the script displays the User ID, ARN, Access Key, and Secret Key for the selected profile.

#### Instructions

1. Running without parameters will directly output the default configured identity information:
```bash
awsx
```

2. Using the `--profile` flag, the tool will prompt you to select an AWS CLI profile. If you already know the profile name you want to use, you can pass it as the `profilename` parameter:
```bash
awsx --profile
```
or
```bash
awsx --profile your_profilename
```

3. Use the `--region` flag to specify the AWS region:
```bash
awsx --region us-west-1
```

#### Detailed code explanation

Here is a brief explanation of some code snippets:

- `get_identity()`: Get AWS identity information.
- `get_parent_process_name()`: Gets the name of the parent process, which is used to determine whether it is running in `powershell` or `cmd`.
- `copy_env_command_to_clipboard()`: Based on the operating system and process name, generate a command to set the `AWS_PROFILE` environment variable and copy it to the clipboard.
- `list_aws_profiles()`: List all AWS CLI profiles.
- `get_region_from_profile()`: Get the default region from the given AWS CLI profile.
- `switch_aws_profile_interactive()`: Interactively prompts the user to select an AWS CLI profile and returns its name and default region.

The tool uses the `click` library to parse command line arguments, the `boto3` library to interact with AWS, the `pyperclip` library to copy text to the clipboard, and several other libraries to obtain system information and read configuration document.

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
