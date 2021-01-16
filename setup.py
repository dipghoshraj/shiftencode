import setuptools

setuptools.setup(
    name="shiftencode", # Replace with your own username
    version="0.0.1",
    author="Dip Ghosh",
    author_email="dipghoshraj@gmail.com",
    description="shift-encode is a encoding and decoding libery for text and messages",
    long_description= open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dipghoshraj/shiftencode",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)