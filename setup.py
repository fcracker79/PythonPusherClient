from setuptools import setup
import sys

VERSION = "0.3.0"

major, minor1, minor2, release, serial = sys.version_info

def readfile(filename):
    with open(filename, **readfile_kwargs) as fp:
        contents = fp.read()
    return contents
        
def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="pusherclient",
    version=VERSION,
    description="Pusher websocket client for python",
    long_description=readme(),
    keywords="pusher websocket client",
    author="Erik Kulyk",
    author_email="e.kulyk@gmail.com",
    license="MIT",
    url="https://github.com/ekulyk/PythonPusherClient",
    install_requires=readfile(os.path.join(os.path.dirname(__file__), "requirements.txt")),
    packages=["pusherclient"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries ",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
