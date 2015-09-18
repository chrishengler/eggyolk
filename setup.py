from distutils.core import setup, Extension
import os

os.environ["CC"] = "g++"

checkyrsai = Extension('_checkyrsai',
                    sources = ['checkyrsai_wrap.cxx','ai.cpp'],
                    include_dirs = ['/usr/local/include','../checkyrs/checkyrs'],
                    libraries = ['CheckyrsAI','CheckyrsBase'],
                    library_dirs = ['../checkyrs/Build/Products/Release/'],
                    extra_link_args = ['-std=c++11']
                    )



setup (name = 'checkyrsai',
       version = '1.0',
       description = 'checkyrsAI',
       ext_modules = [checkyrsai])
