from setuptools import setup

setup(name='smartbarclip',
      version='1.0',
      description='Library for barbell positioning alert',
      author='Moose Munna',
      author_email='mrm815@nyu.edu',
      url='https://github.com/mrm815/Smart-Bar-Clip',
      install_requires=['ADXL345','i2c','PS1240'],
      py_modules=['smartbarclip'],
      )
