from setuptools import setup, find_packages

setup(
    name='employee_system',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'emp=employee_system.main_cli:main'
        ]
    },
    install_requires=[]
)