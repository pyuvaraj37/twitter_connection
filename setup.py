import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="twitter_connection", # Replace with your own username
    version="0.0.4",
    author="Prithviraj Yuvaraj",
    author_email="ryuvaraj37@gmail.com",
    description="A library to connect to twitter API as a free user.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pyuvaraj37/twitter_connection",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)