
 









# Macro() BETA Quick Reference
## Functional Groupings


_key:_ built-in \(options\) **required** content



HTML Text Styling | &nbsp;
----------------- | ----
 <tt>&#91;p content&#93;</tt> |  HTML paragraph
 <tt>&#91;bq content&#93;</tt> |  HTML blockquote
 <tt>&#91;b content&#93;</tt> |  HTML bold
 <tt>&#91;i content&#93;</tt> |  HTML italics
 <tt>&#91;u content&#93;</tt> |  HTML underline
 <tt>&#91;color **HEX3&#124;HEX6** content&#93;</tt> |  HTML text color

HTML Linking | &nbsp;
------------ | ----
 <tt>&#91;a \(tab&#44;\)**URL**\(&#44;linkedContent\)&#93;</tt> |  HTML link
 <tt>&#91;urlencode **content**&#93;</tt> |  URL encoding
 <tt>&#91;url \(sep=&#124;&#44;\)\(css=CSS&#44;\)\(tgt=_target&#44;\)\(nam=Name&#44;\)\(URLsepLINKED_CONTENT\)&#93;</tt> | Create URL

HTML Images | &nbsp;
----------- | ----
 <tt>&#91;img \(imageTitle&#44;\)**imageURL** \(linkURL\)&#93;</tt> |  HTML image
 <tt>&#91;limg \(target=&#44;\)\(lpath=&#44;\)\(wpath=\)\(title=&#44;\)\(alt=&#44;\)**imageName**&#93;</tt> |  HTML image name, figures size (uses &#91;lipath&#93;,&#91;wepath&#93;)
 <tt>&#91;lipath **filePathToImages**&#93;</tt> |  path for &#91;locimg&#93;
 <tt>&#91;wepath **webPathToImages**&#93;</tt> |  path for &#91;locimg&#93;

HTML Lists | &nbsp;
---------- | ----
 <tt>&#91;ul \(istyle=hstyle&#44;\)\(lstyle=hstyle&#44;\)\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt> |  HTML unordered list
 <tt>&#91;ol \(type=X&#44;\)\(start=N&#44;\)\(istyle=hstyle&#44;\)\(lstyle=hstyle&#44;\)\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt> |  HTML ordered list
 <tt>&#91;iful \(istyle=hstyle&#44;\)\(lstyle=hstyle&#44;\)\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt> |  HTML unordered list IF &gt; one item
 <tt>&#91;ifol \(istyle=hstyle&#44;\)\(lstyle=hstyle&#44;\)\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt> |  HTML ordered list IF &gt; one item
 <tt>&#91;t \(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt> |  style wrap around item(s)

HTML Tables | &nbsp;
----------- | ----
 <tt>&#91;table \(options\)&#44;content&#93;</tt> |  HTML table \(comma is *not* optional\)
 <tt>&#91;row \(options\)&#44;content&#93;</tt> |  HTML table row \(comma is *not* optional\)
 <tt>&#91;header \(options\)&#44;content&#93;</tt> |  HTML table header cell \(comma is *not* optional\)
 <tt>&#91;cell \(options\)&#44;content&#93;</tt> |  HTML table data cell \(comma is *not* optional\)

Variables | &nbsp;
--------- | ----
 <tt>&#91;local **varname** varContent&#93;</tt> |  local variable definition

Variables | &nbsp;
--------- | ----
 <tt>&#91;raw **varname** varContent&#93;</tt> |  local variable definition
 <tt>&#91;global **varName** varContent&#93;</tt> |  global variable definition
 <tt>&#91;graw **varName** varContent&#93;</tt> |  global variable definition
 <tt>&#91;v **varName**&#93;</tt> |  local/global variable
 <tt>&#91;vs **varName** varContent&#93;</tt> |  local variable definition
 <tt>&#91;gv **varName**&#93;</tt> |  global variable
 <tt>&#91;lv **varName**&#93;</tt> |  local variable
 <tt>&#91;vinc \(pre=1&#44;\)\(quiet=1&#44;\)**varName**&#93;</tt> |  increment local(global) variable
 <tt>&#91;vdec \(pre=1&#44;\)\(quiet=1&#44;\)**varName**&#93;</tt> |  decrement local(global) variable
 <tt>&#91;load **varName** **fileName**&#93;</tt> |  load file into local variable
 <tt>&#91;gload **varName** **fileName**&#93;</tt> |  load file into global variable
 <tt>&#91;save **varName** **fileName**&#93;</tt> |  save file from local variable
 <tt>&#91;gsave **varName** **fileName**&#93;</tt> |  save file from global variable

