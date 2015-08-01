#!/usr/bin/python

# Convert markdown file source files to aa_macro source files

import sys
import re
from aa_macro import *

ecape = {	'[':'{lb}',']':'{rb}',
			'{':'{ls}','}':'{rs}',
		}

def cape(c):
	return ecape.get(c,c)

testfilename = "mtmtestfile.html"

def help():
	print '()=required, |= "or", []=optional'
	print 'USE: (python|./) martomac.py [-c] [-s] [-t] inputFilename[.md] [outputFilename]'
	print "-c flag suppresses leading default style definitions, supply your own"
	print "-s flag suppresses blank lines between block elements"
	print '-t flag creates macro() processed output test file "%s"' % (testfilename)
	raise SystemExit

usedefs = True
maketest = False
whiteline = '\n'
argv = []
for el in sys.argv:
	if el == '-c':
		usedefs = False
	elif el == '-s':
		whiteline = ''
	elif el == '-t':
		maketest = True
	else:
		argv += [el]

print str(argv),maketest

argc = len(argv)
if argc != 2 and argc != 3:
	print 'Unexpected number of arguments: %d' % (argc-1)
	print 'args: %s' % (str(argv[1:]))
	help()

ifn = argv[1]

try:
	fh = open(ifn)
except:
	tfn = ifn+'.md'
	try:
		fh = open(tfn)
	except:
		print 'Cannot open input file "%s" or "%s"' % (ifn,tfn)
		help()
	else:
		ifn = tfn
fh.close()

if argc == 3:
	ofn = argv[2]
else:
	ofn = ifn.replace('.md','.txt')

print ' Input File: "%s"' % (ifn,)
print 'Output File: "%s"' % (ofn,)

try:
	ofh = open(ofn,'w')
except:
	print 'Cannot open output file "%s"' % (ifn,)
	help()

defs = ''
if usedefs == True:
	defs = """[style h1 <h1>[b]</h1>]  
[style h2 <h2>[b]</h2>]  
[style h3 <h3>[b]</h2>]  
[style h4 <h4>[b]</h4>]  
[style h5 <h5>[b]</h5>]  
[style h6 <h6>[b]</h6>]  
[style br <br>]  
[style lb [lb]]  
[style rb [rb]]  
[style ls [ls]]  
[style rs [rs]]  
[style p [p [nl][b][nl]]]  
[style b [b [b]]]  
[style i [i [b]]]  
[style u [u [b]]]  
[style blockquote <blockquote>[nl][b][nl]<blockquote>]  
[style img [split [co],[b]][img [parm 0],[parm 1]]]  
[style a [split [co],[b]][a [parm 1],[parm 0]]]  
"""
o = defs
to = ''
prevline = ''
blankline = False
thispara = ''

# change all underline-style header codes to #-stype header codes:
source = []
pline = ''

ifh = open(ifn)
for line in ifh:
	if line[0] == '-':
		line = '# ' + pline
		pline = ''
	elif line[0] == '=':
		line = '## ' + pline
		pline = ''
	else:
		if pline != '':
			source += [pline]
	pline = line
ifh.close()

if pline != '':
	source += [pline]

OUTSTATE  = 0
PARASTATE = 1
QUOTESTATE = 2
BOLDSTATE = 3
ITALICSTATE = 4
UNDERLINESTATE = 5
# parser for header-converted lines
# ---------------------------------	
pstate = OUTSTATE
qstate = OUTSTATE
bstate = OUTSTATE
istate = OUTSTATE
ustate = OUTSTATE
wl = whiteline

urldex = 1
verbdex = 1
urlcode  = '8gYfTdRsE4'
verbcode = '3cDvFbGnH9'
urlstash = {}
verbstash = {}

for line in source:
	llen = len(line)
	blankline = False
	consume = False
	if line.strip() == '':	# detect blank lines -- they terminate paragraphs if paras are open
		blankline = True
		line = ''
	else:					# this is not a blank line
		line = line.replace('  \n','{br}\n')	# auto-append line breaks

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

# Every line read; close and open states
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
	print key,verbstash[key]
for key in urlstash.keys():
	o = o.replace(key,urlstash[key])
	print key,urlstash[key]

try:
	ofh.write(o)
except:
	print 'ERROR: Could not complete write to "%s"' % (ofn,)
try:
	ofh.close()
except:
	print 'ERROR: Could not close "%s"' % (ofn,)

if maketest == True:
	mod = macro()
	oo = mod.do(o)
	try:
		fh = open(testfilename,'w')
	except:
		print 'ERROR: Could not open "%s"' % (testfilename,)
	else:
		try:
			fh.write(oo)
		except:
			print 'ERROR: Could not complete write to "%s"' % (testfilename,)
		try:
			fh.close()
		except:
			print 'ERROR: Could not close "%s"' % (tetsfilename,)
