from setuptools import find_packages, setup
import glob

package_name = 'decision'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/data', glob.glob('data/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'sonar_park = decision.sonar_park:main',
            'color_detect = decision.color_detect:main',
            'aruco_detect = decision.aruco_detect:main',
            'track_line = decision.track_line:main',
            'arm_grab = decision.arm_grab:main'
        ],
    },
)
