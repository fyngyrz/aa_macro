#!/usr/bin/python

# see class htmlAnsii, down a bit, for docs, attribution, etc.

escape = chr(27)

black = blk = bla = escape+'[0;30m'
blue = blu = escape+'[0;34m'
green = grn = escape+'[0;32m'
cyan = cya = cyn = escape+'[0;36m'
red = escape+'[0;31m'
purple = magenta = pur = mag = escape+'[0;35m'
brown = bro = brn = escape+'[0;33m'
lightgrey = lightgray = lgy = escape+'[0;37m'
darkgrey = darkgray = dgr = escape+'[1;30m'
lightblue = lbl = escape+'[1;34m'
lightgreen = lgr = escape+'[1;32m'
lightcyan = lcy = escape+'[1;36m'
lightred = lre = escape+'[1;31m'
lightpurple = lightmagenta = lpu  = escape+'[1;35m'
yellow = yel = escape+'[1;33m'
white = wht = escape+'[1;37m'

class colorsetup(object):
	def __init__(self):
		self.e = chr(27)
		self.v = {	# colorName : [ANSII foreCode, HTML colorCode, ANSII backCode]
			'black'    :['0;30', '000000', '40'],	# background colors same in both sets
			'dred'     :['0;31', '880000', '41'],
			'dgreen'   :['0;32', '008800', '42'],
			'dyellow'  :['0;33', '888800', '43'],
			'dblue'    :['0;34', '000088', '44'],
			'dpurple'  :['0;35', '880088', '45'],
			'dmagenta' :['0;35', '880088', '45'],
			'daqua'    :['0:36', '008888', '46'], # example #1 of color name symonym...
			'dcyan'    :['0:36', '008888', '46'], # ...'daqua' and 'dcyan' act the same
			'dwhite'   :['0;37', '888888', '47'],
			# This is the 2nd set of colors. Brighter, usually. Mostly.
			'grey'     :['1;30', '444444', '40'],	# background colors same in both sets
			'red'      :['1;31', 'ff0000', '41'],
			'green'    :['1;32', '00ff00', '42'],
			'yellow'   :['1;33', 'ffff00', '43'],
			'blue'     :['1;34', '0000ff', '44'],
			'purple'   :['1;35', 'ff00ff', '45'], # example #2 of color name symonym...
			'magenta'  :['1;35', 'ff00ff', '45'], # ...'purple' and 'magenta' act the same
			'aqua'     :['0:36', '00ffff', '46'],
			'cyan'     :['0:36', '00ffff', '46'],
			'white'    :['1;37', 'ffffff', '47']
			}

class tcolorsetup(object):
	def __init__(self):
		self.e = chr(27)
		self.v = {	# ANSII fore, HTML colorCode, ANSII back
			'black'  :['0;30', '000000', '40'],	# background colors same in both sets
			'red'    :['1;31', 'ff0000', '41'],
			'green'  :['1;32', '00ff00', '42'],
			'blue'   :['1;34', '0000ff', '44'],
			}

	def wrap(self,cc):
		return self.e+'['+cc+'m'

