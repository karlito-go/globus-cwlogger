from setuptools import setup, find_packages

setup(
    name="globus_cw_daemon",
    version=1.0,
    packages=find_packages(),
    install_requires=[
        'boto==2.48.0'
    ],

    entry_points={
        'console_scripts': [
            'globus_cw_daemon = globus_cw_daemon.daemon:main',
            'globus_cw_daemon_install = globus_cw_daemon_install.install:main']
    },

    include_package_data = True,

    # descriptive info, non-critical
    description="Daemon for Globus CloudWatch Logger",
    url="https://github.com/globus/globus-cwlogger",
)
