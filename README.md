# Select AWS Profile [![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/antonipy/slapr.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/antonipy/slapr/context:python)

Select AWS Profile (slapr) is a simple tool that lets you select which AWS Profile you want to use and sets it as the default AWS profile, so that you can easily use your favorite AWS CLI commands.

## Installation

```bash
pip install slapr
```

## Usage

> **WARNING**: 
>
> If you already have configured a **default aws cli profile**, please rename it otherwise the tool will overwrite it.
>
> If you have set the **AWS_PROFILE** environment variable the tool won't work.

![use_slapr.gif](https://raw.githubusercontent.com/antonipy/slapr/main/media/use_slapr.gif)

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

This project is under The GNU General Public License v3.0