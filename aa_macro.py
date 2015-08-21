#!/usr/bin/python

import re
import imghdr
import struct

class macro(object):
	"""Class to provide an HTML macro language
      Author: fyngyrz  (Ben)
     Contact: fyngyrz@gmail.com (bugs, feature requests, kudos, bitter rejections)
     Project: aa_macro.py
    Homepage: https://github.com/fyngyrz/aa_macro
     License: None. It's free. *Really* free. Defy invalid social and legal norms.
 Disclaimers: 1) Probably completely broken. Do Not Use. You were explicitly warned. Phbbbbt.
              2) My code is blackbox, meaning I wrote it without reference to other people's code
              3) I can't check other people's contributions effectively, so if you use any version
                 of aa_macro.py that incorporates accepted commits from others, you are risking
                 the use of OPC, which may or may not be protected by copyright, patent, and the
                 like, because our intellectual property system is pathological. The risks and
                 responsibilities and any subsequent consequences are entirely yours. Have you
                 written your congresscritter about patent and copyright reform yet?
  Incep Date: June 17th, 2015     (for Project)
     LastRev: August 21st, 2015     (for Class)
  LastDocRev: August 21st, 2015     (for Class)
 Tab spacing: 4 (set your editor to this for sane formatting while reading)
    Policies: 1) I will make every effort to never remove functionality or
                 alter existing functionality. Anything new will be implemented
                 as something new, thus preserving all behavior and the API.
                 The only intentional exceptions to this are if a bug is found
                 that does not match the intended behavior, or I determine there
                 is some kind of security risk. What I *will* do is not document
                 older and less capable versions of a function, unless the new
                 functionality is incapable of doing something the older
                 version(s) could do.
    Examples: At bottom. Run in shell like so:    python aa_macro.py
              The best way to use them is open a shell and run them there,
			  and open a shell with aa_macro.py in an editor or reader,
			  then scroll through the example results in the one shell as
			  you peruse the source for them in the other within aa_macro.py
     Testing: python test_aa_macro.py
 Typical Use: from aa_macro import *
              mod = macro()
              mod.do(text)
     Warning: Do NOT use this to parse general user input without fully sanitizing that
	          input for subsequent string processing in Python FIRST, as well as for
			  output via your webserver (because <script>, etc.) Otherwise, you've
			  just created a huge security hole. Not Good! The default intention is that
			  class macro() is for authoring by you, the person who ISN'T trying to
			  hack your website, not access to the public, which may very well contain
			  someone who wants to do you wrong. Having said that, see the sanitize()
			  utility function within this class.
     1st-Rel: 1.0.0
     Version: 1.0.34
     History:                    (for Class)
	 	1.0.34
			* added [lpop], [lpush] (synonym for append)
	 	1.0.33
			* Moved the 'dothis' named parameter to first in class for simplest invocation
	 	1.0.32
			* added [lslice]
	 	1.0.31
			* added [llen]
	 	1.0.30
			* added [hsort], [lhsort]
	 	1.0.29
			* added [strip]
	 	1.0.28
			* added [soundex]
	 	1.0.27
			* added [count]
	 	1.0.26
			* added [lc], [wc]
	 	1.0.25
			* added [dtohex], [dtooct], [dtobin], [htodec], [otodec], [btodec]
	 	1.0.24
			* added [gpage],[ghost]
	 	1.0.23
			* added [max], [min]
	 	1.0.22
			* added [ltol]
	 	1.0.21
			* added [scase]
	 	1.0.20
			* added [ssort], [sisort], [issort]
	 	1.0.19
			* added [capw], [caps], [capt], [inter]
	 	1.0.18
			* added (sep=X,) option to [push]
	 	1.0.17
			* added [rjust],[ljust],[center]
			* added sep=X to [list] options
			* added sep=X to [ul] options
			* added sep=X to [ol] options
			* added sep=X to [iful] options
			* added sep=X to [ifol] options
	 	1.0.16
			* added [find],[replace]
	 	1.0.15
			* added [rstrip],[ord],[dup]
	 	1.0.14
			* added [list],[lset],[e],[cmap],[translate],[asort],[aisort],[isort],[dlist],[append]
			* added [splitcount]
	 	1.0.13
		    * added [eq] to complement [ne]
	 	1.0.12
			* added [locimg] to generate images with width and height set (jpg,png,gif)
			* added [lipath] to tell [locimg] where image file is in local filesystem
	 	1.0.11
			* added [urlencode]
	 	1.0.10
			* added [nl] for non-newline newline encoding in source (0x0a)
			* [img] now sets alt= as well as title=
	 	1.0.9
			* added [bq] for HTML blockquote
	 	1.0.8
			* added [mode] to control HTML output mode from source
			* added [back] to control HTML 4.01s background text color from source
			* added __str__() method for output of initially passed-in input in dothis
	 	1.0.7
			* enhanced [img]
			* fixed bug in [web]
			* fixed bug in parser. Regex, sigh. Live by it, die by it.
			* if you end a line with two trailing spaces, object.do()
			  will "eat" them, and the following newline, unles you
			  set nodinner=True
        1.0.6
     	    * added sanitize() utility to help make user input safer
     		* sped up [roman numberString] when fed zero
     		* added home page to class header
     		* added polcies to class header
     		* updated class documentation
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

==> Anything with a * in the first column needs recoding to incorporate (sep=X,)

	Available built-ins:
	====================
	Note that () designate optional parameters, a|b designates alternate parameter a or b

	Text Styling
	------------
	[p paraText]
	[bq quotetext]
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
	[urlencode URL]					# converts certain chars to character entities, etc.:
	                                  '"'='&quot;', ' '='+', '&'='&amp;'
	
	Images
	------
	[img (title,)URL( linkTarget)]		# makes a link if linktarget present
	[lipath localImagePath]				# sets path to local images. This is used by [locimg] to
										  find the image and read it to obtain x,y dimensions
										  [lipath] first, then [locimg]
	[locimg (title,)URL( linkTarget)]	# makes a link if linktarget present, also inserts img size
										# [locimg] can read the size of jpg, png, and gif
										# Examples:
			[lipath]
			[locimg mypic.png]					- image in same dir as python cmd on host
												- and in / of webserver
			[lipth /usr/www/mysite.com/htdocs/]
			[locimg mypic.png]					- image in /usr/www/mysite.com/htdocs/ on host
												- and in / of webserver

			[lipth /usr/www/mysite.com/htdocs/pics/]
			[locimg pics/mypic.png]				- image in /usr/www/mysite.com/htdocs/pics/ on host
												- and in /pics/ of webserver
	
	HTML Lists
	----------
	[ul (wrap=style,)(sep=X,)item1(Xitem2Xitem3...)]
	[ol (wrap=style,)(sep=X,)item1(Xitem2Xitem3...)]
	[iful (wrap=style,)(sep=X,)item1(Xitem2Xitem3...)] - more than one item makes a list
	[ifol (wrap=style,)(sep=X,)item1(Xitem2Xitem3...)] - more than one item makes a list
	[t (wrap=style,)(sep=X,)item1(Xitem2Xitem3...)]
 
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
	[page]											# reset local environment: variables
													  global variables are unaffected

	Data Lists
	----------
	[append listname,item]							# add an item to the end of a list
	[lpush listname,item]							# add an item to the end of a list (synonym for [append])
	[slice sliceSpec,listToSlice,resultList]		# [lslice 3:6,mylist,mylist] or [lslice 3:6,myList,otherList]
	[lpop listName(,index)]							# [lpop] == [lpop -1] remove list item
	[lset listName,index,stuff]						# set a list item by index (must exist)
	[llen listName]									# length of list
	[cmap listName]									# creates 256-entry list of 1:1 8-bit char mappings
	[dlist (style=X,)listName]						# output list, optionally wrapped with style X
	[translate listName,text]						# characters are mapped to listName (see examples)
	[scase listName,content]						# Case words as they are cased in listName
	[ltol listName,content]							# splits lines into a list
	[list (sep=X,)listName,item(Xitem)]				# Create list: sep default: ','
													  [list mylist,a,b,c]
													  [list sep=|,myblist,nil|one|2|0011|IV|sinco]
	[e listName,index]								# fetch an item from a list, base of zero:
													  [e mylist,0] = 'a'
													  [e myblist,4] = 'IV'
	[asort listName]								# sort the list as case-sensitive text
	[aisort listName]								# sort the list as case-insensitive text
	[lhsort listName]								# sort the list by leading ham radio callsign
	[isort (sep=x,)listName]						# sort the list according to a leading numeric value
													  ie [1,this thing][2,that thing] sep default: ','

	Dictionaries
	------------
	[dict (sep=X,)(keysep=Y,)dictName,keyYvalue(XkeyYvalue)] # create multivalue dictionary
	[dset (keysep=Y,)dictName,keyYvalue]			# set a single dictionary value (can create dict)
	[d dictName,key]								# retrieve a single dictionary value

	Stack
	-----
	[push (sep=X,)(nX)CONTENT]						# push CONTENT n deep onto stack. 1 is the same as no N.
	[pop]											# pop stack. If stack empty, does nothing.
	[fetch (N)]										# get element N from stack but no pop. 0 is top, no N = 0
	[flush]											# toss out entire stack

	Math
	----
	[add value addend]								# add a number to a number
	[sub value subtrahend]							# subtract a number from a number
	[mul value multiplier]							# multiply a number by a number
	[div value divisor]								# divide a number by a number
	[max v1 v2]										# return larger value
	[min v1 v2]										# return smaller value
	[inc value]										# add one to a number
	[dec value]										# subtract one from a number

	Conditionals
	------------
*	[even value conditionalContent]					# use conditional content if value is even
*	[odd value conditionalContent]					# use conditional content if value is odd
*	[if value match conditionalContent]				# use conditional content if value == match
*	[else value match conditionalContent]			# use conditional content if value != match
*	[ne value,conditionalContent]					# use conditional content if value Not Empty
*	[eq value,conditionalContent]					# use conditional content if value Empty
	
	
	Parsing and text processing
	---------------------------
	[slice sliceSpec,contentToSlice]				# [slice 3:6,foobarfoo] = bar ... etc.
	[splitcount N]									# limit number of splits to N for next split ONLY
*	[split splitSpec,contentToSplit]				# [split |,x|y|z] results in parms 0,1,2
													  Because a comma is used to separate the
													  splitSpec from the contentToSplit, you
													  can't just use a comma directly. But
													  there is a syntax to support it...
													     [split [co],contentToSplit]]
													  ...where contentToSplit is separated by
													  actual commas. Comes in handy sometimes.
													  Obeys [splitcount]
	[parm N]										# per above [split, [parm 1] results in y
	[upper textString]								# convert to uppercase
	[lower textString]								# convert to lowercase
	[rstrip content]								# remove trailing whitespace
	[len content]									# return length of content in characters
	[lc content]									# return length of content in lines
	[wc content]									# return length of content in words
	[wwrap (wrap=style,)col,content]				# wrap content at col - styles usually want newlines
	[roman decNumber]								# convert decimal to roman (1...4000)
	[dtohex decNumber]								# convert decimal to hexadecimal
	[dtooct decNumber]								# convert decimal to octal
	[dtobin decNumber]								# convert decimal to binary
	[htodec hexNumber]								# convert hexadecimal to decimal
	[otodec octNumber]								# convert octal to decimal
	[btodec binNumber]								# convert binary to decimal
	[chr number]									# e.g. [chr 65] = "A"
	[ord character]									# e.g. [ord A] = "65"
	[csep integer]									# e.g. [csep 1234] = "1,234"
	[fcsep integer]									# e.g. [fcsep 1234.56] = "1,234.56"
	[soundex content]								# returns soundex code
	[strip content]									# strip out HTML tags
	[dup count,content]								# e.g. [dup 3,foo] = "foofoofoo"
	[find (sep=X,)thisStringXinString]				# returns -1 if not found, X default=,
	[count (overlaps=yes)(casesens=yes,)(sep=X,)patternXcontent] # count term occurances in content
	[replace (sep=X,)thisStrXwithStrXinStr]			# e.g. [replace b,d,abc] = "adc" X default=,
	[caps content]									# Capitalize first letter of first word
	[capw content]									# Capitalize first letter of every word
	[capt content]									# Use title case (style: U.S. Government Printing Office Style Manual)
	[specialcase listName,content]					# Case words as they are cased in listName
	[ssort content]									# sort lines cases-INsensitive
	[sisort content]								# sort lines cases-sensitive
	[issort content]								# sort lines by leading integer,comma,content
	[hsort content]									# sort lines by leading ham radio callsign
	[inter iStr,L|R,everyN,content]					# intersperse iStr every N in content from left or right
*	[rjust width,padChar,content]					# e.g. [rjust 6,#,foo] = "###foo"
*	[ljust width,padChar,content]					# e.g. [ljust 6,#,foo] = "foo###"
*	[center width,padChar,content]					# e.g. [center 7,#,foo] = "##foo"
													  negative width means pad both sides:
														   [center -7,=,foo] = "==foo=="

	Misc
	----
	[repeat count content]							# repeat content count times
	[comment content]								# content does not render
	[back HEX3|HEX6]								# set back color for HTML 4.01s operations
	[mode 3.2|4.01s]								# set HTML version/mode
	
	Escape Codes:
	-------------
	[co]							# produces HTML ',' as &#44;
	[sp]							# produces HTML ' ' as &#32;
	[lb]							# produces HTML '[' as &#91;
	[rb]							# produces HTML ']' as &#93;
	[ls]							# produces HTML '{' as &#123;
	[rs]							# produces HTML '}' as &#125;
	[lf]							# produces HTML newline (0x0a)
	
	Styles
	------
	[style styleName Style]			# Defines a local style. Use [b] for body of style
	[gstyle styleName]				# Defines a global style. Use [b] for body of style

	[s styleName contentToStyle]	# contentToStyle goes where [b] tag(s) is/are in style...
									  uses local style, if doesn't exist, then uses global style

	[glos styleName contentToStyle]	# contentToStyle goes where [b] tag(s) is/are in style...
									  only uses global styles

	[locs styleName contentToStyle]	# contentToStyle goes where [b] tag(s) is/are in style...
									  only uses local styles

	{styleName contentToStyle}		# ...same as [s styleName], but simplified "squiggly" syntax

	==> Only if crtospace is True:
	{styleNameNLcontentToStyle}		# ...same thing, but simplified "squiggly" syntax
									# NL is a *nix newline, 0x0A

	[spage]							# reset local environment: styles
									  global styles are unaffected
	
	More on styles:
	---------------
	Styles give you ultimate power in creating your own text processing tool.

	Styles are pretty easy to understand. You can have as many as you want, and they
	can contain other styles, presets and so on. There are two components to styles;
	defining them, and using them.
	
	Here's a simple style definition:

        +-- DEFINE a style
        |      +-- name of style
        |      |      +-- beginning of style
        |      |      |       +-- where the content fed to the style will go
        |      |      |       |  +-- rest of pre-defined style
        |      |      |       |  |        +-- ends style definition
        |      |      |       |  |        |
		[style strike <strike>[b]</strike>]

	So now to use that, you do this:

        +-- USE a style
        |  +-- name of style to use
        |  |      +-- the content that goes where the [b] tag(s) is/are in the style
        |  |      |     +-- ends style content
        |  |      |     |
        [s strike me out]

	Or you can do this, which is intended to be more readable and convenient:

        +-- USE a style
        |+-- name of style to use
        ||      +-- the body that goes where the [b] tag(s) is/are in the style
        ||      |     +-- ends style content
        ||      |     |
		{strike me out}

	Either of which will come out of object.do() as:

		<strike>me out</strike>

	You can also break the content into multiple parameters and use them individually
	using a combination of the [split] and [parm] functions. See the examples at the
	end of this file for details on that.

	You can nest more or less indefinitely:
	---------------------------------------
	[b bold text [s strike [i bold and italic text]]]

	Parameters to object instantiation:
	-----------------------------------
	mode ------ '3.2'  (default) or '4.01s' to set HTML rendering mode
	nodinner -- True   (default) or False eats sequences of two spaces followed by a newline
	back ------ ffffff (default) HEX3 or HEX color for background color in HTML 4.01s mode
	dothis ---- None   (default) you can pass in initial text to be processed here if you like
	            the object returns the result in its string method:
					mod = macro(dothis='[style x foo [b]]'{x bar})
					print mod # prints 'foo bar'

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
	  Also see [nc contentToConvertCommasIn], which is a handy way to see to it that your
	  content can have commas, but the macro system won't see them. Of course, you can't
	  use that on anything that *needs* commas for parameters. Life is so complicated. :)

"""
	def __init__(self,dothis=None,mode='3.2',back="ffffff",nodinner=False):
		self.setMode(mode)
		self.setBack(back)
		self.setNoDinner(nodinner)
		self.page()
		self.setFuncs()
		self.resetLocals()
		self.resetLists()
		self.resetDicts()
		self.resetGlobals()
		self.placeholder = 'Q|zXaH7RppY#32m' # hopefully you'll never use this string, lol
		self.styles = {}
		self.gstyles = {}
		self.stack = []
		self.parms = []
		self.padCallLocalToggle = 0
		self.padCallLocalRegion = -1
		self.sexdigs = '01230120022455012623010202'
		self.romans = ['m','cm','d','cd','c','xc','l','xl','x','ix','v','iv','i']
		self.integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
		self.notcase = ['a','an','the','at','by','for',
						'in','of','on','to','up','and','as',
						'but','or','nor']
		self.result = ''
		self.lipath = ''
		self.splitCount = 0
		if dothis != None:
			self.do(dothis)

	def __str__(self):
		return self.result

	def setNoDinner(self,nd=False):
		if nd != False:
			nd = True
		self.noDinner = nd

	def cReduce(self,txtCall):
		l = re.split('([0-9]*)',txtCall.upper(),1)
		if len(l) != 3:
			return 'z',0,'t'
		return l[0],int(l[1]),l[2]

	def sCallsignKeyF(self,line):
		txtCall = ''
		for c in line:
			if ((c >= 'a' and c <= 'z') or
				(c >= 'A' and c <= 'Z') or
				(c >= '0' and c <= '9')):
				txtCall += c
			else:
				break
		a,b,c = self.cReduce(txtCall)
		return b,a,c

	def gis(self,fn):
		def rhead(fn, length):
			try:
				fh = open(fn)
				content = fh.read(length)
				fh.close()
			except:
				return ''
			if len(content) != length:
				return ''
			return(content)

		x = 0
		y = 0
		insmell = '<'
		moto = '>'
		int4 = 'i'
		uint16 = 'H'
		try:
			it = imghdr.what(fn)
		except:
			return 'unable to handle "%s"' % (fn,)
		if it == 'jpeg':
			try:
				fh = open(fn)
				sz = 2; ft = 0
				while not 0xC0 <= ft <= 0xCF:
					fh.seek(sz,1)
					b = fh.read(1)
					while ord(b) == 0xFF: b = fh.read(1)
					sz = struct.unpack(moto + uint16,fh.read(2))[0]-2
					ft = ord(b)
				fh.seek(1,1)
				y,x = struct.unpack(moto + uint16 + uint16, fh.read(4))
			except:
				try:
					fh.close()
				except:
					pass
				return 'unable to parse "%s"' % (fn,)
			fh.close()		
		elif it == 'gif':
			header = rhead(fn, 10)
			if header == '': return '"%s" is pathological' % (fn,)
			x,y = struct.unpack(insmell + uint16 + uint16, header[6:10])
		elif it == 'png':
			header = rhead(fn, 24)
			if header == '': return '"%s" is pathological' % (fn,)
			x,y = struct.unpack(moto + int4 + int4, header[16:24])
		else:
			return 'unhandled image type: "%s"' % (it,)
		return x,y

	def sanitize(self,
	             s,												# input string
	             uwl='',										# user whitelist
	             ubl=[],										# user blacklist
	             wl=' []{}()<>~/!@#$%^&*_-+=;:",.?/|\t\n"'+"'",	# default whitelist
	             bl=['<script','<!--#'],						# default blacklist
	             linelimit=0,									# lines truncate at nonzero linelimit
	             newline='\n',									# character that delineates a line
	             limit=0,										# string truncate at nonzero length
	             pre=True,										# limit entire string length prior to line limits
	             report=True,									# provide error reports
	             dt=True):										# defeat HTML tags flag
		"""Utility to clean user-provided text of things you don't want in it.
sanitize() provides character whitelisting and string blacklisting.
sanitize() allows letters and numbers through, as well as the
characters in dwl and wl, while stripping out any string in the
ubl or bl lists.

If you don't like the defaults, you can over-ride wl and/or bl with
'' and [] respectively and feed in uwl and/or ubl instead; or, you
can leave wl and/or bl alone, and extend either or both with uwl and/or
ubl.

If something is found that is in one of the blacklists, the returned
string will have all <> characters converted into HTML entities,
which will prevent any tag from working. If you don't want this
behavior, set nff=False.

If you set linelimit to a non-zero value, the string will be treated
as lines delineated by the newline character, and each line that exceeds
a length of linelimit will be truncated to linelimit-1, plus a newline
character, so the resulting lines are guaranteed to be at or under
linelimit in size. Terminating newlines are preserved. You can set
newline to any character you want.

If you set limit to a non-zero value, strings that are longer than
that number will be truncated to that size. Any terminating newline is
not preserved. If pre is True (the default), this limit is processed
prior to any processing of linelimit.

On return, you get the string back, and a list that may contain warnings
about any issues if report=True (the default):

    ['cs ordinal'] means that non-whitelisted character was stripped
    ['ss stripcount oldsize'] means that the string of oldsize was stripcount too long
    ['ls stripcount oldsize'] means that a line of oldsize was stripcount too long
    ['bs] means that one or more blacklisted strings were stripped
    ['hc'] means that < and/or > were present after ['bs'] and converted to HTML entities

The contents of the list are safe to include in the output if you like.
"""
		o = ''
		warnings = []
		s = str(s)
		if pre == True:
			if limit != 0:
				ct = len(s)
				if ct > limit:
					s = s[:limit]
					if report == True: warnings += ['ss %d %d' % (ct,ct-limit)]
		if linelimit != 0:
			ull = linelimit - 1
			to = ''
			slist = s.split(newline)
			lastflag = False
			for line in slist:
				ct = len(line)
				if ct > ull:
					line = line[0:linelimit]
					if report == True: warnings += ['ls %d %d' % (ct,ct-ull)]
				line += newline
				to += line
			if len(to) > 0:
				to = to[0:-1]
			s = to
		if pre != True:
			if limit != 0:
				ct = len(s)
				if ct > limit:
					s = s[:limit]
					if report == True: warnings += ['ss %d %d' % (ct,ct-limit)]
		for c in s:
			if ((c >= '0' and c <= '9') or
			    (c >= 'A' and c <= 'Z') or
			    (c >= 'a' and c <= 'z') or
			    (c in wl) or
			    (c in uwl)):
				o += c
			else:
				if report == True: warnings += ['cs '+str(ord(c))]
		nf = o
		for f in bl:
			o = o.replace(f,'')
		for f in ubl:
			o = o.replace(f,'')
		if nf != o:
			if report == True: warnings += ['bs']
			if dt == True:
				nf = o
				o = o.replace('<','&lt;')
				o = o.replace('>','&gt;')
				if nf != o:
					if report == True: warnings += ['hs']
		return o,warnings

	def resetGlobals(self):
		self.theGlobals = {}
		self.gstyles = {}

	def resetLocals(self):
		self.theLocals = {}
		self.styles = {}

	def resetDicts(self):
		self.theDicts = {}

	def resetLists(self):
		self.theLists = {}

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

	def popts(self,olist,data):
		plist = data.split(',')
		ropts = []
		run = True
		while run == True:
			hit = False
			for el in olist:
				el += '='
				l = len(el)
				if plist[0][:l] == el:
					ropts += [[el,plist[0][l:]]]
					plist.pop(0)
					hit = True
			if hit == False:
				run = False
			result = ''
			for el in plist:
				if result != '':
					result += ','
				result += el
		return ropts,result

	# [llen listName]
	def llen_fn(self,tag,data):
		ll = self.theLists.get(data,[])
		return str(len(ll))

	# [wwrap (wrap=style,)cols,content]
	def wwrap_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['wrap'],data)
		wrap = ''
		for el in opts:
			if el[0] == 'wrap=':
				t = self.styles.get(el[1],'')
				if t != '':
					wrap = el[1]
		p = data.split(',',1)
		if len(p) == 2:
			try:
				col = int(p[0])
			except:
				pass
			else:
				llist = p[1].split('\n')
				if len(llist) != 0:
					wlist = []
					for el in llist:
						if el != '':
							el = el.replace('\t',' ')
							oel = ''
							while oel != el:
								oel = el
								el = el.replace('  ',' ')
							el = el.strip()
							wlist += el.split(' ')
					ll = 0
					bol = True
					li = ''
					for w in wlist:
						uw = w
						if bol != True:
							uw = ' ' + w
						wl = len(uw)
						if ll + wl > col:	# then wrap exceeded
							if bol == True:	# 	then word is longer than wrap can handle
								li = w
								w = ''
							# current line is ready for output
							# --------------------------------
							if wrap != '':	# use style?
								o += self.do('[s ' + wrap + ' ' + li + ']')
							else:			# no style
								o += li + '\n'
							bol = True
							li = w
							ll = len(li)
							if ll != 0:
								bol = False
						else:				# ll not exceeded, join word to line
							bol = False
							li += uw
							ll += wl
					if ll != '':	# IF line pending
						if wrap != '':	# IF use style
							o += self.do('[s ' + wrap + ' ' + li + ']')
						else:			# ELSE no style
							o += li + '\n'
		return o

	def hsort_fn(self,tag,data):
		o = ''
		tlist = data.split('\n')
		if len(tlist) > 1:
			tlist = sorted(tlist,key=self.sCallsignKeyF)
			o = '\n'.join(tlist)
		return o

	def lhsort_fn(self,tag,data):
		tlist = self.theLists.get(data,[])
		if len(tlist) > 1:
			tlist = sorted(tlist,key=self.sCallsignKeyF)
			self.theLists[data] = tlist
		return ''

	def olpcount(self,string,pattern):
		l = len(pattern)
		ct = 0
		for c in range(0,len(string)):
			if string[c:c+l] == pattern:
				ct += 1
		return ct

	# [strip htmlContent]
	def strip_fn(self,tag,data):
		return re.sub(r'<[^>]*>','',data)

	# [count (overlaps=yes,)(casesens=yes,)(sep=X)patternXcontent]
	def count_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['casesens','sep','overlaps'],data)
		if data != '':
			cs = False
			sep = ','
			over = False
			for el in opts:
				if el[0] == 'sep=':
					sep = el[1]
				elif el[0] == 'casesens=' and el[1] == 'yes':
					cs = True
				elif el[0] == 'overlaps=' and el[1] == 'yes':
					over = True
			p = data.split(sep)
			if len(p) == 2:
				term,content = p
				if cs == False:
					term = term.lower()
					content = content.lower()
				if over == True:
					o = str(self.olpcount(content,term))
				else:
					o = str(content.count(term))
		return o

	# [soundex (len=n,)lastName]
	# as per Knuth's algorithm in vol 3 of "The Art of Computer Programming", pub 1968
	def sex_fn(self,tag,data):
		opts,data = self.popts(['len'],data)
		slen = 4
		for el in opts:
			if el[0] == 'len=':
				try:
					slen = int(el[1])
				except:
					slen = 4
		o = ''
		if data != '':
			first = ''
			soundex = ''
			base = ord('a')
			name = data.lower()
			for c in name:
				oc = ord(c)
				if first == '':
					first = c
				dex = oc - base
				try:
					sex = self.sexdigs[dex]
				except:
					sex = '0'
				if soundex == '' or sex != soundex[-1]:
					soundex += sex
			soundex = first + soundex[1:]
			soundex = soundex.replace('0','')
			ll = len(soundex)
			if ll < slen:
				soundex += '0' * (slen - ll)
			o = soundex[:slen].upper()
		return o
		

	# [lc content]
	def lc_fn(self,tag,data):
		if data == '': return '0'
		llist = data.split('\n')
		return str(len(llist))

	# [wc content]
	def wc_fn(self,tag,data):
		if data == '': return '0'
		wc = 0
		llist = data.split('\n')
		for line in llist:
			wlist = line.split(' ')
			wc += len(wlist)
		return str(wc)

	# [dtohex decNumber]
	def d2h_fn(self,tag,data):
		o = ''
		try:
			n = int(data)
		except:
			pass
		else:
			o = '%x' % (n,)
		return o

	# [dtoct decNumber]
	def d2o_fn(self,tag,data):
		o = ''
		try:
			n = int(data)
		except:
			pass
		else:
			o = '%o' % (n,)
		return o

	# [dtobin decNumber]
	def d2b_fn(self,tag,data):
		o = ''
		try:
			n = int(data)
		except:
			pass
		else:
			o = bin(n)[2:]
		return o

	# [htodec hexNumber]
	def h2d_fn(self,tag,data):
		o = ''
		try:
			o = str(int(data,16))
		except:
			pass
		return o

	# [otodec octNumber]
	def o2d_fn(self,tag,data):
		o = ''
		try:
			o = str(int(data,8))
		except:
			pass
		return o

	# [btod binNumber]
	def b2d_fn(self,tag,data):
		o = ''
		try:
			o = str(int(data,2))
		except:
			pass
		return o

	# [ghost (source=local|global,)styleName]
	def ghost_fn(self,tag,data):
		opts,data = self.popts(['source'],data)
		slocal = False
		sglobal = False
		for el in opts:
			if el[0] == 'source=':
				if el[1] == 'global':
					sglobal = True
				if el[1] == 'local':
					slocal = True
		if slocal == True:
			o = self.styles.get(data,'')
		elif sglobal == True:
			o = self.gstyles.get(data,'')
		else:
			o = self.styles.get(data,self.gstyles.get(data,''))
		return o

	# [ltol listName,content]
	def ltol_fn(self,tag,data):
		o = ''
		parms = data.split(',',1)
		if len(parms) == 2:
			if parms[0] != '':
				llist = parms[1].split('\n')
				self.theLists[parms[0]] = llist
		return o

	def dict_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['keysep','sep'],data)
		wraps = ''
		sep = ','
		keysep = ':'
		for el in opts:
			if el[0] == 'keysep=':
				keysep = el[1]
			elif el[0] == 'sep=':
				sep = el[1]
				if sep == '': return o
		parms = data.split(',',1)
		if len(parms) != 2: return o
		lname = parms[0]
		data = parms[1]
		els = data.split(sep)
		if len(els) == 0: return o
		for el in els:
			kv = el.split(keysep,1)
			if len(kv) != 2: return o
			key = kv[0]
			val = kv[1]
			if key == '': return o
			ldict = self.theDicts.get(lname,{})
			ldict[key] = val
			self.theDicts[lname] = ldict
		return o

	def d_fn(self,tag,data):
		o = ''
		parms = data.split(',',1)
		if len(parms) == 2:
			ldict = self.theDicts.get(parms[0],{})
			o = ldict.get(parms[1],'')
		return o

	# [setd (keysep=X,)dictName,keyXvalue]
	def setd(self,tag,data):
		o = ''
		opts,data = self.popts(['keysep'],data)
		keysep = ':'
		for el in opts:
			if el[0] == 'keysep=':
				keysep = el[1]
		parms = data.split(',',1)
		if len(parms) == 2:
			lname = parms[0]
			if len(lname) != 0:
				kv = parms[1].split(keysep)
				if len(kv) == 2:
					key = kv[0]
					val = kv[1]
					if key != '':
						ldict = self.theDicts.get(lname,{})
						ldict[key] = val
						self.theDicts[lname] = ldict
		return o

	def cap_fn(self,tag,data):
		o = ''
		if data != '':
			o = data[:1].capitalize() + data[1:].lower()
		return o

	# [inter iChar,L|R,everyN,content]
	def inter_fn(self,tag,data):
		o = ''
		ll = data.split(',',3)
		if len(ll) == 4:
			try:
				iChar = ll[0]
				lr = ll[1].lower()
				n = int(ll[2])
				content = ll[3]
			except:
				pass
			else:
				if iChar != '':
					if lr == 'l' or lr == 'r':
						ct = 0
						oc = ''
						if lr == 'r':
							content = content[::-1]
						for c in content:
							oc += c
							ct += 1
							if ct == n:
								oc += iChar
								ct = 0
						if lr == 'r':
							oc = oc[::-1]
						o = oc
		return o

	def capw_fn(self,tag,data):
		return data.title()

	def tcase_fn(self,tag,data):
		o = ''
		data = data.lower()
		wlist = data.split(' ')
		for w in wlist:
			if o != '':
				o += ' '
			cap = True
			for ncw in self.notcase:
				if ncw == w:
					cap = False
					break
			if cap == True:
				w = w.capitalize()
			o += w
		return o

	def back_fn(self,tag,data):
		self.setBack(data)
		return ''

	def setMode(self,mode='3.2'):
		if type(mode) != str or mode != '3.2':
			mode = '4.01s'
		self.mode = mode

	def mode_fn(self,tag,data):
		self.setMode(data)
		return ''

	def fetchVar(self,vName):
		lo = 1
		x = self.theLocals.get(vName,'')
		if x == '':
			lo = 0
			x = self.theGlobals.get(vName,'')
		return lo,str(x)

	def non_fn(self,tag,data):	# can't find  tag, so detail the problem
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

	def chr_fn(self,tag,data):
		try:
			x = int(data)
		except:
			o = ''
		else:
			o = chr(x)
		return o

	def len_fn(self,tag,data):
		return str(len(data))

	def q_fn(self,tag,data):
		return '&quot;'+data+'&quot;'

	def urle_fn(self,tag,data):
		data = data.replace(' ','+')
		data = data.replace('"','&quot;')
		data = data.replace('&','&amp;')
		return data

	def bq_fn(self,tag,data):
		return '<blockquote>'+data+'</blockquote>'

	def b_fn(self,tag,data):
		if self.mode == '3.2':
			return '<b>'+data+'</b>'
		return '<span style="font-weight: bold;">%s</span>' % (data)

	def dup_fn(self,tag,data):
		o = ''
		sep=','
		ll = data.split(sep,1)
		if len(ll) == 2:
			try:
				n = int(ll[0])
			except:
				pass
			else:
				o = ll[1] * n
		return o

	def rstrip_fn(self,tag,data):
		return data.rstrip()

	def ord_fn(self,tag,data):
		o = ''
		if data != '':
			o = str(ord(data[0]))
		return o

	def splitcount_fn(self,tag,data):
		try:
			n = int(data)
		except:
			n = 0
		self.splitCount = n
		return ''

	def split_fn(self,tag,data):
		o = ''
		dl = data.split(',',1)
		n = self.splitCount
		if len(dl) == 2:
			if str(dl[0]) == '&#44;':
				if n == 0:
					self.parms = str(dl[1]).split(',')
				else:
					self.parms = str(dl[1]).split(',',n)
			else:
				if n == 0:
					self.parms = str(dl[1]).split(str(dl[0]))
				else:
					self.parms = str(dl[1]).split(str(dl[0]),n)
		else:
			o = ' ?split? '
		self.splitCount = 0
		return o

	def parm_fn(self,tag,data):
		o = ''
		try:
			o = self.parms[int(data)]
		except:
			pass
		return o

	# [lpop listName(,index)]
	def lpop_fn(self,tag,data):
		o = ''
		p = data.split(',',1)
		if len(p) == 1:
			name = p[0]
			dex = -1
		elif len(p) == 2:
			name = p[0]
			try:
				dex = int(p[1])
			except:
				dex = -1
		if name != '':
			try:
				o = self.theLists[name].pop(dex)
			except:
				pass
		return o

	# [lslice 3:6,mylist,mylist] or [lslice 3:6,myList,otherList]
	def lslice_fn(self,tag,data):
		o = ''
		ll = []
		p = data.split(',',2)
		if len(p) == 3:
			spec,src,tgt = p
			lsrc = self.theLists.get(src,[])
			if lsrc != [] and tgt != '':
				try:
					slist = spec.split(':')
					if len(slist) == 1:
						ll = [lsrc[int(slist[0])]]
					elif len(slist) == 2:
						a = None
						b = None
						if slist[0] != '': a = int(slist[0])
						if slist[1] != '': b = int(slist[1])
						ll = lsrc[a:b]
					elif len(slist)==3:
						a = None
						b = None
						c = None
						if slist[0] != '': a = int(slist[0])
						if slist[1] != '': b = int(slist[1])
						if slist[2] != '': c = int(slist[2])
						ll = lsrc[a:b:c]
					else:
						o = ' ?lsplit? '
				except:
					pass
				self.theLists[tgt] = ll
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
		return o

	def u_fn(self,tag,data):
		if self.mode == '3.2':
			return '<u>'+data+'</u>'
		else:
			return '<span style="text-decoration: underline;">%s</span>' % (data)

	def t_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['wrap','sep'],data)
		wraps = ''
		sep = ','
		for el in opts:
			if el[0] == 'wrap=':
				wraps = el[1]
			elif el[0] == 'sep=':
				sep = el[1]
				if sep == '': return o
		plist = data.split(sep)
		for el in plist:
			if wraps != '':
				el = self.s_fn('s','%s %s' % (wraps,el))	# wrap with style if called for
			o += el
		return o

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
				if block == '':						# then there is no style M1
					o += ' ? Unknown Style: "'+data+'" '
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

	def geniflist(self,tag,data,ty):
		o = ''
		opts,data = self.popts(['wrap','sep'],data)
		wraps = ''
		sep = ','
		for el in opts:
			if el[0] == 'wrap=':
				wraps = el[1]
			if el[0] == 'sep=':
				sep = el[1]
				if sep == '': return o
		entries = data.split(sep)
		if len(entries) > 1:				# if remaining data has more than one entry
			o += '<%s>\n' % (ty,)			# BUILD a list
			for en in entries:
				if wraps != '':
					en = self.s_fn('s','%s %s' % (wraps,en))	# wrap with style if called for
				o += '<li>%s</li>\n' % str(en)					# add list entry
			o += '</%s>\n' % (ty,)
		else: # list isn't called for:
			if wraps != '':
				en = self.s_fn('s','%s %s' % (wraps,entries[0]))
				o += '%s<br>\n' % str(en)
			else: # list not supplied. Just dump data as-is
				o += data + '<br>'
		return o

	def iful_fn(self,tag,data):
		return self.geniflist(tag,data,'ul')

	def ifol_fn(self,tag,data):
		return self.geniflist(tag,data,'ol')

	def genlist(self,tag,data,ty):
		o = ''
		opts,data = self.popts(['wrap','sep'],data)
		wraps = ''
		sep = ','
		for el in opts:
			if el[0] == 'wrap=':
				wraps = el[1]
			if el[0] == 'sep=':
				sep = el[1]
				if sep == '': return o
		entries = data.split(sep)
		o += '<%s>\n' % (ty,)						# BUILD a list
		for en in entries:
			if wraps != '':
				en = self.s_fn('s','%s %s' % (wraps,en))	# wrap with style if called for
			o += '<li>%s</li>\n' % str(en)					# add list entry
		o += '</%s>\n' % (ty,)
		return o

	def ul_fn(self,tag,data):
		return self.genlist(tag,data,'ul')

	def ol_fn(self,tag,data):
		return self.genlist(tag,data,'ol')

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

	def style_fn(self,tag,data):
		if data != '':
			try:
				d1,d2 = data.split(' ',1)
			except:
				return ' ?style?="%s","%s" ' % (str(tag),str(data))
			self.styles[d1] = d2
		return ''

	def gstyle_fn(self,tag,data):
		if data != '':
			try:
				d1,d2 = data.split(' ',1)
			except:
				return ' ?gstyle?="%s","%s" ' % (str(tag),str(data))
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

	def xyhelper(self,ifn):
		xy = ''
		tifn = ''
		rfn = ifn[::-1]
		run = True
		for c in rfn:
			if (run == True and
				((c >= 'a' and c <= 'z') or 
				 (c >= 'A' and c <= 'Z') or
				 (c >= '0' and c <= '9') or
				  (c == '-' or c == '_' or c == '.'))):
				tifn = c + tifn
			else:
				run = False
		plist = self.gis(self.lipath + tifn)
		if len(plist) == 2:
			xy = " width=%d height=%d" % (int(plist[0]),int(plist[1]))
		return xy

	def lipath_fn(self,tag,data):
		self.lipath = data
		return ''

	def low_img_fn(self,tag,data,getxy=False):
		tit = ''
		txy = ''
		rv = ''
		try:
			tit,d2 = data.split(',',1)
		except:
			pass
		else:
			data = d2
		try:
			d1,d2 = data.split(' ',1)
		except:
			if tit == '':
				if getxy == True: txy = self.xyhelper(data)
				rv = '<img%s src="%s">' % (txy,data)
			if rv == '':
				if getxy == True: txy = self.xyhelper(data)
				rv = '<img%s alt="%s" title="%s" src="%s">' % (txy,tit,tit,data)
		if rv == '' and tit == '':
			if getxy == True: txy = self.xyhelper(d1)
			rv = '<a href="%s" target="_blank"><img%s src="%s"></a>' % (d2,txy,d1)
		if rv == '':
			if getxy == True: txy = self.xyhelper(d1)
			rv ='<a href="%s" target="_blank"><img%s alt="%s" title="%s" src="%s"></a>' % (d2,txy,tit,tit,d1)
		return rv

	def img_fn(self,tag,data):
		return self.low_img_fn(tag,data)

	def locimg_fn(self,tag,data):
		return self.low_img_fn(tag,data,True)

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
			else:		# "URL,linked text"
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

	def nl_fn(self,tag,data):
		return '\n'

	def v_fn(self,tag,data):
		l,x = self.fetchVar(data)
		return x

	def lv_fn(self,tag,data):
		return self.theLocals.get(data,'')

	def gv_fn(self,tag,data):
		return self.theGlobals.get(data,'')

	# [list (sep=X,)listName,listContent]
	def list_fn(self,tag,data):
		o = ''
		sep = ','
		opts,data = self.popts(['sep'],data)
		for el in opts:
			if el[0] == 'sep=':
				sep = el[1]
				if sep == '': return o
		ll = data.split(',',1)
		if len(ll) != 2: return o
		locname = ll[0]
		if len(locname) == 0: return o
		loclist = ll[1].split(sep)
		self.theLists[locname] = loclist
		return o

	def pullint(self,s):
		try:
			ll = s.split(',',1)
			n = int(ll[0])
		except:
			n = 0
		return n

	def specialcase(self,word,theList):
		wordm = word
		xword = ''
		for c in word:
			if ((c >= 'A' and c <= 'Z') or
				(c >= 'a' and c <= 'z') or
				(c >= '0' and c <= '9')):
				xword += c
		lel = xword.lower()
		repl = False
		try:
			for w in theList:
				lw = w.lower()
				if lel == lw:
					xword = w
					repl = True
					break
		except:
			pass
		if repl == True:
			word = ''
			dex = -1
			ldex = 0
			sdex = -1
			for c in wordm:
				dex += 1
				if ((c >= 'A' and c <= 'Z') or
					(c >= 'a' and c <= 'z') or
					(c >= '0' and c <= '9')):
					sdex += 1
					word += xword[sdex]
				else:
					word += c
		return word

	def scase_fn(self,tag,data):
		o = ''
		plist = data.split(',',1)
		if len(plist) == 2:
			wlist = plist[1].split(' ')
			clist = self.theLists[plist[0]]
			for w in wlist:
				w = self.specialcase(w,clist)
				if o != '':
					o += ' '
				o += w
		return o

	# [isort listName]
	def isort_fn(self,tag,data):
		try:
			self.theLists[data].sort(key=self.pullint)
		except:
			pass
		return ''

	# [issort content]
	def issort_fn(self,tag,data):
		o = ''
		try:
			ll = data.split('\n')
			ll.sort(key=self.pullint)
			for el in ll:
				o += el+'\n'
		except:
			pass
		return o

	# [asort listName]
	def asort_fn(self,tag,data):
		try:
			self.theLists[data].sort()
		except:
			pass
		return ''

	# [ssort content]
	def ssort_fn(self,tag,data):
		o = ''
		try:
			ll = data.split('\n')
			ll.sort()
			for el in ll:
				o += el+'\n'
		except:
			pass
		return o

	# [aisort listName]
	def aisort_fn(self,tag,data):
		try:
			self.theLists[data].sort(key=str.lower)
		except:
			pass
		return ''


	# [ssort content]
	def sisort_fn(self,tag,data):
		o = ''
		try:
			ll = data.split('\n')
			ll.sort(key=str.lower)
			for el in ll:
				o += el+'\n'
		except:
			pass
		return o

	# [dlist (style=styleName,)listName]
	def dlist_fn(self,tag,data):
		o = ''
		ll = data.split(',',1)
		using = False
		if len(ll) == 2: # wrap with style case
			if ll[0][:6] == 'style=':
				using = True
				style=ll[0][6:]
				if style != '':
					listname = ll[1]
					if self.styles.get(style,'') != '':
						if ll[1] != '':
							try:
								for el in self.theLists[listname]:
									ss = '[s %s %s]' % (style,el)
									o += self.do(ss)
							except:
								pass
		if using == False:
			listname = data
			if listname != '':
				try:
					for el in self.theLists[listname]:
						o += el
				except:
					pass
		return o

	# [cmap listName]
	def cmap_fn(self,tag,data):
		if data != '':
			loclist = []
			for i in range(0,256):
				loclist += [chr(i)]
			self.theLists[data] = loclist
		return ''

	# [lset listname,index,stuff]
	def lset_fn(self,tag,data):
		ll = data.split(',',2)
		if len(ll) == 3:
			if ll[0] != '':
				try:
					n = int(ll[1])
					self.theLists[ll[0]][n] = ll[2]
				except:
					pass
		return ''

	# [translate listName,text]
	def translate_fn(self,tag,data):
		o = ''
		ll = data.split(',',1)
		if len(ll) == 2:
			if ll[0] != '':
				try:
					for c in ll[1]:
						o += self.theLists[ll[0]][ord(c)]
				except:
					pass
		return o

	# [append listname,text]
	def append_fn(self,tag,data):
		ll = data.split(',',1)
		if len(ll) == 2:
			try:
				loclist = self.theLists.get(ll[0],[])
				loclist += [ll[1]]
				self.theLists[ll[0]] = loclist
			except:
				pass
		return ''

	# [e listName,n]
	def element_fn(self,tag,data):
		o = ''
		ll = data.split(',')
		if len(ll) == 2:
			try:
				n = int(ll[1])
				o = self.theLists[ll[0]][n]
			except:
				pass
		return o

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
		return o

	def push_fn(self,tag,data):
		o = ''
		sep = ','
		opts,data = self.popts(['sep'],data)
		for el in opts:
			if el[0] == 'sep=':
				sep = el[1]
				if sep == '': return o
		if data != '':
			dats = data.split(sep,1)
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

	def spage_fn(self,tag,data):
		self.styles = {}
		return ''

	def ne_fn(self,tag,data):
		o = ''
		dlist = data.split(',',1)
		if len(dlist) == 2:
			if dlist[0] != '':
				o = dlist[1]
		return o

	def eq_fn(self,tag,data):
		o = ''
		dlist = data.split(',',1)
		if len(dlist) == 2:
			if dlist[0] == '':
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

	def find_fn(self,tag,data):
		o = '-1'
		ll = data.split(',',1)
		sep = ','
		if len(ll) == 2:
			if ll[0][:4] == 'sep=':
				sep = ll[0][4:]
				if sep == '':
					return o
				ll = ll[1].split(sep,1)
				if len(ll) != 2:
					return o
			o = str(ll[1].find(ll[0]))
		return o

	# [replace (sep=X,)repStringXwithStringXinString] X default=,
	def replace_fn(self,tag,data):
		mode = 0
		ll = data.split(',',1)
		if len(ll) != 2: return data
		if ll[0][:4] == 'sep=':
			sep = ll[0][4:]
			if sep == '': return data
			mode = 1
		if mode == 0:
			a = ll[0]
			ll = ll[1].split(',',1)
			if len(ll) != 2: return data
			b,c = ll
		else:
			ll = ll[1].split(sep,2)
			if len(ll) != 3: return data
			a,b,c = ll
		o = c.replace(a,b)
		return o

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

	def csep_fn(self,tag,data):
		return self.commaSep(data)

	def fcsep_fn(self,tag,data):
		return self.fCommaSep(data)

	def max_fn(self,tag,data):
		o = '0'
		p = data.split(' ')
		if len(p) == 2:
			try:
				a = int(p[0])
				b = int(p[1])
			except:
				pass
			else:
				if a > b:	o = str(a)
				else:		o = str(b)
		return o

	def min_fn(self,tag,data):
		o = '0'
		p = data.split(' ')
		if len(p) == 2:
			try:
				a = int(p[0])
				b = int(p[1])
			except:
				pass
			else:
				if a < b:	o = str(a)
				else:		o = str(b)
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
			if number > 0 and number < 4001:
				for v in range(0,13):
					ct = int(number / self.integers[v])
					o += self.romans[v] * ct
					number -= self.integers[v] * ct
		return o

	def rjust_fn(self,tag,data):
		ll = data.split(',',2)
		if len(ll) != 3: return data
		try:
			w = int(ll[0])
		except:
			return data
		if ll[1] == '': return data
		l = len(ll[2])
		if l >= w: return ll[2]
		pad = ll[1] * (w-l)
		return pad+ll[2]

	def ljust_fn(self,tag,data):
		ll = data.split(',',2)
		if len(ll) != 3: return data
		try:
			w = int(ll[0])
		except:
			return data
		if ll[1] == '': return data
		l = len(ll[2])
		if l >= w: return ll[2]
		pad = ll[1] * (w-l)
		return ll[2]+pad

	def center_fn(self,tag,data):
		ll = data.split(',',2)
		if len(ll) != 3: return data
		try:
			w = int(ll[0])
		except:
			return '1:'+data
		if ll[1] == '': return '2:'+data
		l = len(ll[2])
		both = False
		if w < 0:
			both = True
			w = -w
		if l >= w: return '3:'+data
		c = int((w-l)/2)
		pad = ll[1] * c
		if both == True:
			rc = w - (c + l)
			rpad = ll[1] * rc
			return pad+ll[2]+rpad
		return pad+ll[2]

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
					'nl'	: self.nl_fn,		#   newline (0x0a)

					# basic text formatting
					# ---------------------
					'color'	: self.color_fn,	# P1=HHH or HHHHHH then P2 is what gets colored
					'i'		: self.i_fn,		# P1 is italicized
					'b'		: self.b_fn,		# P1 is bolded
					'u'		: self.u_fn,		# P1 is underlined
					'p'		: self.p_fn,		# P1 is an HTML paragraph
					'q'		: self.q_fn,		# Wrap content in HTML-entity quotes
					'bq'	: self.bq_fn,		# P1 is an HTML blockquote

					# Data dictionary handling
					'dict'	: self.dict_fn,		# [dict (sep=X,)(keysep=Y,)dictName,keyYvalue(XkeyYvalue)]
					'setd'	: self.setd,		# [setd (keysep=Y,)dictName,keyYvalue]
					'd'		: self.d_fn,		# [d dictName,key] = "value"

					# Data list handling
					'list'	: self.list_fn,		# create list:  [list (sep=X,)listName,listElements]
					'e'		: self.element_fn,	# fetch element:[e listName,n] = list[n]
					'append': self.append_fn,	# [append listName,stuff]
					'lpush'	: self.append_fn,	# [lpush listName,stuff]
					'translate':self.translate_fn, # [translate listName,stuff]
					'lset'	: self.lset_fn,		# [lset listName,index,stuff]
					'cmap'	: self.cmap_fn,		# [cmap listName]
					'dlist'	: self.dlist_fn,	# [dlist (style=styleName,)listName] dump list
					'asort'	: self.asort_fn,	# [asort listName] sort by alpha, case-sensitive
					'aisort': self.aisort_fn,	# [aisort listName] sort by alpha, case-insensitive
					'isort'	: self.isort_fn,	# [isort listName] sort by leading integer,
					'lhsort': self.lhsort_fn,	# [lhsort listName] sort by leading ham radio callsign
					'ltol'	: self.ltol_fn,		# [ltol listName,content] content to list by line
					'llen'	: self.llen_fn,		# [llen listName] length of list
					'lslice': self.lslice_fn,	# [lslice sliceSpec,listToSlice,intoList]
					'lpop'	: self.lpop_fn,		# [lpop listName( index)]

					# HTML list handling
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
					'urlencode': self.urle_fn,	# encodes space, ampersand, double quotes
					
					# Image handling
					# --------------
					'img'	: self.img_fn,		# img emplacement from URL
					'locimg': self.locimg_fn,	# local image (tries for x y sizes)
					'lipath': self.lipath_fn,	# set local image path

					# math
					# ----
					'add'	: self.math_fn,		# P1 + P2
					'sub'	: self.math_fn,		# P1 - P2
					'mul'	: self.math_fn,		# P1 * P2
					'div'	: self.math_fn,		# P1 / P2
					'inc'	: self.math_fn,		# P1 + 1
					'dec'	: self.math_fn,		# P1 - 1
					'max'	: self.max_fn,		# max v1 v2
					'min'	: self.min_fn,		# min v1 v2

					# conditionals
					# ------------
					'if'	: self.ifelse_fn,	# if P1 == P2 then P3
					'else'	: self.ifelse_fn,	# if P1 != P2 then P3
					'even'	: self.evenodd_fn,	# if P1 even then P2
					'odd'	: self.evenodd_fn,	# if P1 odd then P2
					'ne'	: self.ne_fn,		# if P1 non-empty,P2 (p1,p2)
					'eq'	: self.eq_fn,		# if P1 empty,P2 (p1,p2)

					# variable handling
					# -----------------
					'local'	: self.local_fn,	# define local variable:					P1 <-- P2
					'vs'	: self.local_fn,	# "     ditto         "						P1 <-- P2
					'global': self.global_fn,	# define global variable					P1 <-- P2
					'page'	: self.page_fn,		# clear local variables
					'spage'	: self.spage_fn,	# clear local styles
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

					# Parsing and text processing
					# ---------------------------
					'splitcount': self.splitcount_fn,	# [splitcount n]
					'slice'	: self.slice_fn,	# [slice sliceSpec,textToSlice]
					'split'	: self.split_fn,	# [split splitSpec,testToSplit] (obeys splitcount)
					'rstrip': self.rstrip_fn,	# [rstrip stuff] trailing whitespace removed
					'parm'	: self.parm_fn,		# [parm N] where N is 0...n of split result
					'upper'	: self.upper_fn,	# [upper textString]
					'lower'	: self.lower_fn,	# [lower textString]
					'roman'	: self.roman_fn,	# [roman numberString] e.g. [roman 17] = "xvii"
					'dtohex': self.d2h_fn,		# [d2hex decString]
					'dtooct': self.d2o_fn,		# [d2oct decString]
					'dtobin': self.d2b_fn,		# [d2bin decString]
					'htodec': self.h2d_fn,		# [htodec binaryString]
					'otodec': self.o2d_fn,		# [otodec binaryString]
					'btodec': self.b2d_fn,		# [btodec binaryString]
					'chr'	: self.chr_fn,		# [chr number] e.g. [chr 65] = "A"
					'ord'	: self.ord_fn,		# [ord character] e.g. [ord A] = 65
					'csep'	: self.csep_fn,		# [csep integer] e.g. [csep 1234] = "1,234"
					'fcsep' : self.fcsep_fn,	# [fcsep float] e.g. [fcsep 1234.56] = "1,234.56"
					'dup'	: self.dup_fn,		# [dup content] e.g. [dup 3,foo] = "foofoofoo"
					'find'	: self.find_fn,		# [find (sep=X,)thisStringXinString] X default=,
					'count'	: self.count_fn,	# [count (overlaps=yes,)(casesens=yes,)(sep=X,)findTermXinContent]
					'replace': self.replace_fn,	# [replace (sep=X,)repStrXwithStrXinStr] X default=,
					'rjust'	: self.rjust_fn,	# [rjust width,padChar,content]
					'ljust'	: self.ljust_fn,	# [ljust width,padChar,content]
					'center': self.center_fn,	# [center width,padChar,content]
					'capt'	: self.tcase_fn,	# [capt joe and a dog] = "Joe and a Dog"
					'caps'	: self.cap_fn,		# [caps joe and a dog] = "Joe and a dog"
					'capw'	: self.capw_fn,		# [capw joe and a dog] = "Joe And A Dog"
					'scase'	: self.scase_fn,	# [scase listName,content]
					'inter'	: self.inter_fn,	# [inter iChar,L|R,everyN,content]
					'ssort'	: self.ssort_fn,	# [ssort content] - sorts lines case-sensitive
					'sisort': self.sisort_fn,	# [sisort content] - sorts lines case-INsensitive
					'issort': self.issort_fn,	# [issort content] - sorts lines by leading integer string
					'hsort'	: self.hsort_fn,	# [hsort content] - sorts lines by leading ham radio callsign
					'len'	: self.len_fn,		# length(P1)
					'lc'	: self.lc_fn,		# line count content
					'wc'	: self.wc_fn,		# word count content
					'soundex': self.sex_fn,		# soundex surname coding
					'strip'	: self.strip_fn,	# [strip htmlContent] - remove HTML tags
					'wwrap'	: self.wwrap_fn,	# [wwrap (wrap=style,)cols,content] - word wrap content at/before cols

					# Miscellaneous
					# -------------
					'repeat': self.repeat_fn,	# N ThingToBeRepeated
					'nc'	: self.nc_fn,		# [nc TEXT] escape all commas
					'comment': self.comment_fn, # contained content will not render
					'mode'	: self.mode_fn,		# [mode 3.2] or [mode 4.01s] sets HTML output mode
					'back'	: self.back_fn,		# P1=HHH or HHHHHH then P2 is what gets colored
					'ghost'	: self.ghost_fn,	# [ghost styleName] print verbatim
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
		# its parameter(s) with either a space or a newline, by converting
		# the newlines used this way into a space so as to simplify
		# subsequent processing.
		# ----------------------------------------------------------------
		s = s.replace('{','[s ')
		s = re.sub(r'(\[s\s[\w-])\n',r'\1 ',s)
		if self.noDinner == False:
			s = s.replace('  \n','')

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
		self.result = o
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
	# RISC computer instruction set. It's minimal, but what is here was carefully chosen
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

	# You can use a newline instead of a space after a squiggly name, which can
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
	test += '[style fullname You provided [q [b]]<br>\n[split [co],[b]]First name: [parm 0]<br>\n Last name: [parm 1]<br>]'
	test += '{fullname John,Doe}'
	xprint("Example 26 -- Using multiple parameters within a style")
	print mod.do(test)

	# How to use parameters:
	# ----------------------
	test = ''
	test += '[style addvars [split  ,[b]][add [v [parm 0]] [v [parm 1]]]]'
	test += '[local a 4]'
	test += '[local b 5]'
	test += 'a + b = {addvars a b}\n'
	xprint("Example 27 -- using parameters as variables")
	print mod.do(test)

	# Practical use:
	# --------------
	test  = ''
	test += '[style v [if [slice :1,[b]] $ [v [slice 1:,[b]]]][else [slice :1,[b]] $ [b]]]'
	test += '[style add [split  ,[b]][add {v [parm 0]} {v [parm 1]}]]'
	test += '[local x 5]'
	test += '[local y 4]'
	test += '$x == {v $x}\n'
	test += '$y == {v $y}\n'
	test += '$x + 3 = {add $x 3}\n'
	test += '$x + $y = {add $x $y}\n'
	test += '2 + $y = {add 2 $y}\n'
	xprint("Example 28 -- Practical variable and scalar use")
	print mod.do(test)

	test  = '[list cvt,HTML,Python,PHP]'
	test += '[scase cvt,I prefer html, and python, to Html and php.\n]'
	xprint("Example 29 -- Special casing words")
	print mod.do(test)

	test  = ''
	test += '[list cvt,PooBah,L00kyLoo]'
	test += "[scase cvt,He's the grand poo-bah!\n]"
	test += "[scase cvt,She's just a l00ky-loo: Really!\n]"
	xprint("Example 30 -- Special casing words with embedded special characters")
	print mod.do(test)

	test  = ''
	test += '[slice 3:6,foobarbip]\n'
	test += '[slice :3,foobarbip]\n'
	test += '[slice :-1,foobarbip]\n'
	test += '[slice ::-1,foobarbip]\n'
	xprint("Example 31 -- Slicing content")
	print mod.do(test)

	test  = ''
	test += '[dict mydict,foo:bar,gee:whiz]'
	test += 'gee="[d mydict,gee]"\n'
	test += 'foo="[d mydict,foo]"\n'
	test += 'bip="[d mydict,bip]"\n'
	test += 'resetting foo...\n[setd mydict,foo:guggle]'
	test += 'foo="[d mydict,foo]"\n'

	xprint("Example 32 -- Data dictionaries")
	print mod.do(test)

	# One task programmers constantly run into is formatting
	# section headings. Here, we'll tackle it directly. This
	# isn't so much a HTML task (unless you're using non-prop
	# fonts) as it is a "let's document something in text"
	# task, but it serves to demonstrate just how far you
	# can go in making something happen within macro():
	# ------------------------------------------------------
	test  = ''
	test += '[style sline [center -[v csize],#, [b] ]\n]'
	test += '[style cline # [ljust [sub [v csize] 4], ,[b]] #\n]'
	test += '[style eline [dup [v csize],#]\n]'

	test += '[local csize 31]'
	test += '{sline Comment Block}'
	test += '{cline}'
	test += '{cline This is a comment block.}'
	test += '{cline and this is more of it.}'
	test += '{cline ditto.}'
	test += '{cline}'
	test += '{eline}'
	xprint("Example 33 -- Justice: Just Justifying justification, Justin.")
	print mod.do(test)

	# Ok, let's reprise that into something actually useful in practice.
	# There are two items of interest: the title of the block and the content.
	# The block be should as wide as the content, and since we have the content,
	# we'll calculate that size. Then we can generate the appropriate size block.
	# This is a fairly complex use of styles, but the end result meets the
	# goal of macro, which is that it should reduce a text formatting task
	# to very little work:
	# ----------------------------------------------------------------------
	test  = ''
	test += '[style sline # [center -[sub [v csize] 4], , [b] ] #\n]'			# The line types:	start (header)
	test += '[style cline # [ljust [sub [v csize] 4], ,[b]] #\n]'	#					center (body)
	test += '[style eline [dup [v csize],#]\n]'						#					end (filled bar)

	# These four provide the functionality of finding the longest line in the
	# content. Includes the title length, too, because we put it in slist to start.
	# This also splits the body into a list of lines for use by style cctr later.
	# ---------------------------------------------------------------------------
	test += '[style mm [local csize [max [v csize] [b]]]]'
	test += '[style ccalc [local csize 0][dlist style=mm,slist]]'
	test += '[style getlen [append slist,[len [b]]]]'
	test += '[style wcalc [ltol blkl,[b]][dlist style=getlen,blkl]{ccalc}[local csize [add [v csize] 4]]]'

	# This handles all lines in the body
	# ----------------------------------
	test += '[style cctr [dlist style=cline,blkl]]'

	# This is the top level style that uses all of the above to do the job at hand:
	# -----------------------------------------------------------------------------
	test += '[style cblock [splitcount 1][split [co],[b]][append slist,[len [parm 0]]]{wcalc [parm 1]}{eline}{sline [parm 0]}{eline}{cline}{cctr [parm 1]}{cline}{eline}]'

	# So this is how it's used: super-simple.
	# ---------------------------------------
	test += '{cblock The Title,The Body\n'
	test += 'more body\n'
	test += 'still more body\n'
	test += 'and a last body line, long-ish}'
	test += '[style mw ([b])]'

	xprint("Example 34 -- Auto-sized comment block")
	print mod.do(test)