class htmlAnsii(object):
	"""Class to provide easy access to ANSII and equivalant HTML coloring.

      Author: fyngyrz  (Ben)
     Contact: fyngyrz@gmail.com (bugs, feature requests, kudos, bitter rejections)
     Project: aa_ansicolor.py
  Incep Date: February 1st, 2015
     LastRev: July 24th, 2015
  LastDocRev: April 26th, 2015
 Tab spacing: 4 (set your editor to this for sane formatting while reading)
     1st-Rel: 1.0.0
     Version: 1.0.4
     History:
        1.0.4 -- New dumpDicts() flags: novalues, nokeys, nosum
        1.0.4 -- New ways to legitimately use dumpDicts() using above flags
        1.0.4 -- Fixed bug in console section of color table (aqua/cyan was white)
        1.0.4 -- dumpDicts() to 1.0.1, see class for details

        1.0.3 -- Added dumpDicts() class. Lots of fun. :) Examples too.

        1.0.2 -- Added color synonyms to the color names supported (magenta, cyan)
        1.0.2 -- Added some detail to the comments, explained how to add synonyms

        1.0.1 -- Smarter about background colors, more efficient
        1.0.1 -- Calling mechanism for puntReport changed, see example 5,6

        1.0.0 -- Initial Release

For examples of what this can do, just execute aa_ansiicolor.py in a shell.
The examples are at the end of the file and demonstrate various
ways to use the class.

The intent here is to provide a unified mechanism for generating
text to both the console and HTML pages, so you can generate
text reports and so forth either way easily, and have them look
consistent. Consequently, the ANSII colors are what we're
interested in.
"""
	def __init__(self,	fore='red',
						back='black',
						mode='text',
						default='green',
						backdef='black',
						pageback='unknown'):
		self.ref = colorsetup()
		self.fore = fore
		self.back = back
		self.backdef = backdef
		self.default = default
		self.mode = mode
		self.fmem = None
		self.pageback = pageback

	def setMode(self,m=None):
		if m == None:
			m = self.mode
		self.mode = m

	def setBack(self,b=None):
		if b == None:
			b = self.back
		self.back = b

	def setFore(self,f=None):
		if f == None:
			f = self.fore
		self.fore = f

	def bothColors(self,f=None,b=None):
		if f == None:
			f = self.fore
		if b == None:
			b = self.back
		if self.mode == 'text':
			r1 = self.ref.v.get(f,						# try for user setting
					self.ref.v.get(self.default,		# else try for user default
						self.ref.v.get('green')))[0]	# else green, baby
			r2 = self.ref.v.get(b,						# try for user setting
					self.ref.v.get(self.backdef,		# else try for user default
						self.ref.v.get('black')))[2]	# else black, baby
			rt = self.ref.e+'['+r1+';'+r2+'m'
		else: # html
			r2 = self.ref.v.get(f,						# try for user setting
					self.ref.v.get(self.default,		# else try for user default
						self.ref.v.get('green')))[1]	# else green, baby
			r1 = self.ref.v.get(b,						# try for user setting
					self.ref.v.get(self.backdef,		# else try for user default
						self.ref.v.get('black')))[1]	# else black, baby
			r2 = '<font color="#'+r2+'">'				# html <font> wrapper
			r1 = '<span style="background: #'+r1+';">'
			if (self.pageback != b):
				rt = r1+r2
			else:
				rt = r2
		return rt

	def setDefault(self,d=None):
		if d != None:
			self.default = d

	def setBackDef(self,d=None):
		if d != None:
			self.backdef = d

	def setPageBack(self,d=None):
		if d != None:
			self.pageback = d

	def close(self):
		rt = ''
		if self.mode == 'text':
			rt += self.bothColors(self.default,self.backdef)
		else: # html
			if self.back != self.pageback:
				rt += '</font></span>'
			else:
				rt += '</font>'
		return rt

	def c(self,text,fore=None,back=None,mode=None): # wrap text in colors
		bb = self.back
		ff = self.fore
		self.setFore(fore)
		self.setBack(back)
		self.setMode(mode)
		if text == None:
			text = ''
		t = self.bothColors() + text + self.close()
		self.back = bb
		self.fore = ff
		return t

	def prefixPage(self,title='Report',back=None):
		if back == None:
			bgc = self.pageback
			if bgc == 'unknown':
				bgc = self.pageback = 'white';
		bgu = self.ref.v.get(bgc,					# try for user setting
			self.ref.v.get('white'))[1]				# else white, baby
		if self.mode == 'text':
			return ''								# nothing need be done
		s = "Content-type: text/html\n\n"
		s+= '<HTML>\n'
		s+= '<HEAD>\n'
		s+= '<TITLE>'+title+'</TITLE>\n'
		s+= '</HEAD>\n'
		s+= '<BODY bgcolor="#'+bgu+'" text="#'+self.fore+'">\n'
		return s

	def postfixPage(self):
		if self.mode == 'text':
			return ''	# nothing need be done in that case
		s = '\n</BODY>\n'
		s+= '<HTML>\n'
		return s

	def puntReport(self,r,title='Report'):
		s = self.prefixPage(title)
		s+= r
		s+= self.postfixPage()
		return s

