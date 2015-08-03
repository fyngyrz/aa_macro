#!/usr/bin/python

# Convert markdown file source files to aa_macro source files

import sys
import os
import re
from aa_macro import *

defs = """
[style a [split [co],[b]][a [urlencode [parm 1]],[parm 0]]]  
[style b [b [b]]]  
[style blockquote <blockquote>[nl][b][nl]<blockquote>]  
[style br <br>]  
[style code [split [co],[b]]<pre>[parm 1]</pre>[comment parm 0]]  
[style comma [co]]  
[style gt &gt;]  
[style h1 <h1>[b]</h1>]  
[style h2 <h2>[b]</h2>]  
[style h3 <h3>[b]</h2>]  
[style h4 <h4>[b]</h4>]  
[style h5 <h5>[b]</h5>]  
[style h6 <h6>[b]</h6>]  
[style hcell [header [b]]]  
[style i [i [b]]]  
[style img [split [co],[b]][img [parm 0],[urlencode [parm 1]]]]  
[style inline <tt>[b]</tt>]  
[style lb [lb]]  
[style ls [ls]]  
[style lt &lt;]  
[style nbsp &nbsp;]  
[style rb [rb]]  
[style ol [ol [b]]]  
[style p [p [nl][b][nl]]]  
[style row [row [b]]]  
[style rs [rs]]  
[style table [table border=1,[b]]]  
[style tcell [cell [b]]]  
[style u [u [b]]]  
[style ul [ul [b]]]  
"""

ecape = {	'[':'{lb}',']':'{rb}',
			'{':'{ls}','}':'{rs}',
		}

def cape(c):
	return ecape.get(c,c)

def escapeForHTML(c):
	if c == '<': return '{lt}'
	if c == '>': return '{gt}'
	return c

def rint(string,err=False,term='\n'):
	if err == True:
		sys.stderr.write(string+term)
	else:
		sys.stdout.write(string+term)

testfilename = "mtmtestfile.html"
canname = 'cannedstyles.txt'

def help():
	rint('()=required, |= "or", []=optional')
	rint('USE: (python|./) martomac.py [-m macroFilename][-c ][-s ][-t ][-p ][-x ]inputFilename[.md] [outputFilename]')
	rint("-c flag suppresses leading default style definitions, supply your own")
	rint("-s flag suppresses blank lines between block elements")
	rint('-t flag creates macro() processed output test file "%s"' % (testfilename))
	rint('-h flag wraps content of "%s" or stdout in basic HTML page' % (testfilename,))
	rint('-x flag suppresses printing filename report')
	rint('-o open default OS X browser on "%s"' % (testfilename,))
	rint('-p flag routes normal output to stdout')
	rint('-l flag strips terminating newlines off of list elements')
	rint('-d flag dumps canned styles to the file "%s" for your reference' % (canname,))
	rint('-m macroFileName prefixes your styles, which can override the built-ins')
	raise SystemExit

github = True
usedefs = True
maketest = False
usestdout = False
noreport = False
lnlstrip = False
wrapper = False
openit = False
whiteline = '\n'
mfilename = ''

argv = []
lookformf = False
for el in sys.argv:
	if el == '-c':
		usedefs = False
	elif el == '-o':
		openit = True
	elif el == '-l':
		lnlstrip = True
	elif el == '-p':
		usestdout = True
	elif el == '-x':
		noreport = True
	elif el == '-s':
		whiteline = ''
	elif el == '-h':
		wrapper = True
	elif el == '-d':
		try:
			fh = open(canname,'w')
			fh.write(defs)
			fh.close()
		except:
			rint('Could not write "%s" file',True)
			help()
	elif el == '-t':
		maketest = True
	elif el == '-m':
		lookformf = True
	else:
		if lookformf == False:
			argv += [el]
		else:
			lookformf = False
			mfilename = el

print str(argv)

usemfile = False
if mfilename != '':
	try:
		fh = open(mfilename)
	except:
		rint('Cannot open macro file "%s"' % (mfilename,),True)
		help()
	else:
		fh.close()
		usemfile = True

argc = len(argv)
if argc != 2 and argc != 3:
	rint('Unexpected number of arguments: %d' % (argc-1),True)
	rint('args: %s' % (str(argv[1:])),True)
	help()

ifn = argv[1]

try:
	fh = open(ifn)
except:
	tfn = ifn+'.md'
	try:
		fh = open(tfn)
	except:
		rint('Cannot open input file "%s" or "%s"' % (ifn,tfn),True)
		help()
	else:
		ifn = tfn
