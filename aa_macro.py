#!/usr/bin/python

import re

class macro(object):
	"""Class to provide an HTML macro language
      Author: fyngyrz  (Ben)
     Contact: fyngyrz@gmail.com (bugs, feature requests, kudos, bitter rejections)
     Project: aa_webpage.py
	 License: None. It's free. *Really* free. Defy invalid social and legal norms.
  Disclaimer: Probably completely broken. Do Not Use. You were explicitly warned. Pbbbbt.
  Incep Date: June 17th, 2015     (for Project)
     LastRev: July 28th, 2015     (for Class)
  LastDocRev: July 28th, 2015     (for Class)
 Tab spacing: 4 (set your editor to this for sane formatting while reading)
    Examples: At bottom. Run in shell like so:    python aa_macro.py
              The best way to use them is open a shell and run them there,
			  and open a shell with aa_macro.py in an editor or reader,
			  then scroll through the example results in the one shell as
			  you peruse the source for them in the other within aa_macro.py
 Typical Use: from aa_macro import *
     Warning: Do NOT use this to parse general user input without fully sanitizing that
	          input for subsequent string processing in Python FIRST, as well as for
			  output via your webserver (because <script>, etc.) Otherwise, you've
			  just created a huge security hole. Not Good! As it stands as of 1.0.5,
			  class macro() is for authoring by you, the person who ISN'T trying to
			  hack your website, not access to the public, which may very well contain
			  someone who wants to do you wrong.
     1st-Rel: 1.0.0
     Version: 1.0.5
     History:                    (for Class)
	 	1.0.5
			* added warning about parsing user input
			* wrote a walkthrough for generating roman numerals, consequently I...
			* added [upper textString]
			* added [lower textString]
			* added [roman numberString]
	 	1.0.4
			* added advice on how to use examples
	    1.0.3
			* spiffied up the class docs a little
			* added [split splitSpec,contentToSplit]
			* added [parm N]
			* added to examples
	 	1.0.2
			* added new URL link mechanism [a (tab,)URL(,LinkedText)]
				[link] and [web] will remain as per my "I will never
				take away something you may have used" policy, but
				[a] is really a better way to go about it now.
			* added escape for all commas [nc TextToBeEscaped]
			* added non-rendering [comment content] capability
			* added [slice sliceSpec,contentToSlice] capability
	 	1.0.1
			* added HTML paragraphs as [p paragraph]
		1.0.0
			* Initial Release

	Available macros:
	=================
	Note that () designate optional parameters, a|b designates alternate parameter a or b

	Text Styling
	------------
	[p paragraph]
	[b bold text]
	[i italic text]
	[u underlined text]
	[color HEX3|HEX6 colored text]	# HEX3 example: f09 (which means FF0099) HEX6 example: fe7842
	
	Linking
	-------
	[a (tab,)URL(,linked text)]		# The WORD tab, not a tab character. As in a browser tab
	
	Older Linking (will remain, but [a URL] is better)
	--------------------------------------------------
	[web URL (text)]				# If you don't provide text, you get "On the web"
	[link URL (text)]				# If you don't provide text, you get the URL as the text
	
	Images
	------
	[img URL]
	
	Lists
	-----
	[ul item1(,item2,item3...)]		where item1 can be wrap=STYLE
	[ol item1(,item2,item3...)]		where item1 can be wrap=STYLE
	[iful item1(,item2,item3...)]	where item1 can be wrap=STYLE
	[ifol item1(,item2,item3...)]	where item1 can be wrap=STYLE
	[t item1(,item2,item3...)]		Where item1 may be wrap=STYLE

	Tables
	------
	[table (options,)CONTENT]						HTML table
	[row (options,)CONTENT]							table ROW
	[header (options,)CONTENT]						table header cell
	[cell (options,)CONTENT]						table cell

	Variables
	---------
	[local variableName value]						# define a variable in the local environment
	[vs variableName value]							# ditto - same as local
	[global variableName value]						# define a variable in the global environment
	[v variableName]								# use a variable (local, if not local, then global)
	[gv variableName]								# use the global variable and ignore the local
	[lv variableName]								# use the local variable and ignore the global
	[page]											# reset local environment

	Stack
	-----
	[push (N,)CONTENT]								# push CONTENT N deep onto stack. 1 is the same as no N.
	[pop]											# pop stack. If stack empty, does nothing.
	[fetch (N)]										# get element N from stack but no pop. 0 is top, no N = 0
	[flush]											# toss out entire stack

	Math
	----
	[add value addend]								# add a number to a number
	[sub value subtrahend]							# subtract a number from a number
	[mul value multiplier]							# multiply a number by a number
	[div value divisor]								# divide a number by a number
	[inc value]										# add one to a number
	[dec value]										# subtract one from a number
	
	Conditionals
	------------
	[even value conditionalContent]					# use conditional content if value is even
	[odd value conditionalContent]					# use conditional content if value is odd
	[if value match conditionalContent]				# use conditional content if value == match
	[else value match conditionalContent]			# use conditional content if value != match
	[ne value,conditionalContent]					# use conditional content if value Not Empty
	
	Misc
	----
	[repeat count content]							# repeat content count times
	[comment content]								# content does not render
	[slice sliceSpec,contentToSlice]				# [slice 3:6,foobarfoo] = bar ... etc.
	[split splitSpec,contentToSplit]				# [split |,x|y|z] results in parms 0,1,2
	[parm N]										# per above [split, [parm 1] results in y
	[upper textString]								# convert to uppercase
	[lower textString]								# convert to lowercase
	[roman numberString]							# convert decimal to roman (1...4000)
	
	Escape Codes:
	-------------
	[co]							# produces HTML ',' as &#44;
	[sp]							# produces HTML ' ' as &#32;
	[lb]							# produces HTML '[' as &#91;
	[rb]							# produces HTML ']' as &#93;
	[ls]							# produces HTML '{' as &#123;
	[rs]							# produces HTML '}' as &#125;
	
	Styles
	------
	[style styleName Style]			# Defines a local style. Use [b] for body of style (see [s] tag, next)
	[gstyle styleName]				# Defines a global style. Use [b] for body of style (see [s] tag, next)
	[s styleName contentToStyle]	# contentToStyle goes where [b] tag(s) is/are in style...
	[glos styleName contentToStyle]	# contentToStyle goes where [b] tag(s) is/are in style...
	[locs styleName contentToStyle]	# contentToStyle goes where [b] tag(s) is/are in style...
	{styleName contentToStyle}		# ...same thing, but simplified "squiggly" syntax
	==> Only if crtospace is True:
	{styleNameCRcontentToStyle}		# ...same thing, but simplified "squiggly" syntax
									# CR is a newline
	
	More on styles:
	---------------
	Styles give you ultimate power in creating your own text processing tool.

	Styles are pretty easy to understand. You can have as many as you want, and they
	can contain other styles, presets and so on. There are two components to styles;
	defining them, and using them.
	
	Here's a simple style definition:

         +-- DEFINE a style
         |     +-- name of style
         |     |      +-- beginning of style
         |     |      |       +-- where the body of the style will go
         |     |      |       |  +-- rest of pre-defined style
         |     |      |       |  |       +-- end of style
         |     |      |       |  |       |
		[style strike <strike>[b]</strike>]

	So now to use that, you do this:

         +-- USE a style
         | +-- name of style to use
         | |      +-- the body that goes where the [b] tag(s) is/are in the style
         | |      |
		[s strike me out]

	Which will come out of object.do() as:

		<strike>me out</strike>

	You can nest more or less indefinitely:
	---------------------------------------
	[b bold text [s strike [i bold and italic text]]]

	The Rules:
	----------
	o Do not attempt to define one style inside another.
	o Style names may contain anything but a space or a newline
	o repeat gets a number or a variable parameter. Nothing else. No nesting in the parameter!
	  (but you can use anything in what you want it to repeat)
	o Give me a space or a newline. One space or newline only, Vasily.
	  Between the tag and any parameters, that is
	o observe the format for tags. Some require spaces, some commas, to separate items.
	  or suffer the consequences, which will be aborted macros. :)
	  FYI: Generally commas are used for variable numbers of parameters.
	o You can use [co] for literal commas, likewise [lb] [rb] [ls] and [rs] for literal braces.
	  Any operation that uses a comma for parameters or optional parameters is looking
	  for commas, so use [co] in the content of anything you feed to them. Else format=yuck
	  Also see [nc contentToConvertCommasIn], which is a hany way to see to it that your
	  content can have commas, but the macro system won't see them. Of course, you can't
	  use that on anything that *needs* commas for parameters. Life is so complicated. :)

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
		self.parms = []
		self.romans = ['m','cm','d','cd','c','xc','l','xl','x','ix','v','iv','i']
		self.integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
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

	def p_fn(self,tag,data):
		return '<p>'+data+'</p>'

	def len_fn(self,tag,data):
		return str(len(data))

	def b_fn(self,tag,data):
		if self.mode == '3.2':
			return '<b>'+data+'</b>'
		return '<span style="font-weight: bold;">%s</span>' % (data)

	def split_fn(self,tag,data):
		o = ''
		dl = data.split(',',1)
		if len(dl) == 2:
			if str(dl[0]) == '&#44;':
				self.parms = str(dl[1]).split(',')
			else:
				self.parms = str(dl[1]).split(str(dl[0]))
		else:
			o = ' ?split? '
		return o

	def parm_fn(self,tag,data):
		o = ''
		try:
			o = self.parms[int(data)]
		except:
			pass
		return o

	def slice_fn(self,tag,data):
		o = ''
		plist = data.split(',',1)
		if len(plist) == 2:
			try:
				slist = plist[0].split(':')
				if len(slist) == 1:
					o = str(plist[1])[int(slist[0])]
				elif len(slist) == 2:
					a = None
					b = None
					if slist[0] != '': a = int(slist[0])
					if slist[1] != '': b = int(slist[1])
					o = str(plist[1])[a:b]
				elif len(slist)==3:
					a = None
					b = None
					c = None
					if slist[0] != '': a = int(slist[0])
					if slist[1] != '': b = int(slist[1])
					if slist[2] != '': c = int(slist[2])
					o = str(plist[1])[a:b:c]
				else:
					o = ' ?split? '
			except:
				pass
#		print o
		return o

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

	def nc_fn(self,tag,data):
		return data.replace(',','&#44;')

	def a_fn(self,tag,data):
		o = ''
		dlist = data.split(',')
		llen = len(dlist)
		if llen == 1:	# "URL"
			o = '<a href="%s">%s</a>' % (dlist[0],dlist[0])
		elif llen == 2:	# "tab,URL"
			if dlist[0].lower() == 'tab':
				o = '<a target="_blank" href="%s">%s</a>' % (dlist[1],dlist[1])
			else:
				o = '<a href="%s">%s</a>' % (dlist[0],dlist[1])
		elif llen == 3:	# "tab,URL,LinkedText"
			o = '<a target="_blank" href="%s">%s</a>' % (dlist[1],dlist[2])
		return o

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

	def comment_fn(self,tag,data):
		return ''

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

	def lower_fn(self,tag,data):
		return data.lower()

	def upper_fn(self,tag,data):
		return data.upper()

	def roman_fn(self,tag,data):
		o = ''
		try:    number = int(data)
		except: pass
		else:
			if number > -1 and number < 4001:
				for v in range(0,13):
					ct = int(number / self.integers[v])
					o += self.romans[v] * ct
					number -= self.integers[v] * ct
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
					'p'		: self.p_fn,		# P1 is an HTML pargraph

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
					'a'		: self.a_fn,		# [a (tab,)URL(,LinkedText)]
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
					'nc'	: self.nc_fn,		# [nc TEXT] escape all commas
					'comment': self.comment_fn, # contained content will not render
					'slice'	: self.slice_fn,	# [slice sliceSpec,textToSlice]
					'split'	: self.split_fn,	# [split splitSpec,testToSplit]
					'parm'	: self.parm_fn,		# [parm N] where N is 0...n of split result
					'upper'	: self.upper_fn,	# [upper textString]
					'lower'	: self.lower_fn,	# [lower textString]
					'roman'	: self.roman_fn,	# [roman numberString]
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

		# This is a bit gnarly; first, I replace "{" with "[s " as "{"
		# is simply a shorthand for a style invocation. Then I allow
		# for the syntax of separating the invocation of a style from
		# its paramter(s) with either a space or a newline, by converting
		# the newlines used this way into a space so as to simplify
		# subsequent processing. I expected to use \[ in the first param,
		# as it is a literal search for '[s ' at that point, but the
		# the re import module doesn't seem to see things that way. Weird.
		# ----------------------------------------------------------------
		s = s.replace('{','[s ')
		s = re.sub(r'([s\s[\w-])\n',r'\1 ',s)

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
	def xprint(s):
		print s
		print '-' * len(s)

	test  = ''
	
	# built-ins
	# ---------
	test += 'this is a [b bold [i bold-italic]] [i italic] test.\n'
	test += 'this is [color 00F blue text]\n'
	test += 'and this is [color ff8844 orange text.]\n'
	test += "I'd like to [u underline this text.]\n"
	mod = macro()							# Defaults to HTML 3.2 color generation, foreground only.
	xprint('Example 1 -- using built-ins, HTML 3.2 assumption')
	print mod.do(test)						# You can use tables or page backdrop color to set background in HTML 3.2

	mod.setMode('4.01s')					# HTML 4.01 strict uses CSS, and sets the background color too.
	xprint('Example 2 -- HTML 4.01 compatible color generation, plus background color')
	print mod.do(test)						# Which defaults to white, but you can set it after instantiation:

	mod.setBack('00f')						# 3 or 6 hex chars in upper, lower or mixed case, are okay
	xprint('Example 3 -- background color gsetting for HTML 4.01s')
	print mod.do(test)						# if you were in HTML 3.2 mode, back color is not used

	mod.setBack()							# the default is a white background, white also used if color pathological
	mod = macro(mode='4.01s',back='f0f')	# You can set mode and back color at the start
	xprint('Example 4 -- setting mode and color at object instantiation')
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
	xprint('Example 5 -- basic style demonstration')
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
	xprint('Example 6 -- alternating operations')
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
	xprint('Example 7 -- doing math')
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
	xprint('Example 8 -- operating upon variables (decrement example)')
	print mod.do(test)		# prints 'q=4'

	# Some simple, practical HTML
	# ---------------------------
	test  = ''
	test += '[style greetings '
	test += 'Welcome to the webserver, [i [b]]'
	test += ']'
	test += '{greetings Floyd}'
	xprint('Example 9 -- simple example using HTML built-ins')
	print mod.do(test)

	# Been using the object a bit. Here is the current object state:
	# --------------------------------------------------------------
	pmode = 'text'	# 'text' | 'html' | 'table' -- try each one
	xprint('Example 9B -- object state')
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
	xprint('Example 10 -- basic HTML table')
	print mod.do(test)
	

	# again, but with a header row. I'll break the process out on multiple lines,
	# but of course it's no different than doing it all in one line, other than
	# being easier to comprehend:
	test  = '[table '
	test += '[row [header col 1][header col 2]]'
	test += '[row [cell test1][cell test2]]'
	test += ']'
	xprint('Example 11 -- table header row')
	print mod.do(test)

	# another, but with some table, row and cell options
	test  = '[table border=1,'
	test += '[row bgcolor="ffffdd",[header col 1][header col 2]]'
	test += '[row [cell align="center",test1][cell align="right",test2]]'
	test += ']'
	xprint('Example 12 -- optional settings for cells and tables')
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
	xprint('Example 13 -- table with alternating line characteristics')
	print mod.do(test)
	
	# 'table' and 'cell' and 'header' and 'row' too wordy for you? Fine:
	test  = ''
	test += '[style ta [table [b]]]'
	test += '[style tr [row [b]]]'
	test += '[style td [cell [b]]]'
	test += '[style th [header [b]]]'

	test += '{ta {tr {td cell 1}{td cell 2}}}'
	xprint('Example 14 -- use your own keywords')
	print mod.do(test)

	# why stop there? lets go absolutely minimalist:
	test  = ''
	test += '[style t [table [b]]]'
	test += '[style r [row [b]]]'
	test += '[style d [cell [b]]]'
	test += '[style h [header [b]]]'

	test += '{t {r {d cell one}{d cell two}}}'
	xprint('Example 15 -- minimalism')
	print mod.do(test)

	# can we make that even simpler? Yes, with just a few short styles:
	
	test  = ''
	test += '[style t [table [b]]]'
	test += '[style mcell [cell [b]]]'
	test += '[style mhdr [header [b]]]'
	test += '[style h [row [t wrap=mhdr,[b]]]]'
	test += '[style w [row [t wrap=mcell,[b]]]]'

	test += '{t {w one,two}}'
	xprint('Example 16 -- minimal minimalism :)')
	print mod.do(test)
	
	# several rows with a header
	# this uses above-defined styles t, h and w.
	test  = ''
	test += '{t '
	test += '{h Col 1,Col 2}'
	test += '{w one,two}'
	test += '{w three,four}'
	test += '}'
	xprint('Example 17 -- minimal minimalism with a header')
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
	xprint('Example 18 -- minimalism, with alternating row styles')
	print mod.do(test)

	test  = ''
	test += '[a http://fyngyrz.com]\n'
	test += '[a tab,http://fyngyrz.com]\n'
	test += '[a http://fyngyrz.com,Visit my website!]\n'
	test += '[a http://fyngyrz.com,[nc Today, visit my website!]]\n'
	test += '[a tab,http://fyngyrz.com,Follow this link]\n'
	test += '[a tab,http://fyngyrz.com,[nc Follow this link, please, or else]]\n'

	xprint('Example 19 -- the [a] and [nc] tags')
	print mod.do(test)

	# You can use a newline instead of a space after a sqiggly name, which can
	# make your work more readable. Here the style just surrounds with parens,
	# just enough activity to make it clear the style works properly with a
	# newline or a space. The newline prior to the closing } is treated as part
	# of the body fed to the style, so it generates a newline on output, whereas
	# the newline or the space after the style name is "eaten" as it is a
	# delimiter in the context of specifying the style, not part of the
	# body fed to the style.
	# ------------------------------------------------------------------------
	test = """
