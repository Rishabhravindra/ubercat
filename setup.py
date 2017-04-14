from setuptools import setup

setup(name='UberCat', version='1.0',
      description='Show Uber price estimate from one point to dorm halls at the University of Cincinnati',
      author='Rishabh Ravindra', author_email='hello@rishravi.me',
      url='http://rishravi.me/ubercat',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['flask',
                        'uber-rides'
      ],
     )
