from setuptools import setup, find_packages
LONG_DESCRIPTION = """
# DesktoPy
## Description:
A Library For Building Desktop Applications and Interfaces that is built on top of tkinter, customtkinter, and other libraries associated.

## Getting Started:

## Documentation:

"""
setup(
    name='desktopy',
    version='0.0.1',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    url='https://github.com/AnmarHani/DesktoPy',
    license='MIT',
    author='Anmar Hani',
    install_requires=['tkinter', 'Pillow', 'tkintermapview', 'customtkinter', 'pyinstaller'],
    keywords=['python', 'desktop', 'gui', 'ui' 'development'],
    author_email='AnmarHaniV1@gmail.com',
    description='A Library For Building Desktop Applications and Interfaces that is built on top of tkinter, customtkinter, and other libraries associated.',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent'
    ]
)