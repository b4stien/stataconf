import os

from setuptools import setup
from setuptools.command.build_py import build_py


class CustomBuildPy(build_py):
    def _get_package_data_output_mapping(self):
        platform = os.environ["PLAT_NAME"]

        if platform == "macosx_11_0_arm64":
            must_ends_with = "arm64"
        elif platform == "manylinux2014_x86_64":
            must_ends_with = "amd64"
        else:
            raise Exception("Unknown platform")

        return [
            v
            for v in build_py._get_package_data_output_mapping(self)
            if v[0].endswith(must_ends_with)
        ]


setup(cmdclass={"build_py": CustomBuildPy})
