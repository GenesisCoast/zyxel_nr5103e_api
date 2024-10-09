from setuptools import find_packages, setup

setup(
    name='zyxel_nr5103e_api',
    packages=find_packages(),
    version='0.1.0',
    description='RESTful API for the ZyXEL NR5103E router',
    author='GenesisCoast',
    install_requires=[
        'base64',
        'marshmallow',
        'marshmallow-dataclass',
        'requests',
        'smspdudecoder'
    ]
)