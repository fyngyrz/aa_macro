#!/usr/bin/python

class macro(object):
	"""Class to provide an HTML macro language
      Author: fyngyrz  (Ben)
     Contact: fyngyrz@gmail.com (bugs, feature requests, kudos, bitter rejections)
     Project: aa_webpage.py
  Incep Date: June 17th, 2015     (for Project)
     LastRev: July 1st, 2015      (for Class)
  LastDocRev: July 23rd, 2015     (for Class)
 Tab spacing: 4 (set your editor to this for sane formatting while reading)
    Examples: At bottom. Run in shell like so:    python aa_macro.py
 Typical Use: from aa_macro import *
     1st-Rel: 1.0.0
     Version: 1.0.0
     History:                    (for Class)
		1.0.0 - Initial Release
        Docs: See README.md

"""
	def __init__(self,mode='3.2',back="ffffff",dothis=None):
		self.setMode(mode)
		self.setBack(back)
		self.page()
		self.setFuncs()
		self.resetLocals()
		self.resetGlobals()
		self.placeholder = 'Q|zXaH7RppY#32m' # hopefully you'll never use this string, lol
		self.styles = {}
		self.gstyles = {}
		self.stack = []
		if dothis != None:
			self.do(dothis)

	def resetGlobals(self):
		self.theGlobals = {}

	def resetLocals(self):
		self.theLocals = {}

	def htest(self,c):
		if type(c) != str:
			return False
		c = c.upper()
		for n in c:
			if n < '0' or n > 'F':
				return False
			if n > '9' and n < 'A':
				return False
		return True

	def mcolor(self,c):
		d = 'ffffff'
		if type(c) != str:
			c = d
		if len(c) == 3:
			c = c[0]+c[0] + c[1]+c[1] + c[2]+c[2]
		if len(c) != 6:
			c = d
		if self.htest(c) != True:
			c = d
		c = c.upper()
		return c

	def setBack(self,back="ffffff"):
		self.back = self.mcolor(back)

	def setMode(self,mode='3.2'):
		if type(mode) != str or mode != '3.2':
			mode = '4.01s'
		self.mode = mode

	def fetchVar(self,vName):
		lo = 1
		x = self.theLocals.get(vName,'')
		if x == '':
			lo = 0
			x = self.theGlobals.get(vName,'')
		return lo,str(x)

	def non_fn(self,tag,data):	# can't find the tag, so detail the problem
		return ' (Unknown Built-in or Squiggly:  tag="%s" data="%s") ' % (tag,data)

	def doTag(self,tag,data):
		tag = tag.lower()
		f = self.fns.get(tag,self.non_fn)
		return f(tag,data)

	def i_fn(self,tag,data):
		if self.mode == '3.2':
			return '<i>'+data+'</i>'
		else:
			return '<span style="font-style: italic;">%s</span>' % (data)

	def len_fn(self,tag,data):
		return str(len(data))

	def b_fn(self,tag,data):
		if self.mode == '3.2':
			return '<b>'+data+'</b>'
		else:
			return '<span style="font-weight: bold;">%s</span>' % (data)

	def u_fn(self,tag,data):
		if self.mode == '3.2':
			return '<u>'+data+'</u>'
		else:
			return '<span style="text-decoration: underline;">%s</span>' % (data)

	def s_fn(self,tag,data):
		o = ''
		try:
			da1,da2 = data.split(' ',1)
		except:
			da1 = data
			da2 = ''
		d1 = da1.split(',')
		ssiz = len(d1)
		if ssiz == 1:
			d2 = [da2]
		else:
			d2 = da2.split(',')
		dsiz = len(d2)
		if dsiz == ssiz:
			for i in range(0,ssiz):
				md1 = d1[i]
				md2 = d2[i]
				block = self.styles.get(md1,self.gstyles.get(md1,''))
				if block == '':
					o += tag+data
				else:
					block = block.replace('[b]',md2)
					res = self.do(block)
					o += res
		else:
			o += ' Macro error: Unmatched styleCount=%d and bodyListSize=%d (%s||%s) ' % (ssiz,dsiz,str(d1),str(d2))
		return o

	def glos_fn(self,tag,data):
		o = ''
		try:
			da1,da2 = data.split(' ',1)
		except:
			da1 = data
			da2 = ''
		d1 = da1.split(',')
		ssiz = len(d1)
		if ssiz == 1:
			d2 = [da2]
		else:
			d2 = da2.split(',')
		dsiz = len(d2)
		if dsiz == ssiz:
			for i in range(0,ssiz):
				md1 = d1[i]
				md2 = d2[i]
				block = self.gstyles.get(md1,'')
				if block == '':
					o += tag+data
				else:
					block = block.replace('[b]',md2)
					res = self.do(block)
					o += res
		else:
			o += ' Macro error: Unmatched styleCount=%d and bodyListSize=%d (%s||%s) ' % (ssiz,dsiz,str(d1),str(d2))
		return o

	def locs_fn(self,tag,data):
		o = ''
		try:
			da1,da2 = data.split(' ',1)
		except:
			da1 = data
			da2 = ''
		d1 = da1.split(',')
		ssiz = len(d1)
		if ssiz == 1:
			d2 = [da2]
		else:
			d2 = da2.split(',')
		dsiz = len(d2)
		if dsiz == ssiz:
			for i in range(0,ssiz):
				md1 = d1[i]
				md2 = d2[i]
				block = self.styles.get(md1,'')
				if block == '':
					o += tag+data
				else:
					block = block.replace('[b]',md2)
					res = self.do(block)
					o += res
		else:
			o += ' Macro error: Unmatched styleCount=%d and bodyListSize=%d (%s||%s) ' % (ssiz,dsiz,str(d1),str(d2))
		return o

	def iful_fn(self,tag,data):
		o = ''
		if data.find(',') != -1:
			entries = data.split(',')
			wraps = ''
			if len(entries) > 1:				# list supplied
				if entries[0][:5] == 'wrap=':	# if we have a wrapper
					wraps = entries[0][5:]		# extract the style name
					entries.pop(0)				# remove the wrapper
			if len(entries) > 1:				# if remaining date has more than one entry
				o += '<ul>\n'					# BUILD a list
				for en in entries:
					if wraps != '':
						en = self.s_fn('s','%s %s' % (wraps,en))	# wrap with style if called for
					o += '<li>%s</li>\n' % str(en)					# add list entry
				o += '</ul>\n'
			else: # had a wrapper, but a list isn't called for:
				if wraps != '':
					en = self.s_fn('s','%s %s' % (wraps,entries[0]))
				o += '%s<br>\n' % str(en)
		else: # list not supplied. Just dump data as-is
			o += data + '<br>'
		return o

	def ul_fn(self,tag,data):
		o = ''
		entries = data.split(',')
		wraps = ''
		if len(entries) > 1:				# list supplied
			if entries[0][:5] == 'wrap=':	# if we have a wrapper
				wraps = entries[0][5:]		# extract the style name
				entries.pop(0)				# remove the wrapper
		o += '<ul>\n'					# BUILD a list
		for en in entries:
			if wraps != '':
				en = self.s_fn('s','%s %s' % (wraps,en))	# wrap with style if called for
			o += '<li>%s</li>\n' % str(en)					# add list entry
		o += '</ul>\n'
		return o

	def t_fn(self,tag,data):
		o = ''
		plist = data.split(',')
		wraps = ''
		if plist[0][:5] == 'wrap=':
			wraps = plist[0][5:]
			plist.pop(0)
		for el in plist:
			if wraps != '':
				el = self.s_fn('s','%s %s' % (wraps,el))	# wrap with style if called for
			o += el
		return o

	def table_fn(self,tag,data):
		o = '<table'
		plist = data.split(',',1)
		if len(plist) == 1:
			o += '>\n'
			o += plist[0]
		elif len(plist) == 2: # table params
			params = plist[0].replace('&quot;','"')
			o += ' '+params
			o += '>\n'
			o += plist[1]
		else:
			return ' bad parameters for table '
		o += '</table>\n'
		return o

	def row_fn(self,tag,data):
		o = '<tr'
		plist = data.split(',',1)
		if len(plist) == 1:
			o += '>'
			o += plist[0]
		elif len(plist) == 2: # row params
			params = plist[0].replace('&quot;','"')
			o += ' '+params
			o += '>'
			o += plist[1]
		else:
			return ' bad parameters for row '
		o += '</tr>\n'
		return o

	def header_fn(self,tag,data):
		o = '<th'
		plist = data.split(',',1)
		if len(plist) == 1:
			o += '>'
			o += plist[0]
		elif len(plist) == 2: # header cell  params
			params = plist[0].replace('&quot;','"')
			o += ' '+params
			o += '>'
			o += plist[1]
		else:
			return ' bad parameters for header cell '
		o += '</th>'
		return o

	def cell_fn(self,tag,data):
		o = '<td'
		plist = data.split(',',1)
		if len(plist) == 1:
			o += '>'
			o += plist[0]
		elif len(plist) == 2: # table cell params
			params = plist[0].replace('&quot;','"')
			o += ' '+params
			o += '>'
			o += plist[1]
		else:
			return ' bad parameters for cell '
		o += '</td>'
		return o

	def ol_fn(self,tag,data):
		o = ''
		entries = data.split(',')
		wraps = ''
		if len(entries) > 1:				# list supplied
			if entries[0][:5] == 'wrap=':	# if we have a wrapper
				wraps = entries[0][5:]		# extract the style name
				entries.pop(0)				# remove the wrapper
		o += '<ol>\n'					# BUILD a list
		for en in entries:
			if wraps != '':
				en = self.s_fn('s','%s %s' % (wraps,en))	# wrap with style if called for
			o += '<li>%s</li>\n' % str(en)					# add list entry
		o += '</ol>\n'
		return o

	def ifol_fn(self,tag,data):
		o = ''
		if data.find(',') != -1:
			entries = data.split(',')
			wraps = ''
			if len(entries) > 1:				# list supplied
				if entries[0][:5] == 'wrap=':	# if we have a wrapper
					wraps = entries[0][5:]		# extract the style name
					entries.pop(0)				# remove the wrapper
			if len(entries) > 1:				# if remaining date has more than one entry
				o += '<ol>\n'					# BUILD a list
				for en in entries:
					if wraps != '':
						en = self.s_fn('s','%s %s' % (wraps,en))	# wrap with style if called for
					o += '<li>%s</li>\n' % str(en)					# add list entry
				o += '</ol>\n'
			else: # had a wrapper, but a list isn't called for:
				if wraps != '':
					en = self.s_fn('s','%s %s' % (wraps,entries[0]))
				o += '%s<br>\n' % str(en)
		else: # list not supplied. Just dump data as-is
			o += data + '<br>'
		return o

	def style_fn(self,tag,data):
		if data != '':
			try:
				d1,d2 = data.split(' ',1)
			except:
				return tag + data
			self.styles[d1] = d2
		return ''

	def gstyle_fn(self,tag,data):
		if data != '':
			try:
				d1,d2 = data.split(' ',1)
			except:
				return tag + data
			self.gstyles[d1] = d2
		return ''

	def color_fn(self,tag,data):
		o = ''
		try:
			d1,d2 = data.split(' ',1)
		except:
			return tag+data
		col = self.mcolor(d1)
		if self.mode == '3.2':
			o += '<font color="#%s">%s</font>' % (col,d2)
		else:
			o += '<span style="background-color: #%s; color: #%s;">%s</span>' % (self.back,col,d2)
		return o

	def img_fn(self,tag,macro):
		try:
			d1,d2 = data.split(' ',1)
		except:
			return '<center><img src="%s"></center>' % data
		return '<center><a href="%s" target="_blank"><img src="%s"></a></center>' % (d2,d1)

	def web_fn(self,tag,data):
		try:
			d1,d2 = data.split(' ',1)
		except:
			d1 = tag
			d2 = 'On The Web'
		return '<a href="%s" target="_blank">%s</a>' % (d1,d2)

	def link_fn(self,tag,data):
		try:
			d1,d2 = data.split(' ',1)
		except:
			d1 = tag
			d2 = tag
		return '<a href="%s" target="_blank">%s</a>' % (d1,d2)

	def co_fn(self,tag,data):
		return '&#44;'

	def sp_fn(self,tag,data):
		return '&#32;'

	def lb_fn(self,tag,data):
		return '&#91;'

	def rb_fn(self,tag,data):
		return '&#93;'

	def ls_fn(self,tag,data):
		return '&#123;'

	def rs_fn(self,tag,data):
		return '&#125;'

	def v_fn(self,tag,data):
		l,x = self.fetchVar(data)
		return x

	def lv_fn(self,tag,data):
		return self.theLocals.get(data,'')

	def gv_fn(self,tag,data):
		return self.theGlobals.get(data,'')

	def local_fn(self,tag,data):
		try:
			d1,d2 = data.split(' ',1)
		except:
			pass
		else:
			self.theLocals[d1]=d2
		return ''

	def clear_fn(self,tag,data):
		if data != '':
			self.theLocals[data] = ''
		return ' --> %s <-- ' % (data,)

	def pop_fn(self,tag,data):
		o = ''
		if len(self.stack) > 0:
			try:
				o = self.stack.pop()
			except:
				o = ''
		return o

	def flush_fn(self,tag,data):
		self.stack = []
		return ''

	def fetch_fn(self,tag,data):
		o = ''
		l = len(self.stack)
		if l == 0:
			return o
		try:
			n = int(data)
		except:
			n = 0
		if n < 0: n = 0
		if n < l:
			o = self.stack[-(n+1)]
		o += ' stack is %d, fetch was %d ' % (l,n)
		return o

	def push_fn(self,tag,data):
		if data != '':
			dats = data.split(',',1)
			if len(dats) == 1:
				r = 1
				dats += [data]
			else:
				try:
					r = int(dats[0])
				except:
					r = 1
			r -= 1
			if r < 0: r = 0
			self.stack.append(dats[1])
			if r != 0:
				for i in range(0,r):
					self.stack.append('')
		return ''

	def global_fn(self,tag,data):
		try:
			d1,d2 = data.split(' ',1)
		except:
			pass
		else:
			self.theGlobals[d1]=d2
		return ''

	def page_fn(self,tag,data):
		self.theLocals = {}
		return ''

	def ne_fn(self,tag,data):
		o = ''
		dlist = data.split(',',1)
		if len(dlist) == 2:
			if dlist[0] != '':
				o = dlist[1]
		return o

	def ifelse_fn(self,tag,data):
		o = ''
		try:
			d1,d2,d3 = data.split(' ',2)
			if tag == 'if':
				if d1 == d2:
					o += d3
			else:
				if d1 != d2:
					o += d3
		except:
			pass
		return o

	def repeat_fn(self,tag,data):
		o = ''
		try:
			d1,d2 = data.split(' ',1)
			if d1[:2] == '[v' or d1[:3] == '[gv':
				accum = ''
				run = 1
				skip = 1
				d2 = ''
				for c in data:
					if run == 1:
						accum += c
						if c == ']':
							run = 2
					else:
						if skip == 1:
							skip = 0
						else:
							d2 += c
				d1 = self.do(accum) # parse the variable
			x = abs(int(d1))
		except:
			pass
		else:
			for i in range(0,x):
				o += self.do(d2)
		return o

	def evenodd_fn(self,tag,data):
		o = ''
		try:
			d1,d2 = data.split(' ',1)
			x = int(d1)
		except:
			pass
		else:
			z = 1
			if tag == 'even':
				z = 0
			if x & 1 == z:
				o += d2
		return o

	def math_fn(self,tag,data):
		o = ''
		try:
			if tag == 'add' or tag == 'sub' or tag == 'div' or tag == 'mul':
				d1,d2 = data.split(' ',1)
			else:
				d1 = data
				d2 = '1'
			d2 = int(d2)
			x = int(d1)
		except:
			pass
		else:
			if tag == 'add' or tag == 'inc':
				x = str(x + d2)
			elif tag == 'mul':
				x = str(x * d2)
			elif tag == 'div':
				try:
					x = str(int(x / d2))
				except:
					x = '0'
			else: # sub or dec
				x = str(x - d2)
			o += x
		return o

	def setFuncs(self): #    '':self._fn,
		self.fns = {
					# escape codes
					# ------------
					'co'	: self.co_fn,		#	,	comma
					'sp'	: self.sp_fn,		#	,	space
					'lb'	: self.lb_fn,		#	[	left square bracket
					'rb'	: self.rb_fn,		#	]	right square bracket
					'ls'	: self.ls_fn,		#	{	left brace
					'rs'	: self.rs_fn,		#	}	right brace

					# basic text formatting
					# ---------------------
					'color'	: self.color_fn,	# P1=HHH or HHHHHH then P2 is what gets colored
					'i'		: self.i_fn,		# P1 is italicized
					'b'		: self.b_fn,		# P1 is bolded
					'u'		: self.u_fn,		# P1 is underlined

					# list handling
					# P1[,P2]...[,Pn]
					# P1 can optionally be [wrap=STYLE,] for all of these
					# ---------------------------------------------------
					'ol'	: self.ol_fn,		# ordered list, all elements numbered even if just one
					'ul'	: self.ul_fn,		# unordered list, all elements bulleted even if just one
					'ifol'	: self.ifol_fn,		# ordered list IF more than one element, otherwise not a list
					'iful'	: self.iful_fn,		# unordered list IF more than one element, otherwise not a list
					't'		: self.t_fn,		# [t wrap=STYLE,P2,P3...,Pn]

					# HTML tables
					# -----------
					'table' : self.table_fn,	# [table (params,)CONTENT]
					'row'   : self.row_fn,		# [row (params,)CONTENT]
					'header': self.header_fn,	# [header (params,)CONTENT]]
					'cell'  : self.cell_fn,		# [cell (params,)CONTENT]]

					# Internet interfacing
					# --------------------
					'link'	: self.link_fn,		# link URL (text) if no text, then linked URL
					'web'	: self.web_fn,		# link URL (text) if no text, the "On the Web"
					'img'	: self.img_fn,		# img emplacement from URL

					# math
					# ----
					'add'	: self.math_fn,		# P1 + P2
					'sub'	: self.math_fn,		# P1 - P2
					'mul'	: self.math_fn,		# P1 * P2
					'div'	: self.math_fn,		# P1 / P2
					'inc'	: self.math_fn,		# P1 + 1
					'dec'	: self.math_fn,		# P1 - 1
					'len'	: self.len_fn,		# length(P1)

					# conditionals
					# ------------
					'if'	: self.ifelse_fn,	# if P1 == P2 then P3
					'else'	: self.ifelse_fn,	# if P1 != P2 then P3
					'even'	: self.evenodd_fn,	# if P1 even then P2
					'odd'	: self.evenodd_fn,	# if P1 odd then P2
					'ne'	: self.ne_fn,		# if P1 non-empty,P2 (p1,p2)

					# variable handling
					# -----------------
					'local'	: self.local_fn,	# define local variable:					P1 <-- P2
					'vs'	: self.local_fn,	# "     ditto         "						P1 <-- P2
					'global': self.global_fn,	# define global variable					P1 <-- P2
					'page'	: self.page_fn,		# clear local variables
					'gv'	: self.gv_fn,		# use global variable						P1 -->
					'lv'	: self.lv_fn,		# use local variable						P1 -->
					'v'		: self.v_fn,		# use local variable. if none, use global	P1 -->
					'clear'	: self.clear_fn,	# clear a local variable					'' -> P1

					# stack
					# -----
					'pop'	: self.pop_fn,		# pop a value from the stack
					'push'	: self.push_fn,		# push a value onto the stack
					'fetch'	: self.fetch_fn,	# fetch from stack by index, no pop
					'flush'	: self.flush_fn,	# flush entire stack immediately

					# style handling
					# --------------
					'gstyle': self.gstyle_fn,	# define a global style
					'style'	: self.style_fn,	# define a local style
					's'		: self.s_fn,		# local style, or if none, global style
					'glos'	: self.glos_fn,		# global style
					'locs'	: self.locs_fn,		# local style

					# Miscellaneous
					# -------------
					'repeat': self.repeat_fn,	# N ThingToBeRepeated
		}

	def do(self,s):
		if type(s) != str:
			return ''
		inout = 0
		o = ''
		OUT = 0
		IN = 1
		DEFER = 2
		depth = 0
		state = OUT
		macstack = []
		s = s.replace('{','[s ')
		s = s.replace('\r','')
		s = s.replace('\n',' ')
		dex = -1
		tag = ''
		for c in s:
			if c == '}': c = ']'
			dex += 1
			if state == OUT and c == '[':
				if s[dex:dex+7] == '[style ' or s[dex:dex+8] == '[repeat ':
					state = DEFER
					depth = 1
					tag = ''
				else:
					state = IN
					tag = ''
					data = ''
			elif state == DEFER:
				if c == '[':
					tag += c
					depth += 1
				elif c == ']':
					depth -= 1
					if depth == 0:
						if tag.find(' ') > 0:
							tag,data = tag.split(' ',1)
							o += self.doTag(tag,data)
							state = OUT
					else:
						tag += c
				else:
					tag += c
			elif state == IN and c == ']':
				if tag.find(' ') > 0:
					tag,data = tag.split(' ',1)
				fx = self.doTag(tag,data)
				if len(macstack) == 0:
					o += fx
					state = OUT
				else:
					tag = macstack.pop()
					tag += fx
			elif state == IN:
				if c == '[': # nesting
					macstack.append(tag)
					tag = ''
				else:
					tag += c
			else:
				o += c
		return o

	def page(self):
		self.styles = {}

	# modes are: html, text, table
	def localLib(self,mode='text',border=1):
		maxl = 0
		for key in sorted(self.theLocals.keys()):
			ll = len(key)
			if ll > maxl: maxl = ll
		s = ''
		ending = '\n'
		pre = ''
		post = ''
		fmt = '%%%ds : %%s%%s' % (maxl,)
		if mode == 'html':
			ending = '<br>\n'
		elif mode == 'table':
			pre  = '<table border=%s>\n' % (str(border),)
			pre += '<tr><th>Local</th><th>Content</th></tr>\n'
			post = '</table>\n'
			fmt = '<tr><td align="right">%s</td><td>%s%s</td></tr>\n'
			ending = ''
		s += pre
		for key in sorted(self.theLocals.keys()):
			rawsty = self.theLocals[key]
			rawsty = rawsty.replace('\n','\\n')
			s += fmt % (key,rawsty,ending)
		s += post
		return s


	# modes are: html, text, table
	def globalLib(self,mode='text',border=1):
		maxl = 0
		for key in sorted(self.theGlobals.keys()):
			ll = len(key)
			if ll > maxl: maxl = ll
		s = ''
		ending = '\n'
		pre = ''
		post = ''
		fmt = '%%%ds : %%s%%s' % (maxl,)
		if mode == 'html':
			ending = '<br>\n'
		elif mode == 'table':
			pre  = '<table border=%s>\n' % (str(border),)
			pre += '<tr><th>Global</th><th>Content</th></tr>\n'
			post = '</table>\n'
			fmt = '<tr><td align="right">%s</td><td>%s%s</td></tr>\n'
			ending = ''
		s += pre
		for key in sorted(self.theGlobals.keys()):
			rawsty = self.theGlobals[key]
			rawsty = rawsty.replace('\n','\\n')
			s += fmt % (key,rawsty,ending)
		s += post
		return s


	# modes are: html, text, table
	def styleLib(self,mode='text',border=1):
		maxl = 0
		for key in sorted(self.styles.keys()):
			ll = len(key)
			if ll > maxl: maxl = ll
		s = ''
		ending = '\n'
		pre = ''
		post = ''
		fmt = '%%%ds : %%s%%s' % (maxl,)
		if mode == 'html':
			ending = '<br>\n'
		elif mode == 'table':
			pre  = '<table border=%s>\n' % (str(border),)
			pre += '<tr><th>Style</th><th>Content</th></tr>\n'
			post = '</table>\n'
			fmt = '<tr><td align="right">%s</td><td>%s%s</td></tr>\n'
			ending = ''
		s += pre
		for key in sorted(self.styles.keys()):
			rawsty = self.styles[key]
			rawsty = rawsty.replace('\n','\\n')
			s += fmt % (key,rawsty,ending)
		s += post
		return s

