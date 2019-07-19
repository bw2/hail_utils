# based on https://uoftcoders.github.io/studyGroup/lessons/python/packages/lesson/

from setuptools import setup

from setuptools.command.install import install
import os
import urllib.request
import sys
# from https://mvnrepository.com/artifact/com.google.cloud.bigdataoss/gcs-connector/hadoop2-1.9.17

GCS_CONNECTOR_URL = 'https://repo1.maven.org/maven2/com/google/cloud/bigdataoss/gcs-connector/hadoop2-1.9.17/gcs-connector-hadoop2-1.9.17.jar'


class PostInstallCommand(install):

    def run(self):
        self.announce(self.install_platlib, level=3)
        self.announce(self.install_lib, level=3)
        self.announce(self.install_scripts, level=3)
        #raise ValueError(os.path.abspath(os.getcwd()) + "\n")
        raise ValueError(str(self.install_base) + "\n")
        raise ValueError(str(self.root) + "\n")

        os.path.join(self.install_base,)
        try:
            urllib.request.urlretrieve(GCS_CONNECTOR_URL, '/usr/local/lib/python3.7/site-packages/pyspark/jars/gcs-connector-hadoop2-latest.jar')
        except Exception as e:
            self.warn('Unable to download GCS connector: ' + str(e))

        install.run(self)

setup(
    name='hail_utils',
    url='https://github.com/bw2/hail-utils',
    author='Ben',
    author_email='ben.weisburd@gmail.com',
    packages=['hail_utils'],
    install_requires=['hail'],
    version='0.1',
    license='MIT',
    description='Misc. hail utils',
    cmdclass={
        'install': PostInstallCommand,
    },
)
