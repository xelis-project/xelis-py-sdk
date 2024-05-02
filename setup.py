from setuptools import setup, find_packages

setup(
  name="xelis-py-sdk",
  author="g45t345rt",
  version="0.1.0",
  description="Xelis software development kit for Python",
  packages=find_packages(),
  install_requires=["mashumaro", "websockets"],
  setup_requires=["pytest-runner"],
  tests_require=["pytest"],
  test_suite="tests"
)