fh.close()

if argc == 3:
	ofn = argv[2]
else:
	ofn = ifn.replace('.md','.txt')

if noreport == False:
	rint(' Input File: "%s"' % (ifn,))
	rint('Output File: "%s"' % (ofn,))

if usedefs == False:
	defs = ''

if usemfile == True:
	fh = open(mfilename)
	chunk = fh.read()
	fh.close()
	defs += chunk

o = defs
to = ''
prevline = ''
blankline = False
thispara = ''

# change all underline-style header codes to #-stype header codes:
pline = ''

ifh = open(ifn)
xsource = []
tflag = -1
killkey = 'jncfvs8jn2247y8fajn0'
for line in ifh:
	if line[0] == '-': # this can also indicate a table header/body interspersal
		if github == True:	# then we can look for tables
			if line.find(' | ') > 0:
				line = killkey
				xsource += [pline]
			else:
				line = '# ' + pline	# title line
				pline = ''
		else:	# not github, just do titles
			line = '# ' + pline # title line
			pline = ''
	elif line[0] == '=':
		line = '## ' + pline
		pline = ''
	else:
		if pline != killkey:
			xsource += [pline]
	pline = line

xsource += [pline]
xsource += ['\n']
ifh.close()

# Escape all the characters that drive macro():
# ---------------------------------------------
source = []
tmode = -1
pipekey = 'nMbVcGhItR'
prctkey = 'uHyGtFrDeS'
for line in xsource:
	droptag = ''
	floptag = ''
	if github == True and line.find(' | ') > 0:
		tline = ''
		line = line.replace(r'\|',pipekey) 	# bury any escaped |'s
		line = line.replace(',','{comma}')	# intern commas -- we use 'em
		if tmode == -1: # header row?
			celltype = 'hcell'
			tmode += 1	# now zero
			tline += '{table '
		else: # normal row
			celltype = 'tcell'
			tmode += 1	# first line is #1 -- can pass out counter later
		celllist = line.split('|')
		tline += '{row '
		for cell in celllist:
			cell = cell.replace('%',prctkey)	# bury any existing %'s
			cell = cell.strip()
			asm = '{%s '+cell+'}'
			asm = asm % (celltype,)
			asm = asm.replace(prctkey,'%')		# restore % signs
			asm = asm.replace(pipekey,r'\|')	# restore escaped |'s
			tline += asm # add the cell to the line
		tline += '}' # close the row
		line = tline
	else:
		if tmode != -1: 	# were we in a table?
			tmode = -1		# then bail
			floptag += '}\n'	# close the table

	line = line.replace(r'\[','{lb}')
	line = line.replace(r'\]','{rb}')
	line = line.replace(r'\{','{ls}')
	line = line.replace(r'\}','{rs}')
	line = line.replace(',','{comma}')
	if floptag != '':
		source[-1] = source[-1] + floptag
		print source[-1]
	source += [line]

OUTSTATE  = 0
PARASTATE = 1
QUOTESTATE = 2
BOLDSTATE = 3
ITALICSTATE = 4
UNDERLINESTATE = 5
CODESTATE = 6

# parser for header-converted lines
# ---------------------------------	
pstate = OUTSTATE
qstate = OUTSTATE
bstate = OUTSTATE
istate = OUTSTATE
ustate = OUTSTATE
cstate = OUTSTATE
wl = whiteline

urldex = 1
verbdex = 1
urlcode  = '8gYfTdRsE4'
verbcode = '3cDvFbGnH9'
urlstash = {}
verbstash = {}

tabsize = 4

def emphasis(s):
	reject = r'([^\s\n\t])' # anything but a space, tab or return

	if 1:
		pat = r'([^\\])\*\*' + reject	# leading **
		repl = r'\1{b \2'
		s = re.sub(pat,repl,s)

	if 1:
		pat = r'([^\\])\_\_' + reject	# leading __
		repl = r'\1{b \2'
		s = re.sub(pat,repl,s)

	if 1:
		pat = reject + r'\*\*'	# trailing **
		repl = r'\1}'
		s = re.sub(pat,repl,s)

	if 1:
		pat = reject + r'\_\_'	# trailing __
		repl = r'\1}'
		s = re.sub(pat,repl,s)

	if 1:
		pat = reject + r'\*'	# trailing *
		repl = r'\1}'
		s = re.sub(pat,repl,s)

	if 1:
		pat = reject + r'\_'	# trailing _
		repl = r'\1}'
		s = re.sub(pat,repl,s)
	if 1:
		pat = r'([^\\])\*' + reject	# leading *
		repl = r'\1{i \2'
		s = re.sub(pat,repl,s)

	if 1:
		pat = r'([^\\])\_' + reject	# leading _
		repl = r'\1{i \2'
		s = re.sub(pat,repl,s)

	return s

