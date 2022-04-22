# Set up package

## Define fuction
- Define a or more folder as packages. Each folder as a package, name folder present name package (what function?)
- example: package name 'normalize' have 2 functions: clean columns (columns.py) & support spark (spark.py) in a folder have name is "normalize".
## Define setup.py
```
    ## name of package
    name="normalize",
    ## version
    version="0.0.6",
    ## info author 
    author="Pham Manh",
    author_email="pvm@26042000@gmail.com",

    ## descibe package 
    description="package for normalize columns dataframe",
    long_description= "package for normalize columns dataframe and support clean dataset",

    ## type descibe package 
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    ##  environment used
    python_requires='>=3.7',

    ## install libary have in environment or used in function
    install_requires = ['pandas']
```
## Set up
Open terminal at dirname ~/setup:
```
python setup.py bdist_wheel

```
After setup is successed, can view package at ~/setup/dist/name_package.whl
## Thank you, I'm ManhPham!