Data Lists | &nbsp;
---------- | ----
 <tt>&#91;list \(sep=X&#44;\)**listname**&#44;itemContent\(XitemContent\)&#93;</tt> |  create or overwrite a list
 <tt>&#91;clearl **listName**&#93;</tt> |  Discards list content
 <tt>&#91;lcopy **sourceList** **destinationList**&#93;</tt> |  copy list to new or existing list
 <tt>&#91;ltol **listName** content&#93;</tt> |  convert lines of content to list
 <tt>&#91;append **listName**&#44;itemContent&#93;</tt> |  append an item to a list (can create new list)
 <tt>&#91;lpush **listName**&#44;itemContent&#93;</tt> |  append an item to a list (can create new list)
 <tt>&#91;lpop **listName&#44;**\(listIndex\)&#93;</tt> |  pop an item out of a list at top, or at listIndex
 <tt>&#91;lset **listName&#44;****listIndex&#44;**itemContent&#93;</tt> |  Set a list item
 <tt>&#91;llen **listName**&#93;</tt> |  returns length of list
 <tt>&#91;lslice **sliceSpec&#44;****listName&#44;****targetList**&#93;</tt> |  slice listName to targetList
 <tt>&#91;lsplit \(sep=^&#44;\)\(num=N&#44;\)**listName**&#44;content&#93;</tt> |  split content into list
 <tt>&#91;ljoin **listName**&#44;\(joinTerm\)&#93;</tt> |  Join a list with joinTerm(s) between elements
 <tt>&#91;dlist \(fs=styleName&#44;\)\(ls=styleName&#44;\)\(wrap=styleName&#44;\)\(parms=PRE&#44;\)\(inter=INT&#44;\)\(ntl=NTL&#44;\)\(posts=PST&#44;\)listName&#93;</tt> |  dump a list
 <tt>&#91;e **listName&#44;****listIndex**&#93;</tt> |  output item from list of length n (listIndex = 0 to n-1)
 <tt>&#91;lcc **listOne&#44;****listTwo&#44;****listResult**&#93;</tt> |  list concatenate
 <tt>&#91;lsub \(ci=1&#44;\)\(sep=X&#44;\)**listName&#44;**content&#93;</tt> |  list of form AsepB, A=B in content
 <tt>&#91;asort \(rev=1&#44;\)**listName**&#93;</tt> |  ASCII alphabetic sort of list&#44; in place
 <tt>&#91;aisort \(rev=1&#44;\)**listName**&#93;</tt> |  ASCII case-insensitive sofr of list&#44; in place
 <tt>&#91;isort \(rev=1&#44;\)\(sep=X&#44;\)**listName**&#93;</tt> |  sort by leading integer&#44; sep defaults to &quot;&#44;&quot;
 <tt>&#91;lhsort \(rev=1&#44;\)**listName**&#93;</tt> |  sort list by leading amateur radio callsign&#44;, any non-alphanumeric sep
 <tt>&#91;cmap **listName**&#93;</tt> |  create 1:1 character map
 <tt>&#91;hmap **listName**&#93;</tt> |  create 1:1 character map to hex values
 <tt>&#91;translate \(pre=PRE&#44;\)\(post=POST&#44;\)\(inter=INTER&#44;\)**listName&#44;**content&#93;</tt> |  translate content using character map formatted list
 <tt>&#91;postparse content&#93;</tt> |  pretty-print Python 2.7 code (use black background)
 <tt>&#91;pythparse content&#93;</tt> |  pretty-print Python 2.7 code (use black background)
 <tt>&#91;getc \(var=varName&#44;\)\(high=lang&#44;\)\(tabsiz=n&#44;\)\(tabchar=X&#44;\)filename&#93;</tt> |  import c or oc source file as aa_macro

Data Dictionaries | &nbsp;
----------------- | ----
 <tt>&#91;dict \(sep=X&#44;\)\(keysep=Y&#44;\)**dictName&#44;****keyYvalue\(XkeyYvalue\)**&#93;</tt> |  create/replace dictionary
 <tt>&#91;dcopy **sourceDictionary&#44;****destinationDictionary**&#93;</tt> |  copy/replace destination with source
 <tt>&#91;dkeys **sourceDictionary&#44;****destinationList**&#93;</tt> |  create a <b>list</b> of keys from source
 <tt>&#91;dset \(keysep=Y&#44;\)**dictName&#44;****keyYvalue**&#93;</tt> |  create/replace dictionary item
 <tt>&#91;d \(sep=X&#44;\)**dictName****Xkey**\(XnotFound\)&#93;</tt> |  retrieve a dictionary value using key

General Stack | &nbsp;
------------- | ----
 <tt>&#91;push content&#93;</tt> |  Push an item on to the general stack
 <tt>&#91;pop&#93;</tt> |  Pop an item off the top of the general stack
 <tt>&#91;fetch **itemIndex**&#93;</tt> |  fetch any item from stack - 0 is top of stack
 <tt>&#91;flush&#93;</tt> |  delete stack contents

Math | &nbsp;
---- | ----
 <tt>&#91;int **value**&#93;</tt> |  integer of number

Math | &nbsp;
---- | ----
 <tt>&#91;abs **value**&#93;</tt> |  absolute value of number

Math | &nbsp;
---- | ----
 <tt>&#91;add \(mode=float&#44;\)**value** **addend**&#93;</tt> |  add two numbers
 <tt>&#91;sub \(mode=float&#44;\)**value** **subtrahend**&#93;</tt> |  subtract two numbers
 <tt>&#91;mul \(mode=float&#44;\)**value** **multiplier**&#93;</tt> |  multiply two numbers
 <tt>&#91;div \(mode=float&#44;\)**value** **divisor**&#93;</tt> |  divide two numbers
 <tt>&#91;max **value1** **value2**&#93;</tt> |  maximum of two numbers
 <tt>&#91;min **value1** **value2**&#93;</tt> |  minimum of two numbers
 <tt>&#91;inc **value**&#93;</tt> |  add one to value
 <tt>&#91;dec **value**&#93;</tt> |  subtract one from value
 <tt>&#91;random \(seed=none&#44;\(icount=N&#44;\)\)&#93;</tt> |  generate random from 0.0-1.0
 <tt>&#91;stage \(mode=float&#44;\)\(digits=N&#44;\)**start** **end** **steps** **step**&#93;</tt> |  subtract one from value