class dumpDicts(object):
	"""Class to provide lots of ways to dump dictionaries usefully

      Author: fyngyrz  (Ben)
     Contact: fyngyrz@gmail.com (bugs, feature requests, kudos, bitter rejections)
     Project: aa_ansicolor.py
  Incep Date: February 1st, 2015 (for Project)
     LastRev: May 25th, 2015     (for Class)
  LastDocRev: May 9th, 2015      (for Class)
 Tab spacing: 4 (set your editor to this for sane formatting while reading)
     1st-Rel: 1.0.0
     Version: 1.0.4
     History:                    (for Class)
         1.0.4 Added fCommaSep() for comma-separated floats

         1.0.3 New control flags: (nototal, limit)
         1.0.3 New interspersing text (inter) for negative limit case
         1.0.3 New .commaSep() utility for comma-separated integers
         1.0.3 New .fmtTime() utility for printing out seconds as durations

         1.0.2 Bugfix for nsort in dumpDicts()

         1.0.1 New control flags: (nokeys, novalues, nosum)
         1.0.1 calling parameter documentation

         1.0.0 Initial release

dumpDicts() provides a means to dump lists and dictionaries in
various useful formats. It is well integrated with htmlAnsii,
and will obey and/or use console and HTML color information
within the context of the dumps. dumpDicts() is generally a
one-call operation, although there are still things you can
do to prepare the key lists of dictionaries to make them
more interesting, such as color them prior to displaying the
keys using value order, with or without the values being
displayed.

dumpDict() parameter description:
==================================
ac : an htmlAnsii() object. If you want color support, supply this.

Example:
--------
    ha = htmlAnsii()						# Acquire ha, dd separately to enable
    dd = dumpDicts(ha)						# the convenience of...
    coloredText = ha.c('text','color')		# ...using htmlAnsii() like this

Non-advised example:
--------------------
    dd = dumpDict(htmlAnsii())				# If you do this...
    coloredText = dd.ac.c('text','color')	# ...you must use htmlAnsii() like this
    										# Although this way saves memory for single use.
    										# And is agreeably consistent.
    										# Memory is cheap. Keystrokes cost time. :)

dumpDict() is use by calling it's d() proceedure, documented next.

Note:	You should only need one htmlAnsii object and/or one dumpDicts object.
		Both can completely reconfigure based on supplied parameters.

dumpDict.d() parameter descriptions:
====================================

Required:
---------
     l : list [a,b,...], or list of keys for dictionary eg dict.keys()
icolor : color you want the list entries rendered in
ccolor : color for commas between list elements on the same line
  what : Used to describe empty lists: "Zero 'what'""

Optional. Provide in order or by name:
--------------------------------------
          Default setting
          |  Description
          |  |
  mdict : {} Supply mdict=dictionary if you want values in dump (otherwise,
             nsort won't work, nor will any modifier for nsort)

  ddict : {} Supply ddict=dictionary if you want non-main dictionary values for
             your keys. This allows nsort to sort on mdict contents, while diplaying
             the contents of ddict as the values, using the same keys.

  mtype : 0  Signals numeric data in mdict. 1=text data in mdict. You
             must supply mdict if you want numeric values or intend to
             use ddict

    fmt : '' format string for single-line reporting format "\n%s verbiage %s

 zcolor : '' color for numeric mdict values that are zero

 wrapat : 4  How many items to list on same line

 ncolor : '' color for summary count of items and report of 'Zero what'

  zlast : 0  1=force ZERO numeric dictionary values to end of dump

  nsort : 0  1=sort dictionary by values in mdict

  asort : 0  1=sort dictionary or list by key names

  rsort : 0  1=reverse sort order (for nsort, asort)

nocolor : 0  1=suppress color generation (set=1 if class has no htmlAnsii() object)

   prop : 0  1=signal that you're using proportional fonts, so alignment is toast

nocomma : 0  1=use spaces between items listed on same line (required for 1-item/line)

  nokey : 0  1=suppress the key in reports that feature values

novalue : 0  1=suppress the value in reports that use value to sort

  nosum : 0  1=suppress the reporting of just the sum of values in key value dumps

nototal : 0  1=suppress the reporting of ANY total in key value dumps

  limit : 0  X > 0 means limit report to first X elements.
             Supplying a negative number limits to first X, then last X

  inter : '' If != '': outputs this between first group and last group
             when limit is negative
"""
	def __init__(self,ac=None):
		self.diag = ''
		self.setNewHO(ac)

	# pass durt as seconds integer
	# raw = 1 means no coloring
	# structure = 1 means values take up defined amounts of space
	# lead = 1 means all values are present, even if zero
	# blank = 1 means that leading zero values are replaced with spaces
	# ccolor = 'white', set to color you want the designnators (d,h,m,s)
	# Remember to set the text colors
	# Recommend you have an ansiiHtml() object set up, example:
	#    ac = htmlAnsii()
	#    dd = dumpDict(ac)
	#    string = ac.c(fmtTime(1234567),'green')
	# ---> 14d  6h 56m  7s
	# where d,h,m and s are white, and 14, 6, 56 and 7 are green
	# ------------------------------------------------------------------
	def fmtTime(self,durt,raw=0,structure=1,lead=1,blank=0,ccolor='white'):
		try:
			cd = self.ac.c('d',ccolor)
			ch = self.ac.c('h',ccolor)
			cm = self.ac.c('m',ccolor)
			cs = self.ac.c('s',ccolor)
		except:
			cd = 'd'
			ch = 'h'
			cm = 'm'
			cs = 's'

		am = 60
		ah = 60 * am
		ad = 24 * ah

		aj = 31 * ad
		ay = 12 * aj

		durd = int(durt / ad)
		durh = int((durt - (durd * ad)) / ah)
		durx = durt - ((durh * ah) + (durd * ad))
		durm = int(durx / am)
		durs = durx % am
		if raw == 0:
			if lead == 1:
				if structure == 1:
					fmt = '%3d%s %2d%s %2d%s %2d%s'
					tup = (durd,cd,durh,ch,durm,cm,durs,cs)
				else:
					fmt = '%d%s %d%s %d%s %d%s'
					tup = (durh,ch,durm,cm,durs,cs)
			else: # no lead
				fmt = ''
				tup = ()
				if durd > 0:
					if structure == 1: fmt += '%3d%s '
					else:              fmt += '%d%s '
					tup += (durd,cd)
				elif blank == 1:
					fmt += '     '
				if durh > 0 or durd > 0:
					if structure == 1: fmt += '%2d%s '
					else:              fmt += '%d%s '
					tup += (durh,ch)
				elif blank == 1:
					fmt += '    '
				if durd > 0 or durm > 0 or durm > 0:
					if structure == 1: fmt += '%2d%s '
					else:              fmt += '%d%s '
					tup += (durm,cm)
				elif blank == 1:
					fmt += '    '
				if structure == 1: fmt += '%2d%s'
				else:              fmt += '%d%s'
				tup += (durs,cs)
		else: # raw
			if lead == 1:
				tup = (durd,durh,durm,durs)
				if structure == 0:
					fmt = '%dd %dh %dm %ds'
				else:
					fmt = '%3dd %2dh %2dm %2ds'
			else: # lead == 0
				fmt = ''
				tup = ()
				if durd > 0:
					if structure == 1: fmt += '%3dd '
					else:              fmt += '%dd '
					tup += (durd,)
				if durh > 0 or durd > 0:
					if structure == 1: fmt += '%2dh '
					else:              fmt += '%dh '
					tup += (durh,)
				elif blank == 1:
					fmt += '      '
				if durd > 0 or durh > 0 or durm > 0:
					if structure == 1: fmt += '%2dm '
					else:              fmt += '%dm '
					tup += (durm,)
				elif blank == 1:
					fmt += '     '
				if structure == 1: fmt += '%2ds'
				else:              fmt += '%ds'
				tup += (durs,)
		return fmt % tup

	# pretty straightforward.
	# pass it 1024, string or integer, and you get back 1,024 as a string
	# -------------------------------------------------------------------
	def commaSep(self,n):
		ou = ''
		ouc = 0
		pending = 0
		tn = str(n)
		tn = tn[::-1]
		for c in tn:
			if pending == 1:
				ou+=','
				pending = 0
			ou += c
			ouc += 1
			if ouc == 3:
				ouc = 0
				pending = 1
		return ou[::-1]

	# This one will comma separate floats, string or float
	# Make sure you pass it the number of decimal places
	# you want back. No decimal places? Then you get n.0
	# ----------------------------------------------------
	def fCommaSep(self,n):
		n = str(n)
		try:
			x = float(n)
		except:
			return '0.0'
		if len(n) > 0:
			if n.find('.') >= 0: # if there's a decimal point in there
				i,d = n.split('.')
				if len(d) == 0: # ensure we have decimal places
					d = '0'
				if len(i) > 0: # was there an int portion?
					n = self.commaSep(i)
					n = n + '.' + d
				else: # n was empty
					n = '0.' + d
			else: # no decimal point
				n = self.commaSep(n) + '.0'
		else: # empty string
			n = '0.0'
		return n

	def znum(self,num):
		s = str(num)
		if num == 0:
			s = 'Zero'
		return s

	def setNewHO(self,ho=None,local=None):
		t = str(type(ho))
		if not (t  == "<class '__main__.htmlAnsii'>" or
		        t  == "<class 'aa_ansiicolor.htmlAnsii'>" or
		        ho == None):
			ho = None
			self.diag = t

		self.ac = ho
		if ho == None:
			self.nocolor = 1
			self.c  = None
		else:
			self.c  = ho.c
			self.nocolor = 0

		if local == None:
			if ho != None:
				if ho.mode == 'text':
					self.local = 1
				else:
					self.local = 0
			else:
				self.local = 1
		else:
			if local == 1 or local == 0:
				self.local = local
			else:
				self.local = 1

	def d(self,
			l,
			icolor,
			ccolor,
			what,
			mdict={},
			ddict={},
			mtype=0,
			fmt='',
			zcolor='',
			wrapat=4,
			ncolor='',
			zlast=0,
			nsort=0,
			asort=0,
			rsort=0,
			nocolor=None,
			prop=0,
			nocomma=0,
			nokey=0,
			novalue=0,
			nosum=0,
			nototal=0,
			limit=0,
			inter='',
			title='',
			trailer=''):
		nset = 0
		ss = ''
		if nocolor == None:
			nocolor = self.nocolor
		if self.local == 0: # html?
			if prop != 1:
				s += '<tt>'
		needcr = 1
		ct = 0
		cu = 0
		summer = 0
		if asort == 1 and mdict != {}:
			l = sorted(mdict.keys(), key=lambda x: x.lower())
		elif nsort == 1 and mdict != {}:
			l = sorted(mdict,key=mdict.get)
		if zlast == 1 and mdict != {}:
			alist = []
			blist = []
			for key in l:				# for each key
				if mdict[key] != 0:		#    THEN goes in >0 list
					alist += [key]		#        Put it there
				else:					#    ELSE goes in =0 list
					blist += [key]		#        Put it there
			l = alist + blist			# list of >0 items THEN =0 items
		if rsort==0:
			l.reverse()
		loccount = 0
		endlimit = len(l) + limit # if limit is negative, it gives us the last set margin
		if endlimit < 0:
			endlimit = 0
		for key in l:
			s = ''
			loccount += 1
			if nocomma == 0:
				if needcr == 0:
					ms = ','
					if nocolor == 1:
						s += ms
					else:
						s += self.c(ms,ccolor)
			else: # space instead of comma
				if fmt == '':
					s += ' '
			if needcr == 1 and fmt == '':
				s+= '\n' #+indent
				needcr = 0
			elif needcr == 1 and fmt != '':
				pass
