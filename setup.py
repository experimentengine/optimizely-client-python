from setuptools import setup

setup(name='optimizely_ee',
      version='0.3.2',
      description='An interface to Optimizely\'s REST API.',
      url='https://github.com/optimizely/optimizely-client-python',
      author='Optimizely',
      packages=['optimizely_ee'],
      install_requires=[
        'requests',
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])
