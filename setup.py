from setuptools import setup, find_packages

setup(
        name='django-leaflet-point',
        version='0.3.1',
        author='Anton van Berlekom',
        author_email='anton@berlekom.com',
        url='https://github.com/Anton-vBR/django-leaflet-point',
        download_url="https://pypi.org/project/django-leaflet-point/",
        description="Use Leaflet with point data (lat, lng)",
        long_description= "",
        license='MIT',
        install_requires=['Django'],
        extras_require={
            'docs': ['sphinx', 'sphinx-autobuild'],
        },
        packages=find_packages(exclude=("tests.*", "tests", "example")),
        include_package_data=True,
        zip_safe=False,
        classifiers=[],
)