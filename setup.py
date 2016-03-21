import setuptools

setuptools.setup(
    author='Hazel Court',
    author_email='hcourt@uchicago.edu',
    description=__doc__,
    install_requires=[
        Flask,
        flask-flatpages,
        Frozen-Flask,
        pyyaml,
    ],
    name='resume',
    packages=setuptools.find_packages(),
)
