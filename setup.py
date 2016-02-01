from setuptools import setup

setup(
        name='mqtt-message-cataloger',
        version='1.0',
        packages=[''],
        url='https://github.com/bjaanes/mqtt-message-cataloger',
        license='MIT',
        author='Gjermund Bjaanes',
        author_email='bjaanes@gmail.com',
        description='Python application that subscribes to MQTT messages and saves them to a database',
        install_requires=[
            'paho-mqtt'
        ]
)
