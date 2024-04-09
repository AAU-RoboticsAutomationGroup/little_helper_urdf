from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'little_helper_urdf'

# Function to recursively get all files within a directory
def get_all_files(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name), glob("launch/*.launch.py")), (os.path.join('share', package_name), glob('urdf/*')), (os.path.join('share', package_name) + "/mir/collision", glob('mir/collision/*')), (os.path.join('share', package_name) + "/mir/visual", glob('mir/visual/*')), (os.path.join('share', package_name) + "/mir/include", glob('mir/include/*')), (os.path.join('share', package_name) + "/ur5_to_convert", glob('ur5_to_convert/*')), (os.path.join('share', package_name) + "/meshes", glob('meshes/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='elias',
    maintainer_email='93720605+EliasTDam@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
