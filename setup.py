"""
    To update versionner:

    pip install versioneer

    cd pcircle-repo
    versioneer install

    This will bring versioneer.py etc to the latest in YOUR source tree.

    Now commit everything.

    make # generate tar ball, and try "make deploy" to verify

"""
import setuptools
import versioneer
import sys

requires = [
    'cffi>=1.11.5',
    'mpi4py>=3.1.5',
    'xattr>=0.10.1',
    'scandir>=1.10.0',
    'numpy>=1.19.5',
    'bitarray>=2.9.0',
    'future>=0.18.3'
]

details = """
More details on the package
"""

print("Version:", versioneer.get_version())

setuptools.setup(name='pcircle',
                 description="A parallel file system tool suite",
                 url="https://github.com/fwang2/pcircle/tree/master",
                 license="Apache",
                 author='Feiyi Wang',
                 author_email='fwang2@ornl.gov',
                 packages=['pcircle'],
                 data_files=[],
                 entry_points={
                     'console_scripts': [
                         'fcp=pcircle.fcp:main',
                         'fwalk=pcircle.fwalk:main',
                         'fsum=pcircle.fsum:main',
                         'fcorruptor=pcircle.fcorruptor:main',
                         'fdiff=pcircle.fdiff:main',
                         'fgen=pcircle.fgen:main',
                         'fprof=pcircle.fprof:main',
                         'fpipe=pcircle.fpipe:main'
                     ]
                 },
                 classifiers=[
                     'Development Status :: 3 - Beta',
                     'Intended Audience :: System Administrators',
                     'Topic :: System :: Monitoring',
                     'Programming Language :: Python :: 3.6',
                 ],
                 install_requires=requires,
                 long_description=details,
                 version=versioneer.get_version(),
                 cmdclass=versioneer.get_cmdclass(),
                 )

