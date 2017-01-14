# macro() BETA Changelog

### Note

This log reflects changes to the aa_macro.py import library. Other changes
such as to the associated utlitilies and sample files are not tracked here.

### Log
1.0.76
 * wtfm version of user manual goes live
 * error message on missing style for [locs] and [glos] improved
 * [switch] added
 * [case] added
 * [gt] and [lt] escapes added
 * [s], [glos] and [locs] all get sep= option for multiple style invocation
 * [asort] gets rev=1 option
 * [aisort] gets rev=1 option
 * [isort] gets rev=1 option
 * [lhsort] gets rev=1 option
 * [ssort] gets rev=1 option
 * [sisort] gets rev=1 option
 * [issort] gets rev=1 option
 * [hsort] gets rev=1 option
 * [dlist] gets fs=styleName and ls=styleName options

1.0.75
 * [eval] added

1.0.74
 * [wwrap] now has nohtml=1 option (plus [wwrap] entirely re-written)

1.0.73
 * [vinc] and [vdec] added

1.0.72
 * ? lol

1.0.71
 * [if] and [else] now have sep=X option

1.0.70
 * [th] and [nd] added

1.0.69
 * bug in [pythparse], fixed

1.0.68
 * [resolve] now has hex=1 option

1.0.67
 * [translate] now has pre=, post= and inter= options

1.0.66
 * [lsub] now has ci=1 option

1.0.65
 * [dlist] bugfix: non-style post= moved prior to inter= 

1.0.64
 * [dlist] now has ntl=NTL option

1.0.63
 * [dlist] now has inter=INT option

1.0.62
 * [split] now sets local variable loc_splitcount
 * [replace] now has lf=1 option

1.0.61
 * [pythparse] added

1.0.60
 * Changed default color for nonkeyword python from 008800 to 00ff00

1.0.59
 * Bug in [postparse] with sub-line-sized code fragments fixed

1.0.58
 * [postparse] added

1.0.57
 * [hmap] added

1.0.56
 * [slit] got (wrap=1,) option
 * Pretty-printing now handles in-quotes
 * Pretty-printing now calls out keywords and stylenames
 * new built-in variables for all of the above (see docs)

1.0.55
 * [hlit], [vlit] and [slit] all got (format=1,) options

1.0.54
 * aa_macro no longer translates {stylename} to [s stylename], {} is now native

1.0.53
 * [slit] bug fixed
 * [hlit], [vlit] and [slit] translations now mapped through variables txl_...

1.0.52
 * [vlit] added
 * [slit] added
 * styling variables added that are used by [hlit], [vlit], and [slit]

1.0.51
 * [wepath] added, function of [locimg] changed (documented)
 * [global] and [local] now accept empty: [global varName] and [local varName] (documented)
 * [lsplit] added (documented)
 * [lsplit] understands a single [sp] as a command to split on ' '
 * [ljoin] added (documented)
 * [hlit] added (documented)
 * [usdate] added

1.0.50
 * [dlist] now understands local else global style wrapping (documented)
 * [crush] added (documented)
 * [clearl] added (documented)
 * [if] now accepts wrap as a syn for style (dcoumented)

1.0.49
 * [stripe (charset=chars,)content] added
 * [img] now produces empty title and alt tags to comply with HTML 4.01 strict
 * [style], [gstyle] and [lstyle] can now all be set to empty styles viz. [style styleName] with no content
 * unittests
 * users guide
 * quickref

1.0.48
 * [repeat] now understands any of [v], [gv], [lv] and [parm]
 * [listg (source=local,)listName] added
 * [stage (mode=float,)(digits=N)start end steps step] added
 * htodec,otodec,btodec,dtohex,dtooct,dtobin all have new digits=N option
 * [dlist \(style=styleName,\)] syn for [dlist \(wrap=styleName,\)]
 * unit tests updated
 * users guide
 * quickref
 * features

1.0.47 - December 13th, 2015
 * Bug in [eq] remediated

1.0.46 - December 13th, 2015
 * Bug in [gstyle] remediated
 * unit tests updated to test for above bug

1.0.45 - September 2nd, 2015
 * conditional styles now add output to processing stream:  
 [if], [else], [even], [odd], [ne], [eq], [ifge], [ifle]

1.0.44 - September 1st, 2015
 * added style=styleName to all conditionals

1.0.43
 * removed auto-generation of newlines in [table] and [row]
 * added [vb] escape for |

1.0.42
 * added parms=X and posts=X to [dlist]

1.0.41
 * added [lcopy], [dcopy], [dkeys]

1.0.40
 * added [fref], [resolve]

1.0.39
 * added [date], [time], [sys]

1.0.38
 * added [ifge], [ifle]

1.0.37
 * added [lcc]

1.0.36
 * added [lsub]

1.0.35
 * added [include], [embrace], [lf], [expand]

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
