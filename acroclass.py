import re

class core(object):
	# Project Info:
	# =============
	#   Written by: fyngyrz - codes with magnetic needle
	#   Incep date: November 24th, 2018
	#  Last Update: January 27th, 2019 (this code file only)
	#  Environment: Python 2.7
	# Source Files: acroclass.py, acrobase.txt
	#  Tab Spacing: Set to 4 for sane readability of Python source
	#     Security: Suitable for benign users only (IOW, me.)
	#      Purpose: Creates informative <abbr> tag wraps around
	#               all-caps terms in the source text. Written
	#               to support use of <abbr> on soylentnews.org
	#      License: None. Use as you will. PD, free, etc.
	# Dependencies: standard Python re import library
	# ----------------------------------------------------------

	def version_set(self):
		return('0.0.6 Beta')

	def __init__(self,	detectterms=True,			# disable class.makeacros() = False
						numberterms=False,			# disable detecting terms incorporating numbers
						detectcomps=True,			# detect electronic components
						iglist=[],					# terms to ignore
						acrofile='acrobase.txt',	# file to load term expansions from
						editor=False,				# use editor's marks
						inquotes=False,				# use editor's marks only within blockquote spans
						edpre = '',					# editor prefix
						edpost = ''):				# editor postfix
		self.version = self.version_set()
		self.detectterms = detectterms
		self.numberterms = numberterms
		self.detectcomps = detectcomps
		self.acrofile = acrofile
		self.igdict = {}
		self.undict = {}
		self.editor = editor
		self.inquotes = inquotes
		self.inspan = 0
		self.edpre = edpre
		self.edpost = edpost
		self.acros = {}
		self.rmlist = []
		self.relist = []
		self.errors = u'' # note that errors are unicode strings!
		self.setacros(acrofile)
		self.geniglist(iglist)

	# Generate ignore list, remove items from main list
	# -------------------------------------------------
	def geniglist(self,iglist):
		for el in iglist:
			el = str(el).upper()
			self.igdict[el] = True
			try:
				del self.acros[el]
			except:
				pass

	# Convert a unicode string to an ASCII string, replacing any
	# characters > 127 with the appropriate character entity.
	# That in turn makes the text compatible with the macro
	# processor, as character entities are 100$ ASCII.
	# ----------------------------------------------------------
	def makeascii(self,text):
		o = ''
		for i in range(0,len(text)):
			try:
				c = text[i].encode("ascii")
				o += c
			except:
				o += '&#{:d};'.format(ord(text[i]))
		return o

	# Convert HTML character entities into unicode
	# --------------------------------------------
	def subents(self,text):
		state = 0 # nothing detected
		accum = u''
		o = u''
		for c in text:
			if state == 0:		# nothing as yet?
				if c == u'&':	# ampersand?
					state = 1	# ampersand!
				else:
					o += c
			elif state == 1:	# ampersand found?
				if c == u'#':	# hash?
					state = 2	# hash!
					accum = u''	# clear accumulator
				else:			# not a hash, so not an entity encoding
					state = 0	# abort
					o += u'&'+c	# flush char, done
			elif state == 2:	# expecting digits or terminating semicolon
				if c.isdigit():	# digit?
					accum += c	# add it to accumulator if so
				elif c == u';':	# terminating
					s = u'\\U%08x' % (int(accum))
					ss= s.decode('unicode-escape')
					o += ss
					state = 0
				else: # bad encoding?
					o += u'&#'
					o += accum
					state = 0
		return o

	# Read term expansion file into memory
	# ------------------------------------
	def setacros(self,acrofile):
		try:
			with open(acrofile) as fh:
				self.acrobase = fh.read()
		except Exception,e:
			self.acrobase = u''
			self.errors += u'failed to read file'+str(e)+u'\n'
		else:
			self.acrobase = self.acrobase.replace(u'"',u'&quot;') # can't have quotes in abbr tags
			self.makedict()

	# Test string for integer representation
	# --------------------------------------
	def chkint(self,text):
		try:
			n = int(text)
		except:
			return False
		return True

	# Create dictionary from the acronym / abbreviation file contents
	# ---------------------------------------------------------------
	def makedict(self):
		self.acros = {}
		linecounter = 1
		l1 = self.acrobase.split(u'\n')
		edpr = u''
		edpo = u''
		if self.editor == True:
			edpr = self.edpre
			edpo = self.edpost
		for el in l1:
			if len(el) != 0:
				if el[0:1] != u'#':
					try:
						veri = True
						key,alternate,expansion = el.split(u',',2)
						if expansion.find('<') != -1: veri = False
						if expansion.find('>') != -1: veri = False
						if veri == True:
							if key == '*': # if this is a component designator
								if self.detectcomps == True:
									self.rmlist.append(expansion)
									self.relist.append(alternate)
								else:
									pass
							elif self.numberterms == False and self.chkint(key) == True:
								pass
							else: # normal term definition
								term = key
								if alternate != u'':
									term = alternate
								if self.acros.get(key,'') != '':
									self.errors += u'Duplicate ACRO key: '+ unicode(key) + u'\n'
								alist = expansion.split('|')
								if len(alist) == 1:
									self.acros[key] = expansion
								else:
									alist.sort()
									s = u''
									n = 1
									for el in alist:
										if n != 1: s = s + u' '
										s = s + u'(' + unicode(str(n)) + u'): '+unicode(str(el))
										n += 1
									self.acros[key] = s
						else:
							self.errors += u'&lt; or &gt; found in ACRO: '+ unicode(key) + u'\n'
					except Exception,e:
						self.errors += u'line '+str(linecounter)+u': '
						self.errors += u'"'+unicode(el)+u'"\n'+unicode(str(e))
			linecounter += 1

	# Match term against component encodings
	# --------------------------------------
	def compmatch(self,term):
		if self.detectcomps == False: return term
		if self.igdict.get(term,False) == True: return term
		if self.isnumeric(term) == False: # if not fully numeric
			rmatch = False
			ren = 0
			edpr = u''
			edpo = u''
			if self.editor == True:
				edpr = self.edpre
				edpo = self.edpost
			for el in self.relist:
				ln = len(el)
				el = el + '\d*'
				if re.match(el,term):
					try:
						n = int(term[ln:])
					except: # not a number, bail
						pass
					else:
						comp = self.rmlist[ren]
						ell = comp.split('|')
						smark = edpr
						emark = edpo
						if self.inquotes == True:
							if self.inspan == 0:
								smark = u''
								emark = u''
						if len(ell) == 1:
							string = '<abbr title="%s%s %s%s">%s</abbr>' % (smark,comp,n,emark,term)
