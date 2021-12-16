from distutils.core import setup
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
  name = 'slapr',
  packages = ['slapr'],
  version = '1.1',
  license='gpl-3.0',
  description = 'A simple tool that allows you to change your default AWS CLI profile.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Antoni Yanev',
  author_email = 'antonipyanev@gmail.com',
  url = 'https://github.com/antonipy/slapr',
  download_url = 'https://github.com/antonipy/slapr/archive/refs/tags/1.1.tar.gz',
  keywords = ['aws', 'awscli', 'awscliv2', 'linux', 'tools'],
  install_requires=[
          'inquirer',
          'click'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Topic :: Internet',
    'Topic :: Software Development :: Build Tools',
    'Topic :: Utilities',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  entry_points = '''
        [console_scripts]
        slapr=slapr.main:cli
    ''',
  include_package_data=True
)