#				fmt = fmt.replace('\n','\n'+indents,1)
#				needcr = 0
			if mdict != {}:
				if mtype == 0:
					v = mdict[key]
					summer += v
					ucolor = icolor
					if v == 0:
						if zcolor != '':
							ucolor = zcolor
					else:
						cu += 1 # non-zero items
					if fmt == '':
						if nokey == 1:
							ms = str(v)
						elif novalue == 1:
							ms = key
						else:
							ms = str(v)+' '+key
						if nocolor == 1:
							s += ms
						else:
							s += self.c(ms,ucolor)
					else:
						v = self.znum(v)
						if ddict != {}:
							v = ddict[key]
						tup = (str(v),key)
						bs = fmt % tup
						if self.local == 0: # html?
							if prop != 1:
								bs = bs.replace(' ','&nbsp;')
						if nocolor == 1:
							s += bs
						else:
							s += self.c(bs,ucolor)
				else: # text content in mdict
					if ddict == {}:
						ms = str(key)+'='+str(mdict[key])
					else:
						ms = str(key)+'='+str(ddict[key])
					if nocolor == 1:
						s += ms
					else:
						s += self.c(ms,icolor)
			else: # no mdict
				if nocolor == 1:
					s += str(key)
				else:
					s += self.c(str(key),icolor)
			ct += 1
			if ct % wrapat == 0:
				needcr = 1
			if limit == 0:
				ss += s
			else: # limit of some kind
				if limit > 0:
					if loccount <= limit:
						ss += s
				else: # negative limit... do trailers
					tmp = -limit
					if loccount <= tmp:
						ss += s
					elif loccount > endlimit:
						if nset == 0:
							nset = 1
							s = inter+s
						ss += s
					
		s = ss
		flag = 1
		if cu != 0:
			ct = cu
		if s == '':
			ms = '\nNo '+what+'\n'
			if nocolor == 1:
				s += ms
			else:
				s += self.c(ms,ncolor)
		else:
			if mdict != {}:
				if mtype == 0: # numeric
					if nototal == 0:
						if nosum == 1:
							ms = ' ('+str(ct)+')\n'
						else:
							ms = ' ('+str(summer)+'/'+str(ct)+')\n'
						if nocolor == 1:
							s += ms
						else:
							s += self.c(ms,ncolor)
					flag = 0
			if flag == 1:
				ms = ' ('+str(ct)+')\n'
				if nocolor == 1:
					s += ms
				else:
					s += self.c(ms,ncolor)
		if self.local == 0:
			s = s.replace('\n','<br>\n')
		if self.local == 0: # html?
			if prop != 1:
				s += '</tt>\n'
		if s != '':
			if title != '':
				s = title+s
			if trailer != '':
				s = s + trailer
		return s

