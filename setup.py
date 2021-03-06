from setuptools import setup, find_packages

setup(
    name="torngas",
    version="0.9.1",
    description="torngas based on tornado",
    author="qingyun.meng",
    url="https://github.com/mqingyn/torngas",
    license="BSD",
    packages=find_packages(),
    package_data={'torngas': ['resource/exception.html']},
    author_email="maingyn@gmail.com",
    requires=['Tornado', 'futures'],
    scripts=[],
)
