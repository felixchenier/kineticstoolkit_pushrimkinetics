"""Setup tool for building a pip-accessible package."""

import setuptools

#--------------------------------------------------------------------------------
# Please modify to fit your extension (particularly the text in CAPITALS)
#--------------------------------------------------------------------------------
name = "kineticstoolkit_pushrimkinetics"
description = "Provide functions to process kinetic data from instrumented wheelchair wheels."
url = "https://github.com/felixchenier/kineticstoolkit_pushrimkinetics"
author = "Félix Chénier"
author_email = "chenier.felix@uqam.ca"
#--------------------------------------------------------------------------------
# It may be advised to avoid modifying the rest of this file.
#--------------------------------------------------------------------------------


with open("README.md", "r") as fh:
    long_description = fh.readline()

setuptools.setup(
    name=name,
    description=(description),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    author=author,
    author_email=author_email,
    license='Apache',
        license_files=['LICENSE.txt'],
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    packages=['*.py'].extend(setuptools.find_packages()),
    install_requires=[],
    python_requires='>=3.8',
)
