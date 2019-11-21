import subprocess
try:
    import setuptools
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    setuptools = use_setuptools()

from setuptools import find_packages, setup  # noqa: F811

try:  # for pip >= 10
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError:  # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession

links = []
requires = []

try:
    requirements = list(parse_requirements('requirements.txt'))
except Exception:
    # new versions of pip requires a session
    requirements = list(parse_requirements('requirements.txt', session=PipSession()))

for item in requirements:
    # we want to handle package names and also repo urls
    print(dir(item))
    print(item.req)
    print(item.link)

    link = None
    if getattr(item, 'url', None):   # older pip has url
        link = str(item.url)
    elif getattr(item, 'link', None):  # newer pip has link
        link = str(item.link)

    if link is not None and item.editable:
        command = 'pip install -e {}'.format(link)
        print("Installing editable repo with command: {}".format(command))
        subprocess.run(command.split())
        continue

    elif link is not None:
        links.append(link)

    if item.req:
        requires.append(str(item.req))



setup(
    name='sqair',
    version='0.1',
    packages=find_packages(),
)
