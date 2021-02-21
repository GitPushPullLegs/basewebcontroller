from setuptools import setup, find_packages

setup(
    name='basewebcontroller',
    version='0.0.1',
    description='A base package for my web controllers.',
    url='https://github.com/GitPushPullLegs/basewebcontroller',
    author='Joe Aguilar',
    author_email='jose.aguilar.6694@gmail.com',
    license='MIT License',
    packages=find_packages(exclude=[]),
    install_requires=['selenium'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    package_data={'': ['basewebcontroller/drivers/chromedriver.exe', 'basewebcontroller/html/welcome.html']},
    include_package_data=True,
)