from setuptools import setup, find_packages

setup(
    name="ADOBase",
    version="0.1.0",
    description="为 ADOFAI 游戏的 .adofai 关卡文件提供读写、查找、增删改等操作的库",
    author="你的名字",
    author_email="你的邮箱",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[],
    url="https://github.com/你的github/ADOBase",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 