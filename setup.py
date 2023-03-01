import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='pynimbar',
    version='1.0.0',
    author='Gabriel Mitelman Tkacz',
    description='Make your Python scripts more user friendly with loading animations',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    py_modules=['pynimbar'],
    package_dir={'': 'pynimbar/src'},
    install_requires=[]
)
