from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt") as req:
        content = req.read()
        requirements = content.split("\n")
    return requirements

setup(
    name = "looknice",
    version = "0.1",
    packages = ["looknice"],
    package_dir = {"looknice": "looknice"},
    include_package_data = True,
    package_data = {"looknice": ["config/*.txt"]},
    install_requires = read_requirements(),
    entry_points = """
        [console_scripts]
        my_test = looknice.cli:my_test
        looknice_lint = looknice.cli:lint
        looknice_params = looknice.cli:print_parameters
        looknice_fix = looknice.cli:fix
        looknice_print_path = looknice.cli:print_path
    """
)