# ===================================================================
#                         Examples
# ===================================================================

# Here's how you use the import library
# most of this first example is iteration;
# just pay attention to the lines that
# have comments to the right.
# ========================================

# This kicks off only if the import is directly executed
# from the command line, for instance:
#
#     python aa_ansicolor.py[ENTER]
#
# ------------------------------------------------------------
if __name__ == "__main__":
	import sys
	t = 'test'

# changeme!
	bc = 'unknown'										# no idea what console color
														# you're using
	c = htmlAnsii(pageback=bc,backdef=bc)				# you'll want the object
														# you should set the BOTH the
														# def back color and the back
														# color that the screen or
														# html page is using if you
														# know what it is. This allows
														# avoiding constantly resetting
														# the background color on
														# every output.
														#
														# Since I don't know what
														# your console back color is,
														# I set it here to "unknown",
														# that way the background is
														# set no matter what back
														# color you're using.

# just a little utility for prettier output
# -----------------------------------------
	def hline(s,y=0):
		eol = '\n'
		if y == 1 or c.mode != 'text':
			eol = '<br>\n'
		sys.stdout.write(eol + s + eol + (len(s) * '-'))

# Choose an operating mode:
# -------------------------
	for means in ('html','text',):
		c.setMode(means)								# this can set html or text mode