def checklist(line):
	tabsize = 4
	depth = 0
	mstring = ''
	listtype = None
	listmode = False
	ll = len(line)
	for i in range(0,ll):
		c = line[i]
		if c == ' ':
			depth += 1
		elif c == '\t':
			depth += tabsize
		elif c >= '0' and c <= '9':
			if line[i+1:i+3] == ') ':
				listmode = True
				listtype = 0
				mstring = c+') '
				break
		elif line[i:i+2] == '* ':
			listmode = True
			listtype = 1
			mstring = '* '
			break
		else:
			break
	return listmode,listtype,depth,mstring

def makelists(lstack):
	global lnlstrip
	lmode = -1
	lo = ''
	deep = 0
	depth = -1
	for lel in lstack:
		ltype = lel[0]
		lline = lel[1]
		ldepth= lel[2]
		lline = lline.replace(',','{comma}')
		lline = lline.lstrip()
		if lnlstrip == True:
			lline = lline.rstrip()
		if ldepth > depth:		# new list, deeper
			deep += 1
			lbreak = ''
			if deep > 1:
				lbreak = '\n'
			if ltype == 0:	lo += lbreak+'{ol ' + lline
			else:			lo += lbreak+'{ul ' + lline
		elif ldepth < depth:	# previous list, shallower
			lo += '}\n'
			deep -= 1
			lo += ','+lline
		else:					# same list
			lo += ','+lline
		depth = ldepth
	while deep > 0:
		lo += '}\n'
		deep -= 1
	return lo

def inlinecode(line):
	state = 0
	oline = ''
	trigger = 0
	ll = len(line)
	for i in range(0,ll):
		c = line[i]
		if state == 0: # not inside backticks
			if line[i:i+2] == r' `':
				trigger = 1
				oline += c
			elif c == r'`' and trigger == 1:
				trigger = 0
				oline += '{inline '
				state = 1
			else:
				trigger = 0
				oline += c
		else:			# inside backticks
			if c == r'`':
				oline += '}'
				state = 0
			else:
				c = escapeForHTML(c)
				oline += c
	return oline

def forspacecode(line):
	if line[0:4] == '    ':
		line = line.replace(' ','{nbsp}')
		line = '{inline '+line.rstrip()+'}\n'
	return line

listmode = False
liststack = []

for line in source:
	llen = len(line)
	blankline = False
	consume = False
	if line.strip() == '':	# detect blank lines -- they terminate paragraphs if paras are open
		blankline = True
		line = ''
	else:					# this is not a blank line
		if cstate == OUTSTATE:
			line = line.replace('  \n','{br}\n')	# auto-append line breaks
			line = emphasis(line)
			line = inlinecode(line)
			line = forspacecode(line)

		# Handle headers
		for i in range(6,0,-1):
			if line[:i] == '#' * i:
				hc = line[i:].strip()
				h = '{h%d %s}\n%s' % (i,hc,wl)
				line = h
				consume = True

		if line[:2] == '> ':						# init or continue quote state
			if qstate != QUOTESTATE:
				qstate = QUOTESTATE
				line = '{blockquote %s' % (line[2:],)
				consume = True

		if github == True:		
			if line[:3] == '```':
				if cstate == OUTSTATE:
					cstate = CODESTATE
					lang = line.rstrip()[3:]
					if lang == '':
						lang = 'raw'
					line = '{code %s,' % (lang,)
				else:
					cstate = OUTSTATE
					line = '}\n'
			else:
				if cstate == CODESTATE:
					line = line.replace('<','{lt}')
					line = line.replace('>','{gt}')
					line = line.replace(',','{comma}')

	lmode,ltype,depth,mstring = checklist(line)
	if listmode == False:		# IF not presently in list mode
		if lmode == True:		#     IF we need to switch to list mode
			listmode = True
			line = line.replace(mstring,'',1)
			liststack += [[ltype,line,depth]]
			line = ''
			blankline = True
	else:						# ELSE already in list mode
		if lmode == True:		#    IF still in list mode
			line = line.replace(mstring,'',1)
			liststack += [[ltype,line,depth]]
			line = ''
			blankline = True
		else:					#    ELSE in, but need to get out
			o += makelists(liststack)
			liststack = []
			listmode = False

	if line.find('{row ') >= 0:
