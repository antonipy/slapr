from distutils.core import setup
setup(
  name = 'slapr',
  packages = ['slapr'],
  version = '0.1',
  license='gpl-3.0',
  description = 'A simple tool that allows you to change your default AWS CLI profile.',
  author = 'Antoni Yanev',
  author_email = 'antonipyanev@gmail.com',
  url = 'https://github.com/antonipy/slapr',
  download_url = 'https://github.com/antonipy/slapr/archive/refs/tags/0.1.tar.gz',
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
    'License :: OSI Approved :: GPL-3.0 License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  entry_points = '''
        [console_scripts]
        slapr=slapr.main:cli
    '''
)