#							string = '<abbr title="'+edpr+comp + ' ' + str(n) +edpo+ '">'+term+'</abbr>'
						else: # multiple elements
							x = 1
							smark = edpr
							emark = edpo
							if self.inquotes == True:
								if self.inspan == 0:
									smark = u''
									emark = u''
							string = '<abbr title="'+smark
							ell.sort()
							for element in ell:
								if x != 1: string += ' '
								string += '(%d): %s %d' % (x,element,n)
								x += 1
							string += emark+'">'+term+'</abbr>'
						return string
				ren += 1
		return term

	# Explicit match against numerals 0...9
	# -------------------------------------
	def isnumeric(self,text):
		for c in text:
			if c < u'0' or c > u'9': return False
		return True

	# Conversion including translation to unicode
	# -------------------------------------------
	def a2u(self,text):				# ASCII in
		if type(text) is not str:
			self.errors += u'class function a2u() requires ASCII input\n';
			return u''
		return self.makeacros(unicode(text))	# generate <abbr> tags, unicode out

	def a2a(self,text):				# ASCII in
		if type(text) is not str:
			self.errors += u'class function a2a() requires ASCII input\n';
			return u''
		text =  self.makeacros(unicode(text))	# generate <abbr> tags, unicode out
		return self.makeascii(text)				# get back an entity-encoded string

	# Conversion including translation from unicode
	# ---------------------------------------------
	def u2a(self,text):				# unicode in
		if type(text) is not unicode:
			self.errors += u'class function u2a() requires unicode input\n';
			return ''
		text = self.makeacros(text)	# generate <abbr> tags, ASCII out
		return self.makeascii(text) # convert to ASCII string

	def cleanbraces(self,text):
		text = text.replace('<','&lt;')
		text = text.replace('>','&gt;')
		return text

	def makeacros(self,text): # for compatibility only
		return self.u2u(text)

	# Convert all instances of TERM to <abbr title="expansion">TERM</abbr>
	# where TERM is capAlpha or some combination of capAlpha and Numeric
	# This is unicode in, unicode out
	# --------------------------------------------------------------------
	def u2u(self,text):
		tlen = len(text)
		ccnt = 0
		if self.detectterms == False: return text
		if type(text) is not unicode:
			self.errors += 'class function makeacros() requires unicode input\n';
			return ''
		incaps = False
		accum = u''
		o = u''
		ctag = u''
		btag = u''
		wait = False
		wait2 = False
		for c in text: # iterate all characters
			ccnt += 1
			if c == u'<':
				wait = True	# if within an HTML tag, don't bother
				ctag = u''	# reset abbr detector
				btag = u''	# reset blockquote detector
			elif c == u'>': wait = False
			ctag += c.lower()
			btag += c.lower()
			if btag[:11] == u'<blockquote':
				self.inspan += 1
				btag = u''
			elif btag[:12] == u'</blockquote':
				self.inspan -= 1
				if self.inspan < 0:
					self.inspan = 0
				btag = u''
			if ctag[:5] == u'<abbr':
				wait2 = True	# ignore between <abbr></abbr>
				ctag = u''
			elif ctag[:6] == u'</abbr':
				wait2 = False
				ctag = u''
			if wait == False and wait2 == False and ((c >= u'A' and c <= u'Z') or (c >= u'0' and c <= u'9')):
				accum += c
			else: # not a cap now
				if len(accum) > 1:
					taccum = self.acros.get(accum,accum)
					if taccum == accum: # not found
						if self.isnumeric(accum) == False: # if not fully numeric
							taccum = self.compmatch(accum)
							if taccum == accum: # still not found
								if self.igdict.get(taccum,'') == '':
									self.undict[taccum] = 1 # we don't know this one
					else: # we found it
						if self.editor == True:
							smark = self.edpre
							emark = self.edpost
						else:
							smark = u''
							emark = u''
						if self.inquotes == True:
							if self.inspan == 0:
								smark = u''
								emark = u''
						taccum = '<abbr title="%s%s%s">%s</abbr>' % (smark,taccum,emark,accum)
					accum = taccum
					accum += c
					o += accum
					accum = u''
				else: # 1 or 0
					o += accum
					accum = u''
					o += c
		if accum != u'': # any pending on end of post?
			if len(accum) > 1:
				taccum = self.acros.get(accum,accum)
				if taccum == accum:
					if self.isnumeric(taccum) == False:
						taccum = self.compmatch(accum)
						if taccum == accum: # still not found
							if self.igdict.get(taccum,'') == '':
								self.undict[taccum] = 1 # we don't know this one
				else:
					if self.editor == True:
						smark = self.edpre
						emark = self.edpost
					else:
						smark = u''
						emark = u''
					if self.inquotes == True:
						if self.inspan == 0:
							smark = u''
							emark = u''
					taccum = '<abbr title="%s%s%s">%s</abbr>' % (smark,taccum,emark,accum)
				accum = taccum
				o += accum
			else: # 1 or 0
				o += accum
		return o
