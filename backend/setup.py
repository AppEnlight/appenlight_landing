import os
import re

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

REQUIREMENTS = open(os.path.join(here, 'requirements.txt')).readlines()

compiled = re.compile('([^=><]*).*')


def parse_req(req):
    return compiled.search(req).group(1).strip()


requires = [_f for _f in map(parse_req, REQUIREMENTS) if _f]

setup(name='appenlight_landing',
      version='0.0',
      description='appenlight_landing',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      package_dir={'': 'src'},
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='appenlight_landing',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = appenlight_landing:main
      """,
      )
