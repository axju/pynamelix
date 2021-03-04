from setuptools import setup


setup(
    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    include_package_data=True,

    packages=['pynamelix'],
    install_requires=[
        'requests',
        'check-pypi-name',
    ],
    entry_points={
        'console_scripts': [
            'pynamelix=pynamelix.__main__:main',
        ],
    },

)
