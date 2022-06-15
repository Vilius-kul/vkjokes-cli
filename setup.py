from setuptools import setup

setup(
    name='vkjokes',
    version='0.1',
    py_modules=['vkjokes'],
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'vkjokes = vkjokes:cli',
            ],
    },
)