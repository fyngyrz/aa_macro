#!/usr/bin/python

import re
import imghdr
import struct
import imp
import time
import datetime
import subprocess
import random
try:
	import acroclass
except:
	pass

class macro(object):
	"""Class to provide an HTML macro language
      Author: fyngyrz  (Ben)
     Contact: fyngyrz@gmail.com (bugs, feature requests, kudos, bitter rejections)
     Project: aa_macro.py
    Homepage: https://github.com/fyngyrz/aa_macro
     License: None. It's free. *Really* free. Defy invalid social and
              legal norms.
 Disclaimers: 1) Probably completely broken. Do Not Use. You were explicitly
                 warned. Phbbbbt.
              2) My code is blackbox, meaning I wrote it without reference
                 to other people's code.
              3) I can't check other people's contributions effectively,
                 so if you use any version of aa_macro.py that incorporates
                 accepted commits from others, you are risking the use of
                 OPC, which may or may not be protected by copyright,
                 patent, and the like, because our intellectual property
                 system is pathological. The risks and responsibilities
                 and any subsequent consequences are entirely yours. Have
                 you written your congresscritter about patent and
                 copyright reform yet?
  Incep Date: June 17th, 2015       (for Project)
     LastRev: December 22nd, 2019     (for Class)
  LastDocRev: December 22nd, 2019     (for Class)
	"""
	def version_set(self):
		return('1.0.138 Beta')
	"""
 Tab spacing: 4 (set your editor to this for sane formatting while reading)
     Dev Env: OS X 10.6.8, Python 2.6.1 from inception
              OS X 10.12, Python 2.7.10 as of Jan 31st, 2017
	  Status:  BETA
     1st-Rel: 1.0.0
    Policies: 1) I will make every effort to never remove functionality or
                 alter existing functionality once past BETA stage. Anything
				 new will be implemented as something new, thus preserving all
				 behavior and the API. The only intentional exceptions to this
				 are if a bug is found that does not match the intended behavior,
				 or I determine there is some kind of security risk. What I
				 *will* do is not document older and less capable versions of a
				 function, unless the new functionality is incapable of doing
				 something the older version(s) could do. Remember, this only
				 applies to production code. Until the BETA status is removed,
				 ANYTHING may change. Sorry this was unclear previously.
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
     History:                    (for Class)
	 	See changelog.md

	Todo:
		Anything with a * in the first column needs recoding
		to incorporate (sep=X,)

	Available built-ins:
	====================
	Note that () designate optional parameters, a|b designates alternate parameter a or b

	Text Styling
	------------
	[p paraText]
	[bq quotetext]           NOTE: semantic defaults to True
	[b bold text]   (uses b tag if semantic is False, otherwise, strong tag)
	[i italic text] (uses i tag if semantic is False, otherwise, em tag)
	[u underlined text]
	[color HEX3|HEX6 colored text]	# HEX3 example: f09 (which means FF0099) HEX6 example: fe7842
	
	Linking
	-------
	[url (sep=|,)(nam=Name,)(css=CSS,)(tgt=_target,)URLsepITEM]
	
	Older Linking (will remain, but [url] is better)
	--------------------------------------------------
	[a (tab,)URL(,linked text)]		# The WORD tab, not a tab character. As in a browser tab
	[web URL (text)]				# If you don't provide text, you get "On the web"
	[link URL (text)]				# If you don't provide text, you get the URL as the text
	[urlencode URL]					# converts certain chars to character entities, etc.:
	
	Images
	------
	[img (title,)URL( linkTarget)]		# makes a link if linktarget present
	[lipath localImagePath]				# sets filesystem path to local images. This is used by [limg] to
										  find the image and read it to obtain x,y dimensions
										  [lipath] and [wepath] first, then [limg]
	[wepath localImagePath]				# sets web path to images. This is used by [limg] to
										  find set the image's URL properly
										  [lipath] and [wepath] first, then [limg]
	[limg (title=,)(alt=,)(target=,)ImageFileName]	# makes a link if target present, also inserts img size
										# [limg] can read the size of jpg, png, and gif
										# Examples:
			[lipath]
			[limg mypic.png]					- image in same dir as python cmd on host
												- and in / of webserver
			[lipath /usr/www/mysite.com/htdocs/]
			[limg mypic.png]					- image in /usr/www/mysite.com/htdocs/ on host
												- and in / of webserver

			[lipath /usr/www/mysite.com/htdocs/pics/]
			[limg pics/mypic.png]				- image in /usr/www/mysite.com/htdocs/pics/ on host
												- and in /pics/ of webserver
	
	HTML Lists
	----------
	[ul (lstyle=hstyle,)(istyle=hstyle,)(wrap=style,)(sep=X,)item1(Xitem2Xitem3...)]
	[ol (lstyle=hstyle,)(istyle=hstyle,)(wrap=style,)(type=X)(start=N,)(sep=X,)item1(Xitem2Xitem3...)]
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
	[raw variableName value]						# define a variable in the local environment
	[vs variableName value]							# ditto - same as local
	[global variableName value]						# define a variable in the global environment
	[graw variableName value]						# define a variable in the global environment
	[v variableName]								# use a variable (local, if not local, then global)
	[gv variableName]								# use the global variable and ignore the local
	[lv variableName]								# use the local variable and ignore the global
	[vinc (quiet=1,)(pre=1,)variableName]			# increment a local(global) variable
	[vdec (quiet=1,)(pre=1,)variableName]			# deccrement a local(global) variable
	[load variableName fileName]					# load filename into local variable
	[gload variableName fileName]					# load filename into global variable
	[save variableName fileName]					# save filename from local variable
	[gsave variableName fileName]					# save filename from global variable
	
	[page]											# reset local environment: variables
													  global variables are unaffected

	Data Lists
	----------
	[append (opt=yes|no,)listname,item]				# add an item to the end of a list
	[lcopy srcList,destList]						# copy a list to a new or existing list
	[lpush listname,item]							# add an item to the end of a list (synonym for [append])
	[slice sliceSpec,listToSlice,resultList]		# [lslice 3:6,mylist,mylist] or [lslice 3:6,myList,otherList]
	[lsplit (sep=^,)listName,splitKey^contentToSplit] # [lsplit myList, ,A Good Test] = ['A','Good','Test']
	[lpop listName(,index)]							# [lpop] == [lpop -1] remove list item
	[lset listName,index,stuff]						# set a list item by index (must exist)
	[lcc srcList,addList,tgtList]					# concatinate lists
	[llen listName]									# length of list
	[cmap listName]									# creates 256-entry list of 1:1 8-bit char mappings
	[hmap listName]									# creates 256-entry list of 1:1 2-digit hex char mappings
	[postparse pythoncode]							# pretty-prints python (must replace [] {})
	[pythparse pythoncode]							# pretty-prints python into local loc_pyth
	[getc (var=varName,)(tabsiz=n,)(tabchar=X,)(high=c|cp|oc)filename]	# c/cpp/oc file or var to aa_macro format
	[lsub (ci=1,)(sep=X,)listName,content]			# sequenced replacement by list
	[dlist (style=X,)(fs=X,)(ls=X,)(parms=X,)(inter=X)(ntl=X)(posts=X,)listName]
													# output list elements, can be wrapped with style X
													# and with parms, if any, prefixed to list elements
													# and with posts, if any, postfixed to list elements
													# and with inter, if any, interspersed between list elements
													# and ntl, if any, this goes between next to last and last
													# if fs is present, the first display will wrap with fs style
													# if ls is present, the last display will wrap with ls style
													# if wrap is present, displays will wrap with it, barring fs and ls
	[translate (pre=PRE,)(post=POST,)(inter=INTER)listName,text]
													# characters are mapped to listName (see examples)
	[ljoin listname,joinContent]					# join a list into a string with interspersed content
	[scase listName,content]						# Case words as they are cased in listName
	[ltol listName,content]							# splits lines into a list
	[list (sep=X,)listName,item(Xitem)]				# Create list: sep default: ','
													  [list mylist,a,b,c]
													  [list sep=|,myblist,nil|one|2|0011|IV|sinco]
	[e listName,index]								# fetch an item from a list, base of zero:
													  [e mylist,0] = 'a'
													  [e myblist,4] = 'IV'
	[asort (rev=1,)listName]						# sort the list as case-sensitive text
	[aisort (rev=1,)listName]						# sort the list as case-insensitive text
	[lhsort (rev=1,)listName]						# sort the list by leading ham radio callsign
	[isort (rev-1,)(sep=x,)listName]				# sort the list according to a leading numeric value
													  ie [1,this thing][2,that thing] sep default: ','

	Dictionaries
	------------
	[dict (sep=X,)(keysep=Y,)dictName,keyYvalue(XkeyYvalue)] # create multivalue dictionary
	[dcopy srcDict,dstDict]							# copy a dictionary to a new or existing list
	[dkeys srcDict,dstList]							# dictionary keys --> new or existing list
	[dset (keysep=Y,)dictName,keyYvalue]			# set a single dictionary value (can create dict)
	[d (sep=X)dictNameXkey(XnotFound)]				# retrieve a single dictionary value
	[expand dictName,content]						# replace words in content with words in dict
													  dict to be constructed with lower-case keys

	Stack
	-----
	[push (sep=X,)(nX)CONTENT]						# push CONTENT n deep onto stack. 1 is the same as no N.
	[pop]											# pop stack. If stack empty, does nothing.
	[fetch (N)]										# get element N from stack but no pop. 0 is top, no N = 0
	[flush]											# toss out entire stack

	Math
	----
	[add (mode=float,)value addend]					# add a number to a number
	[sub (mode=float,)value subtrahend]				# subtract a number from a number
	[mul (mode=float,)value multiplier]				# multiply a number by a number
	[div (mode=float,)value divisor]				# divide a number by a number

	[abs value]										# return the absolute value of the value
	[max v1 v2]										# return larger value
	[min v1 v2]										# return smaller value
	[inc value]										# add one to a number
	[dec value]										# subtract one from a number
	[int value]										# return the integer of the value
	[round (digits=decdigits,)value]				# return the value, rounded
	[stage start end steps step]					# produce number in range
	[random( )(seed=none,)(icount=N)]				# generate a random number

	Conditionals
	------------
	[even (style=styleName,)value conditionalContent]			# use cc if value is even
	[odd (style=styleName,)value conditionalContent]			# use cc if value is odd
	[if (sep=X,)(style=styleName,)value match conditionalContent]		# use cc if value == match
	[else (sep=X,)(style=styleName,)value match conditionalContent]		# use cc if value != match
	[ne (sep=X,)(style=styleName,)value,conditionalContent]				# use cc if value Not Empty
	[eq (sep=X,)(style=styleName,)value,conditionalContent]				# use cc if value Empty
	[ifge (style=styleName,)iValue,iValue,conditionalContent]	# use cc if integer1 >= integer2
	[ifle (style=styleName,)iValue,iValue,conditionalContent]	# use cc if integer1 <= integer2
	
	Parsing and text processing
	---------------------------
	[alphalead (trail=1,)content]					# return leading alpha, discard remainder
	[alphanumlead (trail=1,)content]				# return leading alphanumerics, discard remainder
	[slice sliceSpec,contentToSlice]				# [slice 3:6,foobarfoo] = bar ... etc.
	[splitcount N]									# limit number of splits to N for next split ONLY
	[splash (inter=,)(pre=,)(post=,)(ntl=,)(sep=,,)(limit=N,)(style=Style,)data]	# Split data, optionally limit times, apply style
	[split splitSpec,contentToSplit]				# [split |,x|y|z] results in parms 0,1,2
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
	[wwrap (eol=X)(nohtml=1,)(wrap=style,)col,content]		# wrap content at col - styles usually want newlines
	[roman decNumber]								# convert decimal to roman (1...4000)
	[dtohex decNumber]								# convert decimal to hexadecimal
	[dtooct decNumber]								# convert decimal to octal
	[dtobin decNumber]								# convert decimal to binary
	[htodec hexNumber]								# convert hexadecimal to decimal
	[otodec octNumber]								# convert octal to decimal
	[btodec binNumber]								# convert binary to decimal
	[crush content]									# return only alphanumerics
	[collapse content]								# whitespace collapsed to single spaces
	[crop (words=no,)(eol=\n,)(neol=\n,)(col=78),content] # a brutal content wrap w/o collapse
	[chr number]									# e.g. [chr 65] = "A"
	[ord character]									# e.g. [ord A] = "65"
	[csep integer]									# e.g. [csep 1234] = "1,234"
	[fcsep integer]									# e.g. [fcsep 1234.56] = "1,234.56"
	[soundex content]								# returns soundex code
	[strip content]									# strip out HTML tags
	[stripe (charset=chars,)content]				# strip whitespace or chars in charset from ends of lines
	[dup count,content]								# e.g. [dup 3,foo] = "foofoofoo"
	[eval (style=styleName,)count,content]			# e.g. [eval 3,foo] = "foofoofoo"
	[find (sep=X,)thisStringXinString]				# returns -1 if not found, X default=,
	[count (overlaps=yes)(casesens=yes,)(sep=X,)patternXcontent] # count term occurances in content
	[replace (sep=X,)thisStrXwithStrXinStr]			# e.g. [replace b,d,abc] = "adc" X default=,
	[caps content]									# Capitalize first letter of first word
	[capw content]									# Capitalize first letter of every word
	[capt content]									# Use title case (style: U.S. Government Printing Office Style Manual)
	[specialcase listName,content]					# Case words as they are cased in listName
	[ssort (rev=1,)content]							# sort lines cases-INsensitive
	[sisort (rev=1,)content]						# sort lines cases-sensitive
	[issort (rev=1,)content]						# sort lines by leading integer,comma,content
	[hsort (rev=1,)content]							# sort lines by leading ham radio callsign
	[hlit (format=1,)content]						# turn content into HTML; process NOTHING
	[vlit (format=1,)variable-name]					# turn variable content into HTML; process NOTHING
	[slit (format=1,)(wrap=1,)style-name]			# turn style content into HTML; process NOTHING
	[inter iStr,L|R,everyN,content]					# intersperse iStr every N in content from left or right
*	[rjust width,padChar,content]					# e.g. [rjust 6,#,foo] = "###foo"
*	[ljust width,padChar,content]					# e.g. [ljust 6,#,foo] = "foo###"
*	[center width,padChar,content]					# e.g. [center 7,#,foo] = "##foo"
													  negative width means pad both sides:
														   [center -7,=,foo] = "==foo=="
	[th integer]									# returns st, nd, rd, th...
	[nd integer]									# returns 1st, 2nd, 3rd, 4th...
	[br (parms=stuff,)(content)]					# generates an HTML break
	
	Encryption
	----------
	[encrypt (mode=1,)(again=1,)(breakat=N,)(seed=N,)(icount=N,)salt=string,)content]
	[decrypt (mode=1,)(seed=N,)(icount=N,)salt=string,)content]

	Misc
	----
	[date]											# date processing took place
	[ddelta YYYYMMDD YYYYMMDD]						# returns difference as 'year month day'
	[time (sfx=,)(asfx=,)(psfx=,)(mode=12|24,)]		# time processing took place
	[datetime]										# atomic YYYYmmDDhhMMss
	[month (mode=long,)N]							# Jan, January
	[ampm N]										# AM or PM from hour
	[twelve N]										# twelve hour number from 24
	[term (astyle=CSSSTYLE)CAPS]					# expand term if it is known to acroclass (requires acroclass.py)
	[fref label]									# forward reference
	[resolve (hex=1,)label,content]					# resolve forward label reference(s) to content
	[sys shellCommand]								# execute shell command
	[repeat count content]							# repeat content count times
													# count may be any one of:
													#	an integer
													#	[v variableName] (local, or global if local does not exist)
													#	[gv globalVariableName]
													#	[lv localvariablename]
													#   [parm parameterNumber] (from [split])
	[comment content]								# content does not render
	[back HEX3|HEX6]								# set back color for HTML 4.01s operations
	[mode 3.2|4.01s]								# set HTML version/mode
	[include filename]								# grab some previously defined content, styles, etc.
	[embrace modulename]							# install new built-ins, and/or replace existing ones
													  see 'embrace-example.py'
	
	Escape Codes:
	-------------
	[co]							# produces HTML ',' as &#44;
	[lt]							# produces HTML '<' as &lt;
	[gt]							# produces HTML '>' as &gt;
	[sp]							# produces HTML ' ' as &#32;
	[lb]							# produces HTML '[' as &#91;
	[rb]							# produces HTML ']' as &#93;
	[ls]							# produces HTML '{' as &#123;
	[rs]							# produces HTML '}' as &#125;
	[vb]							# produces HTML '|' as &#124;
	[lf]							# produces HTML newline (0x0a)
	[nl]							# produces HTML newline (0x0a)
	
	Styles
	------
	[style (help=helpstring,)(help2=helpstring,)styleName Style]	# Defines a local style. Use [b] for body of style
	[gstyle (help=helpstring,)(help2=helpstring,)styleName Style]	# Defines a global style. Use [b] for body of style

	[helps localstylename]						# returns helpstring, if any
	[helpg globalstylename]						# returns helpstring, if any
	[helps2 localstylename]						# returns second helpstring, if any
	[helpg2 globalstylename]					# returns second helpstring, if any

	[glos styleName contentToStyle]	# contentToStyle goes where [b] tag(s) is/are in style...
									  only uses global styles

	[locs styleName contentToStyle]	# contentToStyle goes where [b] tag(s) is/are in style...
									  only uses local styles

	[s styleName contentToStyle]	# contentToStyle goes where [b] tag(s) is/are in style...
									  uses local style, if doesn't exist, then uses global style
									  but use {styleName contentToStyle} as shown next
									  you can thank me later. :)

	{styleName contentToStyle}		# ...same as [s styleName], in preferred "squiggly" syntax

	==> Only if crtospace is True:
	{styleNameNLcontentToStyle}		# ...same thing, but simplified "squiggly" syntax
									# NL is a *nix newline, 0x0A

	[spage]							# reset local environment: styles
									  global styles are unaffected
	
    [for style,X,Y,Z]
	[in style,list]
	[case (sep=X,)switchName caseXcontent]
 	[switch (csep=X,)(isep=Y,)(default=styleName,)switchName caseYstyleName(XcaseXstylename)]
	
	[ghost (source=local,) stylename]	# allows output of a style in web-compatible format
	
	[listg (source=local,)listName]		# names of global or local styles --> listname
	
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
	dlimit ----- max nesting depth of looping constructs:
					for
					repeat
					dup
					eval
	xlimit ----- max number of iterations for looping constructs:
					for
					repeat
					dup
					eval
	locklipath - '' (default) if string is non-empty, lipath cannot be changed from string
	lockwepath - '' (default) if string is non-empty, wepath cannot be changed from string
	debug ------ False  (default) or True, then call getdebug()
	mode ------- '3.2'  (default) or '4.01s' to set HTML rendering mode
	nodinner --- True   (default) or False eats sequences of two spaces followed by a newline
	noshell ---- False (default) or True disables [sys] [load] and [gload] built-ins
	noembrace -- False (default) or True disables [embrace] built-in
	noinclude -- False (default) or True disables [include] built-in
	back ------- ffffff (default) HEX3 or HEX color for background color in HTML 4.01s mode
	ucin ------- False (default) presumes input is 0-127 ASCII; True is Unicode
	ucout ------ False (default) output is ASCII; True converts output to Unicode
	dothis ----- None   (default) you can pass in initial text to be processed here if you like
	             the object returns the result in its string method:
					mod = macro(dothis='[style x foo [b]]'{x bar})
					print mod # prints 'foo bar' if the data is ASCII
					if it is unicode, you need to do a little more
	semantic --- defaults to True. This means [b text] will use <strong>
                 and [i text] will use <em>, whereas if you set it to
                 false, [b text] will use <b> and [i text] will use <i>

	Unicode
	=======
	Unicode presents encoding issues for Python 2.7
	The following examples show how to deal with
	unicode in the context of aa_macro:

	Processing unicode input to ASCII / HTML output:
	------------------------------------------------
	mod = macro(ucin=True)
	s = mod.unido(testBlock) # s will be ASCII with unicode HTML entities

	Processing Unicode input to Unicode output:
	-------------------------------------------
	mod = macro(ucin=True,ucout=True)
	mod.unido(testBlock)
	s = mod.uniget() # s will be unicode

	The Rules:
	----------
	o Unicode requires specific processing as shown above.
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
	def __init__(self,dothis=None,mode='3.2',back="ffffff",nodinner=False,noshell=False,noinclude=False,noembrace=False,debug=False,locklipath='',lockwepath='',xlimit=0,dlimit=0,ucin=False,ucout=False,acrofile='acrobase.txt',semantic=True):
		self.locklipath = locklipath
		self.lockwepath = lockwepath
		self.xlimit = xlimit
		self.dlimit = dlimit
		self.xdcount = 0
		self.semantic = semantic
		self.ucin = ucin
		self.ucout = ucout
		self.lipath = locklipath
		self.wepath = lockwepath
		self.setMode(mode)
		self.setBack(back)
		self.setNoDinner(nodinner)
		self.setDebug(debug)
		self.page()
		self.setFuncs()
		self.resetLocals()
		self.resetLists()
		self.resetDicts()
		self.resetGlobals()
		self.placeholder = 'Q|zXaH7RppY#32m' # hopefully you'll never use this string, lol
		self.styles = {}
		self.gstyles = {}
		self.dstyles = {}
		self.dgstyles = {}
		self.dstyles2 = {}
		self.dgstyles2 = {}
		self.stack = []
		self.parms = []
		self.refs = {}
		self.switches = {}
		self.refcounter = 0
		self.padCallLocalToggle = 0
		self.padCallLocalRegion = -1
		self.noshell = noshell
		try:
			self.acros = acroclass.core(acrofile=acrofile)
		except:
			self.haveacros = False
		else:
			self.haveacros = True
		self.noembrace = noembrace
		self.noinclude = noinclude
		self.sexdigs = '01230120022455012623010202'
		self.romans = ['m','cm','d','cd','c','xc','l','xl','x','ix','v','iv','i']
		self.integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
		self.notcase = ['a','an','the','at','by','for',
						'in','of','on','to','up','and','as',
						'but','or','nor']
		self.result = ''
		self.splitCount = 0

		self.theGlobals['txl_lb'] = '[lb]'
		self.theGlobals['txl_rb'] = '[rb]'
		self.theGlobals['txl_ls'] = '[ls]'
		self.theGlobals['txl_rs'] = '[rs]'
		self.theGlobals['txl_lt'] = '&lt;'
		self.theGlobals['txl_gt'] = '&gt;'
		self.theGlobals['txl_am'] = '&amp;'
		self.theGlobals['txl_qu'] = '&quot;'
		self.theGlobals['txl_lf'] = '<br>'

		self.theGlobals['cpp_fpre'] = 'ff8844'
		self.theGlobals['cpp_spre'] = '4488ff'
		self.theGlobals['cpp_stpre'] = 'ffffff'
		self.theGlobals['cpp_copre'] = '888888'
		self.theGlobals['cpp_pppre'] = 'ff0000'
		self.theGlobals['cpp_atpre'] = 'ff00ff'

		self.theGlobals['aam_version'] = self.version_set()
		
		if self.semantic == True:
			self.theGlobals['i401s_open'] = '<em>'
			self.theGlobals['i401s_clos'] = '</em>'
			self.theGlobals['b401s_open'] = '<strong>'
			self.theGlobals['b401s_clos'] = '</strong>'
		else:
			self.theGlobals['i401s_open'] = '<span style="font-style: italic;">'
			self.theGlobals['i401s_clos'] = '</span>'
			self.theGlobals['b401s_open'] = '<span style="font-weight: bold;">'
			self.theGlobals['b401s_clos'] = '</span>'
		self.theGlobals['u401s_open'] = '<span style="text-decoration: underline;">'
		self.theGlobals['u401s_clos'] = '</span>'
		self.theGlobals['c401s_open'] = '<span style="background-color: #BACKCOLOR; color: #FORECOLOR;">'
		self.theGlobals['c401s_clos'] = '</span>'
		
		self.theGlobals['pp_trigger'] = '#'

		self.theGlobals['tx_pybrace'] = '<span style="color:#ff8844;">'
		self.theGlobals['tx_pysym'] = '<span style="color:#00ffff;">'
		self.theGlobals['tx_epybrace'] = '</span>'
		self.theGlobals['tx_epysym'] = '</span>'

		self.theGlobals['tx_prekey'] = '<span style="color: #ff00ff">'
		self.theGlobals['tx_poskey'] = '</span>'
		self.theGlobals['tx_prequo'] = '<span style="color: #ffffff">'
		self.theGlobals['tx_posquo'] = '</span>'
		self.theGlobals['tx_precod'] = '<span style="color: #00ff00">'
		self.theGlobals['tx_poscod'] = '</span>'
		self.theGlobals['tx_pretxt'] = '<span style="color: #ff0000">'
		self.theGlobals['tx_postxt'] = '</span>'
		self.theGlobals['tx_precom'] = '<span style="color: #ffff00">'
		self.theGlobals['tx_poscom'] = '</span>'

		self.theGlobals['loc_splitcount'] = 0
		self.theGlobals['loc_splitnum'] = 0
		self.theGlobals['loc_splashcount'] = 0

		self.keywords = ['and','del','from','not','while',
					'as','elif','global','or','with',
					'assert','else','if','pass','yeild',
					'break','except','import','print',
					'class','exec','in','raise',
					'continue','finally','is','return',
					'def','for','lambda','try']

		self.months = ['January','February','March','April','may','June','July','August','September','October','November','December']
		self.setup_urle()
		if dothis != None:
			if self.ucin == True:
				self.unido(dothis)
			else:
				self.do(dothis)

	def __str__(self):
		return self.result

	def uniget(self):
		if self.ucout == True:
			self.result = self.asciitounicode(self.result)
		return self.result

	def unido(self,text):
		tmp = unicode(text)
		text = self.unicodetoascii(tmp) # convert input unicode to ASCII
		self.do(text)
		return self.result

	def asciitounicode(self,text):
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

	def unicodetoascii(self,text):
		o = ''
		n = len(text)
		for i in range(0,n):
			try:
				c = text[i].encode("ascii")
				o += c
			except:
				o += '&#{:d};'.format(ord(text[i]))
		return o

	def setDebug(self,db):
		if db != False:
			self.debug = True
		else:
			self.debug = False
		self.debuglevel = 0
		self.debstack = []

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
		self.dgstyles = {}
		self.dgstyles2 = {}

	def resetLocals(self):
		self.theLocals = {}
		self.styles = {}
		self.dstyles = {}
		self.dstyles2 = {}

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

	def getm(self,vname):
		o = self.theLocals.get(vname,self.theGlobals.get(vname,''))
		return o

	def mcolor(self,cc):
		ll = len(cc)
		if ll != 3 and ll != 6: return cc
		c = cc
		d = 'ffffff'
		if type(c) != str:
			c = d
		if len(c) == 3:
			c = c[0]+c[0] + c[1]+c[1] + c[2]+c[2]
		if len(c) != 6:
			c = d
		c = c.upper()
		if self.htest(c) != True:
			c = cc
		return c

	def setBack(self,back="ffffff"):
		self.back = self.mcolor(back)

	def popts(self,olist,data,justopts=False):
		ropts = []
		plist = []
		if justopts == True:
			if data.find(',') == -1:
				plist += [data];
			else:
				plist = data.split(',')
			if len(plist) == 0 or plist[0] == '':
				return ropts,data
		else:
			if data.find(',') != -1:
				plist = data.split(',')
			else:
				return ropts,data
		run = True
		while run == True:
			hit = False
			for el in olist:
				el += '='
				l = len(el)
				if len(plist) != 0:
					mystr = plist[0]
					if mystr[:l] == str(el):
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

	def mkey(self,key):
		return 'hY#n_K+fR'+key+'6/tt@8f*d0!!rf'

	# [dkeys srcDict,dstList]
	def dkeys_fn(self,tag,data):
		o = ''
		p = data.split(',',1)
		if len(p) ==  2:
			a,b = p
			if a != '' and b != '':
				try:
					self.theLists[b] = self.theDicts.get(a,{}).keys()
				except:
					try:
						self.theLists[b] = []
					except:
						pass
		return o

	# [dcopy srcDict,dstDict]
	def dcopy_fn(self,tag,data):
		o = ''
		p = data.split(',',1)
		if len(p) ==  2:
			a,b = p
			if a != '' and b != '':
				try:
					self.theDicts[b] = self.theDicts.get(a,{})
				except:
					try:
						self.theDicts[b] = {}
					except:
						pass
		return o

	# [lcopy srcList,dstList]
	def lcopy_fn(self,tag,data):
		o = ''
		p = data.split(',',1)
		if len(p) ==  2:
			a,b = p
			if a != '' and b != '':
				try:
					self.theLists[b] = self.theLists.get(a,[])
				except:
					try:
						self.theLists[b] = []
					except:
						pass
		return o

	# [term TERM]
	def term_fn(self,tag,data):
		opts,data = self.popts(['astyle'],data)
		if self.haveacros == False: return(data)
		for el in opts:
			if el[0] == 'astyle=':
				self.acros.setstyle(el[1])
		try:
			data = self.acros.a2a(data)
		except:
			data = data
		return(data)

	# [fref label]
	def fref_fn(self,tag,data):
		o = ''
		if data != '':
			key = self.mkey(data)
			o += key
		return o

	# [reso (hex=1,)label,content]
	def reso_fn(self,tag,data):
		dh = ''
		opts,data = self.popts(['hex'],data)
		for el in opts:
			if el[0] == 'hex=':
				dh = el[1]
		p = data.split(',',1)
		if len(p) == 2:
			k,c = p
			if dh == '1':
				em = 'bad hex value for resolve of label "'+k+'"'
				kl = len(c)
				cc = ''
				if (kl & 1 == 0) and kl != 0: # has to be even, can't be non-zero
					for i in range(0,kl,2):
						try:
							cc += chr(int(c[i:i+2],16))
						except:
							return em
					c = cc
				else:
					return em
			key = self.mkey(k)
			self.refs[key] = c
		return ''

	# [gload variableName fileName]
	def gload_fn(self,tag,data):
		o = ''
		em = ' aa_macro gload operator error '
		if self.noshell == True: return '! gload Not Available !'
		plist = data.split(' ')
		if len(plist) != 2: return em
		vn = plist[0]
		fn = plist[1]
		if len(vn) == 0: return em+'(variable name) '
		if len(fn) == 0: return em+'(file name) '
		try:
			fh = open(fn)
		except:
			return em+'(file open failure) '
		try:
			fc = fh.read()
		except:
			return em+'(file read failure) '
		try:
			fh.close()
		except:
			pass
		try:
			self.theGlobals[vn] = fc
		except:
			return em+'(unable to create/update global variable) '
		return o

	# [gsave variableName fileName]
	def gsave_fn(self,tag,data):
		o = ''
		em = ' aa_macro gsave operator error '
		if self.noshell == True: return '! gsave Not Available !'
		try:
			plist = data.split(' ')
		except:
			plist = ['','']
		if len(plist) != 2: return em
		vn = plist[0]
		fn = plist[1]
		if len(vn) == 0: return em+'(variable name) '
		if len(fn) == 0: return em+'(file name) '
		try:
			fh = open(fn,'w')
		except:
			return em+'! (write file open failure) !'
		try:
			fh.write(self.theGlobals.get(vn,''))
		except:
			return em+'! (file write failure) !'
		try:
			fh.close()
		except:
			return em+'! (file close failure) !'
		return o

	# [save variableName fileName]
	def save_fn(self,tag,data):
		o = ''
		em = ' aa_macro save operator error '
		if self.noshell == True: return '! save Not Available !'
		try:
			plist = data.split(' ')
		except:
			plist = ['','']
		if len(plist) != 2: return em
		vn = plist[0]
		fn = plist[1]
		if len(vn) == 0: return em+'(variable name) '
		if len(fn) == 0: return em+'(file name) '
		try:
			fh = open(fn,'w')
		except:
			return em+'! (write file open failure) !'
		try:
			fh.write(self.theLocals.get(vn,''))
		except:
			return em+'! (file write failure) !'
		try:
			fh.close()
		except:
			return em+'! (file close failure) !'
		return o

	# [load variableName fileName]
	def load_fn(self,tag,data):
		o = ''
		em = ' aa_macro load operator error '
		if self.noshell == True: return '! load Not Available !'
		plist = data.split(' ')
		if len(plist) != 2: return em
		vn = plist[0]
		fn = plist[1]
		if len(vn) == 0: return em+'(variable name) '
		if len(fn) == 0: return em+'(file name) '
		try:
			fh = open(fn)
		except:
			return em+'(file open failure) '
		try:
			fc = fh.read()
		except:
			return em+'(file read failure) '
		try:
			fh.close()
		except:
			pass
		try:
			self.theLocals[vn] = fc
		except:
			return em+'(unable to create/update local variable) '
		return o

	def sys_fn(self,tag,data):
		o = ''
		if self.noshell == True: return '! sys Not Available !'
		if data != '':
			try:
				s = subprocess.Popen(data, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
				while True:
					tl = s.stdout.readline()
					if not tl: break
					o += tl
			except Exception,e:
				o += 'System call failed: "%s" (%s)' % (e,data)
		return o

	def int_fn(self,tag,data):
		o = '0'
		try:
			o = str(int(float(data)))
		except:
			pass
		return o

	def round_fn(self,tag,data):
		opts,data = self.popts(['digits'],data)
		digits = 0
		for el in opts:
			if el[0] == 'digits=':
				try:
					digits = int(el[1])
				except:
					digits = 0
		o = '0'
		if digits < 0: digits = 0
		try:
			o = str(round(float(data),digits))
		except:
			pass
		return o

	def abs_fn(self,tag,data):
		o = '0'
		try:
			o = str(abs(float(data)))
		except:
			pass
		return o

	def time_fn(self,tag,data):
		t = time.localtime()
		opts,data = self.popts(['mode','sfx','asfx','psfx'],data,True)
		mode = '24'
		sfx = ''
		asfx = ''
		psfx = ''
		for el in opts:
			if el[0] == 'mode=':
				mmode = el[1]
				if mmode == '12':
					mode = '12'
			elif el[0] == 'sfx=':
				sfx = el[1]
			elif el[0] == 'asfx=':
				asfx = el[1]
			elif el[0] == 'psfx=':
				psfx = el[1]
		if sfx == 'auto':
			asfx = ' AM'
			psfx = ' PM'
			if mode == '24':
				sfx = ' Military Time'
			else:
				if t[3] < 12:
					sfx = asfx
				else:
					sfx = psfx
		if mode == '12':
			if t[3] <= 12:
				sfx = asfx
			else:
				sfx = psfx
		sh = str(t[3])
		thh = t[3];
		if mode == '12':
			if t[3] > 12:
				sh = str(t[3] - 12)
				thh = t[3] - 12
		sm = str(t[4])
		ss = str(t[5])
		if thh < 10: sh = '0'+sh
		if t[4] < 10: sm = '0'+sm
		if t[5] < 10: ss = '0'+ss
		return(sh+sm+ss+sfx)

	def twelve_fn(self,tag,data):
		o = '! Cannot convert to twelve hour format !'
		try:
			ti = int(data)
			if ti > 12:
				ti -= 12
			else:
				if ti == 0:
					ti = 12
			o = str(ti)
		except:
			pass
		return o

	def ampm_fn(self,tag,data):
		o = '! Cannot determine AM/PM !'
		try:
			ap = int(data)
			if ap > 12:
				o = 'PM'
			else:
				o = 'AM'
		except:
			pass
		return o

	def datetime_fn(self,tag,data):
		t = time.localtime()
		sy = str(t[0])
		sm = str(t[1])
		if (t[1] < 10):
			sm = '0'+sm
		sd = str(t[2])
		if (t[2] < 10):
			sd = '0'+sd
		sh = str(t[3])
		if t[3] < 10:
			sh = '0'+sh
		sn = str(t[4])
		if t[4] < 10:
			sn = '0'+sn
		ss = str(t[5])
		if t[5] < 10:
			ss = '0'+ss
		return sy+sm+sd+sh+sn+ss

	def month_fn(self,tag,data):
		o = ''
		err = '! Unable to convert month !'
		opts,data = self.popts(['mode'],data)
		mode = 'short'
		slist = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
		llist = ['January','February','March','April','May','June','July','August','September','October','November','December']
		for el in opts:
			if el[0] == 'mode=':
				if el[1] == 'long':
					mode = el[1]
		try:
			mm = int(data) - 1
			if mm >= 0 and mm < 12:
				if mode == 'long':
					o = llist[mm]
				else:
					o = slist[mm]
			else:
				o = err
		except:
			o = err
		return o

	def date_fn(self,tag,data):
		t = time.localtime()
		sy = str(t[0])
		sm = str(t[1])
		if (t[1] < 10):
			sm = '0'+sm
		sd = str(t[2])
		if (t[2] < 10):
			sd = '0'+sd
		return(sy+sm+sd)

	def dsplit(self,date):
		yy = date[0:4]
		mm = date[4:6]
		dd = date[6:8]
		return (yy,mm,dd)

	def dverify(self,date):
		if len(date) == 8:
			for c in date:
				if c < '0' or c > '9':
					return 1 # bad
			try:
				yy = int(date[0:4])
				mm = int(date[4:6])
				dd = int(date[6:8])
			except:
				return 1 # bad
			if mm < 1: return 1 # bad
			if mm > 12: return 1 # bad
			if dd < 1: return 1 # bad
			if dd > 31: return 1 # bad
		else:
			return 1 # bad
		return 0

	def ddelta_fn(self,tag,data):
		dray = data.split(' ')
		if len(dray) == 2:
			t1 = dray[0]
			t2 = dray[1]
			if self.dverify(t1) == 1: return 'error: 1st parameter is not YYYYMMDD '
			if self.dverify(t2) == 1: return 'error: 2nd parameter is not YYYYMMDD '
			if t2 > t1: # make sure t1 > t2
				tx = t2
				t2 = t1
				t1 = tx
			d1t = self.dsplit(t1)
			d2t = self.dsplit(t2)
			d1y = int(d1t[0])
			d2y = int(d2t[0])
			d1m = int(d1t[1])
			d2m = int(d2t[1])
			d1d = int(d1t[2])
			d2d = int(d2t[2])
			try:
				dt1 = datetime.datetime(d1y,d1m,d1d)
				dt2 = datetime.datetime(d2y,d2m,d2d)
				timedelta = dt1 - dt2
				ddelta = timedelta.days / 365.25
				yy = int(ddelta)
				md = (ddelta - yy) * 365.25
				davg = 30.4375
				mf = md / davg
				mm = int(mf)
				dd = int(davg * (mf-mm))
				return '%d %d %d' % (yy,mm,dd)
			except Exception,e:
				return 'something wrong with date1 and/or date2: '+str(e)
			return 'I feel happy: %s %s' % (str(d1t),str(d2t))
		else: # whoops
			return 'error: requires YYYYMMDD YYYYMMDD '

	# [lcc listOne,listTwo,listResult]
	def lcc_fn(self,tag,data):
		o = ''
		p = data.split(',',2)
		if len(p) == 3:
			ln1,ln2,lnr = p
			if lnr != '':
				l1 = self.theLists.get(ln1,[])
				l2 = self.theLists.get(ln2,[])
				self.theLists[lnr] = l1 + l2
		return o

	def cir(self,term,rterm,content):
		ix0 = 0
		while ix0 < len(content):
			ix = content.lower().find(term.lower(), ix0)
			if ix == -1:
				return content
			content = content[:ix] + rterm + content[ix + len(term):]
			ix0 = ix + len(term)
		return content

	# [lsub (ci=1,)(sep=X,)listName,content] - sep defaults to '|'
	def lsub_fn(self,tag,data):
		o = ''
		sep = '|'
		ci = False
		opts,data = self.popts(['sep','ci'],data)
		p = data.split(',',1)
		if len(p) == 2:
			ln,content = p
			for el in opts:
				if el[0] == 'sep=':
					sep = el[1]
				if el[0] == 'ci=':
					if el[1] == '1':
						ci = True
			ll = self.theLists.get(ln,[])
			if ll != []:
				for el in ll:
					p = el.split(sep)
					if len(p) == 2:
						t,r = p
						if ci:
							content = self.cir(t,r,content)
						else:
							content = content.replace(t,r)
				o = content
		else:
			o = data
		return o

	# [include filename]
	def inclu_fn(self,tag,data):
		if self.noinclude == True:
			return '! include Not Available !'
		o = ''
		if data != '':
			try:
				fh = open(data)
			except:
				pass
			else:
				try:
					textContent = fh.read()
				except:
					try:
						fh.close()
					except:
						pass
				else:
					try:
						fh.close()
					except:
						pass
					else:
#						o = ''
#						for line in textContent.splitlines():
#							if line[-1:] == ' ':
#								line = line.rstrip()
#							o += line
#						o = self.do(o)
						o = self.do(textContent)
		return o


	# [llen listName]
	def llen_fn(self,tag,data):
		ll = self.theLists.get(data,[])
		return str(len(ll))

	def nocounthtml(self,s):
		ll = 0
		for c in s:
			if c == '<': self.wstate = 1
			elif c == '>': self.wstate = 0
			else:
				if self.wstate == 0:
					ll += 1
		return ll

	# wwraplow (nohtml=1,)(wrap=style,)cols,content
	def wwraplow_fn(self,tag,data):
		def emit_line(o,line,wrap):
			if wrap == '':
				o = o + line + '\n'
			else:
				o = o + self.do('[s ' + wrap + ' ' + line + ']')
			return o
		o = ''
		opts,data = self.popts(['wrap','nohtml'],data)
		wrap = ''
		nohtml = ''
		for el in opts:
			if el[0] == 'wrap=':
				t = self.styles.get(el[1],'')
				if t != '':
					wrap = el[1]
			elif el[0] == 'nohtml=':
				nohtml = el[1]
		p = data.split(',',1)
		if len(p) == 2:
			try:
				maxl = int(p[0]) - 1
				if maxl < 1: return data
			except:
				return 'Missing or invalid col value for wwrap:\n'+data
			data = p[1]
			if len(data) == 0: return ''
			data = data.replace('\n',' ')
			data = data.replace('\t',' ')
			while data.find('  ') != -1:
				data = data.replace('  ',' ')
			f = ''
			flag = '0'
			for c in data:
				if c == '<':
					flag = '1'
					f += '1'
				elif c == '>':
					f += '1'
					flag = '0'
				else:
					f += flag
			# now we have a corresponding in-tag/out-tag flagset for the data in f
			wlen = 0
			dl = len(data)
			i = -1
			cll = 0
			accum = ''
			line = ''
			dx = dl - 1
			while i < dx:
				i += 1
				c = data[i]
				if nohtml == '1':
					flag = f[i]
				else:
					flag = '0'
				if flag == '0': # we're parsing non-tag content
					if c == ' ' or i == dl-1: # word break here?
						if c != ' ':
							accum += c
							wlen += 1
						if wlen + 1 > maxl: # ridiculous (word+' ')?
							if line != '':
								o = emit_line(o,line,wrap) # then blow out current line
							o = emit_line(o,accum,wrap) # dump this pig, without a trailing space
							line = '' # and start over
							accum= ''
							wlen = 0
						elif cll + wlen > maxl: # if adding this word is too long
							o = emit_line(o,line,wrap)
							line = accum
							cll = wlen
							wlen = 0
							accum = ''
						else:
							if line != '':
								line += ' '
								cll += 1
							line += accum
							cll += wlen
							accum = ''
							wlen = 0
					else: # character is not a space or last in content
						wlen += 1
						accum += c
				else: # parsing tag content
					accum += c # we just keep adding chars without counting them
			if line != '':
				o = emit_line(o,line,wrap)
		return o

	# [wwrap (nohtml=1,)(wrap=style,)cols,content]
	def wwrap_fn(self,tag,data):
		o = ''
		tdata = data
		opts,data = self.popts(['wrap','nohtml','eol'],data)
		wrap = ''
		nohtml = ''
		eol = ''
		for el in opts:
			if el[0] == 'wrap=':
				t = self.styles.get(el[1],'')
				if t != '':
					wrap = el[1]
			elif el[0] == 'nohtml=':
				nohtml = el[1]
			elif el[0] == 'eol=':
				eol = str(el[1])
		p = data.split(',',1) # try to get column value
		if len(p) != 2:
			return '** missing or invalid col value for wwrap'
		data = p[1]
		if eol != '': # user wants wrap to be in paras
			pdata = data.split(eol)
			o = ''
			for el in pdata:
				topts = ''
				if wrap != '':
					topts += 'wrap='+wrap+','
				if nohtml != '':
					topts += 'nohtml='+nohtml+','
				o += self.wwraplow_fn(tag,topts+p[0]+','+el)
		else:
			return self.wwraplow_fn(tag,tdata) # just pass along unmolested
		return o

	# [hsort (rev=1,)linesOfContent]
	def hsort_fn(self,tag,data):
		rev = ''
		opts,data = self.popts(['rev'],data)
		for el in opts:
			if el[0] == 'rev=':
				rev = el[1]
		o = ''
		tlist = data.split('\n')
		if len(tlist) > 1:
			tlist = sorted(tlist,key=self.sCallsignKeyF)
			if rev == '1':
				tlist = tlist[::-1]
			o = '\n'.join(tlist)
		return o

	# [lhsort (rev=1,)listName]
	def lhsort_fn(self,tag,data):
		rev = ''
		opts,data = self.popts(['rev'],data)
		for el in opts:
			if el[0] == 'rev=':
				rev = el[1]
		tlist = self.theLists.get(data,[])
		if len(tlist) > 1:
			tlist = sorted(tlist,key=self.sCallsignKeyF)
			if rev == '1':
				tlist = tlist[::-1]
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

	# [stripe (charset=chars,)content]
	def stripe_fn(self,tag,data):
		cs = None
		opts,data = self.popts(['charset'],data)
		for el in opts:
			if el[0] == 'charset=':
				cs = el[1]
		return data.strip(cs)

	def collapse_fn(self,tag,data):
		o = ''
		flag = 0
		for c in data:
			if c == ' ' or c == '\n' or c == '\t':
				flag = 1
			else:
				if flag == 1:
					o += ' '
					flag = 0
				o += c
		return o

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
		opts,data = self.popts(['digits'],data)
		digits = -1
		for el in opts:
			if el[0] == 'digits=':
				try:
					digits = abs(int(el[1]))
				except:
					digits = -1
				if digits == 0:
					digits = -1
		o = ''
		try:
			n = int(data)
		except:
			pass
		else:
			if digits == -1:
				o = '%x' % (n,)
			else:
				fmt = '%%0%dx' % (digits)
				o = fmt % (n,)
		return o

	# [dtoct decNumber]
	def d2o_fn(self,tag,data):
		opts,data = self.popts(['digits'],data)
		digits = -1
		for el in opts:
			if el[0] == 'digits=':
				try:
					digits = abs(int(el[1]))
				except:
					digits = -1
				if digits == 0:
					digits = -1
		o = ''
		try:
			n = int(data)
		except:
			pass
		else:
			if digits == -1:
				o = '%o' % (n,)
			else:
				fmt = '%%0%do' % (digits)
				o = fmt % (n,)
		return o

	# [dtobin decNumber]
	def d2b_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['digits'],data)
		digits = -1
		for el in opts:
			if el[0] == 'digits=':
				try:
					digits =abs(int(el[1]))
				except:
					digits = -1
				if digits == 0:
					digits = -1
		try:
			n = int(data)
		except:
			pass
		else:
			if digits == -1:
				o = bin(n)[2:]
			else:
				o = bin(n)[2:].zfill(digits)
		return o

	# [htodec hexNumber]
	def h2d_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['digits'],data)
		digits = -1
		for el in opts:
			if el[0] == 'digits=':
				try:
					digits = abs(int(el[1]))
				except:
					digits = -1
				if digits == 0:
					digits = -1
		try:
			val = int(data,16)
			if digits == -1:
				o += str(val)
			else:
				fmt = '%%0%dd' % (digits)
				o += fmt % (val)
		except:
			pass
		return o

	# [otodec octNumber]
	def o2d_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['digits'],data)
		digits = -1
		for el in opts:
			if el[0] == 'digits=':
				try:
					digits = abs(int(el[1]))
				except:
					digits = -1
				if digits == 0:
					digits = -1
		try:
			val = int(data,8)
			if digits == -1:
				o += str(val)
			else:
				fmt = '%%0%dd' % (digits)
				o += fmt % (val)
		except:
			pass
		return o

	# [btod binNumber]
	def b2d_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['digits'],data)
		digits = -1
		for el in opts:
			if el[0] == 'digits=':
				try:
					digits = abs(int(el[1]))
				except:
					digits = -1
				if digits == 0:
					digits = -1
		try:
			val = int(data,2)
			if digits == -1:
				o += str(val)
			else:
				fmt = '%%0%dd' % (digits)
				o += fmt % (val)
		except:
			pass
		return o

	# [listg (source=local,)listname]
	def listg_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['source'],data)
		source = 'global'
		for el in opts:
			if el[0] == 'source=':
				source = el[1]
		try:
			data = data.strip()
			if len(data) > 0:
				ll = []
				if source == 'global':
					for key in self.gstyles.keys():
						ll.append(key)
				else:
					for key in self.styles.keys():
						ll.append(key)
				ll.sort()
				self.theLists[data] = ll
		except Exception,e:
			o += 'Error: %s' % (str(e))
		return o

	# [ghost (source=local|global,)(opt=square|curly)styleName]
	def ghost_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['source'],data)
		slocal = False
		sglobal = False
		t = ''
		for el in opts:
			if el[0] == 'source=':
				if el[1] == 'global':
					sglobal = True
				if el[1] == 'local':
					slocal = True
		stag = ''
		if slocal == True:
			t = self.styles.get(data,'')
			stag = 'style'
		elif sglobal == True:
			t = self.gstyles.get(data,'')
			stag = 'gstyle'
		else:
			t = self.styles.get(data,self.gstyles.get(data,''))
		t = t.replace('[','&#91;')
		t = t.replace(']','&#93;')
		t = t.replace('{','&#123;')
		t = t.replace('}','&#125;')
		t = t.replace(',','&#44;')
		t = t.replace('<','&#60;')
		t = t.replace('>','&#62;')
		t = t.replace('"','&quot;')
		o += t
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
		sep = ','
		opts,data = self.popts(['sep'],data)
		for el in opts:
			if el[0] == 'sep=':
				sep = el[1]
		parms = data.split(sep)
		if len(parms) == 2:
			ldict = self.theDicts.get(parms[0],{})
			o = ldict.get(parms[1],'')
		if len(parms) == 3:
			ldict = self.theDicts.get(parms[0],{})
			o = ldict.get(parms[1],parms[2])
		return o

	# [setd (keysep=X,)dictName,keyXvalue]
	def setd_fn(self,tag,data):
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
		wc = 0
		for w in wlist:
			wc += 1
			if o != '':
				o += ' '
			cap = True
			for ncw in self.notcase:
				if ncw == w:
					cap = False
					break
			if wc == 1:
				cap = True
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
			if self.semantic == True:
				return '<em>'+data+'</em>'
			else:
				return '<i>'+data+'</i>'
		else:
			return self.getm('i401s_open')+data+self.getm('i401s_clos')

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

	def char_urle(self,ch):
		h = hex(ord(ch))[2:]
		if len(h) == 1: h = '0'+h
		h = h.upper()
		self.urlmap[ord(ch)] = '%'+h

	def setup_urle(self):
		self.urlmap = []
		self.urlmap.append('%20NULL%20')
		for i in range(1,128):
			self.urlmap.append(chr(i))
		self.char_urle('!')
		self.char_urle('#')
		self.char_urle('$')
		self.char_urle('&')
		self.char_urle("'")
		self.char_urle('(')
		self.char_urle(')')
		self.char_urle('*')
		self.char_urle('+')
		self.char_urle(',')
		self.char_urle('/')
		self.char_urle(':')
		self.char_urle(';')
		self.char_urle('=')
		self.char_urle('?')
		self.char_urle('@')
		self.char_urle('[')
		self.char_urle(']')

	def urle_fn(self,tag,data):
		o = ''
		for c in data:
			o += self.urlmap[ord(c)]
		o = o.replace(' ','+')
		return o

	def bq_fn(self,tag,data):
		return '<blockquote>'+data+'</blockquote>'

	def b_fn(self,tag,data):
		if self.mode == '3.2':
			if self.semantic == True:
				return '<strong>'+data+'<strong>'
			else:
				return '<b>'+data+'</b>'
		return self.getm('b401s_open')+data+self.getm('b401s_clos')

	# [eval (style=styleName,)N,content]
	def eval_fn(self,tag,data):
		self.xdcount += 1
		if self.dlimit != 0:
			if self.xdcount > self.dlimit:
				self.xdcount -= 1
				return '! looping depth exceeded in eval !'
		o = ''
		opts,data = self.popts(['style'],data)
		style = ''
		for el in opts:
			if el[0] == 'style=':
				style = el[1]
		if data.find(',') != -1:
			dd = data.split(',',1)
			try:
				n = abs(int(dd[0]))
				data = dd[1]
			except:
				self.xdcount -= 1
				return ' ERROR: eval N value missing or malformed '
		else:
			try:
				n = int(data)
			except:
				self.xdcount -= 1
				return ' ERROR: eval N value missing or malformed '
		if n == 0:
			self.xdcount -= 1
			return ''
		if self.xlimit != 0:
			if n > self.xlimit:
				n = self.xlimit
		for i in range(0,n):
			if style == '':
				o += data
			else:
				if data != '':
					o += self.do('[s '+style+' '+data+']')
				else:
					o += self.do('[s '+style+']')
		self.xdcount -= 1
		return o

	def dup_fn(self,tag,data):
		o = ''
		self.xdcount += 1
		if self.dlimit != 0:
			if self.xdcount > self.dlimit:
				self.xdcount -= 1
				return '! looping depth exceeded in dup !'
		sep=','
		ll = data.split(sep,1)
		if len(ll) == 2:
			try:
				n = int(ll[0])
			except:
				pass
			else:
				if self.xlimit != 0:
					if n > self.xlimit:
						n = self.xlimit
				o += ll[1] * n
		self.xdcount -= 1
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
		scount = 0
		dl = data.split(',',1)
		n = self.splitCount
		if len(dl) == 2:
			if str(dl[0]) == '&#44;':
				if n == 0:
					self.parms = str(dl[1]).split(',')
				else:
					self.parms = str(dl[1]).split(',',n)
			elif str(dl[0]) == '&#32;':
				if n == 0:
					self.parms = str(dl[1]).split(' ')
				else:
					self.parms = str(dl[1]).split(' ',n)
			else:
				if n == 0:
					self.parms = str(dl[1]).split(str(dl[0]))
				else:
					self.parms = str(dl[1]).split(str(dl[0]),n)
			scount = len(self.parms)
		else:
			o = ' ?split? '
		self.theLocals['loc_splitcount'] = str(scount)
		self.splitCount = 0
		return o

	def splash_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['style','sep','limit','inter','ntl','pre','post'],data)
		style = ''
		sep = ','
		pre = ''
		post = ''
		inter = ''
		ntl = ''
		limit = 0
		for el in opts:
			if el[0] == 'style=':
				style = el[1]
			elif el[0] == 'sep=':
				sep = el[1]
			elif el[0] == 'inter=':
				inter = el[1]
			elif el[0] == 'pre=':
				pre = el[1]
			elif el[0] == 'post=':
				post = el[1]
			elif el[0] == 'ntl=':
				ntl = el[1]
			elif el[0] == 'limit=':
				try:
					limit = abs(int(el[1]))
				except:
					limit = 0
		if limit == 0:
			self.parms = data.split(sep)
		else: # limit non-zero
			self.parms = data.split(sep,limit)
		scount = len(self.parms)
		pre = pre.replace('&#44;',',')
		post = post.replace('&#44;',',')
		inter = inter.replace('&#44;',',')
		ntl = ntl.replace('&#44;',',')
		if style != '':
			for i in range(0,scount):
				self.theLocals['loc_splashnum'] = str(i+1)
				tntl = inter
				if i == scount-1:
					tntl = ''
				if i == scount-2:
					if ntl != '':
						tntl = ntl
				lump = self.parms[i]
				if lump != '':
					t = self.do('[s '+style+' '+lump+']')
				else:
					t = self.do('[s '+style+']')
				o += '%s%s%s%s' % (pre,t,post,tntl)
		else: # no style
			for i in range(0,scount):
				self.theLocals['loc_splashnum'] = str(i+1)
				tntl = inter
				if i == scount-1:
					tntl = ''
				if i == scount-2:
					if ntl != '':
						tntl = ntl
				o += '%s%s%s%s' % (pre,self.parms[i],post,tntl)
		self.theLocals['loc_splashcount'] = str(scount)
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
						o = ' ?lslice? '
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
			return self.getm('u401s_open')+data+self.getm('u401s_clos')

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

	# [crush content]
	def crush_fn(self,tag,data):
		o = ''
		for c in data:
			if ((c >= 'A' and c <= 'Z') or
				(c >= 'a' and c <= 'z') or
				(c >= '0' and c <= '9')):
				o += c
		return o

 	# [switch (csep=X,)(isep=Y,)(default=styleName,)switchName caseYstyleName(XcaseXstylename)]
	def switch_fn(self,tag,data):
		csep = ','
		isep = '|'
		default = ''
		opts,data = self.popts(['csep','isep','default'],data)
		for el in opts:
			if el[0] == 'csep=':
				csep = el[1]
			elif el[0] == 'isep=':
				isep = el[1]
			elif el[0] == 'default=':
				default = el[1]
		em = '? bad switch: "'+data+'" ?'
		try:
			dl = data.split(' ',1)
		except:
			return em+' //nocases-error// '
		switchname = dl[0]
		caselist = dl[1]
		cl = caselist.split(csep)
		switchdict = {}
		for el in cl:
			try:
				case,stylename = el.split(isep,1)
			except:
				return em+' //case-error// '
			switchdict[case] = stylename
		if default != '':
			switchdict['default_default_default'] = default
		self.switches[switchname] = switchdict
		return ''

	# [in style,list]
	def in_fn(self,tag,data):
		o = ''
		style = ''
		list = ''
		em = ' ? //in// problem: "'+data+'" ? '
		dl = data.split(',')
		if len(dl) == 2:
			style = dl[0]
			list = dl[1]
			try:
				ll = self.theLists[list]
				block = self.styles.get(style,self.gstyles.get(style,None))
				if block == None:
					return ' ? in for, Unknown Style \"%s\" ? e4' % (style)
				for el in ll:
					block2 = block.replace('[b]',str(el))
					o += self.do(block2)
			except Exception,e:
				return em + ' //'+str(e)+'// '
		else:
			return em
		return o

	# [for style,X,Y,Z]
	def for_fn(self,tag,data):
		self.xdcount += 1
		if self.dlimit != 0:
			if self.xdcount > self.dlimit:
				self.xdcount -= 1
				return '! nesting limit exceeded in for !'
		o = ''
		style = ''
		em = ' ? //for// iterator problem: "'+data+'" ? '
		dl = data.split(',')
		if len(dl) == 4:
			try:
				style = dl[0]
				x = int(dl[1])
				y = int(dl[2])
				z = int(dl[3])
				if style != '':
					block = self.styles.get(style,self.gstyles.get(style,None))
					if block == None:
						self.xdcount -= 1
						return ' ? in for, Unknown Style \"%s\" ? e4' % (style)
					lct = 0
					for i in range(x,y,z):
						block2 = block.replace('[b]',str(i))
						o += self.do(block2)
						if self.xlimit != 0:
							lct += 1
							if lct > self.xlimit:
								break
				else:
					self.xdcount -= 1
					return em+'e1'
			except Exception,e:
				self.xdcount -= 1
				return em+'e2'+str(e)+' //'
		else:
			self.xdcount -= 1
			return em+'e3'
		self.xdcount -= 1
		return o

	# [case (sep=X,)switchName caseXcontent]
	def case_fn(self,tag,data):
		o = ''
		sep = ','
		opts,data = self.popts(['sep'],data)
		for el in opts:
			if el[0] == 'sep=':
				sep = el[1]
		em = '? case: "'+data+'" ?'
		try:
			switchname,casecontent = data.split(' ',1)
		except:
			return em
		try:
			case,content = casecontent.split(sep,1)
		except:
			return em
		try:
			default = self.switches[switchname]['default_default_default']
		except:
			default = ''
		if default == '':
			try:
				stylename = self.switches[switchname][case]
			except: # no style, 
				return em+'//no matching case for "'+case+'"// ' # no matching style, no default, you get nuttin
		else: # there is a default
			try:
				stylename = self.switches[switchname][case]
			except: # no case, so use default 
				stylename = default
		block = self.styles.get(stylename,self.gstyles.get(stylename,'? Unknown Style \"%s\" ?' % (stylename)))
		block = block.replace('[b]',content)
		o = self.do(block)
		return o

	# [glos]
	def glos_fn(self,tag,data):
		sep = ','
		opts,data = self.popts(['sep'],data)
		for el in opts:
			if el[0] == 'sep=':
				sep = el[1]
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
			d2 = da2.split(sep)
		dsiz = len(d2)
		if dsiz == ssiz:
			for i in range(0,ssiz):
				md1 = d1[i]
				md2 = d2[i]
				block = self.gstyles.get(md1,'? Unknown Local Style Invocation "'+str(md1)+'" ?')
				block = block.replace('[b]',md2)
				res = self.do(block)
				o += res
		else:
			o += ' Macro error: Unmatched styleCount=%d and bodyListSize=%d (%s||%s) ' % (ssiz,dsiz,str(d1),str(d2))
		return o

	# [locs]
	def locs_fn(self,tag,data):
		sep = ','
		opts,data = self.popts(['sep'],data)
		for el in opts:
			if el[0] == 'sep=':
				sep = el[1]
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
			d2 = da2.split(sep)
		dsiz = len(d2)
		if dsiz == ssiz:
			for i in range(0,ssiz):
				md1 = d1[i]
				md2 = d2[i]
				block = self.styles.get(md1,'? Unknown Local Style Invocation "'+str(md1)+'" ?')
				block = block.replace('[b]',md2)
				res = self.do(block)
				o += res
		else:
			o += ' Macro error: Unmatched styleCount=%d and bodyListSize=%d (%s||%s) ' % (ssiz,dsiz,str(d1),str(d2))
		return o

	# [s]
	def s_fn(self,tag,data):
		sep = ','
		opts,data = self.popts(['sep'],data)
		for el in opts:
			if el[0] == 'sep=':
				sep = el[1]
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
			d2 = da2.split(sep)
		dsiz = len(d2)
		if ssiz > 1 and dsiz == 1:
			d2 = [da2] * ssiz
			dsiz = ssiz
		if dsiz == ssiz:
			for i in range(0,ssiz):
				md1 = d1[i]
				md2 = d2[i]
				block = self.styles.get(md1,self.gstyles.get(md1,'? Unknown Style \"%s\" ?' % (md1)))
				block = block.replace('[b]',md2)
				res = self.do(block)
				o += res
		else:
			o += ' Macro error: Unmatched styleCount=%d and bodyListSize=%d (%s||%s) ' % (ssiz,dsiz,str(d1),str(d2))
		return o

	def geniflist(self,tag,data,ty):
		o = ''
		opts,data = self.popts(['wrap','sep','istyle','lstyle'],data)
		wraps = ''
		sep = ','
		istyle = ''
		lstyle = ''
		for el in opts:
			if el[0] == 'wrap=':
				wraps = el[1]
			elif el[0] == 'sep=':
				sep = el[1]
				if sep == '': return o
			elif el[0] == 'istyle=':
				istyle = el[1]
			elif el[0] == 'lstyle=':
				lstyle = el[1]
		entries = data.split(sep)
		if lstyle != '':
			lstyle = ' style="%s"' % (lstyle)
		if istyle != '':
			istyle = ' style="%s"' % (istyle)
		if len(entries) > 1:				# if remaining data has more than one entry
			o += '<%s%s>\n' % (ty,lstyle)			# BUILD a list
			for en in entries:
				if wraps != '':
					en = self.s_fn('s','%s %s' % (wraps,en))	# wrap with style if called for
				o += '<li%s>%s</li>\n' % (istyle,str(en))					# add list entry
			o += '</%s>\n' % (ty,)
		else: # list isn't called for:
			if wraps != '':
				en = self.s_fn('s','%s %s' % (wraps,entries[0]))
				if istyle == '':
					o += '%s<br>\n' % (str(en),)
				else:
					o += '<span%s>%s</span><br>\n' % (istyle,str(en))
			else: # list not supplied. Just dump data as-is
				if istyle == '':
					o += data + '<br>'
				else:
					o += '<span%s>%s</span><br>' % (istyle,data)
		return o

	def iful_fn(self,tag,data):
		return self.geniflist(tag,data,'ul')

	def ifol_fn(self,tag,data):
		return self.geniflist(tag,data,'ol')

	def genlist(self,tag,data,ty):
		o = ''
		opts,data = self.popts(['type','wrap','sep','istyle','lstyle','start'],data)
		wraps = ''
		sep = ','
		istyle = ''
		lstyle = ''
		start = ''
		ltype = ''
		for el in opts:
			if el[0] == 'wrap=':
				wraps = el[1]
			elif el[0] == 'type=':
				ltype = ' type="'+el[1]+'"'
			elif el[0] == 'start=':
				start = ' start="'+el[1]+'"'
			elif el[0] == 'sep=':
				sep = el[1]
				if sep == '': return o
			elif el[0] == 'lstyle=':
				lstyle = el[1]
			elif el[0] == 'istyle=':
				istyle = el[1]
		entries = data.split(sep)
		if lstyle != '':
			lstyle = ' style="%s"' % (lstyle)
		o += '<%s%s%s%s>\n' % (ty,ltype,start,lstyle)						# BUILD a list
		if istyle != '':
			istyle = ' style="%s"' % (istyle)
		for en in entries:
			if wraps != '':
				en = self.s_fn('s','%s %s' % (wraps,en))	# wrap with style if called for
			o += '<li%s>%s</li>\n' % (istyle,str(en))					# add list entry
		o += '</%s>\n' % (ty)
		return o

	def ul_fn(self,tag,data):
		return self.genlist(tag,data,'ul')

	def ol_fn(self,tag,data):
		return self.genlist(tag,data,'ol')

	def table_fn(self,tag,data):
		o = '<table'
		plist = data.split(',',1)
		if len(plist) == 1:
			o += '>'
			o += plist[0]
		elif len(plist) == 2: # table params
			params = plist[0].replace('&quot;','"')
			params = params.strip()
			if params != '':
				o += ' '+params
			o += '>'
			o += plist[1]
		else:
			return ' bad parameters for table '
		o += '</table>'
		return o

	def row_fn(self,tag,data):
		o = '<tr'
		plist = data.split(',',1)
		if len(plist) == 1:
			o += '>'
			o += plist[0]
		elif len(plist) == 2: # row params
			params = plist[0].replace('&quot;','"')
			params = params.strip()
			if params != '':
				o += ' '+params
			o += '>'
			o += plist[1]
		else:
			return ' bad parameters for row '
		o += '</tr>'
		return o

	def header_fn(self,tag,data):
		o = '<th'
		plist = data.split(',',1)
		if len(plist) == 1:
			o += '>'
			o += plist[0]
		elif len(plist) == 2: # header cell  params
			params = plist[0].replace('&quot;','"')
			params = params.strip()
			if params != '':
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
			params = params.strip()
			if params != '':
				o += ' '+params
			o += '>'
			o += plist[1]
		else:
			return ' bad parameters for cell '
		o += '</td>'
		return o

	def qvar(self,vName):
		x = self.theLocals.get(vName,self.theGlobals.get(vName,''))
		return str(x)

	def pconvert(self,data):
		a = ''
		vs = 'hIugTynhryXxV'
		vll = len(vs)
		inflag = 0
		quotflag = 0
		ll = len(data)
		for i in range(0,ll):
			c = data[i]
			if   c == '[':
				c = self.qvar('ppre_lb')+self.qvar('txl_lb')+self.qvar('ppos_lb')
				inflag = 1
				c += self.qvar('ppre_ak') #'<span style="color:#ffffff;">'
			elif c == ']':
				c = ''
				if inflag == 1:
					c = self.qvar('ppos_ak')#'</span>'
					inflag = 0
				elif inflag == 2:
					c = self.qvar('ppos_sk')#'</span>'
					inflag = 0
				c += self.qvar('ppre_rb')+self.qvar('txl_rb')+self.qvar('ppos_rb')
			elif c == '{':
				c = self.qvar('ppre_ls')+self.qvar('txl_ls')+self.qvar('ppos_ls')
				inflag = 2
				c += self.qvar('ppre_sk') #'<span style="color:#00ff00;">'
			elif c == '}':
				c = ''
				if inflag == 1:
					c = self.qvar('ppos_ak')#'</span>'
					inflag = 0
				elif inflag == 2:
					c = self.qvar('ppos_sk')#'</span>'
					inflag = 0
				c += self.qvar('ppre_rs')+self.qvar('txl_rs')+self.qvar('ppos_rs')
			elif c == '<': c = self.qvar('ppre_la')+self.qvar('txl_lt')+self.qvar('ppos_la')
			elif c == '>': c = self.qvar('ppre_ra')+self.qvar('txl_gt')+self.qvar('ppos_ra')
			elif c == '&': c = self.qvar('ppre_amp')+self.qvar('txl_am')+self.qvar('ppos_amp')
			elif c == '"':
				if quotflag == 0: # then not inside yet
					c = self.qvar('ppre_quo')+self.qvar('txl_qu')+self.qvar('ppos_quo')
					quotflag = 1
				else: # we're inside
					c = self.qvar('ppre_cqu')+self.qvar('txl_qu')+self.qvar('ppos_cqu')
					quotflag = 0
			elif c == '\n':
				c = ''
				if inflag == 1:
					c = self.qvar('ppos_ak')#'</span>'
					inflag = 0
				elif inflag == 2:
					c = self.qvar('ppos_sk')#'</span>'
					inflag = 0
				c += self.qvar('ppre_lf')+self.qvar('txl_lf')+self.qvar('ppos_lf')
			elif c == ' ':
				c = ''
				if inflag == 1:
					c = self.qvar('ppos_ak')#'</span>'
					inflag = 0
				elif inflag == 2:
					c = self.qvar('ppos_sk')#'</span>'
					inflag = 0
				c += vs
			a += c
		return a

	def key_up(self,symbol,context):
		if context.strip() == '': return context
		b = self.qvar('tx_prekey')
		a = self.qvar('tx_poskey')
		ll = len(context)
		ls = len(symbol)
		o = ''
		i = 0
		while i < ll:
			if context[i:i+ls] == symbol: # if looks like symbol
				llegit = True
				rlegit = True
				if i == 0: # beginning of context is legit
					pass
				else: # check for alpha to left
					c = context[i-1]
					if c >= 'a' and c <= 'z':
						llegit = False
				if llegit:
					if i == ll-1: # end of context is legit
						pass
					else: # check for alpha to the right
						c = context[i+ls]
						if c >= 'a' and c <= 'z':
							rlegit = False
				if rlegit and llegit: # then we really found our thing
					o += b+symbol+a
				else: # this isn't our thing
					o += symbol
				i += ls
			else: # doesn't match
				o += context[i]
				i += 1
		return o

	def sym_up(self,s,c,r,b,a):
		c = c.replace(s,b+r+a)
		return c

	def setsyms(self,bc,sc,be,se):
		self.symbols = [['//=','De',sc,se],['>>=','Re',sc,se], # 3x
					['<<=','Le',sc,se],['**=','Me',sc,se],
					['<=','le',sc,se],['>=','ge',sc,se], # 2x
					['+=','pe',sc,se],['-=','me',sc,se],
					['%=','Pe',sc,se],['&=','ae',sc,se],
					['|=','oe',sc,se],['^=','te',sc,se],
					['*=','ME',sc,se],['/=','de',sc,se],
					['**','DM',sc,se],['//','DD',sc,se],
					['<<','DL',sc,se],['>>','DR',sc,se],
					['==','DE',sc,se],['!=','NE',sc,se],
					['<>','nE',sc,se],
					['%','pc',sc,se],['&','am',sc,se], # 1x
					['|','or',sc,se],['^','ca',sc,se],
					['+','pl',sc,se],['-','mi',sc,se],
					['/','di',sc,se],['*','mu',sc,se],
					['<','lt',sc,se],['>','gt',sc,se],
					['[','lb',bc,be],[']','rb',bc,be],
					['{','ls',bc,be],['}','rs',bc,be],
					['(','lp',bc,be],[')','rp',bc,be],
					['@','at',sc,se],['=','eq',sc,se],
					[',','co',sc,se],[':','ko',sc,se],
					['.','pE',sc,se],['`','bt',sc,se],
					[';','sc',sc,se],['~','tl',sc,se]]

	def keyword_up(self,o,c):
		if c == None: return o
		if len(c) == 0: return o
		sympre = 'gYThvhY12'
		sympos = 'gYt7txz97'
		for sym in self.symbols: # sub out all the python symbols
			if c != None:
				c = c.replace(sym[0],sympre+sym[1]+sympos)
		for kw in self.keywords: # highlight the keywords
			if c != None:
				c = self.key_up(kw,c)
		for sym in self.symbols: # sub back in all the symbols
			if c != None:
				c = self.sym_up(sympre+sym[1]+sympos,c,sym[0],sym[2],sym[3])
		if c == None:
			c = 'ERROR: No Context'
		return o + c

	def unstate(self,state,o):
		INSING = 1
		INDOUB = 2
		INCOMM = 3
		INCODE = 4
		postxt = self.qvar('tx_postxt')
		poscom = self.qvar('tx_poscom')
		if   state == INCOMM: o += self.qvar('tx_poscom')
		elif state == INCODE: o += self.qvar('tx_poscod')
		elif state == INSING: o += self.qvar('tx_posquo')
		elif state == INDOUB: o += self.qvar('tx_posquo')
		return o

	def pprep(self,o):
		o = o.replace('[','xy33y')
		o = o.replace(']','[rb]')
		o = o.replace('xy33y','[lb]')
		o = o.replace('{','xy33y')
		o = o.replace('}','[rs]')
		o = o.replace('xy33y','[ls]')
		return o

	def pythparse_fn(self,tag,data):
		o = self.postparse_fn(tag,data)
		o = self.pprep(o)
		self.theGlobals['loc_pyth'] = o
		return ''

	def postparse_fn(self,tag,data):
		INSING = 1
		INDOUB = 2
		INCOMM = 3
		INCODE = 4
		bc = self.qvar('tx_pybrace')
		sc = self.qvar('tx_pysym')
		be = self.qvar('tx_epybrace')
		se = self.qvar('tx_epysym')
		self.setsyms(bc,sc,be,se)
		state = INCODE
		i = -1
		poslin = '\n'
		prequo = self.qvar('tx_prequo')
		posquo = self.qvar('tx_posquo')
		precod = self.qvar('tx_precod')
		poscod = self.qvar('tx_poscod')
		pretxt = self.qvar('tx_pretxt')
		postxt = self.qvar('tx_postxt')
		precom = self.qvar('tx_precom')
		poscom = self.qvar('tx_poscom')
		codeblock = ''
		state = INCODE
		prevchar = ''
		o = precod
		for c in data:
			i += 1
			if c == poslin: # quit whatever at end of line, then enter INCODE
				if state == INCODE:
					o = self.keyword_up(o,codeblock)
					codeblock = ''
				o = self.unstate(state,o)
				o += c
				o += precod
				state = INCODE
			elif state == INCOMM:
				o += c
			elif state == INSING:
				if c == "'" and prevchar != "\\":
					o = self.unstate(state,o)
					o += prequo
					o += c
					o += posquo
					o += precod
					state = INCODE
				else:
					o += c
			elif state == INDOUB:
				if c == '"' and prevchar != '\\':
					o = self.unstate(state,o)
					o += prequo
					o += c
					o += posquo
					o += precod
					state = INCODE
				else:
					o += c
			elif state == INCODE:
				if (prevchar != '\\' and c == '"') or (prevchar != '\\' and c == "'") or c == '#':
					o = self.keyword_up(o,codeblock)
					codeblock = ''
				if c == '"': # switching to string
					o = self.unstate(state,o)
					o += prequo
					o += c
					o += posquo
					o += pretxt
					state = INDOUB
				elif c == "'": # switching to string
					o = self.unstate(state,o)
					o += prequo
					o += c
					o += posquo
					o += pretxt
					state = INSING
				elif c == '#':
					o = self.unstate(state,o)
					state = INCOMM
					o += precom
					o += c
				else: # still in code
					codeblock += c
			prevchar = c
		if state == INCODE and codeblock != '':
			o = self.keyword_up(o,codeblock)
			codeblock = ''
		o = self.unstate(state,o)
		return o

	def chunky_spaces(self,s):
		smax = -1
		sctr = -1
		vs = 'hIugTynhryXxV'
		s = s.replace(vs,'&nbsp;')
		return s

	# [hlit literalcontent]
	def hlit_fn(self,tag,data):
		vs = 'hIugTynhryXxV'
		opts,data = self.popts(['format'],data)
		form = ''
		sep = ','
		for el in opts:
			if el[0] == 'format=':
				form = el[1]
		o = ''
		a = self.pconvert(data)
		if form == 't' or form == 'T' or form == 1 or form == '1':
			a = self.chunky_spaces(a)
		else:
			a = a.replace(vs,' ')
		o = self.do(a)
		self.theLocals['loc_hlit'] = o
		return ''

	# [vlit variablename]
	def vlit_fn(self,tag,data):
		vs = 'hIugTynhryXxV'
		opts,data = self.popts(['format'],data)
		form = ''
		sep = ','
		for el in opts:
			if el[0] == 'format=':
				form = el[1]
		l,x = self.fetchVar(data)
		data = x
		o = ''
		a = self.pconvert(data)
		if form == 't' or form == 'T' or form == 1 or form == '1':
			a = self.chunky_spaces(a)
		else:
			a = a.replace(vs,' ')
		o = self.do(a)
		self.theLocals['loc_vlit'] = o
		return ''

	def stylegetter(self,style):
		mode = 1 # local
		emsg = '? Unknown Style \"%s\" ?'
		data = self.styles.get(style,'')
		if data == '':
			mode = 2 # global
			data = self.gstyles.get(style,emsg)
			if data == emsg:
				mode = 0
		return mode,data

	# [slit stylename]
	def slit_fn(self,tag,data):
		vs = 'hIugTynhryXxV'
		opts,sname = self.popts(['format','wrap'],data)
		form = ''
		wrap = ''
		sep = ','
		for el in opts:
			if el[0] == 'format=':
				form = el[1]
			elif el[0] == 'wrap=':
				wrap = el[1]
		mode,data = self.stylegetter(sname)
		o = ''
		if wrap == 't' or wrap == 'T' or wrap == 1 or wrap == '1':
			if mode == 1: # local
				data = '[style ' + sname + ' ' + data + ']'
			elif mode == 2: # global
				data = '[gstyle ' + sname + ' ' + data + ']'
		a = self.pconvert(data)
		if form == 't' or form == 'T' or form == 1 or form == '1':
			a = self.chunky_spaces(a)
		else:
			a = a.replace(vs,' ')
		o = self.do(a)
		self.theLocals['loc_slit'] = o
		return ''

	# [hlit literalcontent]
	def oldhlit_fn(self,tag,data):
		o = ''
		a = ''
		for c in data:
			if   c == '[': c = '[lb]'
			elif c == ']': c = '[rb]'
			elif c == '{': c = '[ls]'
			elif c == '}': c = '[rs]'
			elif c == '<': c = '&lt;'
			elif c == '>': c = '&gt;'
			elif c == '&': c = '&amp;'
			elif c == '"': c = '&quot;'
			elif c == '\n':c = '<br>'
			a += c
		o = self.do(a)
		self.theLocals['loc_hlit'] = o
		return ''

	def style_fn(self,tag,data):
		if data != '':
			lhelp = None
			llhelp = None
			opts,data = self.popts(['help','help2'],data)
			for el in opts:
				if el[0] == 'help=':
					lhelp = el[1]
				elif el[0] == 'help2=':
					llhelp = el[1]
			try:
				d1,d2 = data.split(' ',1)
			except:
				if data != '':
					d1 = data
					d2 = ''
				else:
					return ' ?style?="%s","%s" ' % (str(tag),str(data))
			self.styles[d1] = d2
			if lhelp != None:
				self.dstyles[d1] = lhelp
			if llhelp != None:
				self.dstyles2[d1] = llhelp
		return ''

	def gstyle_fn(self,tag,data):
		if data != '':
			lhelp = None
			llhelp = None
			opts,data = self.popts(['help','help2'],data)
			for el in opts:
				if el[0] == 'help=':
					lhelp = el[1]
				elif el[0] == 'help2=':
					llhelp = el[1]
			try:
				d1,d2 = data.split(' ',1)
			except:
				if data != '':
					d1 = data
					d2 = ''
				else:
					return ' ?gstyle?="%s","%s" ' % (str(tag),str(data))
			self.gstyles[d1] = d2
			if lhelp != None:
				self.dgstyles[d1] = lhelp
			if llhelp != None:
				self.dgstyles2[d1] = llhelp
		return ''
	
	def helps_fn(self,tag,data):
		try:
			o = self.do(self.dstyles[data])
		except:
			return ''
		return o
	
	def helpg_fn(self,tag,data):
		try:
			o = self.do(self.dgstyles[data])
		except:
			return ''
		return o
	
	def helps2_fn(self,tag,data):
		try:
			o = self.do(self.dstyles2[data])
		except:
			return ''
		return o
	
	def helpg2_fn(self,tag,data):
		try:
			o = self.do(self.dgstyles2[data])
		except:
			return ''
		return o
	
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
			op = self.getm('c401s_open')
			op = op.replace('BACKCOLOR',self.back)
			op = op.replace('FORECOLOR',col)
			o += op+d2+self.getm('c401s_clos')
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
			xy = ' width="%d" height="%d"' % (int(plist[0]),int(plist[1]))
		return xy

	def lipath_fn(self,tag,data):
		if self.locklipath != '': return ''
		self.lipath = data
		return ''

	def wepath_fn(self,tag,data):
		if self.lockwepath != '': return ''
		self.wepath = data
		return ''

	def new_low_img_fn(self,tag,data,getxy=False):
		tit = ''
		alt = ''
		txy = ''
		tgt = ''
		opts,data = self.popts(['lpath','wpath','alt','title','target'],data)
		blpath = lpath = self.lipath
		bwpath = wpath = self.wepath
		for el in opts:
			if el[0] == 'lpath=':
				lpath = el[1]
			elif el[0] == 'wpath=':
				wpath = el[1]
			elif el[0] == 'alt=':
				alt = el[1]
			elif el[0] == 'title=':
				tit = el[1]
			elif el[0] == 'target=':
				tgt = el[1]
		if self.locklipath == '':
			self.lipath = lpath
		if self.lockwepath == '':
			self.wepath = wpath
		if getxy == True:
			txy = self.xyhelper(data)
		if tgt != '':
			o = '<a href="%s"><img%s alt="%s" title="%s" src="%s"></a>' % (tgt,txy,alt,tit,self.wepath+data)
		else:
			o = '<img%s alt="%s" title="%s" src="%s">' % (txy,alt,tit,self.wepath+data)
		self.lipath = blpath
		self.wepath = bwpath
		return o

	def low_img_fn(self,tag,data,getxy=False):
		opts,data = self.popts(['lpath','wpath'],data)
		blpath = lpath = self.lipath
		bwpath = wpath = self.wepath
		for el in opts:
			if el[0] == 'lpath=':
				lpath = el[1]
			elif el[0] == 'wpath=':
				wpath = el[1]
		if self.locklipath == '':
			self.lipath = lpath
		if self.lockwepath == '':
			self.wepath = wpath
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
				rv = '<img%s src="%s" alt="" title="">' % (txy,self.wepath+data)
			if rv == '':
				if getxy == True: txy = self.xyhelper(data)
				rv = '<img%s alt="%s" title="%s" src="%s">' % (txy,tit,tit,self.wepath+data)
		if rv == '' and tit == '':
			if getxy == True: txy = self.xyhelper(d1)
			rv = '<a href="%s" target="_blank"><img%s src="%s" alt="" title=""></a>' % (d2,txy,self.wepath+d1)
		if rv == '':
			if getxy == True: txy = self.xyhelper(d1)
			rv ='<a href="%s" target="_blank"><img%s alt="%s" title="%s" src="%s"></a>' % (d2,txy,tit,tit,self.wepath+d1)
		self.lipath = blpath
		self.wepath = bwpath
		return rv

	def limg_fn(self,tag,data):
		return self.new_low_img_fn(tag,data,True)

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

	def url_fn(self,tag,data):
		opts,data = self.popts(['sep','tgt','css','nam'],data,True)
		sep='|'
		tgt=''
		css=''
		nam=''
		o = ''
		for el in opts:
			if el[0] == 'sep=':
				if el[1] == '&#44;':
					el[1] = ','
				sep = el[1]
			elif el[0] == 'tgt=':
				tgt = ' target="'+el[1]+'"'
			elif el[0] == 'css=':
				css = ' style="'+el[1]+'"'
			elif el[0] == 'nam=':
				nam = ' name="'+el[1]+'"'
		if data == '':
			data = '|'
		try:
			url,string = data.split(sep)
		except:
			o = ' MALFORMED_URL Error sep="%s" data="%s"' % (sep,data)
		else:
			if data != '|':
				o = '<a'+nam+css+tgt+' href="'+url+'">'+string+'</a>'
			else: # no data provided
				if nam=='':
					o = ' EMPTY_URL_AND_NAM Error '
				else:
					o = '<a'+nam+'></a>'
		return o

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

	def lt_fn(self,tag,data):
		return '&lt;'

	def gt_fn(self,tag,data):
		return '&gt;'

	def co_fn(self,tag,data):
		return '&#44;'

	def th_fn(self,tag,data):
		try:
			n = int(data)
		except:
			return ''
		x = n % 10
		th = 'th'
		if x == 1 and n != 11: th = 'st'
		elif x == 2 and n != 12: th = 'nd'
		elif x == 3 and n != 13: th = 'rd'
		return th

	def nd_fn(self,tag,data):
		try:
			n = int(data)
		except:
			return ''
		return str(n)+self.th_fn('',n)

	# [usdate YYYYmmDD]
	def usdate_fn(self,tag,data):
		e = '? usdate: bad date ?'
		if len(data) != 8: return e
		for c in data:
			if c < '0' or c > '9': return e
		y = int(data[0:4])
		m = int(data[4:6]) - 1
		d = int(data[6:8])
		if d < 1: return e
		if d > 31: return e
		if m < 0: return e
		if m > 11: return e
		th = 'th'
		if   d == 1 or d == 21 or d == 31: th = 'st'
		elif d == 2 or d == 22: th = 'nd'
		elif d == 3 or d == 23: th = 'rd'
		o = '%s %s%s, %s' % (self.months[m],str(d),th,str(y))
		return o

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

	def vb_fn(self,tag,data):
		return '&#124;'

	def nl_fn(self,tag,data):
		return '\n'

	def v_fn(self,tag,data):
		l,x = self.fetchVar(data)
		return x

	def lv_fn(self,tag,data):
		return self.theLocals.get(data,'')

	def gv_fn(self,tag,data):
		return self.theGlobals.get(data,'')

	# [clearl listName]
	def clearl_fn(self,tag,data):
		if data != '':
			self.theLists[data] = []
		return ''

	# [vinc (quiet=1,)(pre=1,)variableName]
	def vmod_fn(self,tag,data,amt):
		pre = ''
		quiet = ''
		x = '0'
		opts,data = self.popts(['pre','quiet'],data)
		for el in opts:
			if el[0] == 'pre=':
				pre = el[1]
			if el[0] == 'quiet=':
				quiet = el[1]
		try:
			l,x = self.fetchVar(data)
			x = int(x)
			dv = str(x)
			x += amt
			if pre != '1':
				dv = str(x)
			if l == 1: # if local var was fetched
				self.theLocals[data] = str(x)
			else: # global
				self.theGlobals[data] = str(x)
			x = str(dv)
		except: x = '0'
		if quiet == '1': x = ''
		return(x)

	# [vdec (quiet=1,)(pre=1,)variableName]
	def vdec_fn(self,tag,data):
		return self.vmod_fn(tag,data,-1)

	# [vinc (quiet=1,)(pre=1,)variableName]
	def vinc_fn(self,tag,data):
		return self.vmod_fn(tag,data,1)

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

	# [ljoin listname,joinContent]
	def ljoin_fn(self,tag,data):
		ll = data.split(',',1)
		if len(ll) != 2: return '? ljoin no join spec ?'
		listname,joiner = ll
		if listname == '': '? ljoin no list name ?'
		ml = self.theLists.get(listname,[])
		if ml == []: return ''
		go = 0
		o = ''
		for el in ml:
			if go == 1:
				o += joiner
			else:
				go = 1
			o += el
		return o

	# [lsplit (sep=^,)listName,splitKey^contentToSplit]
	def lsplit_fn(self,tag,data):
		sep = ','
		splitcount = None
		opts,data = self.popts(['sep','num'],data)
		for el in opts:
			if el[0] == 'sep=':
				sep = el[1]
				if sep == '': return '? lsplit sep=EMPTY ?'
			if el[0] == 'num=':
				if el[1] == '': return '? lsplit num=EMPTY ?'
				try:	splitcount = int(el[1])
				except:	return "? lsplit num=NAN ?"
		dlist = data.split(',',1)
		if len(dlist) != 2:	return "? lsplit can't parse out listName ?"
		listname,data = dlist
		if listname == '':	return '? lsplit no list name ?'
		dlist = data.split(sep)
		if len(dlist) != 2:	return "? lsplit can't parse out splitKey ?"
		splitby,data = dlist
		if splitby == '&#44;':	splitby = ','
		elif splitby == '&#32;':	splitby = ' '
		if data == '':		self.theLists[listname] = []
		else:
			if splitcount == None:
				self.theLists[listname] = data.split(splitby)
			else:
				self.theLists[listname] = data.split(splitby,splitcount)
		return ''

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

	def isuln(self,c):
		if c >= 'a' and c <= 'z': return True
		if c >= 'A' and c <= 'Z': return True
		if c >= '0' and c <= '9': return True
		return False

	def specialexpand(self,word,theDict):
		rword = word[::-1]
		pre = ''
		post = ''
		w = ''
		state = 0
		cont = ''
		for c in word:
			if state == 0:
				if self.isuln(c) == False:
					pre += c
				else:
					state = 1
					cont += c
			else:
				cont += c
		state = 0
		for c in rword:
			if state == 0:
				if self.isuln(c) == False:
					post = c + post
					cont = cont[:-1]
				else:
					state = 1
			else:
				pass
		res = theDict.get(cont.lower(),'')
		if res != '':
			fl = cont[0]
			word = res
			if fl >= 'A' and fl <= 'Z':
				word = res[0].upper() + res[1:]
			word = pre + word + post
		return word

	# [expand dict,content]
	def expand_fn(self,tag,data):
		o = ''
		p = data.split(',',1)
		if len(p) == 2:
			dict,content = p
			ncontent = ''
			content = content.replace('\t',' ')
			content = content.replace('\n',' ')
			content = content.replace('\r',' ')
			while ncontent != content:
				ncontent = content
				content = content.replace('  ',' ')
			d = self.theDicts.get(dict,{})
			if d != {}: # TODO: space collapse and tab / LF conversion
				wlist = content.split(' ')
				for w in wlist:
					w = self.specialexpand(w,d)
					if o != '':
						o += ' '
					o += w
		return o

	# [isort listName]
	def isort_fn(self,tag,data):
		rev = ''
		opts,data = self.popts(['rev'],data)
		for el in opts:
			if el[0] == 'rev=':
				rev = el[1]
		try:
			self.theLists[data].sort(key=self.pullint)
		except:
			pass
		else:
			if rev == '1':
				self.theLists[data] = self.theLists[data][::-1]
		return ''

	# [issort (rev=1,)content]
	def issort_fn(self,tag,data):
		rev = ''
		opts,data = self.popts(['rev'],data)
		for el in opts:
			if el[0] == 'rev=':
				rev = el[1]
		o = ''
		try:
			ll = data.split('\n')
			ll.sort(key=self.pullint)
			if rev == '1':
				ll = ll[::-1]
			for el in ll:
				o += el+'\n'
		except:
			pass
		return o

	# [asort listName]
	def asort_fn(self,tag,data):
		rev = ''
		opts,data = self.popts(['rev'],data)
		for el in opts:
			if el[0] == 'rev=':
				rev = el[1]
		try:
			self.theLists[data].sort()
		except:
			pass
		else:
			if rev == '1':
				self.theLists[data] = self.theLists[data][::-1]
		return ''

	# [ssort (rev=1,)content]
	def ssort_fn(self,tag,data):
		rev = ''
		opts,data = self.popts(['rev'],data)
		for el in opts:
			if el[0] == 'rev=':
				rev = el[1]
		o = ''
		try:
			ll = data.split('\n')
			ll.sort()
			if rev == '1':
				ll = ll[::-1]
			for el in ll:
				o += el+'\n'
		except:
			pass
		return o

	# [aisort listName]
	def aisort_fn(self,tag,data):
		rev = ''
		opts,data = self.popts(['rev'],data)
		for el in opts:
			if el[0] == 'rev=':
				rev = el[1]
		try:
			self.theLists[data].sort(key=str.lower)
		except:
			pass
		else:
			if rev == '1':
				self.theLists[data] = self.theLists[data][::-1]
		return ''


	# [sisort (rev=1,)content]
	def sisort_fn(self,tag,data):
		rev = ''
		opts,data = self.popts(['rev'],data)
		for el in opts:
			if el[0] == 'rev=':
				rev = el[1]
		o = ''
		try:
			ll = data.split('\n')
			ll.sort(key=str.lower)
			if rev == '1':
				ll = ll[::-1]
			for el in ll:
				o += el+'\n'
		except:
			pass
		return o

	# [dlist (style=styleName,)(wrap=styleName,)(parms=PRE,)(posts=PST,)(inter=INT,)(ntl=NTL,)listName]
	def dlist_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['wrap','style','parms','posts','inter','ntl','fs','ls'],data)
		style = ''
		fstyle = ''
		lstyle = ''
		parms = ''
		posts = ''
		inter = ''
		ntl = ''
		for el in opts:
			if el[0] == 'style=' or el[0] == 'wrap=':
				style = el[1]
			elif el[0] == 'fs=':
				fstyle = el[1]
			elif el[0] == 'ls=':
				lstyle = el[1]
			elif el[0] == 'parms=':
				parms = el[1]
			elif el[0] == 'posts=':
				posts = el[1]
			elif el[0] == 'inter=':
				inter = el[1]
			elif el[0] == 'ntl=':
				ntl = el[1]
		using = False
		if style != '' or fstyle != '' or lstyle != '': # wrap with style mode
			listname = data
			if listname != '':
				if self.styles.get(style,self.gstyles.get(style,'')) != '':
					using = True
					try:
						tc = len(self.theLists[listname])
						i = 1
						for el in self.theLists[listname]:
							ustyle = style
							tint = ''
							if i == 1 and fstyle != '': ustyle = fstyle
							if i != tc:
								tint = inter
							if tc > 1 and i == (tc - 1):
								if ntl != '':
									tint = ntl
							if tc > 1 and i == tc:
								if lstyle != '':
									ustyle = lstyle
							if ustyle != '':
								ss = '[s %s %s%s%s]%s' % (ustyle,parms,el,posts,tint)
								o += self.do(ss)
							else: # style wasn't set, but fs or ls was and we aren't at fs or ls
								o = '%s%s%s%s' % (parms,el,posts,tint)
							i += 1
					except:
						pass
		if using == False:	# no style wrapping mode
			listname = data
			if listname != '':
				try:
					i = 1
					tc = len(self.theLists[listname])
					for el in self.theLists[listname]:
						tint = ''
						if i != tc:
							tint = inter
						if tc > 1 and i == (tc - 1) and ntl != '':
							tint = ntl
						o += parms+el+posts+tint
						i += 1
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

	# [hmap listName]
	def hmap_fn(self,tag,data):
		if data != '':
			loclist = []
			for i in range(0,256):
				loclist += ['%02x' % (i)]
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
		pre = ''
		post = ''
		inter = ''
		opts,data = self.popts(['pre','post','inter'],data)
		for el in opts:
			if el[0] == 'pre=':
				pre = el[1]
			if el[0] == 'post=':
				post = el[1]
			if el[0] == 'inter=':
				inter = el[1]
		ll = data.split(',',1)
		if len(ll) == 2:
			if ll[0] != '':
				s = ll[1]
				try:
					i = 1
					tl = len(s)
					for c in s:
						o += pre+self.theLists[ll[0]][ord(c)]+post
						if i != tl:
							o += inter
						i += 1
				except:
					pass
		return o

	# [append (opt=yes|no,)listname,text]
	def append_fn(self,tag,data):
		opts,data = self.popts(['opt'],data)
		opt = 'yes'
		for el in opts:
			if el[0] == 'opt=':
				opt = el[1].lower()
				if opt != 'no':
					opt = 'yes'
		ll = data.split(',',1)
		if len(ll) == 2:
			try:
				if opt == 'yes':
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

	def local_fn(self,tag,data):
		go = 0
		try:
			d1,d2 = data.split(' ',1)
		except:
			if data != '':
				d1 = data
				d2 = ''
				go = 1
		else:
			go = 1
		if go == 1:
			self.theLocals[d1]=d2
		return ''

	def global_fn(self,tag,data):
		go = 0
		try:
			d1,d2 = data.split(' ',1)
		except:
			if data != '':
				d1 = data
				d2  = ''
				go = 1
		else:
			go = 1
		if go == 1:
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
		style = ''
		sep = ','
		skip = 0
		if len(data) > 0:
			if data[0] == ',':
				skip = 1
		if skip == 0:
			opts,data = self.popts(['style','sep'],data)
			for el in opts:
				if el[0] == 'style=':
					style = el[1]
				elif el[0] == 'sep=':
					sep = el[1]
		dlist = data.split(sep,1)
		if len(dlist) == 2:
			if dlist[0] != '':
				if style != '':
					o += self.do("[s %s]" % style)
				o += dlist[1]
		return o

	def eq_fn(self,tag,data):
		o = ''
		skip = 0
		style = ''
		sep = ','
		opthit = 0
		if len(data) > 0:
			if data[0] == ',':
				skip = 1
		if skip == 0:
			opts,data = self.popts(['style','sep'],data)
			for el in opts:
				if el[0] == 'style=':
					style = el[1]
					opthit = 1
				elif el[0] == 'sep=':
					sep = el[1]
					opthit = 1
		dlist = data.split(sep,1)
		if len(dlist) == 2:
			if dlist[0] == '':
				if style != '':
					o += self.do("[s %s]" % style)
				o += dlist[1]
		return o

	def ifle_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['style'],data)
		style = ''
		for el in opts:
			if el[0] == 'style=':
				style = el[1]
		p = data.split(',',2)
		if len(p) == 3:
			a,b,c = p
			try:
				a = int(a)
				b = int(b)
				if a <= b:
					if style != '':
						o += self.do("[s %s]" % style)
					o += c
			except:
				pass
		return o

	def ifge_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['style'],data)
		style = ''
		for el in opts:
			if el[0] == 'style=':
				style = el[1]
		p = data.split(',',2)
		if len(p) == 3:
			a,b,c = p
			try:
				a = int(a)
				b = int(b)
				if a >= b:
					if style != '':
						o += self.do("[s %s]" % style)
					o += c
			except:
				pass
		return o

	def ifelse_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['style','wrap','sep'],data)
		style = ''
		sep = ' '
		for el in opts:
			if el[0] == 'style=' or el[0] == 'wrap=':
				style = el[1]
			elif el[0] == 'sep=':
				sep = el[1]
		if sep == '&#44;': sep = ','
		try:
			d1,d2,d3 = data.split(sep,2)
			if tag == 'if':
				if d1 == d2:
					if style != '':
						o += self.do("[s %s %s]" % (style,d3))
					else:
						o += d3
			else:
				if d1 != d2:
					if style != '':
						o += self.do("[s %s %s]" % (style,d3))
					else:
						o += d3
		except:
			o = ' ? ifelse error: "'+tag+' '+str(data)+'" ? '
		return o

	def comment_fn(self,tag,data):
		return ''

	# [repeat count stuff]
	# count may be:
	#	integer
	#	[v name]
	#	[lv name]
	#	[gv name]
	#	[parm number]
	def repeat_fn(self,tag,data):
		self.xdcount += 1
		if self.dlimit != 0:
			if self.xdcount > self.dlimit:
				self.xdcount -= 1
				return '! looping depth exceeded in repeat !'
		o = ''
		try:
			d1,d2 = data.split(' ',1)
			if (d1[:2] == '[v' or
				d1[:3] == '[gv' or
				d1[:3] == '[lv' or
				d1[:5] == '[parm'):
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
			if x == 0: return ''
			if self.xlimit != 0:
				if x > self.xlimit:
					x = self.xlimit
			for i in range(0,x):
				o += self.do(d2)
		self.xdcount -= 1
		return o

	def evenodd_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['style'],data)
		style = ''
		for el in opts:
			if el[0] == 'style=':
				style = el[1]
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
				if style != '':
					self.do("[s %s]" % style)
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

	# [replace (sep=X,)(lf=1)repStringXwithStringXinString] X default=,
	def replace_fn(self,tag,data):
		mode = 0
		opts,data = self.popts(['sep','lf'],data)
		style = ''
		sep = ','
		o = ''
		lf = False
		for el in opts:
			if el[0] == 'sep=':
				sep = el[1]
			if el[0] == 'lf=':
				if el[1] == '1':
					lf = True
		ll = data.split(sep,2)
		if len(ll) != 3:
			return 'ERROR: Bad replace format in '+data
		if lf:
			if ll[0] == 'lf': ll[0] = '\n'
			if ll[1] == 'lf': ll[1] = '\n'
		self.theGlobals['inner_diag'] = self.safeup(str(lf)+' '+str(ll)+'**'+o+'**')
		o = ll[2].replace(ll[0],ll[1])
		self.theGlobals['inner_diag'] = self.safeup(str(lf)+' '+str(ll)+'**'+o+'**')
		return o
		ll = data.split(',',1)
		if len(ll) != 2: return data
		if ll[0][:4] == 'sep=':
			sep = ll[0][4:]
			if sep == '': return data
			mode = 1
		if mode == 0:
			a = ll[0]
			if a == '[lf]': a = '\n'
			ll = ll[1].split(',',1)
			if len(ll) != 2: return data
			b,c = ll
			self.theGlobals['inner_diag'] = self.safeup('2:'+a+str(ll))
		else:
			ll = ll[1].split(sep,2)
			if len(ll) != 3: return data
			a,b,c = ll
			self.theGlobals['inner_diag'] = self.safeup('3:'+str(ll))
		o = c.replace(a,b)
		return o

	def safeup(self,s):
		x = 'xy3zy'
		s = s.replace('[',x)
		s = s.replace(']','[rb]')
		s = s.replace(x,'[lb]')
		return s

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

	def fsplit(self,data,splitter):
		ll = data.split(splitter)
		lx = []
		for el in ll:
			lx.append(float(el))
		return lx

	# [alphalead]
	def alphalead_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['trail'],data)
		trail='0'
		o = ''
		t = ''
		sw = 0
		for el in opts:
			if el[0] == 'trail=':
				trail = el[1]
		for c in data:
			if ((sw == 0) and ((c <= 'z' and c >= 'a') or
			    (c <= 'Z' and c >= 'A'))):
				o += c;
			else:
				sw = 1
				if trail == '1':
					t += c
				else:
					break
		if trail == '1':
			o = t
		return o

	# [alphanumlead]
	def alphanumlead_fn(self,tag,data):
		opts,data = self.popts(['trail'],data)
		trail='0'
		o = ''
		t = ''
		sw = 0
		for el in opts:
			if el[0] == 'trail=':
				trail = el[1]
		for c in data:
			if ((sw == 0) and ((c <= 'z' and c >= 'a') or
			    (c <= 'Z' and c >= 'A') or
			    (c <= '9' and c >= '0'))):
				o += c;
			else:
				sw = 1
				if trail == '1':
					t += c
				else:
					break
		if trail == '1':
			o = t
		return o

	# [stage start end steps step]
	def stage_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['mode','digits'],data)
		mode = 'int'
		digits = 2
		for el in opts:
			if el[0] == 'mode=':
				mode = el[1]
			if el[0] == 'digits=':
				try:
					digits = int(el[1])
				except:
					pass
		try: # 250 123 16 1
			start,end,steps,step = self.fsplit(data,' ')
			iend = int(end)
			steps = abs(steps)
			step = abs(step)
			if steps < 1.0:
				steps = 1.0
			perstep = (end-start) / steps
			r = start + (perstep * step)
			if mode == 'int':
				r = int(r)
				if perstep > 0:
					if r > iend:
						r = iend
				else:
					if r < iend:
						r = iend
			else:
				if perstep > 0:
					if r > end:
						r = end
				else:
					if r < end:
						r = end
			if mode == 'int':
				o = "%d" % (r)
			else:
				fmt = '%%.%df' % (digits)
				o += fmt % (r)
		except Exception,e:
			o = 'Error with "%s": "%s" ' % (data,str(e))
		return o

	def crop_fn(self,tag,data):
		opts,data = self.popts(['col','eol','neol','words'],data)
		col = 78
		eol = '\n'
		neol = '\n'
		lneol = 1
		words = ''
		for el in opts:
			if el[0] == 'col=':
				try:
					col = abs(int(el[1]))
				except:
					col = 78
			elif el[0] == 'eol=':
				eol = str(el[1])
			elif el[0] == 'neol=':
				neol = str(el[1])
				lneol = len(neol)
			elif el[0] == 'words=':
				words = str(el[1])
		o = ''
		pos = 0
		dex = -1
		word = -1
		buffer = ''
		for c in data:
			pos += 1 # position in current line
			dex += 1 # position in input data
			if c == ' ':
				word = pos # marks index in buffer of last space encounters (word interspersion)
			if pos > col: # line has exceeded allowed length
				if words != '' and word != -1:	# in this case, there were spaces in the line
					o += buffer[0:word] + eol	# terminate after the last word found
					buffer = buffer[word:]		# buffer now contains only what remains after word
					pos = len(buffer)			# and that's where we are
				else: # no spaces enountered, so we'll arbitrarily crop at set limit:
					buffer += eol
					o += buffer
					buffer = ''
					pos = 0
			else:
				if data[dex:dex+lneol] == neol:
					pos = 0
					o += buffer
					buffer = ''
			buffer += c
		if buffer != '':
			o += buffer
		return o

	def math_fn(self,tag,data):
		opts,data = self.popts(['mode'],data)
		mode = 'int'
		for el in opts:
			if el[0] == 'mode=':
				if str(el[1]) == 'float':
					mode = 'float'
		o = ''
		try:
			if tag == 'add' or tag == 'sub' or tag == 'div' or tag == 'mul':
				d1,d2 = data.split(' ',1)
			else:
				d1 = data
				d2 = '1'
			if mode == 'int':
				d2 = int(d2)
				x = int(d1)
			else:
				d2 = float(d2)
				x = float(d1)
		except:
			pass
		else:
			if tag == 'add' or tag == 'inc':
				x = str(x + d2)
			elif tag == 'mul':
				x = str(x * d2)
			elif tag == 'div':
				try:
					if mode == 'int':
						x = str(int(x / d2))
					else:
						x = str(x / d2)
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
		if l >= w: return ll[2]
		c = int((w-l)/2)
		pad = ll[1] * c
		if both == True:
			rc = w - (c + l)
			rpad = ll[1] * rc
			return pad+ll[2]+rpad
		return pad+ll[2]

	def hug_fn(self,tag,data):
		if self.noembrace == True:
			return '! embrace Not Available !'
		o = ''
		p = data.split('.py')
		try:
			huggee = imp.load_source('plug',data)
		except:
			o += ' !embrace import! '
			pass
		else:
			try:
				exclass = huggee.plug()
				exclass.install(self)
				exfns = exclass.gettable()
				for key in exfns.keys():
					self.fns[key] = exfns[key]
			except Exception,e:
				o = ' !embrace "%s" fail: %s! ' % (data,e)
		return o

	def csssplit(self,line):
		ray = []
		token = ''
		ttype = 0
		inquote = ''
		slashcount = 0
		slashing = 0
		for c in line:
			if c == '/':
				slashcount += 1
				if slashcount == 2:
					slashing = 1
					if len(token) > 1: # case where comment begins w/o whitespace
						ray += [token[0:-1]]
						token = '/'
			else:
				slashcount = 0
			if slashing == 1:
				token += c
			elif c == '"':
				if inquote == '"': # then this is closing quote
					token += c
					ray += [token]
					token = ''
					inquote = ''
					ttype = 0
					c = ''
				else: # this is an opening quote
					inquote = c
					if token != '':
						ray += [token]
						token = ''
						ttype = 4
			if slashing == 1:
				pass
			elif inquote != '':
				token += c
			elif c == ' ' or c == '\t': # this is whitespace
				if ttype == 0 or ttype == 1: # if this is a whitespace token
					token += c
				else: # NOT a whitespace token
					if token != '': # add previous token to list if exists
						ray += [token]
					token = c # new token begins with this whitespace char
				ttype = 1
			elif (	(c >= 'a' and c <= 'z') or
					(c >= 'A' and c <= 'Z') or
					(c >= '0' and c <= '9') or
					(c == '_') or
					(c == '#' and token == '')):
				if ttype == 0 or ttype == 2: # text token
					token += c
				else: # token is NOT text
					if token != '': # add previous token to list
						ray += [token]
					token = c # new token begins with this text char
				ttype = 2
			else: # some kind of special character
				if ttype == 0 or ttype == 3: # special char token
					token += c
				else: # token is NOT special
					if token != '': # add previous token to list
						ray += [token]
					token = c # new token begins with this special char
				ttype = 3
		if token != '': # pending token?
			ray += [token]
		return ray

	def ocsssplit(self,line):
		ray = []
		token = ''
		ttype = 0
		inquote = ''
		slashcount = 0
		slashing = 0
		for c in line:
			if c == '/':
				slashcount += 1
				if slashcount == 2:
					slashing = 1
					if len(token) > 1: # case where comment begins w/o whitespace
						ray += [token[0:-1]]
						token = '/'
			else:
				slashcount = 0
			if slashing == 1:
				token += c
			elif c == '"':
				if inquote == '"': # then this is closing quote
					token += c
					ray += [token]
					token = ''
					inquote = ''
					ttype = 0
					c = ''
				else: # this is an opening quote
					inquote = c
					if token != '':
						ray += [token]
						token = ''
						ttype = 4
			if slashing == 1:
				pass
			elif inquote != '':
				token += c
			elif c == ' ' or c == '\t': # this is whitespace
				if ttype == 0 or ttype == 1: # if this is a whitespace token
					token += c
				else: # NOT a whitespace token
					if token != '': # add previous token to list if exists
						ray += [token]
					token = c # new token begins with this whitespace char
				ttype = 1
			elif (	(c >= 'a' and c <= 'z') or
					(c >= 'A' and c <= 'Z') or
					(c >= '0' and c <= '9') or
					(c == '_') or
					(c == '#' and token == '') or
					(c == '@' and token == '')):
				if ttype == 0 or ttype == 2: # text token
					token += c
				else: # token is NOT text
					if token != '': # add previous token to list
						ray += [token]
					token = c # new token begins with this text char
				ttype = 2
			else: # some kind of special character
				if ttype == 0 or ttype == 3: # special char token
					token += c
				else: # token is NOT special
					if token != '': # add previous token to list
						ray += [token]
					token = c # new token begins with this special char
				ttype = 3
		if token != '': # pending token?
			ray += [token]
		return ray

	def getc_fn(self,tag,data):
		o = ''
		opts,data = self.popts(['tabsiz','tabchar','high','var'],data,True)
		tabsiz = 4
		tabchar = '&nbsp;'
		high = ''
		var = ''
		for el in opts:
			if el[0] == 'tabsiz=':
				try:
					tabsiz = int(el[1])
				except:
					pass
			elif el[0] == 'tabchar=':
				if el[1] == 'sp':
					tabchar = ' '
				else:
					tabchar = el[1]
			elif el[0] == 'high=':
				high = el[1]
			elif el[0] == 'var=':
				var = el[1]
		filename = data
		try:
			if var == '':
				if self.noshell == True:
					return '!! File Read Not Available !!'
				fh = open(filename)
		except:
			o = '--unable to open "%s"--' % (filename)
		else:
			fpre = 'fibble87pre'
			fpost = 'fibble87post'
			spre = 'glocker23pre'
			spost = 'glocker23post'
			stpre = 'wsp74pre'
			stpost = 'wsp74post'
			copre = 'ogy8080pre'
			copost = 'ogy8080post'
			pppre = 'sksk1802pre'
			pppost = 'sksk1802post'
			atpre = 'ghy8000pre'
			atpost = 'ghy8000post'
			ckeys = ['auto','break','case','char',
					'const','continue','default','do',
					'double','else','enum','extern',
					'float','for','goto','if',
					'int','long','register','return',
					'short','signed','sizeof','static',
					'struct','switch','typedef','union',
					'unsigned','void','volatile','while']
			cpkeys = ['alignas','alignof','and','and_eq',
					'asm','atomic_cancel','atomic_commit','atomic_noexcept',
					'auto','bitand','bitor','bool','break','case','catch','char',
					'char16_t','char_32t','class','compl',
					'concept','const','constexpr','conts_cast',
					'continue','decltype','default','delete','do',
					'double','dynamic_cast','else',
					'enum','explicit','export','extern','false',
					'float','for','friend','goto','if','import','inline',
					'int','long','module','mutable',
					'namespace','new','noexcept','not','not_eq',
					'nullptr','operator','or','or_eq','private',
					'protected','public','register','reinterpret_cast',
					'requires','return',
					'short','signed','sizeof','static','static_assert',
					'static_cast','struct','switch','synchronized',
					'template','this','thread_local','throw',
					'true','try','typedef','typeid','typename','union',
					'unsigned','using','virtual','void','volatile',
					'wchar_t','while','xor','xor_eq']
			ockeys = ['auto','break','case','char',
					'const','continue','default','do',
					'double','else','enum','extern',
					'float','for','goto','if',
					'int','long','register','return',
					'short','signed','sizeof','static',
					'struct','switch','typedef','union',
					'unsigned','void','volatile','while',
					'id','inline','restrict']
			skeys = [' ','\t']
			tr = tabchar * tabsiz
			try:
				spacefool = 'space6809fool'
				mlist = []
				if var == '':
					for line in fh:
						mlist.append(line)
				else:
					line = ''
					if self.theLocals.get(var,'') == '': return '???var '+c+'???'
					for c in self.theLocals[var]:
						line += c
						if c == '\n':
							mlist.append(line)
							line = ''
					if line != '':
						mlist.append(line)
				for line in mlist:
					xx = ''
					for c in line:
						if c == chr(9):
							ll = len(xx) # current line length
							rm = ll % tabsiz # remainder to get to next tab
							tr = spacefool * (tabsiz - rm)
							xx += tr
						else:
							xx += c
					line = xx
					if high == 'c':
						cline = self.csssplit(line)
						line = ''
						for el in cline:
							cc = el[0:1]
							if el in ckeys:
								el = fpre + el + fpost
							elif cc == ' ' or cc == '\t':
								pass # whitespace
							elif el[0:2] == '//':
								el = copre + el + copost
							elif cc == '"':
								el = stpre + el + stpost
							elif cc == '#':
								el = pppre + el + pppost
							elif (	(cc >= 'a' and cc <= 'z') or
									(cc >= 'A' and cc <= 'Z') or
									(c == '_') or
									(cc >= '0' and cc <= '9')):
								pass # not a keyword
							else: # special chars
								el = spre + el + spost
							line += el
					if high == 'cp':
						cline = self.csssplit(line)
						line = ''
						for el in cline:
							cc = el[0:1]
							if el in cpkeys:
								el = fpre + el + fpost
							elif cc == ' ' or cc == '\t':
								pass # whitespace
							elif el[0:2] == '//':
								el = copre + el + copost
							elif cc == '"':
								el = stpre + el + stpost
							elif cc == '#':
								el = pppre + el + pppost
							elif (	(cc >= 'a' and cc <= 'z') or
									(cc >= 'A' and cc <= 'Z') or
									(c == '_') or
									(cc >= '0' and cc <= '9')):
								pass # not a keyword
							else: # special chars
								el = spre + el + spost
							line += el
					elif high == 'oc':
						cline = self.ocsssplit(line)
						line = ''
						for el in cline:
							cc = el[0:1]
							if el in ockeys:
								el = fpre + el + fpost
							elif cc == ' ' or cc == '\t':
								pass # whitespace
							elif el[0:2] == '//':
								el = copre + el + copost
							elif cc == '"':
								el = stpre + el + stpost
							elif cc == '#':
								el = pppre + el + pppost
							elif cc == '@':
								el = atpre + el + atpost
							elif (	(cc >= 'a' and cc <= 'z') or
									(cc >= 'A' and cc <= 'Z') or
									(c == '_') or
									(cc >= '0' and cc <= '9')):
								pass # not a keyword
							else: # special chars
								el = spre + el + spost
							line += el
					oo = ''
					for c in line:
						if c == '<': oo += '&lt;'
						elif c == '>': oo += '&gt;'
						elif c == '[': oo += '&#91;'
						elif c == ']': oo += '&#93;'
						elif c == '{': oo += '&#123;'
						elif c == '}': oo += '&#125;'
						elif c == '"': oo += '&quot;'
						elif c == '&': oo += '&amp;'
						else: oo += c

					oo = oo.replace(fpre,'<span style="color: #'+self.theGlobals['cpp_fpre']+';">')
					oo = oo.replace(fpost,'</span>')
					oo = oo.replace(spre,'<span style="color: #'+self.theGlobals['cpp_spre']+';">')
					oo = oo.replace(spost,'</span>')
					oo = oo.replace(stpre,'<span style="color: #'+self.theGlobals['cpp_stpre']+';">')
					oo = oo.replace(stpost,'</span>')
					oo = oo.replace(copre,'<span style="color: #'+self.theGlobals['cpp_copre']+';">')
					oo = oo.replace(copost,'</span>')
					oo = oo.replace(pppre,'<span style="color: #'+self.theGlobals['cpp_pppre']+';">')
					oo = oo.replace(pppost,'</span>')
					oo = oo.replace(atpre,'<span style="color: #'+self.theGlobals['cpp_atpre']+';">')
					oo = oo.replace(atpost,'</span>')

					oo = oo.replace(spacefool,tabchar)
					o += oo
			except Exception,e:
				try:
					if var == '':
						fh.close()
				except:
					pass
				o += '--error while reading "%s": %s--' % (filename,str(e))
			else:
				try:
					if var == '':
						fh.close()
				except:
					o += '--error closing "%s"--' % (filename)
		return o

	def br_fn(self,tag,data):
		o = ''
		parms = ''
		opts,data = self.popts(['parms'],data,True)
		for el in opts:
			if el[0] == 'parms=':
				parms = ' '+el[1]
		if data != '': # if there is content
			o += data+'<br'+parms+'>'
		else: # no content
			o += '<br'+parms+'>'
		return o

	def random_fn(self,tag,data):
		opts,data = self.popts(['seed','icount'],data,True)
		seed = 0
		icount = 1
		for el in opts:
			if el[0] == 'seed=':
				if str(el[1]) == 'none':
					random.seed()
				else:
					random.seed(el[1])
			elif el[0] == 'icount=':
				try:
					icount = abs(int(el[1]))
				except:
					icount = 1
		for i in range(0,icount):
			n = random.random()
		o = str(n)
		return o

	def encrypt_fn(self,tag,data):
		opts,data = self.popts(['seed','salt','icount','breakat','again','mode'],data)
		o = ''
		nsalt = ''
		raw=0
		lmode=0
		nseed = 1
		icount = 1
		breakdef = 16
		breakat = breakdef
		for el in opts:
			if el[0] == 'seed=':
				nseed = el[1]
			elif el[0] == 'salt=':
				nsalt = el[1]
			elif el[0] == 'again=':
				try:
					raw = int(el[1])
				except:
					raw = 0
			elif el[0] == 'mode=':
				try:
					lmode = abs(int(el[1]))
				except:
					lmode = 0
			elif el[0] == 'icount=':
				try:
					icount = abs(int(el[1]))
				except:
					icount = 1
			elif el[0] == 'breakat=':
				try:
					breakat = int(el[1])
				except:
					breakat = breakdef
				if breakat < 1:
					breakat = 1
		if lmode == 0:
			try:
				nseed = abs(int(nseed))
				if nseed == 0:
					nseed = 1
			except:
				nseed = 1
		if raw == 1:
			tmp = ''
			phase = 0
			for c in data:
				if c in 'ABCDEF0123456789':
					if phase == 0:
						phase = 1
						cx = int(c,16) * 16
					else:
						phase = 0
						cx += int(c,16)
						tmp += chr(cx)
			data = tmp
		try:
			rmod = argen(seed=nseed,salt=nsalt,iteratecount=icount,mode=lmode)
		except Exception,e:
			o += str(e)+'\n'
		try:
			v = rmod.encrypt(data)
			if breakat != 0:
				ct = 0
				for c in v:
					o += c
					ct += 1
					if ct >= breakat:
						o += '\n'
						ct = 0
			else:
				o = v
		except Exception,e:
			o += str(e)+'\n'
		return o

	def decrypt_fn(self,tag,data):
		opts,data = self.popts(['seed','salt','icount','mode'],data)
		o = ''
		nsalt = ''
		lmode = 0
		nseed = 1
		icount = 1
		for el in opts:
			if el[0] == 'seed=':
				nseed = el[1]
			if el[0] == 'salt=':
				nsalt = el[1]
			elif el[0] == 'mode=':
				try:
					lmode = abs(int(el[1]))
				except:
					lmode = 0
			if el[0] == 'icount=':
				try:
					icount = abs(int(el[1]))
				except:
					icount = 1
		if lmode == 0:
			try:
				nseed = abs(int(nseed))
				if nseed == 0:
					nseed = 1
			except:
				nseed = 1
		try:
			rmod = argen(seed=nseed,salt=nsalt,iteratecount=icount,mode=lmode)
		except Exception,e:
			o += str(e)+'\n'
		try:
			data = data.replace('\n','')
			x = rmod.decrypt(data)
			for c in x:
				v = ord(c)
				if v == 0x0a:
					o += c
				elif v == 0x0d:
					o += c
				elif v >= 0x20 and v < 0x7F:
					o += c
				else:
					o += '?'
		except Exception,e:
			o += str(e)+'\n'
		return o

	def setFuncs(self): #    '':self._fn,
		self.fns = {
					# escape codes
					# ------------
					'co'	: self.co_fn,		#	,	HTML char-encoded comma
					'lt'	: self.lt_fn,		#	,	HTML char-encoded less-than
					'gt'	: self.gt_fn,		#	,	HTML char-encoded greater-than
					'sp'	: self.sp_fn,		#	,	space
					'lb'	: self.lb_fn,		#	[	left square bracket
					'rb'	: self.rb_fn,		#	]	right square bracket
					'ls'	: self.ls_fn,		#	{	left brace
					'rs'	: self.rs_fn,		#	}	right brace
					'vb'	: self.vb_fn,		#   |   vertical bar
					'nl'	: self.nl_fn,		#   newline (0x0a)
					'lf'	: self.nl_fn,		#   newline (0x0a)

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
					'dcopy'	: self.dcopy_fn,	# [dcopy srcDict,dstDict] copy dictionary
					'dkeys'	: self.dkeys_fn,	# [dkeys srcDict,dstList] dictionary keys --> list
					'setd'	: self.setd_fn,		# [setd (keysep=Y,)dictName,keyYvalue]
					'dset'	: self.setd_fn,		# [dset (keysep=Y,)dictName,keyYvalue]
					'd'		: self.d_fn,		# [d dictName,key] = "value"
					'expand': self.expand_fn,	# [expand dict,content]

					# Data list handling
					'list'	: self.list_fn,		# create list:  [list (sep=X,)listName,listElements]
					'clearl': self.clearl_fn,	# [clearl listName] make list empty
					'lcopy'	: self.lcopy_fn,	# [lcopy srcList,dstList] copy list
					'e'		: self.element_fn,	# fetch element:[e listName,n] = list[n]
					'append': self.append_fn,	# [append listName,stuff]
					'lpush'	: self.append_fn,	# [lpush listName,stuff]
					'translate':self.translate_fn, # [translate listName,stuff]
					'lset'	: self.lset_fn,		# [lset listName,index,stuff]
					'lcc'	: self.lcc_fn,		# [lcc listNameA,listNameB,listNameC] C = A concat B
					'cmap'	: self.cmap_fn,		# [cmap listName]
					'hmap'	: self.hmap_fn,		# [hmap listName]
					'dlist'	: self.dlist_fn,	# [dlist (style=styleName,)listName] dump list
					'asort'	: self.asort_fn,	# [asort listName] sort by alpha, case-sensitive
					'aisort': self.aisort_fn,	# [aisort listName] sort by alpha, case-insensitive
					'isort'	: self.isort_fn,	# [isort listName] sort by leading integer,
					'lhsort': self.lhsort_fn,	# [lhsort listName] sort by leading ham radio callsign
					'ltol'	: self.ltol_fn,		# [ltol listName,content] content to list by line
					'llen'	: self.llen_fn,		# [llen listName] length of list
					'lslice': self.lslice_fn,	# [lslice sliceSpec,listToSlice,intoList]
					'lsplit': self.lsplit_fn,	# [lsplit (sep=^,)listName,splitKey^contentToSplit]
					'ljoin'	: self.ljoin_fn,	# [ljoin listName,joinContent]
					'lpop'	: self.lpop_fn,		# [lpop listName( index)]
					'lsub'	: self.lsub_fn,		# [lsub (sep=X,)listName,content]

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
					'url'	: self.url_fn,		# [url (sep=|,)(nam=Name,)(css=CSS,)(tgt=_target,)URLsepITEM]

					# Image handling
					# --------------
					'img'	: self.img_fn,		# img emplacement from URL
					'limg'	: self.limg_fn,		# local image (tries for x y sizes, title, alt)
					'locimg': self.locimg_fn,	# local image (tries for x y sizes)
					'lipath': self.lipath_fn,	# set local image path
					'wepath': self.wepath_fn,	# set web image path

					# math
					# ----
					'int'	: self.int_fn,		# [int number]
					'round'	: self.round_fn,	# [round number]
					'abs'	: self.abs_fn,		# [abs number]
					'add'	: self.math_fn,		# P1 + P2
					'sub'	: self.math_fn,		# P1 - P2
					'mul'	: self.math_fn,		# P1 * P2
					'div'	: self.math_fn,		# P1 / P2
					'inc'	: self.math_fn,		# P1 + 1
					'dec'	: self.math_fn,		# P1 - 1
					'max'	: self.max_fn,		# max v1 v2
					'min'	: self.min_fn,		# min v1 v2
					'stage'	: self.stage_fn,	# stage start end steps step
					'random': self.random_fn,	# [random( )(seed=none,)(icount=N)]

					# conditionals
					# ------------
					'if'	: self.ifelse_fn,	# if P1 == P2 then P3
					'else'	: self.ifelse_fn,	# if P1 != P2 then P3
					'even'	: self.evenodd_fn,	# if P1 even then P2
					'odd'	: self.evenodd_fn,	# if P1 odd then P2
					'ne'	: self.ne_fn,		# if P1 non-empty,P2 (p1,p2)
					'eq'	: self.eq_fn,		# if P1 empty,P2 (p1,p2)
					'ifle'	: self.ifle_fn,		# if P1 <= P2 then P3
					'ifge'	: self.ifge_fn,		# if P1 >= P2 then P3

					# variable handling
					# -----------------
					'local'	: self.local_fn,	# define local variable:					P1 <-- P2
					'raw'	: self.local_fn,	# define local variable:					P1 <-- P2
					'vs'	: self.local_fn,	# "     ditto         "						P1 <-- P2
					'global': self.global_fn,	# define global variable					P1 <-- P2
					'graw'	: self.global_fn,	# define global variable					P1 <-- P2
					'page'	: self.page_fn,		# clear local variables
					'spage'	: self.spage_fn,	# clear local styles
					'gv'	: self.gv_fn,		# use global variable						P1 -->
					'lv'	: self.lv_fn,		# use local variable						P1 -->
					'v'		: self.v_fn,		# use local variable. if none, use global	P1 -->
					'clear'	: self.clear_fn,	# clear a local variable					'' -> P1
					'vinc'	: self.vinc_fn,		# increment a local(global) variable
					'vdec'	: self.vdec_fn,		# deccrement a local(global) variable
					'load'	: self.load_fn,		# load file into local variable
					'gload'	: self.gload_fn,	# load file into global variable
					'save'	: self.save_fn,		# save file from local variable
					'gsave'	: self.gsave_fn,	# save file from global variable

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
					'switch': self.switch_fn,	# define a switch
					'case'  : self.case_fn,		# define a case
					'for'	: self.for_fn,		# [for style,x,y,z]
					'in'	: self.in_fn,		# [in style,list]
					'helps'	: self.helps_fn,	# [helps stylename]
					'helpg'	: self.helpg_fn,	# [helpg stylename]
					'helps2': self.helps2_fn,	# [helps2 stylename]
					'helpg2': self.helpg2_fn,	# [helpg2 stylename]

					# Parsing and text processing
					# ---------------------------
					'splitcount': self.splitcount_fn,	# [splitcount n]
					'slice'	: self.slice_fn,	# [slice sliceSpec,textToSlice]
					'split'	: self.split_fn,	# [split splitSpec,testToSplit] (obeys splitcount)
					'splash': self.splash_fn,	# [splash (pre=,)(post=,)(inter=,)(ntl=,)(sep=,,)(limit=N,)(style=Style,)data]
					'rstrip': self.rstrip_fn,	# [rstrip stuff] trailing whitespace removed
					'stripe': self.stripe_fn,	# [stripe (charset=chars,)stuff] whitespace, etc removal
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
					'collapse':self.collapse_fn,# [collapse content]
					'crush'	: self.crush_fn,	# [crush content]
					'chr'	: self.chr_fn,		# [chr number] e.g. [chr 65] = "A"
					'ord'	: self.ord_fn,		# [ord character] e.g. [ord A] = 65
					'csep'	: self.csep_fn,		# [csep integer] e.g. [csep 1234] = "1,234"
					'fcsep' : self.fcsep_fn,	# [fcsep float] e.g. [fcsep 1234.56] = "1,234.56"
					'dup'	: self.dup_fn,		# [dup content] e.g. [dup 3,foo] = "foofoofoo"
					'eval'	: self.eval_fn,		# [eval content] e.g. [eval 3,foo] = "foofoofoo"
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
					'crop'	: self.crop_fn,		# [crop (words=no,)(eol=\n,)(neol=\n,)(col=78),content] - crop to column width
					'hlit'	: self.hlit_fn,		# [hlit content]
					'vlit'	: self.vlit_fn,		# [hlit variable-name]
					'slit'	: self.slit_fn,		# [hlit style-name]
					'postparse':self.postparse_fn, # [postparse text]
					'pythparse':self.pythparse_fn, # [pythparse text]
					'th'	: self.th_fn,		# [th integer] = st, nd, rd, th
					'nd'	: self.nd_fn,		# [th integer] = 1st, 2nd, 3rd, 4th
					'getc'	: self.getc_fn,		# [getc filename] import c text
					'alphalead': self.alphalead_fn, #[alphalead (trail=1,)string] return leading alpha
					'alphanumlead': self.alphanumlead_fn, #[alphanumlead (trail=1,)string] return leading alpha
					'encrypt':self.encrypt_fn,	#[encrypt (seed=N,)(seed=String,)content]
					'decrypt':self.decrypt_fn,	#[decrypt (seed=N,)(seed=String,)content]
					'br'	: self.br_fn,		#[br( parms=stuff)(content)]

					# Miscellaneous
					# -------------
					'repeat': self.repeat_fn,	# N ThingToBeRepeated
					'nc'	: self.nc_fn,		# [nc TEXT] escape all commas
					'comment': self.comment_fn, # contained content will not render
					'mode'	: self.mode_fn,		# [mode 3.2] or [mode 4.01s] sets HTML output mode
					'back'	: self.back_fn,		# P1=HHH or HHHHHH then P2 is what gets colored
					'ghost'	: self.ghost_fn,	# [ghost styleName] print verbatim
					'listg'	: self.listg_fn,	# [listg (source=local,) listName]
					'include':self.inclu_fn,	# [include filename] grab some styles, etc.
					'embrace':self.hug_fn,		# [embrace moduleName] extend built-ins
					'time'	: self.time_fn,		# [time] Generation time
					'date'	: self.date_fn,		# [date] Generation date
					'ddelta': self.ddelta_fn,	# [ddelta date1 date2]
					'datetime':self.datetime_fn,# [datetime] = YYYYmmDDhhMMss
					'month'	: self.month_fn,	# [month (mode=long,)N]
					'ampm'	: self.ampm_fn,		# [ampm N]
					'twelve':self.twelve_fn,	# [twelve N]
					'usdate': self.usdate_fn,	# [usdate YYYYmmDD]
					'sys'	: self.sys_fn,		# [sys SHELLCMD]
					'fref'	: self.fref_fn,		# forward reference
					'resolve': self.reso_fn,	# resolve forward reference	
					'term'	: self.term_fn,		# expand known term
		}

	def debugdo(self,s):
		self.debuglevel += 1
		o = ''
		if type(s) != str:
			self.debuglevel -= 1
#			self.debstack.append('input not a string')
# (tag,depth+1,ltln,lastdex,ldata)
			self.debstack.append(('MESSAGE: input not a string',0,0,0,'',self.debuglevel))
			return ''
		if len(s) == 0:
			self.debuglevel -= 1
			self.debstack.append(('MESSAGE: Input string empty',0,0,0,'',self.debuglevel))
#			self.debstack.append('Input string empty')
			return ''
		inout = 0
		fg = 1
		lasttag = ''
		lastdex = 0
		OUT = 0
		IN = 1
		DEFER = 2
		depth = 0
		state = OUT
		macstack = []
		drecord = []
		ln = 1
		ltln = 1

		# This is a bit gnarly; first, I replace "{" with "[s " as "{"
		# is simply a shorthand for a style invocation. Then I allow
		# for the syntax of separating the invocation of a style from
		# its parameter(s) with either a space or a newline, by converting
		# the newlines used this way into a space so as to simplify
		# subsequent processing.
		# ----------------------------------------------------------------
		s = s.replace('\n\r','\n')
		s = s.replace('\r\n','\n')
		tok = 'prolly84673@c@747code'
		s = s.replace('{\n',tok)
		if fg == 0: s = s.replace('{','[s ')
		s = re.sub(r'(\[s\s[\w-])\n',r'\1 ',s)
#		if fg == 1: re.sub(r'(\{[\w-])\n',r'\1 ',s)
		if fg == 1:
			s = re.sub('(\\{\\w*)\n','\\1 ',s)
#			s = re.sub(r'(\{[\w-])\n',r'\1 ',s)
		if self.noDinner == False:
			s = s.replace('  \n','')
		s = s.replace(tok,'{\n')

		dex = -1
		tag = ''
		for c in s:
			if c == '\n':
				ln += 1
			if fg == 0:
				if c == '}':
					c = ']'
			dex += 1
			if state == OUT and (c == '[' or c == '{'):
				if (s[dex:dex+8]  == '[gstyle ' or
					s[dex:dex+7]  == '[style ' or
					s[dex:dex+5]  == '[raw ' or
					s[dex:dex+6]  == '[graw ' or
					s[dex:dex+8]  == '[repeat ' or
					s[dex:dex+11] == '[pythparse ' or
					s[dex:dex+6]  == '[hlit '):
					state = DEFER
					depth = 1
					lasttag = tag
					lastdex = dex
					tag = ''
					data = ''
					ltln = ln
				elif c == '{': # this is equiv to '[s '
					state = IN
					lasttag = tag
					lastdex = dex
					tag = 's '
					data = ''
					depth = 1
					ltln = ln
				else:
					state = IN
					lasttag = tag
					lastdex = dex
					tag = ''
					data = ''
					depth = 1
					ltln = ln
			elif state == DEFER:
				if c == '[' or c == '{':
					tag += c
					depth += 1
					ltln = ln
				elif c == ']' or c == '}':
					depth -= 1
					if depth == 0:
						if tag.find(' ') > 0:
							tag,data = tag.split(' ',1)
#							ldata = data.replace('[','&#91;')
#							ldata = ldata.replace(']','&#93;')
#							ldata = ldata.replace('{','&#123;')
#							ldata = ldata.replace('}','&#125;')
#							self.debstack.append('tag:"%s" depth:%d line:%d char:%d data:\n"%s"\n' % (tag,depth+1,ltln,lastdex,ldata))
							self.debstack.append((tag,depth+1,ltln,lastdex,data,self.debuglevel))
							o += self.doTag(tag,data)
							state = OUT
					else:
						tag += c
				else:
					tag += c
			elif state == IN and (c == ']' or c == '}'):
				depth -= 1
				if tag.find(' ') > 0:
					tag,data = tag.split(' ',1)
#				ldata = data.replace('[','&#91;')
#				ldata = ldata.replace(']','&#93;')
#				ldata = ldata.replace('{','&#123;')
#				ldata = ldata.replace('}','&#125;')
#				self.debstack.append('tag:"%s" depth=%d line:%d char:%d data:\n"%s"\n' % (tag,depth+1,ltln,lastdex,ldata))
				self.debstack.append((tag,depth+1,ltln,lastdex,data,self.debuglevel))
				fx = self.doTag(tag,data)
				if len(macstack) == 0:
					o += fx
					state = OUT
					depth = 0
				else:
					lasttag = tag
					lastdex = dex
					tag = macstack.pop()
					tag += fx
			elif state == IN:
				if c == '[' or c == '{': # nesting
					depth += 1
					ltln = ln
					macstack.append(tag)
					if c == '{':
						tag = 's '
					else:
						tag = ''
				else:
					tag += c
			else:
				o += c
		for key in self.refs.keys():
			o = o.replace(key,self.refs.get(key,''))
		if depth != 0:
			o += 'ERROR: Line %d, Char index %d\n<br>lasttag = "%s"\n<br>Depth != 0 (%d)\n<br>tag="%s"\n<br>data="%s"' % (ltln,lastdex,lasttag,depth,tag[:32],data[:32])
		self.result = o
		self.debuglevel -= 1
		return o

	def do(self,s):
		if self.debug == True:
			return self.debugdo(s)

		if type(s) != str:
			return ''
		if len(s) == 0:
			return ''
		inout = 0
		o = ''
		fg = 1
		lasttag = ''
		lastdex = 0
		OUT = 0
		IN = 1
		DEFER = 2
		depth = 0
		state = OUT
		macstack = []
		ln = 1
		ltln = 1

		# This is a bit gnarly; first, I replace "{" with "[s " as "{"
		# is simply a shorthand for a style invocation. Then I allow
		# for the syntax of separating the invocation of a style from
		# its parameter(s) with either a space or a newline, by converting
		# the newlines used this way into a space so as to simplify
		# subsequent processing.
		# ----------------------------------------------------------------
		s = s.replace('\n\r','\n')
		s = s.replace('\r\n','\n')
		tok = 'prolly84673@c@747code'
		s = s.replace('{\n',tok)
		if fg == 0: s = s.replace('{','[s ')
		s = re.sub(r'(\[s\s[\w-])\n',r'\1 ',s)
#		if fg == 1: re.sub(r'(\{[\w-])\n',r'\1 ',s)
		if fg == 1:
			s = re.sub('(\\{\\w*)\n','\\1 ',s)
#			s = re.sub(r'(\{[\w-])\n',r'\1 ',s)
		if self.noDinner == False:
			s = s.replace('  \n','')
		s = s.replace(tok,'{\n')

		dex = -1
		tag = ''
		for c in s:
			if c == '\n':
				ln += 1
			if fg == 0:
				if c == '}':
					c = ']'
			dex += 1
			if state == OUT and (c == '[' or c == '{'):
				if (s[dex:dex+8]  == '[gstyle ' or
					s[dex:dex+7]  == '[style ' or
					s[dex:dex+5]  == '[raw ' or
					s[dex:dex+6]  == '[graw ' or
					s[dex:dex+8]  == '[repeat ' or
					s[dex:dex+11] == '[pythparse ' or
					s[dex:dex+6]  == '[hlit '):
					state = DEFER
					depth = 1
					lasttag = tag
					lastdex = dex
					tag = ''
					data = ''
					ltln = ln
				elif c == '{': # this is equiv to '[s '
					state = IN
					lasttag = tag
					lastdex = dex
					tag = 's '
					data = ''
					depth = 1
					ltln = ln
				else:
					state = IN
					lasttag = tag
					lastdex = dex
					tag = ''
					data = ''
					depth = 1
					ltln = ln
			elif state == DEFER:
				if c == '[' or c == '{':
					tag += c
					depth += 1
					ltln = ln
				elif c == ']' or c == '}':
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
			elif state == IN and (c == ']' or c == '}'):
				depth -= 1
				if tag.find(' ') > 0:
					tag,data = tag.split(' ',1)
				fx = self.doTag(tag,data)
				if len(macstack) == 0:
					o += fx
					state = OUT
					depth = 0
				else:
					lasttag = tag
					lastdex = dex
					tag = macstack.pop()
					tag += fx
			elif state == IN:
				if c == '[' or c == '{': # nesting
					depth += 1
					ltln = ln
					macstack.append(tag)
					if c == '{':
						tag = 's '
					else:
						tag = ''
				else:
					tag += c
			else:
				o += c
		for key in self.refs.keys():
			o = o.replace(key,self.refs.get(key,''))
		if depth != 0:
			o += 'ERROR: Line %d, Char index %d\n<br>lasttag = "%s"\n<br>Depth != 0 (%d)\n<br>tag="%s"\n<br>data="%s"' % (ltln,lastdex,lasttag,depth,tag[:32],data[:32])
		self.result = o
		return o

#	self.debstack.append('tag:"%s" depth:%d line:%d char:%d data:\n"%s"\n' % (tag,depth+1,ltln,lastdex,ldata))
#	self.debstack.append((tag,depth+1,ltln,lastdex,ldata))
	def getdebug(self):
		o = 'Debug Trace:\n'
		for el in self.debstack:
			tag,depth,line,char,data,dlev = el
			o += 'level:%d tag:"%s" depth:%d line:%d char:%d data:\n"%s"\n' % (dlev,tag,depth,line,char,data)
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
			rawsty = str(self.theGlobals[key])
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

	# modes are: html, text, table
	def gstyleLib(self,mode='text',border=1):
		maxl = 0
		for key in sorted(self.gstyles.keys()):
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
		for key in sorted(self.gstyles.keys()):
			rawsty = self.gstyles[key]
			rawsty = rawsty.replace('\n','\\n')
			s += fmt % (key,rawsty,ending)
		s += post
		return s

class argen(object):
	"""Class to provide simplistic random number generator and encryption"""

	def version_set(self):
		return('0.0.2 Beta')

	def __init__(self,seed=1,iteratecount=1,salt='',mode=0):
		self.version = self.version_set()
		self.setMode(mode)
		self.setSalt(salt)
		self.setSeed(seed)
		self.setIterate(iteratecount)
		self.reset()

	def setMode(self,mode):
		try:
			tmp = abs(int(mode))
			if tmp > 1:
				mode = 0
		except:
			mode = 0
		self.mode = mode

	def setSeed(self,seed):
		if self.mode == 0:
			try:
				self.seed = abs(int(seed)) * 5
				if self.seed == 0:
					self.seed = 5
			except:
				self.seed = 1
		elif self.mode == 1:
			self.seed = seed

	def iterate(self):
		if self.mode == 0:
			for i in range(0,self.iteratecount):
				self.rnum = self.rnum * 5
				lval = (self.rnum & 0xFFFF) >> 8;
				self.rval = lval ^ self.nextGrain()
		elif self.mode == 1:
			for i in range(0,self.iteratecount):
				rfloat = random.random()
				self.rnum = int(255.999 * rfloat)
				self.rval = (self.rnum & 0xff) ^ self.nextGrain() ^ 0x5a

	def reset(self):
		if self.mode == 0:
			self.rnum = self.seed
			self.rval = 0
#			print str(self.seed)
		elif self.mode == 1:
#			print str(self.seed)
			random.seed(self.seed)
			self.iterate()
		self.shaker = 0

	def setIterate(self,iteratecount):
		try:
			self.iteratecount = abs(int(iteratecount))
			if self.iteratecount == 0:
				self.iteratecount = 1
		except:
			self.iteratecount = 1

	def setSalt(self,salt):
		self.salt = str(salt)
		self.shaker = 0
		self.grains = len(salt)

	def nextGrain(self):
		crystal = 0
		if self.grains > 0:
			self.shaker += 1
			if self.shaker >= self.grains:
				self.shaker = 0
			crystal = (ord(self.salt[self.shaker]) & 0x0F) << 4
			self.shaker += 1
			if self.shaker >= self.grains:
				self.shaker = 0
			crystal = crystal | (ord(self.salt[self.shaker]) & 0x0F)
		return crystal

	def advance(self,distance):
		for i in range(0,distance):
			self.iterate()

	def __str__(self):
		return str(self.rval)

	def get(self):
		self.iterate()
		return self.rval

	def encrypt(self,content):
		content = str(content)
		o = ''
		for c in content:
			o += "%0.2X" % (ord(c) ^ self.get())
		return o

	def decrypt(self,content,seed=None,salt=None):
		if seed != None:
			self.seed = seed
		if salt != None:
			self.salt = salt
		content = str(content)
		length = len(content)
		if length & 1 != 0:
			return ''
		i = 0
		o = ''
		while(i < length):
			o += chr(int(content[i:i+2],16) ^ self.get())
			i += 2
		return o


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
