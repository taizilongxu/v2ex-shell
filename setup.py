from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="v2ex",
    version="0.1.0",
    description="V2EX 热门话题终端工具",
    author="xiao.xu",
    author_email="",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "v2ex = v2expkg.v2ex:main"
        ]
    },
    include_package_data=True,
) 