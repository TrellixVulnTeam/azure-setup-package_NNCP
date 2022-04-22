# Set up package

## Define fuction
- Define a or more folder as packages. Each folder as a package, name folder present name package (what function?)
- example: package name 'normalize' have 2 functions: clean columns (columns.py) & support spark (spark.py) in a folder have name is "normalize".
## Define setup.py
<p>
    name="normalize",
    version="0.0.6",
    author="Pham Manh",
    author_email="pvm@26042000@gmail.com",
    description="package for normalize columns dataframe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires = ['pandas']
</p>
## Set up