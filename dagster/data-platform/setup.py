from setuptools import find_packages, setup

setup(
    name="data_platform",
    packages=find_packages(exclude=["data_platform_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-fivetran",
        "dagster-dbt",
        "dagster-census",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