Conditional Content | &nbsp;
------------------- | ----
 <tt>&#91;even **value** content&#93;</tt> |  if value is even&#44; then content
 <tt>&#91;odd **value** content&#93;</tt> |  if value is odd&#44; then content
 <tt>&#91;if \(sep=X&#44;\)\(wrap&#124;style=styleName\)**value** **match** content&#93;</tt> |  if match&#44; then content
 <tt>&#91;else \(sep=X&#44;\)\(wrap&#124;style=styleName\)**value** **match** content&#93;</tt> |  if <b>not</b> match&#44; then content
 <tt>&#91;ne \(sep=X&#44;\)**value&#44;**content&#93;</tt> |  if value is empty&#44; then content
 <tt>&#91;eq \(sep=X&#44;\)**value&#44;**content&#93;</tt> |  if value is <b>not</b> empty&#44; then content
 <tt>&#91;ifle **value1&#44;****value2 &#44;**content&#93;</tt> |  if value1 &lt;= value2&#44; then content
 <tt>&#91;ifge **value1&#44;****value2 &#44;**content&#93;</tt> |  if value1 &gt;= value2&#44; then content

Text Processing | &nbsp;
--------------- | ----
 <tt>&#91;slice **sliceSpec&#44;content**&#93;</tt> |  slice content
 <tt>&#91;alphalead \(trail=1,\)content&#93;</tt> | Return leading alpha characters&#44; or trailing content
 <tt>&#91;alphanumlead \(trail=1,\)content&#93;</tt> | Return leading alphanumeric characters&#44; or trailing content
 <tt>&#91;splitcount **value**&#93;</tt> |  Maximum number of splits to perform in next &#91;split&#93;
 <tt>&#91;split **X&#44;**content\(Xcontent\)&#93;</tt> |  split for use with &#91;parm&#93;
 <tt>&#91;splash \(pre=&#44;\)\(post=&#44;\)\(inter=&#44;\)\(ntl=&#44;\)\(limit=N&#44;\)\(style=Style&#44;\)\(sep=&#44;&#44;\)content&#93;</tt> |  splits content, applies style
 <tt>&#91;parm **value**&#93;</tt> |  returns results of &#91;split&#93;
 <tt>&#91;upper content&#93;</tt> |  convert to uppercase
 <tt>&#91;lower content&#93;</tt> |  convert to lowercase
 <tt>&#91;soundex \(len=N&#44;\)content&#93;</tt> |  return soundex value of content
 <tt>&#91;stripe (charset=chars,)content&#93;</tt> |  strip chars from both ends of line (default = spaces)
 <tt>&#91;strip content&#93;</tt> |  strip HTML tags out
 <tt>&#91;roman **value**&#93;</tt> |  returns lower case roman numeral
 <tt>&#91;dtohex (digits=N&#44;)**value**&#93;</tt> |  decimal to hexadecimal conversion
 <tt>&#91;dtooct (digits=N&#44;)**value**&#93;</tt> |  decimal to octal conversion
 <tt>&#91;dtobin (digits=N&#44;)**value**&#93;</tt> |  decimal to binary conversion
 <tt>&#91;htodec (digits=N&#44;)**value**&#93;</tt> |  hexadecimal to decimal conversion
 <tt>&#91;otodec (digits=N&#44;)**value**&#93;</tt> |  octal to decimal conversion
 <tt>&#91;btodec (digits=N&#44;)**value**&#93;</tt> |  binary to decimal conversion
 <tt>&#91;crush &#44;&#93;</tt> |  return packed alphanumerics
 <tt>&#91;collapse content&#93;</tt> | 
 <tt>&#91;crop (words=no&#44;)(eol=&#44;)(neol=&#44;)(col=78&#44;)content&#93;</tt> | 
 <tt>&#91;wwrap \(eol=X&#44;\)\(wrap=style&#44;\)\(nohtml=1&#44;\)**value&#44;**content&#93;</tt> |  word wrap content at column value
 <tt>&#91;len content&#93;</tt> |  return length of content in characters
 <tt>&#91;wc content&#93;</tt> |  return length of content in words
 <tt>&#91;lc content&#93;</tt> |  return length of content in lines
 <tt>&#91;chr **value**&#93;</tt> |  return ASCII character of code=value
 <tt>&#91;ord **character**&#93;</tt> |  return ASCII code value in decimal
 <tt>&#91;csep **value**&#93;</tt> |  comma-separate an integer
 <tt>&#91;fcsep **value**&#93;</tt> |  comma-separate a floating point number
 <tt>&#91;dup **value&#44;content**&#93;</tt> |  duplicate content <i>after</i> evaluation (also see &#91;repeat&#93;)
 <tt>&#91;eval \(style=styleName&#44;\)**value&#44;content**&#93;</tt> |  duplicate content Nx&#44; eval style Nx if provided
 <tt>&#91;find \(sep=X&#44;\)**stringXcontent**&#93;</tt> |  find string in content&#44; sep default = &quot;&#44;&quot;
 <tt>&#91;replace \(sep=X&#44;\(lf=1&#44;\)\)**targetXreplacementXcontent**&#93;</tt> |  target replaced with replacement in content
 <tt>&#91;count \(sep=X&#44;\)\(overlaps=yes&#44;\)\(casesens=yes&#44;\)**patternXcontent**&#93;</tt> |  count incidences
 <tt>&#91;caps content&#93;</tt> |  sentence case
 <tt>&#91;capw content&#93;</tt> |  word case
 <tt>&#91;capt content&#93;</tt> |  title case
 <tt>&#91;expand **dictName&#44;**content&#93;</tt> |  dictionary based keyword expansion with leading cap forwarding
 <tt>&#91;ssort \(rev=1&#44;\)content&#93;</tt> |  case-sensitive sort of lines
 <tt>&#91;sisort \(rev=1&#44;\)content&#93;</tt> |  case-insensitive sort of lines
 <tt>&#91;issort \(rev=1&#44;\)content&#93;</tt> |  sort of lines by integer followed by a comma
 <tt>&#91;hsort \(rev=1&#44;\)content&#93;</tt> |  sort of lines by amatuer radio callsign followed by non-alphanumeric
 <tt>&#91;inter **iStr&#44;****L&#124;R&#44;****value&#44;**content&#93;</tt> |  intersperse iStr every value in content
 <tt>&#91;rjust **width&#44;****padChar&#44;**content&#93;</tt> |  right justify
 <tt>&#91;ljust **width&#44;****padChar&#44;**content&#93;</tt> |  left justify
 <tt>&#91;center **width&#44;****padChar&#44;**content&#93;</tt> |  center (neg width indicates pad both sides)
 <tt>&#91;th **integer**&#93;</tt> |  st, nd, rd, th...
 <tt>&#91;nd **integer**&#93;</tt> |  1st, 2nd, 3rd, 4th...
 <tt>&#91;encrypt \(mode=1&#44;\)\(again=1&#44;\)\(seed=N&#44;\)\(salt=String&#44;\)\(icount=N&#44;\)\(breakat=N&#44;\)content&#93;</tt> |  (re)Encrypt content
 <tt>&#91;decrypt \(mode=1&#44;\)\(seed=N&#44;\)\(salt=String&#44;\)\(icount=N&#44;\)content&#93;</tt> |  Decrypt content
 <tt>&#91;br \(parms&#44;\)\(content\)&#93;</tt> |  (content) HTML line break (with parms)

