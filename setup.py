from setuptools import setup

setup(
    name="apps",
    version="0.1.0",
    include_package_data=True,
    packages=["apps.account", "apps.base"],
    zip_safe=False,
)
