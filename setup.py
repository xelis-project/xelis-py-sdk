from setuptools import setup, find_packages

setup(
  name="xelis-py-sdk",
  version="0.1.0",
  packages=find_packages(),
  author="g45t345rt",
  description="Xelis software development kit for Python",
  url='https://github.com/xelis-project/xelis-py-sdk',
  install_requires=["mashumaro", "websockets"],
  setup_requires=["pytest-runner"],
  tests_require=["pytest"],
  test_suite="tests"
)