Miscellanea | &nbsp;
----------- | ----
 <tt>&#91;sys **shellCommand**&#93;</tt> |  invoke an operating system command. Output is captured
 <tt>&#91;date&#93;</tt> |  The date of macro() processing (use CGI for live date in HTML)
 <tt>&#91;time \(mode=12&#124;24&#44;\)\(sfx=auto&#124;*&#44;\)\(asfx=&#44;\)\(psfx=&#44;\)&#93;</tt> |  The time of macro() processing (use CGI for live time in HTML)
 <tt>&#91;datetime&#93;</tt> |  The datetime of macro() processing (use CGI for live date in HTML)
 <tt>&#91;ampm N&#93;</tt> |  AM or PM from 12 hour number
 <tt>&#91;twelve N&#93;</tt> |  12 hour number from 24
 <tt>&#91;month \(mode=long,\)N&#93;</tt> |  Month name from ordinal
 <tt>&#91;include **fileName**&#93;</tt> |  include macro() source file
 <tt>&#91;embrace **moduleName**&#93;</tt> |  add&#44; extend&#44; or replace macro() functionality
 <tt>&#91;repeat **value&#44;**content&#93;</tt> |  repeat content&#44; evaluating content <i>each time</i>
 <tt>&#91;comment content&#93;</tt> |  suppress output. <i>note: non-content operations still process</i>
 <tt>&#91;back **HEX3&#124;HEX6**&#93;</tt> |  HTML background text color for HTML 4.01s mode <i>only</i>
 <tt>&#91;mode **3.2&#124;4.01s**&#93;</tt> |  set HTML mode
 <tt>&#91;hlit \(format=1&#44;\)**content**&#93;</tt> |  places LITERAL content in local variable loc_hlit
 <tt>&#91;vlit \(format=1&#44;\)**variable-name**&#93;</tt> |  places LITERAL content in local variable loc_vlit
 <tt>&#91;slit \(format=1&#44;\)\(wrap=1&#44;\)**style-name**&#93;</tt> |  places LITERAL content in local variable loc_slit

Escapes | &nbsp;
------- | ----
 <tt>&#91;co&#93;</tt> |  comma
 <tt>&#91;sp&#93;</tt> |  space
 <tt>&#91;gt&#93;</tt> |  greater-than
 <tt>&#91;lt&#93;</tt> |  less-than
 <tt>&#91;lb&#93;</tt> |  left square bracket
 <tt>&#91;rb&#93;</tt> |  right square bracket
 <tt>&#91;ls&#93;</tt> |  left squiggly bracket
 <tt>&#91;rs&#93;</tt> |  right squiggly bracket
 <tt>&#91;lf&#124;nl&#93;</tt> |  new line

Styles | &nbsp;
------ | ----
 <tt>&#91;style **styleName** **styleContent**&#93;</tt> |  local style
 <tt>&#91;gstyle **styleName** **styleContent**&#93;</tt> |  global style
 <tt>&#91;for **styleName**&#44;**X**&#44;**Y**&#44;**Z**&#93;</tt> |  iterates number to style
 <tt>&#91;in **styleName**&#44;**listName**&#93;</tt> |  iterates list to style
 <tt>&#91;switch \(csep=X&#44;\)\(isep=Y&#44;\)**switchName** **caseYstylename(XcaseYstyleName)**&#93;</tt> |  switch (works with case)
 <tt>&#91;case \(sep=X&#44;\)**switchName** **caseXcontent**&#93;</tt> |  case (works with switch)
 <tt>&#91;s \(sep=X&#44;\)**stylename**\(styleParameters\)&#93;</tt> |  invoke style(s)&#44; local&#44; if no local&#44; then global
 <tt>&#91;glos \(sep=X&#44;\)**stylename**\(styleParameters\)&#93;</tt> |  invoke global style(s)
 <tt>&#91;locs \(sep=X&#44;\)**stylename**\(styleParameters\)&#93;</tt> |  invoke local style(s)
 <tt>&#91;spage&#93;</tt> |  reset local styles to <i>none</i>
 <tt>&#91;ghost \(source=global&#124;local&#44;\)**stylename**&#93;</tt> |  output style without processing it
 <tt>&#91;fref **lable**&#93;</tt> |  forward (or backward) reference
 <tt>&#91;resolve \(hex=1&#44;\)**lable&#44;**content&#93;</tt> |  resolve reference
 <tt>&#91;listg \(mode=global&#93;</tt> | local&#44;\)**listName&#44;**content| resolve reference


