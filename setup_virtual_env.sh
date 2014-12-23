#apt-get install python-virtualenv python-numpy python-imaging 
# for virtualenv >= 1.7 the --system-site-packages is required to 
# include the system-level packages... 
virtualenv --sytem-site-packages tutorial virtualenv tutorial 
# older virtualenvs source tutorial/bin/activate 
# The -I flag ensures we are installed in this virtualenv 
pip install -I http://sourceforge.net/projects/fonttools/files/2.3/fonttools-2.3.tar.gz/download pip install -I TTFQuery PyOpenGL PyOpenGL-accelerate 
pip install -I pydispatcher PyVRML97 PyVRML97-accelerate simpleparse 
pip install -I OpenGLContext
