import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(
    name='pan-img',
    version='0.1',
    scripts=['pan-img'],
    author="Ivan Pandzic",

    author_email="ivan.pandzic@gmail.com",
    description="An image download library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ipandzic/dokr",
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
