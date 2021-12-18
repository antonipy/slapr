#!/usr/bin/env python3
import configparser
import inquirer
import os
import sys
import click
import signal

@click.command()
def cli():
    signal.signal(signal.SIGINT, sig_handler)
    config_path = os.path.expanduser('~/.aws/config')
    credentials_path = os.path.expanduser('~/.aws/credentials')

    if not os.path.exists(config_path):
        sys.exit('''\nAWS config file (~/.aws/config) not found!
                \nRun \'aws configure --profile profile-name\' to configure your profiles!\n''')

    config = configparser.ConfigParser()
    config.read(config_path)
    credentials = configparser.ConfigParser()
    credentials.read(credentials_path)

    # Check if the user has set default profile 
    if 'default' in config.keys():
        # Check if the default profile was previously set by slapr
        if 'slapr' not in config['default'].keys():
            approve_step()

    # Configure inquirer to use the parsed configuration sections
    try:
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
    # If ctrl+c is pressed here, it throws an AttributeError
    except AttributeError:
        sys.stdout.write('\b\b\r')
        sys.exit(0)

    # Inform user
    sys.stdout.write(f'\nSetting {credentials_profile} as default AWS profile.\n\n')

    # Set the default AWS Profile in teh config file
    config['default'] = config[selected_profile]
    # Set that the default profile is configured by slapr
    config['default']['slapr'] = 'True'
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

# Handler function for the keyboard interrupt
def sig_handler(signum, stack):
    sys.stdout.write('\b\b\r')
    sys.exit('Cancelled by user')

# Function to prompt the user for approval
def approve_step():
    while True:
        approve = input(
                        f'\nYou have a configured default profile.\n'
                        f'Slapr will overwite it.\n'
                        f'Do you approve? y/n\n'
                        )
        if approve.strip()[:1].lower() == 'y' or approve.strip().lower() == 'yes':
            break
        if approve.strip()[:1].lower() == 'n' or approve.strip().lower() == 'no':
            sys.exit('Goodbye!')

if __name__ == '__main__':
    cli()