[style foo ([b])]
{foo bar}
{foo
bar}
"""
	xprint("Example 20 -- Alternate use of newline as the style name/body delimiter")
	print mod.do(test)

	test = """
[local chapter Introduction to The Work]
[style h1 <h1>[color 0F0 [v [b]]]</h1>]
	    
{h1 chapter}
"""
	xprint("Example 21 -- Using a variable in a style")
	print mod.do(test)

	test  = ''
	test += '[style v [if [slice :1,[b]] $ [v [slice 1:,[b]]]]'
	test += '[else [slice :1,[b]] $ [b]]]'
	test += 'literal: {v chapter}\n'
	test += 'variable: {v $chapter}\n'
	xprint("Example 22 -- Making a style use a literal or a variable")
	print mod.do(test)

	test  = ''
	test += '[style h1 <h1>{v [b]}</h1>]'
	test += '{h1 chapter}\n'
	test += '{h1 $chapter}\n'
	xprint("Example 23 -- Generalizing literal/variable capability")
	print mod.do(test)


	# Multiple Parameters
	# While [b] is a great way to deal with single bits of content, there
	# are situations where multiple parameter handling is needed. [split]
	# and [parm] work together to create this capability.
	# The following demos show how you can use them. Essentially, you split
	# the body into a parameter list, then you use them from the list.
	# Specifying a parameter that is beyond the list bounds results in ''
	# ---------------------------------------------------------------------

	test  = ''
	test += '[split |,Ben|Meddie|Deb]'
	test += '[parm 1]\n'
	xprint("Example 24 -- Multiple parameter handling")
	print mod.do(test)

	test  = ''
	test += '[split [co],Ben,Meddie,Deb,Mildred]'
	test += '[parm 2]\n'
	xprint("Example 25 -- Multiple parameter handling, comma special case")
	print mod.do(test)

	test  = ''
	test += '[style fullname [split [co],[b]]First name: [parm 0]<br>\n Last name: [parm 1]<br>]'
	test += '{fullname John,Doe}'
	xprint("Example 26 -- Using multiple parameters within a style")
	print mod.do(test)