if __name__ == "__main__":
	test  = ''

	# built-ins
	# ---------
	test += 'this is a [b bold [i bold-italic]] [i italic] test.\n'
	test += 'this is [color 00F blue text]\n'
	test += 'and this is [color ff8844 orange text.]\n'
	test += "I'd like to [u underline this text.]\n"
	mod = macro()							# Defaults to HTML 3.2 color generation, foreground only.
	print 'Example 1'
	print mod.do(test)						# You can use tables or page backdrop color to set background in HTML 3.2

	mod.setMode('4.01s')					# HTML 4.01 strict uses CSS, and sets the background color too.
	print 'Example 2'
	print mod.do(test)						# Which defaults to white, but you can set it after instantiation:

	mod.setBack('00f')						# 3 or 6 hex chars in upper, lower or mixed case, are okay
	print 'Example 3'
	print mod.do(test)						# if you were in HTML 3.2 mode, back color is not used

	mod.setBack()							# the default is a white background, white also used if color pathological
	mod = macro(mode='4.01s',back='f0f')	# You can set mode and back color at the start
	print 'Example 4'
	print mod.do(test)						# or you can set at start, then change at any time.

	# styles:
	# -------
	test  = ''
	mod = macro()
	test += '[style says I say [b] sometimes]'				# define a style called "says" which applies to [b]
	test += '[style hysterical [b [i [color 0f0 [b]]]]]'	# define another style
	test += '[style thrice [b], [b], [b]]'					# repeat use of body
	test += '[s says heck with it]\n'						# use "says" style
	test += 'This is [s hysterical silly formatting]\n'		# use "hysterical" style
	test += '[s hysterical [s says [u mutter], mutter]]\n'	# and again, plus more nested stuff
	test += 'Three times I say: [s thrice mutter].\n'		# use thrice style
	print 'Example 5'
	print mod.do(test)

	test  = ''
	test += '[repeat 3 three times [s says [i foo]]\n]'		# shows how to use repeat
	test += '[global count 5]'
	test += '[local count 20]'								# set a local variable named "count" to 5
	test += '[repeat [v count] x]\n'						# now repeat using the local, which has priority
	test += '[repeat [gv count] y]\n'						# now repeat using the global

	# Remember things get processed from the inside out. It might help
	# to read the comments from bottom to top, right to left. There are
	# three things happening here.
	#     1: A variable is incremented
	#     2: Variable is checked for odd and if so, then output 'red\n'
	#     3: Variable is checked for even and if so, then output 'green\n'
	#
	# Refer to lines A and B below the style as I mention A and B:
	#
	#        +-- create style command
	#        |      +-- name of the style
	#        |      |       +-- resolves to [local x [inc v x]]      1: x = variable x + 1
	#        |      |       |      +-- resolves to x
	#        |      |       |      |   +-- resolves to [inc [v x]]]
	#        |      |       |      |   |    +-- resolves to [v x]
	#        |      |       |      |   |    |  +-- resolves to x
	#        |      |       |      |   |    |  |     +-- resolves to [odd x red\n] 2: if x odd, output 'red\n'
	#        |      |       |      |   |    |  |     |    +-- resolves to [v x]
	#        |      |       |      |   |    |  |     |    |  +-- resolves to x
	#        |      |       |      |   |    |  |     |    |  |    +-- 'red\n'
	#        |      |       |      |   |    |  |     |    |  |    |     +-- resolves to [even x green\n]] 3: if x even, output 'green\n'
	#        |      |       |      |   |    |  |     |    |  |    |     |     +-- resolves to [v x]
	#        |      |       |      |   |    |  |     |    |  |    |     |     |  +-- resolves to x
	#        |      |       |      |   |    |  |     |    |  |    |     |     |  |    +-- 'green\n
	#        |      |       |      |   |    |  |     |    |  |    |     |     |  |    |
	test += '[style oecolor [local [b] [inc [v [b]]]][odd [v [b]] red\n][even [v [b]] green\n]]'
	test += '[local x 0]'					# line A -- simply setting x to zero to start with
	test += '[repeat 5 [s oecolor x]]'		# line B -- now using the style 5 times via repeat

	test += '[s oecolor x]'
	test += '[s oecolor x]'
	test += '[s oecolor x]'
	test += '[s oecolor x]'
	test += '[local x 5]'
	test += '[inc x]'
	test += '[v x]'
	print 'Example 6'
	print mod.do(test)

	# let's do some math:
	# -------------------
	test  = ''
	test += '5 x 4 = [mul 5 4]\n'
	test += '[local X 6][local Y 2]'
	test += 'X=[v X] Y=[v Y]\n'
	test += 'X / Y = [div [v X] [v Y]]\n'
	test += 'Z = X * Y:\n'
	test += '[local Z [mul [v X] [v Y]]]'
	test += 'Z = [v Z]\n'
	print 'Example 7'
	print mod.do(test)

	# So, you may be thinking, gee, this is all somewhat indirect. This is true. However,
	# there's a reason, and if you think about it, it'll make sense to you. It's like a
	# RISC computer instuction set. It's minimal, but what is here was carefully chosen
	# to allow other things to be created from it. For instance, let's cook up a style
	# that directly decrements a local variable:
	# ------------------------------------------------------------------------------------
	test  = ''
	test += '[style decrement [local [b] [dec [v [b]]]]]'
							# ok, now let's test it:
	test += '[local q 5]'	# assign 5 to variable named "q"
	test += '{decrement q}'	# decrement it (could also have written [s decrement q] )]
							# {} is just an easier and more obvious way to use a style
	test += 'q=[v q]'		# and bring the contents into the output stream
	print 'Example 8'
	print mod.do(test)		# prints 'q=4'

	# Some simple, practical HTML
	# ---------------------------
	test  = ''
	test += '[style greetings '
	test += 'Welcome to the webserver, [i [b]]'
	test += ']'
	test += '{greetings Floyd}'
	print 'Example 9'
	print mod.do(test)

	# Been using the object a bit. Here is the current object state:
	# --------------------------------------------------------------
	pmode = 'text'	# 'text' | 'html' | 'table' -- try each one
	print
	print mod.styleLib(pmode)
	print mod.localLib(pmode)
	print mod.globalLib(pmode)

	# You can reset the styles two ways:
	# ----------------------------------
	mod.do('[page]')	# directly from the text stream
	mod.page()			# by asking the object to do it

	# There are also ways to reset the locals and the globals:
	# You'd reset the locals on a page by page basis, while
	# the globals stay there across multipage documents.
	# --------------------------------------------------------
	mod.resetLocals()
	mod.resetGlobals()

	# If you're going to use aa_macro.py as the core of a document processing
	# system, as I do, you'll want to process things in page-sized chunks.
	# So that's the reason for that. Of course, you can instantiate an object
	# for each page... but that sort of misses the point.

	# let's make a HTML 3.2 table:
	test = '[table [row [cell test1][cell test2]]]'
	print 'Example 10'
	print mod.do(test)


	# again, but with a header row. I'll break the process out on multiple lines,
	# but of course it's no different than doing it all in one line, other than
	# being easier to comprehend:
	test  = '[table '
	test += '[row [header col 1][header col 2]]'
	test += '[row [cell test1][cell test2]]'
	test += ']'
	print 'Example 11'
	print mod.do(test)

	# another, but with some table, row and cell options
	test  = '[table border=1,'
	test += '[row bgcolor="ffffdd",[header col 1][header col 2]]'
	test += '[row [cell align="center",test1][cell align="right",test2]]'
	test += ']'
	print 'Example 12'
	print mod.do(test)

	# let's cook up alternating line colors and a row counter:
	test  = ''
	test += '[local c1 bgcolor="#ffddff"]'
	test += '[local c2 bgcolor="#ddddff"]'
	test += '[style ac [local c [inc [v c]]][odd [v c] [v c1]][even [v c] [v c2]]]'
	test += '[style rc [cell align="right",[v c]]]'

	# ok, thats all we we need. Here's a table with four lines:
	test += '[local c 0]'
	test += '[table border=1,'
	test += '[row bgcolor="#ffffff",[header Row #][header Col 1][header Col 2]]'
	test += '[row {ac},{rc}[cell a][cell b]]'
	test += '[row {ac},{rc}[cell c][cell d]]'
	test += '[row {ac},{rc}[cell e][cell f]]'
	test += '[row {ac},{rc}[cell g][cell h]]'
	test += ']'
	print 'Example 13'
	print mod.do(test)

	# 'table' and 'cell' and 'header' and 'row' too wordy for you? Fine:
	test  = ''
	test += '[style ta [table [b]]]'
	test += '[style tr [row [b]]]'
	test += '[style td [cell [b]]]'
	test += '[style th [header [b]]]'

	test += '{ta {tr {td cell 1}{td cell 2}}}'
	print 'Example 14'
	print mod.do(test)

	# why stop there? lets go absolutely minimalist:
	test  = ''
	test += '[style t [table [b]]]'
	test += '[style r [row [b]]]'
	test += '[style d [cell [b]]]'
	test += '[style h [header [b]]]'

	test += '{t {r {d cell one}{d cell two}}}'
	print 'Example 15'
	print mod.do(test)

	# can we make that even simpler? Yes, with just a few short styles:

	test  = ''
	test += '[style t [table [b]]]'
	test += '[style mcell [cell [b]]]'
	test += '[style mhdr [header [b]]]'
	test += '[style h [row [t wrap=mhdr,[b]]]]'
	test += '[style w [row [t wrap=mcell,[b]]]]'

	test += '{t {w one,two}}'
	print 'Example 16'
	print mod.do(test)

	# several rows with a header
	# this uses above-defined styles t, h and w.
	test  = ''
	test += '{t '
	test += '{h Col 1,Col 2}'
	test += '{w one,two}'
	test += '{w three,four}'
	test += '}'
	print 'Example 17'
	print mod.do(test)

	# finally, let's incorporate row count and coloring techniques from above
	# This utilizes styles t, c1, c2, ac, rc, mcell, mhdr and re-defines h and w

	# Notice the use of both [t STUFF] and {t STUFF} here; the namespaces of the
	# built-in capabilities and user-defined styles are entirely independent
	# [t STUFF] is intended to wrap comma-separated items with a style;
	# {t STUFF} is a style defined just previously that instantiates a table.

	test  = ''
	test += '[style w [row {ac},{rc}[t wrap=mcell,[b]]]]'
	test += '[style h [row bgcolor="#ffffff",[t wrap=mhdr,[b]]]]'

	# Because the rows automatically contain an "extra" count cell,
	# the header needs a third entry; that's why it has three cells,
	# whereas the rows only require two:

	test += '[local c 0]'				# initialize the row counter
	test += '{t border=2,'				# open a table with a thick border
	test += '{h Row #,Col 1,Col 2}'		# here's the header row
	test += '{w one,two}'				# a data row
	test += '{w three,four}'			# another data row
	test += '}'							# close the table
	print 'Example 18'
	print mod.do(test)

