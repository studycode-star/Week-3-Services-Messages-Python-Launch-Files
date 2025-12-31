from setuptools import setup
import os
from glob import glob

package_name = 'robocon_basics'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.xml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='khoi',
    maintainer_email='nmkhoii1402@gmail.com',
    description='Robocon basics talker & listener',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "my_talker = robocon_basics.hello_world:main",
            "my_listener = robocon_basics.receiver:main",
        ],
    },
)
