from setuptools import setup

package_name = 'your_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='arigatougozaimaster',
    maintainer_email='hongliang.sun@hotmail.com',
    description='Converts rosbag to pcd file for further',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'save_pcd = your_package.save_pcd:main',
        ],
    },
)
