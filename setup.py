from setuptools import setup, find_packages

setup(
    name='my_alembic_cli',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'sqlalchemy',
    ],
    entry_points='''
        [console_scripts]
        my_alembic_cli=alembic_cli:main
    ''',
)
