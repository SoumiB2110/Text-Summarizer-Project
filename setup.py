import setuptools 
#intializing your readme,you need to read your readme file  , supose you want to publish a package as pypi 
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()
__version__="0.0.0"
REPO_NAME="Text-Summarizer-Project"
AUTHOR_USER_NAME="SoumiB2110"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="b.soumi2110@gmail.com"
#Final initialisation for the project
setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SoumiB2110/Text-Summarizer-Project",
    project_urls={
        "Bug Tracker": "https://github.com/SoumiB2110/Text-Summarizer-Project/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
   
)