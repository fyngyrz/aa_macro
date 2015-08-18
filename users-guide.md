# macro() User's Guide

## General

### How Text is Processed

Class `macro()` generally processes content in an inside-to-outside,
left-to-right order. This has implications for certain types of
operations and may result in some surprises when your content is
complex. Here is a quick example of the text processing process:

    input: [p [i foo] [u bar]]
	step1: [p <i>foo</i> [u bar]]
	step2: [p <i>foo</i> <u>bar</u>]
	step3: <p><i>foo</i> <u>bar</u></p>

There are two exceptions to this rule. The first is any definition of a
`[style]`, and the second is `[repeat]`. In both cases, processing the
content of these built-ins is deferred. This allows their effects to
vary based on subsequent events in the processing stream, rather than
the conditions that obtain at the time of style definition, or in the
case of repeat, at the time of the first repeat.

If you want a style to process immediately for later use in that precise
form, then the best way to go about that is to use the style immediately,
and then store the result in a variable for later placement. This preserves
the style result. An example of such a style use is as follows:

    [style dollars $[b]$]
	[local forlater {dollars moneybags}]

The result, `$moneybags$`, is placed into the variable "forlater" and can be used
at any time after that by simply pulling the variable:

    [v forlater]

Instances in which this would be useful include those where you change the
style before the content would be used, or if the style uses other elements
which themselves change before the content is used.

## A \(very\) Brief Introduction to Styles and Built-Ins

Styles are the heart of what class `macro()` is about. The built-ins you'll
be reading about are the low-level bricks and mortar that get things done,
but styles are how you get things done cleanly and easily and sanely *using*
the built-ins.

### Built-ins

First, here's the built-in for italics. You specify a built-in using square
brackets. Here's how to do italics:

    [i my text]

What happens is that the built-in named "i" receives "my text" as *content.*
It then wraps HTML italics tags around that content, and returns it that
way: "`<i>my text</i>`"

The notation I use to show this in this document is:

    [i my text] = "<i>my text<\i>"

### Built-in Parameter Handling

Generally, the syntax is, the keyword for the built-in, followed
by a space, followed by the parameter\(s.\)

If, however, you invoke a built-in that expects parameters with a
trailing space and no parameter\(s\) after that, it will use the most
recently encountered parameter\(s.\) If you truly intend to pass no
content, then follow the built-in with a space. Here's an example using
the wordcount built-in:

    [local cont this is a test of the emergency broadcast system.]

	[wc [v cont]] = "9"
	[wc] = "9"
	[wc ] = "0"

The content there was evaulated *once*, that is, the \[v cont\]
statement that retrieved the variable `cont` did so when evaluated
during the first \[wc\] invocation, and that already-evaulated content
was provided to the second \[wc\] without re-evaulation.

Another example \(in HTML 3.2 mode\):

    [b style [color F84 me]] = "<b>style <font color="#FF8844">me<font></b>"
    [i] = "<i>style <font color="#FF8844">me<font></i>"
	[u] = "<u>style <font color="#FF8844">me<font></u>"

### Styles

Styles also have names and receive content, but the difference is that *you*
define the names and how the content is handled. You can use one style within
another, or you can use built-ins, or mix them up. Here's how you might
go about creating the exact same functionality as the \[i content\] built-in
just described above. The \[b\] built-in is replaced with the content that is
passed to the style when it is used:

    [style i <i>[b]</i>]

Using it:

    {i my text} = "<i>my text</i>"

Here's another simple example:

    [style hello Well, hello, [b], how are you?]
	{hello Ben} = "Well, hello, Ben, how are you?"

There will be times when you want to pass more than one bit of content
to a style, and that is also available as part of the class
functionality. You can learn about it below where \[split\] and \[parm\]
are described.

Within the built-in reference, below, there are multiple examples of
using styles. If you have questions or suggestions, please contact
me using the information at the top of the `aa_macro.py` file.

#### Style Rules

 * Don't define a style within another style definition
 * Don't define a style within a built-in
 * Recursive style use is okay, *but*, you have to provide a sane exit strategy
 * Style names may contain any character except a space (0x20) or a newline (0x0a)

## Built-In Reference

