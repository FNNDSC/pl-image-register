
from setuptools import setup


def parse_requirements(file_path):
    """
    Parse the requirements.txt file and return a list of requirements, ignoring comments.

    Parameters:
    file_path (str): Path to the requirements.txt file.

    Returns:
    list: List of package names.
    """
    requirements = []
    with open(file_path, 'r') as file:
        for line in file:
            # Strip whitespace and newline characters
            line = line.strip()
            # Skip empty lines and comments
            if not line or line.startswith('#'):
                continue
            # Split the line on the first occurrence of '~='
            package = line.split('~=')[0]
            requirements.append(package)

    return requirements



setup(name='register_image',
    version='1.0.0',
    description='A ChRIS plugin for image registration and re-slicing.',
    author='FNNDSC / Arman Avesta, MD, PhD',
    author_email='dev@babyMRI.org',
    url='https://github.com/FNNDSC/pl-image-register',
    py_modules=['image_register', 'registration_tools', 'visualisation_tools'],
    install_requires=parse_requirements('requirements.txt'),
    license='MIT',
    entry_points={'console_scripts': ['image_register = image_register:main']},
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'],
    extras_require={'none': [], 'dev': ['pytest~=7.1']})
