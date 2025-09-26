from setuptools import setup, find_packages

setup(
    name='hiwonder_sdk',
    version='-1',
    packages=find_packages(),
    include_package_data=True,  # 让包包含其他数据文件
    package_data={
        'hiwonder_sdk': ['data/*'],  # 将数据目录下的文件包含进包
    },
    install_requires=[
        # 依赖的其他包
    ],
)