# You can do it all in one line:
# ------------------------------
		s = 'in '+means+' all in one line'
		l = len(s)
		ss = '-' * l
		print '\n'+s; print ss
		for key1 in c.ref.v:
			for key2 in c.ref.v:
				s = '1:'+c.c(t,key1,key2)				# fore,back,text all at once
				s += ' '+key1+','+key2
				sys.stdout.write(s+'\n')

# Or, you can do it like this:
# ----------------------------
		s = 'in '+means+' by setting colors independently, then getting text'
		l = len(s)
		ss = '-' * l
		print '\n'+s; print ss
		for key1 in c.ref.v:
			for key2 in c.ref.v:
				c.setBack(key2)						# set back color
				c.setFore(key1)						# set fore color
				s = '2:'+c.c(t)						# get the text that way
				s+= ' '+key1+','+key2
				sys.stdout.write(s+'\n')

# Next some very simple, explict examples
# designed to be examined in a *nix shell
# that use some different calling methods
# =======================================
	print

# text first
# ----------
	c = htmlAnsii() # new object defaults to text mode, so mode is redundant here
	print '3:'+c.c('Text example','blue','red')

# now html using c(Text,foreColor,backColor,Mode)
# -----------------------------------------------
	c = htmlAnsii()
	c.setMode('html')
	print '4:'+c.c('HTML/CSS example','blue','red','html')

	print

