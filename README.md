# Select AWS Profile
Select AWS Profile (slapr) is a simple tool that lets you select which AWS Profil you want to use and sets it as the default AWS profile, so that you can easily use your favorite AWS CLI commands.

## Installation
```bash
pip install slapr
```

## Usage
```bash
slapr
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

### How to test
- Setup virtual environment and install requirements
```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
- Once you are ready with your changes and  you want to test them locally, install the tool in editable mode
```bash
pip install --editable .
```

## License