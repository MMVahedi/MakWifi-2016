
from setuptools import setup


# Dynamically calculate the version based on pyautogui.VERSION.
version = __import__('pyautogui').__version__


setup(
    name='PyAutoGUI',
    version=version,
    url='https://github.com/asweigart/pyautogui',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description=('A cross-platform module for GUI automation for human beings. '
                 'Control the keyboard and mouse from a Python script.'),
    license='BSD',
    packages=['pyautogui'],
    test_suite='tests',
    keywords="gui automation test testing keyboard mouse cursor click press keystroke control",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)