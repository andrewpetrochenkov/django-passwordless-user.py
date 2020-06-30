import setuptools

setuptools.setup(
    name='django-passwordless-user',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
