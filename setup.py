from setuptools import setup

setup(
    name="tfdread",
    version="0.1.0",
    description="Python package to read data from TFD files used in geophysical logging",
    packages=("tfdread",),
    install_requires=("click",),
    entry_points={"console_scripts": ("tfdread = tfdread:open_entry_point",)},
)