### Text Styling

**\[p content\]**  
The content is wrapped with HTML paragraph tags:

    [p my verbiage] = <p>my verbiage</p>

**\[bq content\]**  
The content is wrapped with HTML blockquote tags:

    [bq my verbiage] = <blockquote>my verbiage</blockquote>

**\[b content\]**  
The content is wrapped with HTML bold tags, or a span if in HTML 4.01s mode:

    [b my verbiage] = <b>my verbiage</b>
	[b my verbiage] = <span style="font-weight: bold;">my verbiage</span>

**\[i content\]**  
The content is wrapped with HTML italics tags, or a span if in HTML 4.01s mode:

    [i my verbiage] = <i>my verbiage</i>
	[i my verbiage] = <span style="font-style: italic;">my verbiage</span>

**\[u content\]**  
The content is wrapped with HTML underline tags, or a span if in HTML 4.01s mode:

    [u my content] = <u>my content</u>
	[u my content] = <span style="text-decoration: underline;">my content</span>

**\[color HEX3|HEX6 content\]**  
The content is wrapped with HTML font tags, or a span if in HTML 4.01s mode. If in HTML
4.01s mode, the background color is also assigned and used. You can set the background color
when instantiating the macro object as a passed parameter to the class, or you can use the
`[back]` built-in to set it from the body of the processed text. The default for the background
color is white \(FFFFFF\):

    [color f00 my content] = <font color="FF0000#">my content</font>
	[back ff8844]
	[color f00 my content] = <span style="background-color: #FF8844; color: #FF0000;">my content</span>

### Linking

