from setuptools import setup, find_packages


setup(
    name='snapshot',
    packages=find_packages(),
    version='testing',
    entry_points={
        "console_scripts": [
            "snapshot = snapshot.snapshot:main"
        ],
    },
)
