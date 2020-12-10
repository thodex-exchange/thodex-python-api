from setuptools import find_packages, setup

setup(
    name='Thodex',
    version='1.0.3',
    license='MIT',
    description='Python library for the Thodex API designed to be easy to use.',
    author='Atakan DEMIRKIR',
    author_email='atakandemirkir@gmail.com',
    url='https://github.com/atakandemirkir/thodex-python-api',
    packages=find_packages(),
    python_requires=">=3.0",
    install_requires=[
        "requests",
        "websocket",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

)