## Alphabetical Order

_key:_ built-in \(options\) **required** content

Built-in | &nbsp;
-------- | ----
 <tt>&#91;a \(tab&#44;\)**URL**\(&#44;linkedContent\)&#93;</tt> |  HTML link
 <tt>&#91;abs **value**&#93;</tt> |  absolute value of number
 <tt>&#91;add \(mode=float&#44;\)**value** **addend**&#93;</tt> |  add two numbers
 <tt>&#91;aisort \(rev=1&#44;\)**listName**&#93;</tt> |  ASCII case-insensitive sofr of list&#44; in place
 <tt>&#91;alphalead \(trail=1,\)content&#93;</tt> | Return leading alpha characters&#44; or trailing content
 <tt>&#91;alphanumlead \(trail=1,\)content&#93;</tt> | Return leading alphanumeric characters&#44; or trailing content
 <tt>&#91;ampm N&#93;</tt> |  AM or PM from 12 hour number
 <tt>&#91;append **listName**&#44;itemContent&#93;</tt> |  append an item to a list (can create new list)
 <tt>&#91;asort \(rev=1&#44;\)**listName**&#93;</tt> |  ASCII alphabetic sort of list&#44; in place
 <tt>&#91;b content&#93;</tt> |  HTML bold
 <tt>&#91;back **HEX3&#124;HEX6**&#93;</tt> |  HTML background text color for HTML 4.01s mode <i>only</i>
 <tt>&#91;bq content&#93;</tt> |  HTML blockquote
 <tt>&#91;br \(parms&#44;\)\(content\)&#93;</tt> |  (content) HTML line break (with parms)
 <tt>&#91;btodec (digits=N&#44;)**value**&#93;</tt> |  binary to decimal conversion
 <tt>&#91;caps content&#93;</tt> |  sentence case
 <tt>&#91;capt content&#93;</tt> |  title case
 <tt>&#91;capw content&#93;</tt> |  word case
 <tt>&#91;case \(sep=X&#44;\)**switchName** **caseXcontent**&#93;</tt> |  case (works with switch)
 <tt>&#91;cell \(options\)&#44;content&#93;</tt> |  HTML table data cell \(comma is *not* optional\)
 <tt>&#91;center **width&#44;****padChar&#44;**content&#93;</tt> |  center (neg width indicates pad both sides)
 <tt>&#91;chr **value**&#93;</tt> |  return ASCII character of code=value
 <tt>&#91;clearl **listName**&#93;</tt> |  Discards list content
 <tt>&#91;cmap **listName**&#93;</tt> |  create 1:1 character map
 <tt>&#91;collapse content&#93;</tt> | 
 <tt>&#91;color **HEX3&#124;HEX6** content&#93;</tt> |  HTML text color
 <tt>&#91;comment content&#93;</tt> |  suppress output. <i>note: non-content operations still process</i>
 <tt>&#91;count \(sep=X&#44;\)\(overlaps=yes&#44;\)\(casesens=yes&#44;\)**patternXcontent**&#93;</tt> |  count incidences
 <tt>&#91;co&#93;</tt> |  comma
 <tt>&#91;crop (words=no&#44;)(eol=&#44;)(neol=&#44;)(col=78&#44;)content&#93;</tt> | 
 <tt>&#91;crush &#44;&#93;</tt> |  return packed alphanumerics
 <tt>&#91;csep **value**&#93;</tt> |  comma-separate an integer
 <tt>&#91;d \(sep=X&#44;\)**dictName****Xkey**\(XnotFound\)&#93;</tt> |  retrieve a dictionary value using key
 <tt>&#91;datetime&#93;</tt> |  The datetime of macro() processing (use CGI for live date in HTML)
 <tt>&#91;date&#93;</tt> |  The date of macro() processing (use CGI for live date in HTML)
 <tt>&#91;dcopy **sourceDictionary&#44;****destinationDictionary**&#93;</tt> |  copy/replace destination with source
 <tt>&#91;dec **value**&#93;</tt> |  subtract one from value
 <tt>&#91;decrypt \(mode=1&#44;\)\(seed=N&#44;\)\(salt=String&#44;\)\(icount=N&#44;\)content&#93;</tt> |  Decrypt content
 <tt>&#91;dict \(sep=X&#44;\)\(keysep=Y&#44;\)**dictName&#44;****keyYvalue\(XkeyYvalue\)**&#93;</tt> |  create/replace dictionary
 <tt>&#91;div \(mode=float&#44;\)**value** **divisor**&#93;</tt> |  divide two numbers
 <tt>&#91;dkeys **sourceDictionary&#44;****destinationList**&#93;</tt> |  create a <b>list</b> of keys from source
 <tt>&#91;dlist \(fs=styleName&#44;\)\(ls=styleName&#44;\)\(wrap=styleName&#44;\)\(parms=PRE&#44;\)\(inter=INT&#44;\)\(ntl=NTL&#44;\)\(posts=PST&#44;\)listName&#93;</tt> |  dump a list
 <tt>&#91;dset \(keysep=Y&#44;\)**dictName&#44;****keyYvalue**&#93;</tt> |  create/replace dictionary item
 <tt>&#91;dtobin (digits=N&#44;)**value**&#93;</tt> |  decimal to binary conversion
 <tt>&#91;dtohex (digits=N&#44;)**value**&#93;</tt> |  decimal to hexadecimal conversion
 <tt>&#91;dtooct (digits=N&#44;)**value**&#93;</tt> |  decimal to octal conversion
 <tt>&#91;dup **value&#44;content**&#93;</tt> |  duplicate content <i>after</i> evaluation (also see &#91;repeat&#93;)
 <tt>&#91;e **listName&#44;****listIndex**&#93;</tt> |  output item from list of length n (listIndex = 0 to n-1)
 <tt>&#91;else \(sep=X&#44;\)\(wrap&#124;style=styleName\)**value** **match** content&#93;</tt> |  if <b>not</b> match&#44; then content
 <tt>&#91;embrace **moduleName**&#93;</tt> |  add&#44; extend&#44; or replace macro() functionality
 <tt>&#91;encrypt \(mode=1&#44;\)\(again=1&#44;\)\(seed=N&#44;\)\(salt=String&#44;\)\(icount=N&#44;\)\(breakat=N&#44;\)content&#93;</tt> |  (re)Encrypt content
 <tt>&#91;eq \(sep=X&#44;\)**value&#44;**content&#93;</tt> |  if value is <b>not</b> empty&#44; then content
 <tt>&#91;eval \(style=styleName&#44;\)**value&#44;content**&#93;</tt> |  duplicate content Nx&#44; eval style Nx if provided
 <tt>&#91;even **value** content&#93;</tt> |  if value is even&#44; then content
 <tt>&#91;expand **dictName&#44;**content&#93;</tt> |  dictionary based keyword expansion with leading cap forwarding
 <tt>&#91;fcsep **value**&#93;</tt> |  comma-separate a floating point number
 <tt>&#91;fetch **itemIndex**&#93;</tt> |  fetch any item from stack - 0 is top of stack
 <tt>&#91;find \(sep=X&#44;\)**stringXcontent**&#93;</tt> |  find string in content&#44; sep default = &quot;&#44;&quot;
 <tt>&#91;flush&#93;</tt> |  delete stack contents
 <tt>&#91;for **styleName**&#44;**X**&#44;**Y**&#44;**Z**&#93;</tt> |  iterates number to style
 <tt>&#91;fref **lable**&#93;</tt> |  forward (or backward) reference
 <tt>&#91;getc \(var=varName&#44;\)\(high=lang&#44;\)\(tabsiz=n&#44;\)\(tabchar=X&#44;\)filename&#93;</tt> |  import c or oc source file as aa_macro
 <tt>&#91;ghost \(source=global&#124;local&#44;\)**stylename**&#93;</tt> |  output style without processing it
 <tt>&#91;gload **varName** **fileName**&#93;</tt> |  load file into global variable
 <tt>&#91;global **varName** varContent&#93;</tt> |  global variable definition
 <tt>&#91;glos \(sep=X&#44;\)**stylename**\(styleParameters\)&#93;</tt> |  invoke global style(s)
 <tt>&#91;graw **varName** varContent&#93;</tt> |  global variable definition
 <tt>&#91;gsave **varName** **fileName**&#93;</tt> |  save file from global variable
 <tt>&#91;gstyle **styleName** **styleContent**&#93;</tt> |  global style
 <tt>&#91;gt&#93;</tt> |  greater-than
 <tt>&#91;gv **varName**&#93;</tt> |  global variable
 <tt>&#91;header \(options\)&#44;content&#93;</tt> |  HTML table header cell \(comma is *not* optional\)
 <tt>&#91;hlit \(format=1&#44;\)**content**&#93;</tt> |  places LITERAL content in local variable loc_hlit
 <tt>&#91;hmap **listName**&#93;</tt> |  create 1:1 character map to hex values
 <tt>&#91;hsort \(rev=1&#44;\)content&#93;</tt> |  sort of lines by amatuer radio callsign followed by non-alphanumeric
 <tt>&#91;htodec (digits=N&#44;)**value**&#93;</tt> |  hexadecimal to decimal conversion
 <tt>&#91;i content&#93;</tt> |  HTML italics
 <tt>&#91;if \(sep=X&#44;\)\(wrap&#124;style=styleName\)**value** **match** content&#93;</tt> |  if match&#44; then content
 <tt>&#91;ifge **value1&#44;****value2 &#44;**content&#93;</tt> |  if value1 &gt;= value2&#44; then content
 <tt>&#91;ifle **value1&#44;****value2 &#44;**content&#93;</tt> |  if value1 &lt;= value2&#44; then content
 <tt>&#91;ifol \(istyle=hstyle&#44;\)\(lstyle=hstyle&#44;\)\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt> |  HTML ordered list IF &gt; one item
 <tt>&#91;iful \(istyle=hstyle&#44;\)\(lstyle=hstyle&#44;\)\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt> |  HTML unordered list IF &gt; one item
 <tt>&#91;img \(imageTitle&#44;\)**imageURL** \(linkURL\)&#93;</tt> |  HTML image
 <tt>&#91;in **styleName**&#44;**listName**&#93;</tt> |  iterates list to style
 <tt>&#91;inc **value**&#93;</tt> |  add one to value
 <tt>&#91;include **fileName**&#93;</tt> |  include macro() source file
 <tt>&#91;int **value**&#93;</tt> |  integer of number
 <tt>&#91;inter **iStr&#44;****L&#124;R&#44;****value&#44;**content&#93;</tt> |  intersperse iStr every value in content
 <tt>&#91;isort \(rev=1&#44;\)\(sep=X&#44;\)**listName**&#93;</tt> |  sort by leading integer&#44; sep defaults to &quot;&#44;&quot;
 <tt>&#91;issort \(rev=1&#44;\)content&#93;</tt> |  sort of lines by integer followed by a comma
 <tt>&#91;lb&#93;</tt> |  left square bracket
 <tt>&#91;lc content&#93;</tt> |  return length of content in lines
 <tt>&#91;lcc **listOne&#44;****listTwo&#44;****listResult**&#93;</tt> |  list concatenate
 <tt>&#91;lcopy **sourceList** **destinationList**&#93;</tt> |  copy list to new or existing list
 <tt>&#91;len content&#93;</tt> |  return length of content in characters
 <tt>&#91;lf&#124;nl&#93;</tt> |  new line
 <tt>&#91;lhsort \(rev=1&#44;\)**listName**&#93;</tt> |  sort list by leading amateur radio callsign&#44;, any non-alphanumeric sep
 <tt>&#91;limg \(target=&#44;\)\(lpath=&#44;\)\(wpath=\)\(title=&#44;\)\(alt=&#44;\)**imageName**&#93;</tt> |  HTML image name, figures size (uses &#91;lipath&#93;,&#91;wepath&#93;)
 <tt>&#91;lipath **filePathToImages**&#93;</tt> |  path for &#91;locimg&#93;
 <tt>&#91;list \(sep=X&#44;\)**listname**&#44;itemContent\(XitemContent\)&#93;</tt> |  create or overwrite a list
 <tt>&#91;listg \(mode=global&#93;</tt> | local&#44;\)**listName&#44;**content| resolve reference
 <tt>&#91;ljoin **listName**&#44;\(joinTerm\)&#93;</tt> |  Join a list with joinTerm(s) between elements
 <tt>&#91;ljust **width&#44;****padChar&#44;**content&#93;</tt> |  left justify
 <tt>&#91;llen **listName**&#93;</tt> |  returns length of list
 <tt>&#91;load **varName** **fileName**&#93;</tt> |  load file into local variable
 <tt>&#91;local **varname** varContent&#93;</tt> |  local variable definition
 <tt>&#91;locs \(sep=X&#44;\)**stylename**\(styleParameters\)&#93;</tt> |  invoke local style(s)
 <tt>&#91;lower content&#93;</tt> |  convert to lowercase
 <tt>&#91;lpop **listName&#44;**\(listIndex\)&#93;</tt> |  pop an item out of a list at top, or at listIndex
 <tt>&#91;lpush **listName**&#44;itemContent&#93;</tt> |  append an item to a list (can create new list)
 <tt>&#91;lset **listName&#44;****listIndex&#44;**itemContent&#93;</tt> |  Set a list item
 <tt>&#91;lslice **sliceSpec&#44;****listName&#44;****targetList**&#93;</tt> |  slice listName to targetList
 <tt>&#91;lsplit \(sep=^&#44;\)\(num=N&#44;\)**listName**&#44;content&#93;</tt> |  split content into list
 <tt>&#91;lsub \(ci=1&#44;\)\(sep=X&#44;\)**listName&#44;**content&#93;</tt> |  list of form AsepB, A=B in content
 <tt>&#91;ls&#93;</tt> |  left squiggly bracket
 <tt>&#91;ltol **listName** content&#93;</tt> |  convert lines of content to list
 <tt>&#91;lt&#93;</tt> |  less-than
 <tt>&#91;lv **varName**&#93;</tt> |  local variable
 <tt>&#91;max **value1** **value2**&#93;</tt> |  maximum of two numbers
 <tt>&#91;min **value1** **value2**&#93;</tt> |  minimum of two numbers
 <tt>&#91;mode **3.2&#124;4.01s**&#93;</tt> |  set HTML mode
 <tt>&#91;month \(mode=long,\)N&#93;</tt> |  Month name from ordinal
 <tt>&#91;mul \(mode=float&#44;\)**value** **multiplier**&#93;</tt> |  multiply two numbers
 <tt>&#91;nd **integer**&#93;</tt> |  1st, 2nd, 3rd, 4th...
 <tt>&#91;ne \(sep=X&#44;\)**value&#44;**content&#93;</tt> |  if value is empty&#44; then content
 <tt>&#91;odd **value** content&#93;</tt> |  if value is odd&#44; then content
 <tt>&#91;ol \(type=X&#44;\)\(start=N&#44;\)\(istyle=hstyle&#44;\)\(lstyle=hstyle&#44;\)\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt> |  HTML ordered list
 <tt>&#91;ord **character**&#93;</tt> |  return ASCII code value in decimal
 <tt>&#91;otodec (digits=N&#44;)**value**&#93;</tt> |  octal to decimal conversion
 <tt>&#91;p content&#93;</tt> |  HTML paragraph
 <tt>&#91;parm **value**&#93;</tt> |  returns results of &#91;split&#93;
 <tt>&#91;pop&#93;</tt> |  Pop an item off the top of the general stack
 <tt>&#91;postparse content&#93;</tt> |  pretty-print Python 2.7 code (use black background)
 <tt>&#91;push content&#93;</tt> |  Push an item on to the general stack
 <tt>&#91;pythparse content&#93;</tt> |  pretty-print Python 2.7 code (use black background)
 <tt>&#91;random \(seed=none&#44;\(icount=N&#44;\)\)&#93;</tt> |  generate random from 0.0-1.0
 <tt>&#91;raw **varname** varContent&#93;</tt> |  local variable definition
 <tt>&#91;rb&#93;</tt> |  right square bracket
 <tt>&#91;repeat **value&#44;**content&#93;</tt> |  repeat content&#44; evaluating content <i>each time</i>
 <tt>&#91;replace \(sep=X&#44;\(lf=1&#44;\)\)**targetXreplacementXcontent**&#93;</tt> |  target replaced with replacement in content
 <tt>&#91;resolve \(hex=1&#44;\)**lable&#44;**content&#93;</tt> |  resolve reference
 <tt>&#91;rjust **width&#44;****padChar&#44;**content&#93;</tt> |  right justify
 <tt>&#91;roman **value**&#93;</tt> |  returns lower case roman numeral
 <tt>&#91;row \(options\)&#44;content&#93;</tt> |  HTML table row \(comma is *not* optional\)
 <tt>&#91;rs&#93;</tt> |  right squiggly bracket
 <tt>&#91;s \(sep=X&#44;\)**stylename**\(styleParameters\)&#93;</tt> |  invoke style(s)&#44; local&#44; if no local&#44; then global
 <tt>&#91;save **varName** **fileName**&#93;</tt> |  save file from local variable
 <tt>&#91;sisort \(rev=1&#44;\)content&#93;</tt> |  case-insensitive sort of lines
 <tt>&#91;slice **sliceSpec&#44;content**&#93;</tt> |  slice content
 <tt>&#91;slit \(format=1&#44;\)\(wrap=1&#44;\)**style-name**&#93;</tt> |  places LITERAL content in local variable loc_slit
 <tt>&#91;soundex \(len=N&#44;\)content&#93;</tt> |  return soundex value of content
 <tt>&#91;spage&#93;</tt> |  reset local styles to <i>none</i>
 <tt>&#91;splash \(pre=&#44;\)\(post=&#44;\)\(inter=&#44;\)\(ntl=&#44;\)\(limit=N&#44;\)\(style=Style&#44;\)\(sep=&#44;&#44;\)content&#93;</tt> |  splits content, applies style
 <tt>&#91;split **X&#44;**content\(Xcontent\)&#93;</tt> |  split for use with &#91;parm&#93;
 <tt>&#91;splitcount **value**&#93;</tt> |  Maximum number of splits to perform in next &#91;split&#93;
 <tt>&#91;sp&#93;</tt> |  space
 <tt>&#91;ssort \(rev=1&#44;\)content&#93;</tt> |  case-sensitive sort of lines
 <tt>&#91;stage \(mode=float&#44;\)\(digits=N&#44;\)**start** **end** **steps** **step**&#93;</tt> |  subtract one from value
 <tt>&#91;strip content&#93;</tt> |  strip HTML tags out
 <tt>&#91;stripe (charset=chars,)content&#93;</tt> |  strip chars from both ends of line (default = spaces)
 <tt>&#91;style **styleName** **styleContent**&#93;</tt> |  local style
 <tt>&#91;sub \(mode=float&#44;\)**value** **subtrahend**&#93;</tt> |  subtract two numbers
 <tt>&#91;switch \(csep=X&#44;\)\(isep=Y&#44;\)**switchName** **caseYstylename(XcaseYstyleName)**&#93;</tt> |  switch (works with case)
 <tt>&#91;sys **shellCommand**&#93;</tt> |  invoke an operating system command. Output is captured
 <tt>&#91;t \(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt> |  style wrap around item(s)
 <tt>&#91;table \(options\)&#44;content&#93;</tt> |  HTML table \(comma is *not* optional\)
 <tt>&#91;th **integer**&#93;</tt> |  st, nd, rd, th...
 <tt>&#91;time \(mode=12&#124;24&#44;\)\(sfx=auto&#124;*&#44;\)\(asfx=&#44;\)\(psfx=&#44;\)&#93;</tt> |  The time of macro() processing (use CGI for live time in HTML)
 <tt>&#91;translate \(pre=PRE&#44;\)\(post=POST&#44;\)\(inter=INTER&#44;\)**listName&#44;**content&#93;</tt> |  translate content using character map formatted list
 <tt>&#91;twelve N&#93;</tt> |  12 hour number from 24
 <tt>&#91;u content&#93;</tt> |  HTML underline
 <tt>&#91;ul \(istyle=hstyle&#44;\)\(lstyle=hstyle&#44;\)\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt> |  HTML unordered list
 <tt>&#91;upper content&#93;</tt> |  convert to uppercase
 <tt>&#91;url \(sep=&#124;&#44;\)\(css=CSS&#44;\)\(tgt=_target&#44;\)\(nam=Name&#44;\)\(URLsepLINKED_CONTENT\)&#93;</tt> | Create URL
 <tt>&#91;urlencode **content**&#93;</tt> |  URL encoding
 <tt>&#91;v **varName**&#93;</tt> |  local/global variable
 <tt>&#91;vdec \(pre=1&#44;\)\(quiet=1&#44;\)**varName**&#93;</tt> |  decrement local(global) variable
 <tt>&#91;vinc \(pre=1&#44;\)\(quiet=1&#44;\)**varName**&#93;</tt> |  increment local(global) variable
 <tt>&#91;vlit \(format=1&#44;\)**variable-name**&#93;</tt> |  places LITERAL content in local variable loc_vlit
 <tt>&#91;vs **varName** varContent&#93;</tt> |  local variable definition
 <tt>&#91;wc content&#93;</tt> |  return length of content in words
 <tt>&#91;wepath **webPathToImages**&#93;</tt> |  path for &#91;locimg&#93;
 <tt>&#91;wwrap \(eol=X&#44;\)\(wrap=style&#44;\)\(nohtml=1&#44;\)**value&#44;**content&#93;</tt> |  word wrap content at column value


