from setuptools import setup, find_packages


setup(
    name='snapshot',
    packages=find_packages(),
    version='0.0.1dev',
    entry_points={
        "console_scripts": [
            "snapshot = snapshot.snapshot:main"
        ],
    },
)
