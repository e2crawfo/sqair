try:
    import setuptools
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    setuptools = use_setuptools()

from setuptools import find_packages, setup  # noqa: F811

setup(
    name='sqair',
    version='0.1',
    packages=find_packages(),
)
