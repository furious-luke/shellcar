from setuptools import find_packages, setup

setup(
    name='shellcar',
    version='0.0.0',
    author='Luke Hodkinson',
    author_email='luke@expensecheck.com.au',
    maintainer='Luke Hodkinson',
    maintainer_email='luke@expensecheck.com.au',
    description='',
    long_description='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License'
    ],
    packages=find_packages(exclude=['tests', 'extern']),
    include_package_data=True,
    package_data={'': ['*.txt', '*.js', '*.html', '*.*']},
    install_requires=[
        'flask==1.1.1',
    ],
    extras_require={},
    zip_safe=True
)