**\[a \(tab,\)URL\(,linked content\)\]**  
If the keyword "tab" is present as shown, the link will request the browser open a new
tab or window. If not, the link will be a standard link. If the linked content is present,
then the link will wrap that content. If it is not present, the link will wrap its own
address:

    [a http://fyngyrz.com] = <a href="http://fyngyrz.com">http://fyngyrz.com</a>
    [a http://fyngyrz.com,home] = <a href="http://fyngyrz.com">home</a>
    [a tab,http://fyngyrz.com,home] = <a target="_blank_" href="http://fyngyrz.com">home</a>
    [a tab,http://fyngyrz.com] = <a target="_blank_" href="http://fyngyrz.com">http://fyngyrz.com</a>

### Images

**\[img \(imageTitle,\)imageURL\( linkURL\)\]**  
Creates an HTML image tag. If  imageTitle is present, it will be placed
into both the alt and title attributes of the image tag. If linkURL is
present, then the image tag will be wrapped with link tags to linkURL:

    [img pic.jpg] = <img src="pic.jpg">
	[img my shot,pic.jpg] = <img title="my shot" alt="my shot" src="pic.jpg">
	[img pic.jpg /foo.html] = <a href="/foo.html"><img src="pic.jpg"></a>
	[img foo,pic.jpg /foo.html] = <a href="/foo.html"><img title="foo" alt="foo" src="pic.jpg"></a>

**\[locimg \(imageTitle,\)imageURL\( linkURL\)\]**  
The \[locimg\] built-in works exactly like the \[img\] built-in, except
it is designed to be made aware of the image's location in the server's
file system using the related \[lipath\] tag. It uses this information
to look at the image and determine its dimensions, and then it inserts
those dimensions into the HTML img tag. The end result of this is that
browsers will have a much easier time rendering the page for the web
visitor, and will not undergo reformatting of the page as each image
loads, instead formatting it once and then inserting the images as
they are downloaded. The image types the \[locimg\] tag understands are
.png, .jpg, and .gif:

    \[lipath /usr/www/mysite.com/htdocs/pics/\]
	\[locimg pic.jpg\] = <img width=320 height=200 src="pic.jpg">

### HTML Lists

**\[ul \(wrap=style,\)\(sep=X,\)item\(Xitem\)\]**  
This produces an unordered list. If the wrap= parameter is
supplied, then each list element will be wrapped with the
specified style. List elements are separated by commas,
unless the sep= parameter is supplied, in which case
list elements are separated by that instead. The sep
parameter may be mulitiple characters.

    [ul joe,fred] = <ul><li>joe</li><li>fred</li></ul>
	[ul sep=|,joe|fred] = <ul><li>joe</li><li>fred</li></ul>

It may be convenient to define an arbitrary separator as shown here to
prevent parsing errors due to content that may contain any particular
character:

	[style s hYujIkIsP]
	[ul sep={s},joe{s}fred] = <ul><li>joe</li><li>fred</li></ul>

Style wrapping works like this:

    [style splats ![b]!]
    [ul wrap=splats,joe,fred] = <ul><li>!joe!</li><li>!fred!</li></ul>

**\[ol \(wrap=style,\)\(sep=X,\)item\(Xitem\)\]**  
This produces an ordered list. If the wrap= parameter is
supplied, then each list element will be wrapped with the
specified style. List elements are separated by commas,
unless the sep= parameter is supplied, in which case
list elements are separated by that instead. The sep
parameter may be mulitiple characters.

    [ol joe,fred] = <ol><li>joe</li><li>fred</li></ol>
	[ol sep=|,joe|fred] = <ol><li>joe</li><li>fred</li></ol>

It may be convenient to define an arbitrary separator as shown here to
prevent parsing errors due to content that may contain any particular
character:

	[style s hYujIkIsP]
	[ol sep={s},joe{s}fred] = <ol><li>joe</li><li>fred</li></ol>

Style wrapping works like this:

    [style splats ![b]!]
    [ol wrap=splats,joe,fred] = <ol><li>!joe!</li><li>!fred!</li></ol>

**\[iful \(wrap=style,\)\(sep=X,\)item\(Xitem\)\]**  
The \[iful\] built-in works exactly like the \[ul\] built-in \(see above\)
except that if there is only one item supplied, it does not produce a list.

**\[ifol \(wrap=style,\)\(sep=X,\)item\(Xitem\)\]**  
The \[ifol\] built-in works exactly like the \[ol\] built-in \(see above\)
except that if there is only one item supplied, it does not produce a list.

**\[t \(wrap=style,\)\(sep=X,\)item\(Xitem\)\]**  
The \[t\] built-in is used to wrap one or more items in a style. If
no style is provided, the items are produced without the separators:

    [style at @[b]@]
	[t wrap=at,joe,fred] = @joe@@fred@
	[t joe,fred] = joefred
	[style s hYujIkIsP]
	[t sep={s},wrap=at,joe{s}fred] = @joe@@fred@

### HTML Tables

As with HTML itself, tables are managed with table, row, header cell and
table cell concepts. Attributes for these may be supplied if desired.
While the syntax may seem obvious and perhaps even trite at first, the
examples below will demonstrate the considerable power of this
methodology. First, the built-ins themselves:

**\[table \(options,\)content\]**  
The table built-in is to be wrapped around row content:

    [table content] = <table>content</table>
	[table border=1,content] = <table border=1>content</table>

**\[row \(options,\)content\]**  
The row built-in is tobe wrapped around header or cell content:

    [row content] = <tr>content</tr>
	[row bgcolor="#ffdddd",content] = <tr bgcolor="#FFDDDD">content</tr>


**\[header \(options,\)content\]**  
The header built-in is to be wrapped around header cell content:

    [header content] = <th>content</th>
	[header align="right",content] = <th align="right">content</th>


**\[cell \(options,\)content\]**  
The cell built-in should be wrapped around normal table cell content:

    [cell content] = <td>content</td>
	[cell align="right",content] = <td align="right">content</td>

Taken together, an entire table \(one row, one cell\) is built this way...

    [table [row [cell content]]]

...which results in:

    <table><tr><td>content</td></tr></table>

Using style, split and parm you can conveniently pre-define part or all
of a table format. For instance, if you are using a two-cell per row
table, you could do this...

    [style myrow [split [b]][row [cell [parm 1]][cell [parm 2]]]]

...and then your table can be done this way, allowing use of multiple rows...

    [table {myrow joe,larry}
	{myrow freida,sheila}
	]

...which will result in:

    <table><tr><td>joe</td><td>larry</td></tr>
	<tr><td>frieda</td><td>sheila</td></tr>
	</table>

Or you can predefine the entire thing...

    [style mytab [table [split [b]][row [cell [parm 1]][cell [parm 2]]]]]

...which you'd use this way...

	{mytab joe,larry}

...returning this result:

    <table><tr><td>joe</td><td>larry</td></tr></table>

Also using styles, you can adjust the wordiness of the syntax to any
degree you choose. For instance, here's a minimalist version:

    [style t [table [b]]]
	[style r [row [b]]]
	[style h [header [b]]]
	[style c [cell [b]]]

With those in place, the example table can now be written as:

	{t {r {c joe}{c larry}}}

### Variables

**\[local varName varContent\]**  or **\[vs varName varContent\]**  \(synonomous\)
Places varContent into a local variable with the identifier varName.

    [local myvar Ben]

**\[global varName varContent\]**  
Places varContent into a global variable with the identifier varName.

   [global myvar Asia]
   [global myvar2 Leo]

**\[v varName\]**  
Produces the content stored in varName. If a local variable identified as
varName, that is produced. If not, then if there is a global variable
identifed as varName, that is produced instead. If neither class of
variable has been set, then there is no result.

**\[gv varName\]**  
Produces the content stored in a global variable identified as varName.
If no global variable has been set, then there is no result.

**\[lv varName\]**  
Produces the content stored in a local variable identified as varName.
If no local variable has been set, then there is no result.

**\[page\]**  
Unsets all local variables. Global variables are not affected.

### Data Lists

**\[list \(sep=X,\)listName,item\(Xitem\)\]**  
This built-in creates a list in one operation. Here
are some list creation examples:

    [list myList,joe,mary,fred,luna]
	[list sep=|,myList,Michelle|Stella|Terrie]

**\[ltol listName,content\]**
This splits lines \(text separated by newline characters\) into
a list:

    [ltol mylist,line 1
	line 2
	line 3]
	[style lwrap ([b]) ]
	[dlist style=lwrap,mylist] = "(line 1) (line 2) (line 3) "

**\[append listName,item\]**  
This built-in adds an element to the end of a list:

    [list myList,joe,mary,fred,luna]
	[append myList betty]

**\[lset listName,indexN,item\]**  
This changes the value of an existing list item, where the first item is numbered
zero, and the last item index is the length of the list minus one:

    [lset myList,2,leroy]
  
**\[dlist \(wrap=styleName,\)listName\]**  
Dumps/displays a list, optionally wrapped in a style:

    [dlist myList] = joemaryleroylunabetty
	[style lwrap ([b]) ]
	[dlist wrap=lwrap,myList] = "(joe) (mary) (leroy) (luna) (betty) "

**\[e listName,indexN\]**  
This outputs one list item selected by indexN:

    [e myList 2] = "leroy"

**\[asort listName\]**  
Sorts listName alphabetically, case-sensitive (capital letters come first.)

	[asort myList]

**\[aisort\]**  
Sorts listName alphabetically, case-INsensitive \(capital letters same as lower case.\)

**\[isort \(sep=X,)listName\]**  
Sort listName by a leading integer, separated from the rest of the list items
by a comma or the optional separator. So the list would be in this kind of
format:

    [list sep=|,myList 1,joe|3,barry|2,matilda]
	[isort myList]
	[dlist wrap=lwrap,myList] = "(1,joe) (2,matilda) (3,barry) "

**\[cmap listName\]**
This built-in creates a 256-entry list of all the possible 8-bit characters
mapped directly to the list index. For instance, the ASCII character A is
coded with a decimal 65; so if you do this...

    [cmap myList]

...then you can do this:

    [e myList 65] = "A"

So far, sort of boring. But. You can now do this:

    [lset myList,65,!]
	[translate Area fifty one] = "!rea fifty one"

The idea is that you can cause the output of arbitrary characters using
any character coding you like. Simple transposition ciphers, easily
generated sequences of format characters, all are easily built using
this capability.

**\[translate listName,content\]**  
See \[cmap\], just above

### Data Dictionaries

**\[dict (sep=X,)(keysep=Y)dictName,keyYvalue(XkeyYvalue)\]**  
This allows you to create a multi-entry dictionary. sep defaults
to a comma, and keysep defaults to a colon.

    [dict mystuff,foo:bar,this:that,she:he,widget:wodget]

**\[dset (keysep=Y)dictName,keyYvalue\]**  
This allows you to update or create one item in an existing dictionary,
or create a dictionary with one item. The keysep defaults to a colon:

    [dset mystuff,widget:thing-a-ma-bob]
    [dset mystuff,plink:plank, plunk]

**\[d dictName,key\]**
This allows you to retrive one entry from a dictionary:

    [d mystuff,this] = "that"
	[d mystuff,widget] = "thing-a-ma-bob"
	[d mystuff,plink] = "plank, plunk"

### Stack Operations

**\[push content\]**  
Push an element on to the top of the stack:

    [push foo]

**\[pop\]**  

Pop an element off of the stack:

	[push foo]
    [pop] = "foo"

**\[fetch\]**  
Assuming there is data on the stack, this allows you to get at it
without popping the stack:

    [push foo]
	[push bar]
	[push argle-bargle]
	[push constitution]
	[fetch 1] = "argle-bargle"

**\[flush\]**  
This emtpies the stack; all content is discarded.

### Math

The math capabilities are underwhelming used by themselves, but in combination
with styles and variables, they come into their own. First, the operations:

**\[add value addend\]**  

    [add 5 4] = "9"

**\[sub value subtrahend\]**  

    [sub 5 4] = "1"

**\[mul value multiplier\]**  

    [mul 5 4] = "20"

**\[div value divisor\]**  

    [div 20 4] = "5"

**\[max v1 v2\]**

    [max 10 5] = "10"

**\[min v1 v2\]**

    [min 10 5] = "5"

**\[inc value\]**  

    [inc 5] = "6"

**\[dec value\]**  

    [dec 5] = "4"

So with these, you can directly do things with variables such as this:

    [local x 5]
	[local y 4]
	[add [v x] [v y]] = "9"

Using styles, you can create something more friendly that uses
vaariables. The following example splits the content passed to the style
into two parameters based upon a single space. The parameters are then
provided as the two terms for the add:

    [style addvars [split  ,[b]][add [v [parm 0]] [v [parm 1]]]]

...then it's just:

    {addvars x y} = "9"

You probably want the freedom to mix variables and scalars; that's not
difficult to arrange either. The following style does the job based upon
the presence of a leading "$" or lack thereof:

    [style v [if [slice :1,[b]] $ [v [slice 1:,[b]]]][else [slice :1,[b]] $ [b]]]

With that style available, you can now create this:

    [style addvars [split  ,[b]][add {v [parm 0]} {v [parm 1]}]]

Which you would use as follows:

	{addvars $x 3} = "8"
	{addvars $x $y} = "9"
	{addvars 2 $y} = "6"

### Conditionals

**\[even value conditionalContent\]**  
"value" is numeric. If it is even, conditionalContent is the result. If the
value is odd, then there is no result.

	[if 1,testing] = ""
    [if 2,testing] = "testing"

**\[odd value conditionalContent\]**  
"value" is numeric. If it is odd, conditionalContent is the result. If the
value is even, then there is no result.

	[if 1,testing] = "testing"
    [if 2,testing] = ""

**\[if value match conditionalContent\]**  
When value and match are identical, conditionalContent is the result.
Otherwise, there is no result.

    [if foo,bar,testing] = ""
	[if foo,foo,testing] = "testing"

**\[else value notMatch conditionalContent\]**  
When value and match are not identical, conditionalContent is the result.
Otherwise, there is no result.

    [else foo,bar,testing] = "testing"
	[else foo,foo,testing] = ""

**\[ne value,conditionalContent\]**  
When value has no content, conditionalContent is the result.
Otherwise, there is no result.

    [ne ,testing] = "testing"
	[ne foo,testing] = ""

**\[eq value,conditionalContent\]**  
When value has content, conditionalContent is the result.
Otherwise, there is no result.

    [eq ,testing] = ""
	[eq foo,testing] = "testing"

### Parsing and Text Processing

**\[slice sliceSpec,content\]**  
This built-in returns a portion of the content. It works just like
Python's slicing:

    [slice 3:6,foobarbip] = "bar"
	[slice :3,foobarbip] = "foo"
	[slice :-1,foobarbip = "foobarbi"
	[slice ::-1,foobarbip] = "pibraboof"

Inasmuch as that last one reverses the string, the following style
seems almost too obvious:

    [style reverse [slice ::-1,[b]]]
	{reverse xyzzy} = "yzzyx"

**\[splitcount n\]**  
Allows you to limit the number of splits that \[split\] will
perform. See \[split\], below.

**\[\split X,item\(Xitem\)]**  
The split built-in takes content and splits it for use by the \[parm\] built-in.
The idea is that for some styles, you will want to pass more than one parameter,
as shown in the math examples above. It takes a separator parameter, and then
the content to be split. You can specify anything you like as the separator,
although to use a comma, you must use the comma escape, "\[co\]"

    [split |,ben|larry|joe]
	[parm 2] = "joe"
	[parm 1] = "larry"
	[parm 0] = "ben"

    [split [co],Sheila,Michelle,Shevaughn]
	[parm 2] = "Shevaughn"
	[parm 1] = "Michelle"
	[parm 0] = "Sheila"

	[splitcount 2]
    [split [co],Jim,Becky Thatcher,Tom Sawyer, and Huckleberry Finn]
	[parm 0] = "Jim"
	[parm 1] = "Becky Thatcher"
	[parm 2] = "Tom Sawyer, and Huckleberry Finn"

**\[parm n\]**  
See \[split\], above.

**\[upper content\]**  
Convert content to upper case:

    [upper thIs Is a test] = "THIS IS A TEST"

**\[lower content\]**  
Convert content to upper case:

    [lower thIs Is a test] = "this is a test"

**\[soundex (len=n,)content\]**
Returns the Soundex code for the content, Defaults
to len of 4:

    [soundex Knuth] = "K530"

**\[roman decNumber\]**  
Convert a decimal number to a roman numeral:

    [roman 9] = 'ix'
	[upper [roman 14]] = "XIV"

**\[dtohex decNumber\]**
Convert a decimal number to a hexadecimal number:

	[dtohex 17] = "11"

**\[dtooct decNumber\]**
Convert a decimal number to an octal number:

	[dtooct 9] = "11"

**\[dtobin decNumber\]**
Convert a decimal number to a binary number:

	[dtobin 3] = "11"

**\[htodec hexadecimalNumber\]**
Convert an hexadecimal number to a decimal number:

	[htodec 11] = "17"

**\[otodec octalNumber\]**
Convert an octal number to a decimal number:

	[otodec 11] = "9"

**\[htodec binaryNumber\]**
Convert a binary number to a decimal number:

	[btodec 11] = "3"

**\[len content\]**
Return the length of content in characters.

    [len foo] = "3"

**\[lc content\]**
Return the length of content in lines.

    [lc this is a test
	of the emergency broadcast system] = "2"

**\[wc content\]**
Return the length of content in words.

    [lc this is a test
	of the emergency broadcast system] = "9"

**\[chr n\]**  
Convert a number from 0-255 to the associated ASCII character:

    [chr 65] = "A"
	[chr 48] = "0"

**\[ord character\]**  
Convert an ASCII character to it's associated ASCII ordinal:

    [ord A] = "65"
	[ord 0] = "48"

**\[csep intNumber\]**  
Comma-separate an integer:

    [csep 1999333] = "1,999,333"

**\[fcsep floatNumber\]**  
Comma-separate a floating point number:

    [fcsep 1999333.01] = "1,999,333.01"

**\[dup n,content\]**  
Duplicate the content.

    [dup 5 foo] = "foofoofoofoofoo"

Note that this is *not* the same as \[repeat\].
\[dup\] evaluates the content and *then* duplicates it;
\[repeat\] \(re-\)evaluates the content on each repeat. They can
produce significantly different results when the content alters variables
or lists. Here's an example of such a difference:

    [local counter 1]
	[style numberit [v counter]: [b][local counter [inc [v counter]]]]
	[dup 3,{numberit}]    = "1: 1: 1: "
	[repeat 3,{numberit}] = "1: 2: 3: "

**\[find (sep=X,)thisStringXcontent\]**  
This returns the index of where \(if\) thisString was
\(not\) found in the content. If not found, the value
returned is -1.

    [find gik,foobarbip] = "-1"
    [find foo,foobarbip] = "0"
    [find bar,foobarbip] = "3"

**\[replace (sep=X,)repStringXwithStringXcontent\]**  
This allows you to replace one \(sub\)string in the content
with another string:

    [replace foo,bar,I went to the foo today] = "I went to the bar today"

**\[count \(sep=X,\)\(overlaps=yes,\)\(casesens=yes,patternXcontent\)\]**
Returns the number of occuraces of pattern in content. overlaps=yes
will return 2 for aa in aaa; otherwise aa in aaa returns 1. casesens=yes
returns 1 for AA in AAa; otherwise returns 2 for AA in AAa. The two
options may be combined. sep defaults to a comma.

	[count Aa,AaAaaa] = 3
	[count overlaps=yes,Aa,AaAaaa] = 5
	[count casesens=yes,Aa,AaAaaa] = 2
	[count casesens=yes,overlaps=yes,Aa,AaAaaa] = 2

**\[caps content\]**  
Convert content to sentence case:

    [caps thIs Is a test] = "This is a test"

**\[capw content\]**  
Convert content to Word case:

    [capw thIs Is a test] = "This Is A Test"

**\[capt content\]**  
Convert content to title case:

    [capt thIs Is a test] = "This is a Test"

This built-in uses a list of the USG standard lower-cased words
to create sentence-cased output. You can alter the lower cased word
list by changing the class variable `.notcase` similar to this:

    mod = macro()
	mod.notcase = ['an','a','the','test']

After doing that, \[capt\] will only lower case those four words, while
every other word will be capitalized:

    [capt thIs Is a test] = "This Is a Test"

**\[scase content\]**  
Convert space-separated words, minding embedded and attached special
characters, in content to specially cased words in a list. First you set
up a list containing words exactly as you want them converted. The you
use \[specialcase\] on the content. Words that match the list's words
will be converted to the case of the word as it exists in the list.

    [list cvt HTML,PHP,Internet]
	[scase cvt,The internet uses Html, and php.] = "The Internet uses HTML, and PHP."

If a word is hypenated or otherwise has a non-alpha, non-numeric character embedded
in it, that word goes in the list *without* the special character:

    [list cvt,PooBah,L00kyLoo]
	[scase cvt,He's the grand poo-bah: Really!] = "He's the grand Poo-Bah: Really!"
	[scase cvt,She's just a l00ky-loo.] = "She's just a Looky-Loo."]

**\[ssort content\]**  
This sorts lines of content in a case-sensitive manner.

**\[sisort content\]**  
This sorts lines of content in a case-insensitive manner.

**\[issort content\]**  
This sorts lines of content by an integer followed by a comma
at the beginning of each line, like this:

content:

	5,line 2
    3,line 1
	27,line 3
	1,foo

Output of [issort content]:

	1,foo
    3,line 1
	5,line 2
	27,line 3

**\[inter iStr,L|R,everyN,content\]**  
This intersperses iStr within content starting either from the
left or the right:

    [inter -,L,4,123456789] = "1234-5678-9"
    [inter -,R,4,123456789] = "1-2345-6789"

**\[rjust width,padChar,content\]**  
This justifies a string to the right inside a known field-width.

    [rjust 6,#,foo] = "###foo"

**\[ljust width,padChar,content\]**  
This justifies a string to the left inside a known field-width.

    [ljust 6,#,foo] = "foo###"

**\[center width,padChar,content\]**  
This justifies a string to the center inside a known field-width.

    [center 9,#,foo] = "###foo"

If you pass width as a negative number, \[center\] will pad both
sides:

    [center -9,#,foo] = "###foo###"

This is kind of fun; building a variable-width
comment block in the style of coders everywhere:

    [style sline [center -[v csize],#, [b] ][nl]]
	[style cline # [ljust [sub [v csize] 4], ,[b]] #[nl]]
	[style eline [dup [v csize],#][nl]]

	[local csize 31]
    {sline Comment Block}
	{cline}
	{cline This is a comment block.}
	{cline and this is more of it.}
	{cline ditto.}
	{cline}
	{eline}

The result is:

	######## Comment Block ########
	#                             #
	# This is a comment block.    #
	# and this is more of it.     #
	# ditto.                      #
	#                             #
	###############################

So let's make that even easier to use:

	[style sline [center -[v csize],#, [b] ][nl]]
	[style cline # [ljust [sub [v csize] 4], ,[b]] #[nl]]
	[style eline [dup [v csize],#][nl]]
	[style cctr [ltol blkl,[b]][dlist style=cline,blkl]]
	[style cblock [splitcount 2][split [co],[b]][local csize [parm 0]]{sline [parm 1]}{cline}{cctr [parm 2]}{cline}{eline}]

Now we can create a comment block in one shot:

	{cblock 24,The Title,The Body
	more body
	still more body}

Output:

	###### The Title #######
	#                      #
	# The body             #
	# more body            #
	# still more body      #
	#                      #
	########################

> Note that there is a more sophisticated version of comment-block
generation in the examples within `aa_macro.py`

### Miscellanea

**\[repeat n,content\]**  
Repeat the content.

    [repeat 5 foo] = "foofoofoofoofoo"

Note that this is *not* the same as \[dup\]. \[repeat\] \(re-\)evaluates
the content on each repeat; \[dup\] evaluates the content and *then*
duplicates it. They can produce significantly different results when the
content alters variables or lists. Here's an example of such a
difference:

    [local counter 1]
	[style numberit [v counter]: [b][local counter [inc [v counter]]]]
	[dup 3,{numberit}] = "1: 1: 1: "
	[repeat 3,{numberit}] = "1: 2: 3:"

You cannot put \[repeat\] inside a style or define a style within
\[repeat\].

However, you can *use* styles inside \[repeat\] as shown above.

**\[comment remarks\]**  
Anything inside the comment built-in is thrown away during evaluation.

	[comment this is a test] = ""

Multiline comments may be written by placing a trailing space after the *comment*
keyword...

	[comment 
	This is a test,
	and so is this
	] = ""

...or by beginning the comment on the same line:

	[comment This is a test,
	This is a test also,
	and so is this
	] = ""

**\[back HEX3|HEX6\]**  
This sets the background color used by the \[color\] built-in,
but is only effective in HTML 4.01s mode because it can only
be set via a span.

**\[mode 3.2|4.01s\]**  
This controls how some text formatting is specified, basically it
switches between older style HTML tags and the CSS styles that
were intended to supercede the older style tags.

### Escapes

**\[co\]**  
The comma character.

**\[sp\]**  
The space.

**\[lb\]**  
The left square bracket character.

**\[rb\]**  
The right square bracket character.

**\[ls\]**  
The left squiggly brace character.

**\[rs\]**  
The right squiggly brace character.

**\[lf\]**  
The line feed charaacter.

## Styles

**\[style styleName styleContent\]**  
This defines a local style of styleName.

**\[gstyle styleName styleContent\]**  
This defines a global style of styleName.

**\[s styleName\( content\)\]**  
This invokes a style of styleName with the content, if any. A local
style is used if it exists, otherwise a global style is used.

This is *not* the preferred method, however; please use the \{\} method,
described next. With that in mind, this capability will not go away, as
it is my policy not to remove features or make them incompatible with
prior usage patterns.

**\{styleName\( content\)\}**  
This invokes a style of styleName with the content, if any. It is the
preferred shorthand for \[s styleName\]

**\[glos styleName\( content\)\]**  
This invokes a local style of styleName with the content, if any. Local
styles are not used.

**\[locs styleName\( content\)\]**  
This invokes a global style of styleName with the content, if any. Global
styles are not used.

**\[spage\]**  
Unsets all local styles. Global styles are not affected.

**\[ghost \(source=global|local\)\]**
This outputs a style verbatim, without processing it. Invoked without
the source option, it works like \[s styleName\] and \{styleName\}, which
is to say it will output a local style if one exists, otherwise it will
output a global style if it exists. If neither style type exists, then
it will output nothing.

With source=global, it will output the global style, ignoring any local version.
If the global style does not exist, there will be no output.

With source=local, it will output the local style, or if the local style
does not exist, there will be no output.