#		blankline = True
		consume = True

	if consume == False:
		if qstate == QUOTESTATE:
			if blankline == True:
				qstate = OUTSTATE
				line = '}\n%s%s' % (wl,line)
		else:
			if blankline == False:
				if pstate != PARASTATE:
					pstate = PARASTATE
					line = '{p %s' % (line,)

	if pstate == PARASTATE:
		if blankline == True:	# paragraphs end when there is a blank line or at end
			pstate = OUTSTATE
			if o[-1] == '\n':
				o = o[:-1]
			o += '}\n%s' % (wl,) # close para

	# look for images:
	tl = ''
	escape = False
	imagestate = 0
	linkstate = 0
	verbiagestate = 0
	verb = ''
	url = ''
	for c in line:
		if c == '\\':
			if escape == True:
				escape = False
				tl += c			# that's an escaped backslash
			else:				# then we've hit an escape introducer
				escape = True
		else:					# not an escape, then
			if escape == True:	# was this character preceeded by a backslash?
				tl += cape(c)	# in that case, it goes in the output verbatim
				escape = False
			else:				# otherwise, we may need to process it - url,verb::stash,dex,code
				if c == '!':	# image introducer?
					imagestate = 1
				elif c == '[':	# verbiage introducer?
					verb = ''
					verbiagestate = 1
				elif c == ']':	# done with verbiage?
					verbiagestate = 0
				elif c == '(':	# url introducer?
					url = ''
					linkstate = 1
				elif c == ')':	# done with url?
					if url == '': # apparently, just some hanging parens
						tl += '()' # throw em back like the dead fish they are
						imagestate = 0
						linkstate = 0
					else:
						vcode = '%s%d' % (verbcode,verbdex)
						ucode = '%s%d' % (urlcode,urldex)
						verbdex += 1
						urldex += 1
						urlstash[ucode] = url
						verbstash[vcode] = verb
						if imagestate == 1:	# was this an image?
							tl += '{img %s,%s}' % (vcode,ucode)
						else:				# nope, hadda be a link
							tl += '{a %s,%s}' % (vcode,ucode)
						imagestate = 0
						linkstate = 0
				else:	# incoming!
					if linkstate == 1:
						url += c
					elif verbiagestate == 1:
						verb += c
					else:						# it's just a character
						tl += c
		line = tl

	o += line

# Every line read; close any open states
if cstate == CODESTATE:
	if o[-1] == '\n':
		o = o[:-1]
	o += '}\n'
	
if qstate == QUOTESTATE:
	if o[-1] == '\n':
		o = o[:-1]
	o += '}\n'

if pstate == PARASTATE:
	if o[-1] == '\n':
		o = o[:-1]
	o += '}\n'

# Here, we replace raw URLs that are floating around the document:
# ----------------------------------------------------------------
pat = r'([hH][tT][tT][pP]\:\/\/.*?)\s'
repl = '{a \\1,\\1} '
o = re.sub(pat,repl,o)

# Then we replace the url and verb codes with the actual urls and verbs
# ---------------------------------------------------------------------
for key in verbstash.keys():
	o = o.replace(key,verbstash[key])
for key in urlstash.keys():
	o = o.replace(key,urlstash[key])

if wrapper == True:
	o = """<HTML>
<HEAD>
<TITLE>macro() HTML test output page</TITLE>
</HEAD>
<BODY>
%s
</BODY>
</HTML>
""" % (o,)

if usestdout == True:
	rint(o)
else:
	ok = True
	try:
		ofh = open(ofn,'w')
	except:
		rint('Cannot open output file "%s"' % (ifn,),True)
		help()

	try:
		ofh.write(o)
	except:
		rint('ERROR: Could not complete write to "%s"' % (ofn,),True)
		ok = False
	try:
		ofh.close()
	except:
		rint('ERROR: Could not close "%s"' % (ofn,),True)
		ok = False

if maketest == True:
	mod = macro()
	oo = mod.do(o)
	ok = True
	try:
		fh = open(testfilename,'w')
	except:
		rint('ERROR: Could not open "%s"' % (testfilename,),True)
		ok = False
	else:
		try:
			fh.write(oo)
		except:
			rint('ERROR: Could not complete write to "%s"' % (testfilename,),True)
			ok = False
		try:
			fh.close()
		except:
			rint('ERROR: Could not close "%s"' % (tetsfilename,),True)
			ok = False
		if ok == True:
			if openit == True:
				cmd = 'open %s' % (testfilename)
				os.system(cmd)
