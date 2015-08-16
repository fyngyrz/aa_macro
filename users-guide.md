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
content of these built-ins is deferred until they are encountered
left-to-right. This allows their effects to vary based on subsequent
events in the processing stream.

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
way: "<i>my text</i>"

The notation I use to show this in this document is:

    [i my text] = "<i>my text<\i>"

### Styles

Styles also have names and recieve content, but the difference is that *you*
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

## Built-In Reference

### Text Styling

**\[p content\]**  
The content is wrapped with HTML paragraph tags:

    [p my verbiage] = <p>my verbiage</p>

**\[bq content\]**  
The content is wrapped with HTML blockquote tags:

    [bq my verbiage] = <blockquote>my verbiage</blockquote.

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

	[style sepper hYujIkIsP]
	[ul sep={sepper},joe{sepper}fred] = <ul><li>joe</li><li>fred</li></ul>

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

	[style sepper hYujIkIsP]
	[ol sep={sepper},joe{sepper}fred] = <ol><li>joe</li><li>fred</li></ol>

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

**\[append listName,item\]**  
This built-in adds an element to the end of a list:

    [list myList,joe,mary,fred,luna]
	[append myList betty]

**\[lset listName,indexN,item\]**  
This changes the value of an existing list item, where the first item is numbered
zero, and the last item index is the length of the list minus one:

    [lset myList,2,leroy]
  
**\[dlist\]**  
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

### Stack Operations

**\[push\]**  
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
with variables, they come into their own. First, the operations:

**\[add value addend\]**  

    [add 5 4] = "9"

**\[sub value subtrahend\]**  

    [sub 5 4] = "1"

**\[mul value multiplier\]**  

    [mul 5 4] = "20"

**\[div value divisor\]**  

    [div 20 4] = "5"

**\[inc value\]**  

    [inc 5] = "6"

**\[dec value\]**  

    [dec 5] = "4"

So with these, you can do things like this:

    [local x 5]
	[local y 4]
	[add [v x] [v y]] = "9"

Using styles, you can create something quite friendly...

    [style addvars [split sep= ,[b]][add [v [parm 1]] [v [parm 2]]]]

...then it's just:

    {addvars x y} = "9"

### Conditionals

**\[even value conditionalContent\]**  
"value" is numeric. If it is even, conditionalContent is the result. If the
value is odd, then there is no result.

**\[odd value conditionalContent\]**  
"value" is numeric. If it is odd, conditionalContent is the result. If the
value is even, then there is no result.

**\[if value match conditionalContent\]**  
When value and match are identical, conditionalContent is the result.
Otherwise, there is no result.

**\[else value notMatch conditionalContent\]**  
When value and match are not identical, conditionalContent is the result.
Otherwise, there is no result.

**\[ne value,conditionalContent\]**  
When value has no content, conditionalContent is the result.
Otherwise, there is no result.

**\[eq value,conditionalContent\]**  
When value has content, conditionalContent is the result.
Otherwise, there is no result.

### Parsing and Text Processing

**\[slice\]**  

**\[splitcount\]**  

**\[\split]**  

**\[parm\]**  

**\[upper\]**  

**\[lower\]**  

**\[roman\]**  

**\[chr\]**  

**\[ord\]**  

**\[csep\]**  

**\[fcsep\]**  

**\[dup\]**  

**\[find\]**  

**\[replace\]**  

**\[caps\]**  

**\[capw\]**  

**\[capt\]**  

**\[ssort\]**  

**\[sisort\]**  

**\[issort\]**  

**\[inter\]**  

**\[rjust\]**  

**\[ljust\]**  

**\[center\]**  

### Miscellanea

**\[repeat\]**  

**\[comment\]**  

**\[back\]**  

**\[mode\]**  

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
This defines a style of styleName. See "Using Styles, below".

**\[s styleName\( content\)\]**  
This invokes a style of styleName with the content, if any. This
is *not* the preferred method, however; please use the next method:

**\{styleName\( content\)\}**  
This invokes a style of styleName with the content if any.
 See "Using Styles, below"

