from setuptools import setup, find_packages

setup(
    name='mmabia_textpad',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'tkinter',
    ],
    entry_points={
        'console_scripts': [
            'mmabia_textpad=mmabia_textpad:main',
        ],
    },
)