import argostranslate.package, argostranslate.translate

from_code = "ja"
to_code = "en"

argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()

try:
    package_to_install = next(
        filter(
            lambda package: package.from_code == from_code and package.to_code == to_code, available_packages
        )
    )
    argostranslate.package.install_from_path(package_to_install.download())
except StopIteration:
    print(f"No available translation package from '{from_code}' to '{to_code}'.")
    exit()