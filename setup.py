import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="futuresales-denissimo",
    version="0.0.2",
    author="denissimo",
    author_email="twihkapb@gmail.com",
    description="My utility pkg",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Denchidlo/fs-lib",
    project_urls={
        "Bug Tracker": "https://github.com/Denchidlo/fs-lib/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
