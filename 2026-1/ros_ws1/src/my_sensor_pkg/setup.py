from setuptools import find_packages, setup

package_name = 'my_sensor_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hypark',
    maintainer_email='hypark@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'distance_publisher = my_sensor_pkg.distance_publisher:main',
            'distance_subscriber = my_sensor_pkg.distance_subscriber:main',
            'serial_bridge = my_sensor_pkg.serial_bridge_node:main',
            'distance_controller = my_sensor_pkg.distance_controller:main',
        ],
    },
)
