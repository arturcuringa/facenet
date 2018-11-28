from distutils.core import setup

setup(
	name='facenet',
	version='0.0.3',
	description="Face recognition with Google's FaceNet deep neural network.",
	url='https://github.com/arturcuringa/facenet.git',
	packages=['facenet', 'facenet.contributed' , 'facenet.src', 'facenet.src.align'],
	package_data={'facenet.src.align': ['*.npy']}
)

