from setuptools import find_packages
from setuptools import setup


try:
    README = open('README.md').read() + '\n\n' + open('CHANGELOG.md').read()
except IOError:
    README = None

setup(
    name='guillotina_batch',
    version='5.0.3',
    description='batch endpoint for guillotina',
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=[
        'guillotina>=5.0.0.dev0,<6',
        'backoff',
    ],
    author='Nathan Van Gheem',
    author_email='vangheem@gmail.com',
    url='https://github.com/guillotinaweb/guillotina_batch',
    packages=find_packages(exclude=['demo']),
    package_data={"": ["*.txt", "*.rst"], "guillotina_batch": ["py.typed"]},
    include_package_data=True,
    license='BSD',
    extras_require={
        'test': [
            'pytest>=3.8.0',
            'docker',
            'backoff',
            'jsonschema==2.6.0',
            'psycopg2-binary',
            'pytest-asyncio>=0.10.0',
            'pytest-cov',
            'coverage==4.4.0',
            'pytest-docker-fixtures',
            'asyncpg==0.15.0'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
    ],
    entry_points={
    }
)
