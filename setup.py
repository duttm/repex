import setuptools

if __name__ == "__main__":
        setuptools.setup(
            name='repex',
            version="3.0.1",
            description='A scalable, flexible and extensible replica exchange package',
            author='Srinivas Mushnoori',
            url='https://github.com/SrinivasMushnoori/RepEx_3.0',
            license='',
            packages=setuptools.find_packages(),
                install_requires=['numpy',
                                  'radical.pilot',
                                  'radical.entk' ],

            scripts=['bin/repex-version',
                     ],
            zip_safe=True,
            )
