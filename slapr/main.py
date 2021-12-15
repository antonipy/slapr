#!/usr/bin/env python3
import configparser
import inquirer
import os
import sys
import click

@click.command()
def cli():
    config_path = os.path.expanduser('~/.aws/config')
    credentials_path = os.path.expanduser('~/.aws/credentials')

    if not os.path.exists(config_path):
        sys.exit('''\nAWS config file (~/.aws/config) not found!
                \nRun aws config to configure your profiles!\n''')

    config = configparser.ConfigParser()
    config.read(config_path)
    credentials = configparser.ConfigParser()
    credentials.read(credentials_path)

    # Configure inquirer to use the parsed configuration sections
    question = [
        inquirer.List(
            'selected_profile',
            message='Which AWS profile do you want to use?',
            choices=config.sections(),
            carousel=True
        )
    ]

    # Prompt the user to select the profile
    selected_profile = inquirer.prompt(question).get('selected_profile')
    # Remove profile 'profile ' from the selected profile
    credentials_profile = selected_profile.replace('profile ', '')

    # Inform user
    sys.stdout.write(f'\nSetting {credentials_profile} as default AWS profile.\n\n')

    # Set the default AWS Profile in teh config file
    config['default'] = config[selected_profile]
    with open(config_path, 'w') as configfile:
        config.write(configfile)
    # Omit SSO profiles as they don't have credentials
    if credentials_profile in credentials.sections():
        # Set the default AWS in the credentials file
        credentials['default'] = credentials[credentials_profile]
        with open(credentials_path, 'w') as credsfile:
            credentials.write(credsfile)

    # Check if account is SSO and inform user how to login
    if any('sso' in key for key in list(config[selected_profile].keys())):
        sys.stdout.write(f'Your AWS profile {credentials_profile} is using SSO.\n'
                        f'Please run \'aws sso login --profile {credentials_profile}\' to authenticate.\n')

if __name__ == '__main__':
    cli()