# Check it out: text or HTML/CSS report:
# ======================================
	title = 'My Report\n'	
	content = 'blah blah blah\n'

	c = htmlAnsii()						# here's the object we need, defaults to text mode
	c.setPageBack('black')				# let's use a custom HTML-only page color...
										# ...or just this would have worked, too...
										# ...   c = htmlAnsii(pageback='black')
										#            BECAUSE:
										# If the lib knows the background color of the
										# page, it won't set CSS background-control
										# spans around text that has the background
										# color. Saves some bandwidth. In the case
										# of puntReport(), however, if the background
										# is unknown, it will auto-set it to white.
										# Because that's usually what people use.

	s = c.c(title,'blue','yellow')		# color title in text mode
	s+= c.c(content,'white','black')	# color content in text mode
	r = c.puntReport('5:'+s)			# create report in console mode (b will be ignored)
	sys.stdout.write(r+'\n')			# pump it out stdout.

	print

# switching modes in midstream:
# -----------------------------
	c.setMode('html')

	s = c.c(title,'blue','yellow')		# color title in text mode
	s+= c.c(content,'white','black')	# color content in text mode
	r = c.puntReport('6:'+s)			# create report in HTML mode
	sys.stdout.write(r+'\n')			# pump it out stdout.

# Ok, now we'll demo the dictDump() utility. dictDump() is a class that
# can use the htmlANSI class to produce colored, ordered dumps of the
# contents of dictionaries and lists. You don't have to use the colors,
# either, but it's more fun that way. :)
#
# One thing to be aware of: The cenvention I use is that the page or
# console is "at" a new line, column 0, before a dump is output.
# if you don't arrange for that, the first line of the dump will
# appear on the end of the last line YOU output. So don't do that. :)
# ---------------------------------------------------------------------

# We need a dumpDict object:
# --------------------------
	c.setMode('text')	# I'm going to do these to the console. Works in HTML of course
	d = dumpDicts(c)	# pass the htmlAnsii object to it, cuz we want it to use it

# Example 7 shows a simple dictionary that just
# contains entries, the kind of situation where
# you've been looking for things to happen, and
# you take note of which have. Input is list.
# ---------------------------------------------
	hline('Example 7: (dump a list in sets of four)')

	tdict = {'rain':1,'snow':1,'hail':1,'tornado':1,'tsunami':1,'earthquake':1,'rapture':1}
	s = d.d(tdict.keys(),'red','green','Events')
	sys.stdout.write(s)
# ---------------------------------------------

# Example 8
# ---------
# It's also worth showing what happens if there's
# nothing in your list:
# ----------------------------------------------
	hline('Example 8: (empty list)')

	tdict = {}
	s = d.d(tdict.keys(),'red','green','Events')
	sys.stdout.write(s)

# Example 9:
# ----------
# This time, we look at a dict where you are
# actually counting events:
# ---------------------------------------------
	hline('Example 9: (counting events)')

	tdict = {'rain':1,'snow':2,'hail':3,'tornado':5,'tsunami':0,'earthquake':0,'rapture':0}
	s = d.d(tdict.keys(),'red','green','Events',tdict)
	sys.stdout.write(s)

# Example 10:
# ----------
# Same thing as example 9, but we'll color
# the non-happening events in blue
# ---------------------------------------------
	hline('Example 10: (zero events in other color)')

	tdict = {'rain':1,'snow':2,'hail':3,'tornado':5,'tsunami':0,'earthquake':0,'rapture':0}
	s = d.d(tdict.keys(),'red','green','Events',tdict,zcolor='blue')
	sys.stdout.write(s)

# Example 11 shows the same dict, but this one
# in a vertical list format.
# ---------------------------------------------
	hline('Example 11: (in vertical format)')

	tdict = {'rain':1,'snow':2,'hail':3,'tornado':5,
	         'tsunami':0,'earthquake':0,'rapture':0}
	s = d.d(tdict.keys(),'red','green','Events',tdict,fmt='\n%4s Occurances of %s')
	sys.stdout.write(s)

# Example 12:
# -----------
# The same, but zero occurance events in blue
# ---------------------------------------------
	hline('Example 12: (zero occurance in blue)')

	tdict = {'rain':1,'snow':2,'hail':3,'tornado':5,'tsunami':0,'earthquake':0,'rapture':0}
	s = d.d(tdict.keys(),'red','green','Events',tdict,fmt='\n%4s Occurances of %s',zcolor='blue')
	sys.stdout.write(s)

# Example 13:
# -----------
# Be awesome if they were alphabetic, no? Yes! :)
# -----------------------------------------------
	hline('Example 13: (alpha sort)')

	tdict = {'rain':1,'snow':2,'hail':3,'tornado':5,'tsunami':0,'earthquake':0,'rapture':0}
	s = d.d(sorted(tdict.keys()),'red','green','Events',tdict,fmt='\n%4s Occurances of %s',zcolor='blue',asort=1)
	sys.stdout.write(s)

