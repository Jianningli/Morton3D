import os
import sys
from setuptools import setup

setup(
    name='Morton3D',
    version='1.0.1',
    author='Jianning Li',
    author_email='jianningli.me@gmail.com',
    maintainer='Jianning Li',
    maintainer_email='jianningli.me@gmail.com',
    description='Efficient 3D Morton Encoding and Decoding',
    keywords='z-order, morton order, 3D hashing',
    url='https://github.com/Jianningli/Morton3D',
    download_url = 'https://github.com/Jianningli/Morton3D/archive/1.0.1.zip', 
    py_modules=['Morton3D'],
    
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',   
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
  ],
)
