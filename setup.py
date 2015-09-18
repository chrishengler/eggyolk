from distutils.core import setup, Extension
import os

os.environ["CC"] = "g++"

checkyrsai = Extension('_checkyrsai',
                    sources = ['checkyrsai_wrap.cxx','../checkyrs/checkyrs/ai.cpp'],
                    include_dirs = ['/usr/local/include','../checkyrs/checkyrs'],
                    libraries = ['Checkyrs'],
                    library_dirs = ['../checkyrs/Build/Products/Release/'],
                    extra_link_args = ['-std=c++11']
                    )

gamerunner = Extension('_gamerunner',
                    sources = ['gamerunner_wrap.cxx','../checkyrs/checkyrs/gamerunner.cpp'],
                    include_dirs = ['/usr/local/include','../checkyrs/checkyrs'],
                    libraries = ['Checkyrs'],
                    library_dirs = ['../checkyrs/Build/Products/Release/'],
                    extra_link_args = ['-std=c++11']
                    )


setup (name = 'checkyrs',
       version = '1.0',
       description = 'checkyrs',
       ext_modules = [checkyrsai,gamerunner])