# Example 14:
# -----------
# But now that you look at it, the zeros aren't
# as important, are they? So perhaps they should be last.
# They will still be alphabetic, there are two sets...
# zero and non-zero, both alphabetized
# ---------------------------------------------------------
	hline('Example 14: (zeros at bottom, otherwise alpha)')

	tdict = {'rain':1,'snow':2,'hail':3,'tornado':5,'tsunami':0,'earthquake':0,'rapture':0}
	s = d.d(sorted(tdict.keys()),'red','green','Events',tdict,fmt='\n%4s Occurances of %s',zcolor='blue',zlast=1,asort=1)
	sys.stdout.write(s)

# Example 15:
# -----------
# Of course, rather than alphabetic, perhaps
# sorting by value is more what you want.
# That still ends up with the zeros last, too.
# ------------------------------------------
	hline('Example 15: (sort by value, largest first)')

	tdict = {'rain':1,'snow':2,'hail':3,'tornado':5,
	         'tsunami':0,'earthquake':0,'rapture':0}
	c = htmlAnsii()
	d = dumpDicts(c)
	s = d.d(tdict.keys(),'red','green','Events',
	       tdict,fmt='\n%4s Occurances of %s',
	       zcolor='blue',nsort=1,ncolor='white')
	sys.stdout.write(s)

# Example 16:
# -----------
# Or, backwards:
# ------------------------------------------
	hline('Example 16: (sort by value, largest last)')

	tdict = {'rain':1,'snow':2,'hail':3,'tornado':5,'tsunami':0,'earthquake':0,'rapture':0}
	s = d.d(tdict.keys(),'red','green','Events',tdict,fmt='\n%4s Occurances of %s',zcolor='blue',nsort=1,rsort=1)
	sys.stdout.write(s)

# Example 17:
# -----------
# So, what if you have an htmlAnsii object,
# as we have had all along in these examples,
# but you just want text. Then this:
# -----------------------------------------------
	hline('Example 17: (dump a list in sets of four, no coloring)')

	tdict = {'rain':1,'snow':1,'hail':1,'tornado':1,'tsunami':1,'earthquake':1,'rapture':1}
	s = d.d(tdict.keys(),'','','Events',nocolor=1) # nocolor flag does it
	sys.stdout.write(s)

# Example 18:
# -----------
# So, what if you don't even HAVE have an htmlAnsii object?
# Then you still just get text:
# -----------------------------------------------------
	hline('Example 18: (dump a list without htmlAnsii object)',0)

	d = dumpDicts()	# this one isn't passed an htmlAnsii object - colors irrelevant
	tdict = {'rain':1,'snow':2,'hail':3,'tornado':5,'tsunami':0,'earthquake':0,'rapture':0}
	s = d.d(tdict.keys(),'red','green','Events',tdict,fmt='\n%4s Occurances of %s',zcolor='blue')
	sys.stdout.write(s)

# Example 19:
# -----------
# And just for grins and giggles, we'll do no colors in HTML.
# You might note that it aligns the various items by using
# non-breaking spaces. For that to work, you need a non-prop
# font, which as you see is instantiated by wrapping the whole
# enchilda in <tt> and </tt>. If you don't want that for some
# reason, set prop=1 in the call and it'll give up on the
# non-breaking spaces *and* the <tt> </tt> wrapping. Notice
# I changed the supplied format string so the first %s wasn't
# demanding 4 columns as in the previous %4s
# No point to it in a proportional font environment.
# -----------------------------------------------------------
	hline('Example 19: (dump a vertical list without color or alignment in HTML)',1)

	c.setMode('html')	# change environment on existing htmlAnsii object
	d = dumpDicts(c)	# get dumpDicts() based on that object
	tdict = {'rain':1,'snow':2,'hail':3,'tornado':5,'tsunami':0,'earthquake':0,'rapture':0}
	s = d.d(tdict.keys(),'','','Events',tdict,fmt='\n%s Occurances of %s',zcolor='blue',nocolor=1,prop=1)
	sys.stdout.write(s)

# That's all, folks!
# ------------------
	sys.stdout.write('\n')
