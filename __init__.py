from pythonforandroid.recipe import CythonRecipe

class _weakrefRecipe(CythonRecipe):
	version = None
	url = None
	name = '_weakref'

	depends = ['hostpython2', 'python2']

recipe = _weakrefRecipe();