from distutils.core import setup

setup(name='stocktalk',
      version='v2.6',
      description='Data collection toolkit for social media analytics',
      author='Anthony Federico,Ben Harris',
      author_email='dephoona@gmail.com,james.ben.harris@gmail.com',
      url='https://github.com/anfederico/Stocktalk',
      packages=['stocktalk'],
      scripts=['bin/stocktalk-corpus']
     )