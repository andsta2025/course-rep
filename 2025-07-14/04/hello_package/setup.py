from setuptools import setup

setup(
    name="hello_package",
    version="0.1.5",
    py_modules=["hello"],
    entry_points={
        "console_scripts": [
            "hello-world=hello:main",
        ],
    },
    author="Jonas Mekas",
    author_email="your.email@example.com",
    description="A simple script that prints Hello, World!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)