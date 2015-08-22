# ---------------------------------
# Example of plug-in module for the
# aa_macro.py system that follows
# the [embrace module] convention
# ---------------------------------

class plug(object):
	def __init__(self):
		self.settable()

	# This provides a reference to the parent class, macro()
	def install(self,parent):
		self.parent = parent

	# [happy content] - extension
	def happy_fn(self,tag,data):	# an extension of macro() built-ins
		return data + ' :)'

	# [unhappy content] - extension
	def unhappy_fn(self,tag,data):	# another extension of macro() built-ins
		return data + ' :('

	# [i content] - over-ride existing built-in, use <em> instead of <i>
	def i_fn(self,tag,data):
		return '<em>' + data + '</em>'

	# [dtcase] - dump the macro() notcase table
	def dtcase_fn(self,tag,data):
		o = ''
		for el in self.parent.notcase:
			if o != '':
				o += ', '
			o += el
		return o

	def settable(self):
		self.extensions = {
			'happy'		: self.happy_fn,	# add new built-in 'happy'
			'unhappy'	: self.unhappy_fn,	# add new built-in 'unhappy'
			'i'			: self.i_fn,		# replace the 'i' built-in
			'dtcase'	: self.dtcase_fn,	# access macro() varaibles
		}

	# This MUST be named "gettable()"
	# -------------------------------
	def gettable(self):
		return self.extensions
