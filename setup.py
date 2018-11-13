from distutils.core import setup

setup(
	name='facenet',
	version='0.0.2',
	description="Face recognition with Google's FaceNet deep neural network.",
	url='https://github.com/arturcuringa/facenet.git',
	packages=['facenet', 'facenet.src', 'facenet.src.align'],
	package_data={'facenet.src.align': ['*.npy']}
)

