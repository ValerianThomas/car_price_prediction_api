import os
import pathlib
PACKAGE_ROOT = pathlib.Path(__file__).resolve().parent
with open(os.path.join(PACKAGE_ROOT,'VERSION' )) as version_file :
  __version__ = version_file.read().strip()