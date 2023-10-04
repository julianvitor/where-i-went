from setuptools import setup, find_packages
import os
long_description = open("README.md").read()

setup(
    name='where_i_went',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'exifread',
        'folium',
        'tqdm',
        'branca==0.6.0',
        'certifi==2023.7.22',
        'charset-normalizer==3.2.0',
        'ExifRead==3.0.0',
        'idna==3.4',
        'Jinja2==3.1.2',
        'MarkupSafe==2.1.3',
        'numpy==1.25.2',
        'requests==2.31.0',
        'tqdm==4.66.1',
        'urllib3==2.0.4',
    ],
    package_data={'': ['coord_converter.so']},  # Garanta que o .so seja empacotado corretamente
    long_description=long_description,
    long_description_content_type='text/markdown',
)

