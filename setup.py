import setuptools

setuptools.setup(
    name="shiftencode", # Replace with your own username
    version="0.0.1",
    author="Dip Ghosh",
    author_email="author@example.com",
    description="A small example package",
    long_description="long_description",
    long_description_content_type="text/markdown",
    url="https://github.com/dipghoshraj/shiftencode",
    packages=setuptools.find_packages(),
    package_dir={'':'shiftencode'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)