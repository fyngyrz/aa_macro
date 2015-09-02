 
# Macro() Quick Reference
## Functional Groupings


_key:_ built-in \(options\) **required** content



HTML Text Styling | &nbsp;
----------------- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;p" data="content&#93;</tt>")  |  HTML paragraph
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;bq" data="content&#93;</tt>")  |  HTML blockquote
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;b" data="content&#93;</tt>")  |  HTML bold
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;i" data="content&#93;</tt>")  |  HTML italics
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;u" data="content&#93;</tt>")  |  HTML underline
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;color" data="**HEX3&#124;HEX6** content&#93;</tt>")  |  HTML text color

HTML Linking | &nbsp;
------------ | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;a" data="\(tab&#44;\)**URL**\(&#44;linkedContent\)&#93;</tt>")  |  HTML link

HTML Images | &nbsp;
----------- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;img" data="\(imageTitle&#44;\)**imageURL** \(linkURL\)&#93;</tt>")  |  HTML image
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;locimg" data="\(imageTitle&#44;\)**imageURL** \(linkURL\)&#93;</tt>")  |  HTML image, with size (uses &#91;lipath&#93;)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lipath" data="**pathToImages**&#93;</tt>")  |  path for &#91;locimg&#93;

HTML Lists | &nbsp;
---------- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ul" data="\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt>")  |  HTML unordered list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ol" data="\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt>")  |  HTML ordered list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;iful" data="\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt>")  |  HTML unordered list IF &gt; one item
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ifol" data="\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt>")  |  HTML ordered list IF &gt; one item
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;t" data="\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt>")  |  style wrap around item(s)

HTML Tables | &nbsp;
----------- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;table" data="\(options&#44;\)content&#93;</tt>")  |  HTML table
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;row" data="\(options&#44;\)content&#93;</tt>")  |  HTML table row
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;header" data="\(options&#44;\)content&#93;</tt>")  |  HTML table header cell
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;cell" data="\(options&#44;\)content&#93;</tt>")  |  HTML table data cell

Variables | &nbsp;
--------- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;local" data="**varname** varContent&#93;</tt>")  |  local variable definition
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;vs" data="**varName** varContent&#93;</tt>")  |  local variable definition
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;global" data="**varName** varContent&#93;</tt>")  |  global variable definition
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;v" data="**varName**&#93;</tt>")  |  local/global variable
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;gv" data="**varName**&#93;</tt>")  |  global variable
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lv" data="**varName**&#93;</tt>")  |  local variable

Data Lists | &nbsp;
---------- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;list" data="\(sep=X&#44;\)**listname**&#44;itemContent\(XitemContent\)&#93;</tt>")  |  create or overwrite a list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lcopy" data="**sourceList** **destinationList**&#93;</tt>")  |  copy list to new or existing list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ltol" data="**listName** content&#93;</tt>")  |  convert lines of content to list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;append" data="**listName**&#44;itemContent&#93;</tt>")  |  append an item to a list (can create new list)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lpush" data="**listName**&#44;itemContent&#93;</tt>")  |  append an item to a list (can create new list)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lpop" data="**listName&#44;**\(listIndex\)&#93;</tt>")  |  pop an item out of a list at top, or at listIndex
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lset" data="**listName&#44;****listIndex&#44;**itemContent&#93;</tt>")  |  Set a list item
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;llen" data="**listName**&#93;</tt>")  |  returns length of list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lslice" data="**sliceSpec&#44;****listName&#44;****targetList**&#93;</tt>")  |  slice listName to targetList
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dlist" data="\(wrap=styleName&#44;\)\(parms=PRE&#44;\)\(posts=PST&#44;\)listName&#93;</tt>")  |  dump a list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;e" data="**listName&#44;****listIndex**&#93;</tt>")  |  output item from list of length n (listIndex = 0 to n-1)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lcc" data="**listOne&#44;****listTwo&#44;****listResult**&#93;</tt>")  |  list concatenate
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lsub" data="\(sep=X&#44;\)**listName&#44;**content&#93;</tt>")  |  list of form AsepB, A=B in content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;asort" data="**listName**&#93;</tt>")  |  ASCII alphabetic sort of list&#44; in place
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;aisort" data="**listName**&#93;</tt>")  |  ASCII case-insensitive sofr of list&#44; in place
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;isort" data="\(sep=X&#44;\)**listName**&#93;</tt>")  |  sort by leading integer&#44; sep defaults to &quot;&#44;&quot;
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lhsort" data="**listName**&#93;</tt>")  |  sort list by leading amateur radio callsign&#44;, any non-alphanumeric sep
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;cmap" data="**listName**&#93;</tt>")  |  create 1:1 character map
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;translate" data="**listName&#44;**content&#93;</tt>")  |  translate content using character map formatted list

Data Dictionaries | &nbsp;
----------------- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dict" data="\(sep=X&#44;\)\(keysep=Y&#44;\)**dictName&#44;****keyYvalue\(XkeyYvalue\)**&#93;</tt>")  |  create/replace dictionary
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dcopy" data="**sourceDictionary&#44;****destinationDictionary**&#93;</tt>")  |  copy/replace destination with source
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dkeys" data="**sourceDictionary&#44;****destinationList**&#93;</tt>")  |  create a <b>list</b> of keys from source
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dset" data="\(keysep=Y&#44;\)**dictName&#44;****keyYvalue**&#93;</tt>")  |  create/replace dictionary item
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;d" data="**dictName&#44;****key**&#93;</tt>")  |  retrieve a dictionary value using key

General Stack | &nbsp;
------------- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;push" data="content&#93;</tt>")  |  Push an item on to the general stack
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;pop&#93;</tt>" data="")  |  Pop an item off the top of the general stack
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;fetch" data="**itemIndex**&#93;</tt>")  |  fetch any item from stack - 0 is top of stack
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;flush&#93;</tt>" data="")  |  delete stack contents

Math | &nbsp;
---- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;add" data="**value** **addend**&#93;</tt>")  |  add two numbers
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;sub" data="**value** **subtrahend**&#93;</tt>")  |  subtract two numbers
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;mul" data="**value** **multiplier**&#93;</tt>")  |  multiply two numbers
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;div" data="**value** **divisor**&#93;</tt>")  |  divide two numbers
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;max" data="**value1** **value2**&#93;</tt>")  |  maximum of two numbers
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;min" data="**value1** **value2**&#93;</tt>")  |  minimum of two numbers
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;inc" data="**value**&#93;</tt>")  |  add one to value
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dec" data="**value**&#93;</tt>")  |  subtract one from value

Conditional Content | &nbsp;
------------------- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;even" data="**value** content&#93;</tt>")  |  if value is even&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;odd" data="**value** content&#93;</tt>")  |  if value is odd&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;if" data="**value** **match** content&#93;</tt>")  |  if match&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;else" data="**value** **match** content&#93;</tt>")  |  if <b>not</b> match&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ne" data="**value&#44;**content&#93;</tt>")  |  if value is empty&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;eq" data="**value&#44;**content&#93;</tt>")  |  if value is <b>not</b> empty&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ifle" data="**value1&#44;****value2 &#44;**content&#93;</tt>")  |  if value1 &lt;= value2&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ifge" data="**value1&#44;****value2 &#44;**content&#93;</tt>")  |  if value1 &gt;= value2&#44; then content

Text Processing | &nbsp;
--------------- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;slice" data="**sliceSpec&#44;content**&#93;</tt>")  |  slice content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;splitcount" data="**value**&#93;</tt>")  |  Maximum number of splits to perform in next &#91;split&#93;
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;split" data="**X&#44;**content\(Xcontent\)&#93;</tt>")  |  split for use with &#91;parm&#93;
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;parm" data="**value**&#93;</tt>")  |  returns results of &#91;split&#93;
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;upper" data="content&#93;</tt>")  |  convert to uppercase
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lower" data="content&#93;</tt>")  |  convert to lowercase
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;soundex" data="\(len=N&#44;\)content&#93;</tt>")  |  return soundex value of content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;strip" data="content&#93;</tt>")  |  strip HTML tags out
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;roman" data="**value**&#93;</tt>")  |  returns lower case roman numeral
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dtohex" data="**value**&#93;</tt>")  |  decimal to hexadecimal conversion
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dtooct" data="**value**&#93;</tt>")  |  decimal to octal conversion
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dtobin" data="**value**&#93;</tt>")  |  decimal to binary conversion
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;htodec" data="**value**&#93;</tt>")  |  hexadecimal to decimal conversion
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;otodec" data="**value**&#93;</tt>")  |  octal to decimal conversion
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;btodec" data="**value**&#93;</tt>")  |  binary to decimal conversion
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;wwrap" data="\(wrap=style&#44;\)**value&#44;**content&#93;</tt>")  |  word wrap content at column value
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;len" data="content&#93;</tt>")  |  return length of content in characters
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;wc" data="content&#93;</tt>")  |  return length of content in words
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lc" data="content&#93;</tt>")  |  return length of content in lines
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;chr" data="**value**&#93;</tt>")  |  return ASCII character of code=value
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ord" data="**character**&#93;</tt>")  |  return ASCII code value in decimal
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;csep" data="**value**&#93;</tt>")  |  comma-separate an integer
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;fcsep" data="**value**&#93;</tt>")  |  comma-separate a floating point number
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dup" data="**value&#44;content**&#93;</tt>")  |  duplicate content <i>after</i> evaluation (also see &#91;repeat&#93;)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;find" data="\(sep=X&#44;\)**stringXcontent**&#93;</tt>")  |  find string in content&#44; sep default = &quot;&#44;&quot;
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;replace" data="\(sep=X&#44;\)**targetXreplacementXcontent**&#93;</tt>")  |  target replaced with replacement in content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;count" data="\(sep=X&#44;\)\(overlaps=yes&#44;\)\(casesens=yes&#44;\)**patternXcontent**&#93;</tt>")  |  count incidences
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;caps" data="content&#93;</tt>")  |  sentence case
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;capw" data="content&#93;</tt>")  |  word case
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;capt" data="content&#93;</tt>")  |  title case
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;expand" data="**dictName&#44;**content&#93;</tt>")  |  dictionary based keyword expansion with leading cap forwarding
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ssort" data="content&#93;</tt>")  |  case-sensitive sort of lines
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;sisort" data="content&#93;</tt>")  |  case-insensitive sort of lines
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;issort" data="content&#93;</tt>")  |  sort of lines by integer followed by a comma
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;hsort" data="content&#93;</tt>")  |  sort of lines by amatuer radio callsign followed by non-alphanumeric
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;inter" data="**iStr&#44;****L&#124;R&#44;****value&#44;**content&#93;</tt>")  |  intersperse iStr every value in content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;rjust" data="**width&#44;****padChar&#44;**content&#93;</tt>")  |  right justify
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ljust" data="**width&#44;****padChar&#44;**content&#93;</tt>")  |  left justify
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;center" data="**width&#44;****padChar&#44;**content&#93;</tt>")  |  center (neg width indicates pad both sides)

Miscellanea | &nbsp;
----------- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;sys" data="**shellCommand**&#93;</tt>")  |  invoke an operating system command. Output is captured
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;date&#93;</tt>" data="")  |  The date of macro() processing (use CGI for live date in HTML)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;time&#93;</tt>" data="")  |  The time of macro() processing (use CGI for live time in HTML)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;include" data="**fileName**&#93;</tt>")  |  include macro() source file
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;embrace" data="**moduleName**&#93;</tt>")  |  add&#44; extend&#44; or replace macro() functionality
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;repeat" data="**value&#44;**content&#93;</tt>")  |  repeat content&#44; evaluating content <i>each time</i>
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;comment" data="content&#93;</tt>")  |  suppress output. <i>note: non-content operations still process</i>
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;back" data="**HEX3&#124;HEX6**&#93;</tt>")  |  HTML background text color for HTML 4.01s mode <i>only</i>
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;mode" data="**3.2&#124;4.01s**&#93;</tt>")  |  set HTML mode

Escapes | &nbsp;
------- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;co&#93;</tt>" data="")  |  comma
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;sp&#93;</tt>" data="")  |  space
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lb&#93;</tt>" data="")  |  left square bracket
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;rb&#93;</tt>" data="")  |  right square bracket
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ls&#93;</tt>" data="")  |  left squiggly bracket
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;rs&#93;</tt>" data="")  |  right squiggly bracket
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lf&#124;nl&#93;</tt>" data="")  |  new line

Styles | &nbsp;
------ | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;style" data="**styleName** **styleContent**&#93;</tt>")  |  local style
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;gstyle" data="**styleName** **styleContent**&#93;</tt>")  |  global style
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;s" data="**stylename**\( styleParameters\)&#93;</tt>")  |  invoke style&#44; local&#44; if no local&#44; then global
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;glos" data="**stylename**\( styleParameters\)&#93;</tt>")  |  invoke global style
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;locs" data="**stylename**\( styleParameters\)&#93;</tt>")  |  invoke local style
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;spage&#93;</tt>" data="")  |  reset local styles to <i>none</i>
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ghost" data="\(source=global&#124;local&#44;\)**stylename**&#93;</tt>")  |  output style without processing it
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;fref" data="**lable**&#93;</tt>")  |  forward (or backward) reference
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;resolve" data="**lable&#44;**content&#93;</tt>")  |  resolve reference


## Alphabetical Order

_key:_ built-in \(options\) **required** content

Built-in | &nbsp;
-------- | ----
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;a" data="\(tab&#44;\)**URL**\(&#44;linkedContent\)&#93;</tt>")  |  HTML link
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;add" data="**value** **addend**&#93;</tt>")  |  add two numbers
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;aisort" data="**listName**&#93;</tt>")  |  ASCII case-insensitive sofr of list&#44; in place
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;append" data="**listName**&#44;itemContent&#93;</tt>")  |  append an item to a list (can create new list)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;asort" data="**listName**&#93;</tt>")  |  ASCII alphabetic sort of list&#44; in place
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;b" data="content&#93;</tt>")  |  HTML bold
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;back" data="**HEX3&#124;HEX6**&#93;</tt>")  |  HTML background text color for HTML 4.01s mode <i>only</i>
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;bq" data="content&#93;</tt>")  |  HTML blockquote
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;btodec" data="**value**&#93;</tt>")  |  binary to decimal conversion
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;caps" data="content&#93;</tt>")  |  sentence case
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;capt" data="content&#93;</tt>")  |  title case
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;capw" data="content&#93;</tt>")  |  word case
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;cell" data="\(options&#44;\)content&#93;</tt>")  |  HTML table data cell
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;center" data="**width&#44;****padChar&#44;**content&#93;</tt>")  |  center (neg width indicates pad both sides)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;chr" data="**value**&#93;</tt>")  |  return ASCII character of code=value
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;cmap" data="**listName**&#93;</tt>")  |  create 1:1 character map
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;color" data="**HEX3&#124;HEX6** content&#93;</tt>")  |  HTML text color
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;comment" data="content&#93;</tt>")  |  suppress output. <i>note: non-content operations still process</i>
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;count" data="\(sep=X&#44;\)\(overlaps=yes&#44;\)\(casesens=yes&#44;\)**patternXcontent**&#93;</tt>")  |  count incidences
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;co&#93;</tt>" data="")  |  comma
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;csep" data="**value**&#93;</tt>")  |  comma-separate an integer
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;d" data="**dictName&#44;****key**&#93;</tt>")  |  retrieve a dictionary value using key
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;date&#93;</tt>" data="")  |  The date of macro() processing (use CGI for live date in HTML)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dcopy" data="**sourceDictionary&#44;****destinationDictionary**&#93;</tt>")  |  copy/replace destination with source
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dec" data="**value**&#93;</tt>")  |  subtract one from value
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dict" data="\(sep=X&#44;\)\(keysep=Y&#44;\)**dictName&#44;****keyYvalue\(XkeyYvalue\)**&#93;</tt>")  |  create/replace dictionary
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;div" data="**value** **divisor**&#93;</tt>")  |  divide two numbers
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dkeys" data="**sourceDictionary&#44;****destinationList**&#93;</tt>")  |  create a <b>list</b> of keys from source
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dlist" data="\(wrap=styleName&#44;\)\(parms=PRE&#44;\)\(posts=PST&#44;\)listName&#93;</tt>")  |  dump a list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dset" data="\(keysep=Y&#44;\)**dictName&#44;****keyYvalue**&#93;</tt>")  |  create/replace dictionary item
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dtobin" data="**value**&#93;</tt>")  |  decimal to binary conversion
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dtohex" data="**value**&#93;</tt>")  |  decimal to hexadecimal conversion
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dtooct" data="**value**&#93;</tt>")  |  decimal to octal conversion
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;dup" data="**value&#44;content**&#93;</tt>")  |  duplicate content <i>after</i> evaluation (also see &#91;repeat&#93;)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;e" data="**listName&#44;****listIndex**&#93;</tt>")  |  output item from list of length n (listIndex = 0 to n-1)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;else" data="**value** **match** content&#93;</tt>")  |  if <b>not</b> match&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;embrace" data="**moduleName**&#93;</tt>")  |  add&#44; extend&#44; or replace macro() functionality
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;eq" data="**value&#44;**content&#93;</tt>")  |  if value is <b>not</b> empty&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;even" data="**value** content&#93;</tt>")  |  if value is even&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;expand" data="**dictName&#44;**content&#93;</tt>")  |  dictionary based keyword expansion with leading cap forwarding
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;fcsep" data="**value**&#93;</tt>")  |  comma-separate a floating point number
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;fetch" data="**itemIndex**&#93;</tt>")  |  fetch any item from stack - 0 is top of stack
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;find" data="\(sep=X&#44;\)**stringXcontent**&#93;</tt>")  |  find string in content&#44; sep default = &quot;&#44;&quot;
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;flush&#93;</tt>" data="")  |  delete stack contents
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;fref" data="**lable**&#93;</tt>")  |  forward (or backward) reference
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ghost" data="\(source=global&#124;local&#44;\)**stylename**&#93;</tt>")  |  output style without processing it
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;global" data="**varName** varContent&#93;</tt>")  |  global variable definition
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;glos" data="**stylename**\( styleParameters\)&#93;</tt>")  |  invoke global style
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;gstyle" data="**styleName** **styleContent**&#93;</tt>")  |  global style
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;gv" data="**varName**&#93;</tt>")  |  global variable
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;header" data="\(options&#44;\)content&#93;</tt>")  |  HTML table header cell
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;hsort" data="content&#93;</tt>")  |  sort of lines by amatuer radio callsign followed by non-alphanumeric
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;htodec" data="**value**&#93;</tt>")  |  hexadecimal to decimal conversion
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;i" data="content&#93;</tt>")  |  HTML italics
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;if" data="**value** **match** content&#93;</tt>")  |  if match&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ifge" data="**value1&#44;****value2 &#44;**content&#93;</tt>")  |  if value1 &gt;= value2&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ifle" data="**value1&#44;****value2 &#44;**content&#93;</tt>")  |  if value1 &lt;= value2&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ifol" data="\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt>")  |  HTML ordered list IF &gt; one item
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;iful" data="\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt>")  |  HTML unordered list IF &gt; one item
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;img" data="\(imageTitle&#44;\)**imageURL** \(linkURL\)&#93;</tt>")  |  HTML image
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;inc" data="**value**&#93;</tt>")  |  add one to value
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;include" data="**fileName**&#93;</tt>")  |  include macro() source file
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;inter" data="**iStr&#44;****L&#124;R&#44;****value&#44;**content&#93;</tt>")  |  intersperse iStr every value in content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;isort" data="\(sep=X&#44;\)**listName**&#93;</tt>")  |  sort by leading integer&#44; sep defaults to &quot;&#44;&quot;
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;issort" data="content&#93;</tt>")  |  sort of lines by integer followed by a comma
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lb&#93;</tt>" data="")  |  left square bracket
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lc" data="content&#93;</tt>")  |  return length of content in lines
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lcc" data="**listOne&#44;****listTwo&#44;****listResult**&#93;</tt>")  |  list concatenate
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lcopy" data="**sourceList** **destinationList**&#93;</tt>")  |  copy list to new or existing list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;len" data="content&#93;</tt>")  |  return length of content in characters
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lf&#124;nl&#93;</tt>" data="")  |  new line
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lhsort" data="**listName**&#93;</tt>")  |  sort list by leading amateur radio callsign&#44;, any non-alphanumeric sep
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lipath" data="**pathToImages**&#93;</tt>")  |  path for &#91;locimg&#93;
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;list" data="\(sep=X&#44;\)**listname**&#44;itemContent\(XitemContent\)&#93;</tt>")  |  create or overwrite a list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ljust" data="**width&#44;****padChar&#44;**content&#93;</tt>")  |  left justify
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;llen" data="**listName**&#93;</tt>")  |  returns length of list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;local" data="**varname** varContent&#93;</tt>")  |  local variable definition
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;locimg" data="\(imageTitle&#44;\)**imageURL** \(linkURL\)&#93;</tt>")  |  HTML image, with size (uses &#91;lipath&#93;)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;locs" data="**stylename**\( styleParameters\)&#93;</tt>")  |  invoke local style
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lower" data="content&#93;</tt>")  |  convert to lowercase
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lpop" data="**listName&#44;**\(listIndex\)&#93;</tt>")  |  pop an item out of a list at top, or at listIndex
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lpush" data="**listName**&#44;itemContent&#93;</tt>")  |  append an item to a list (can create new list)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lset" data="**listName&#44;****listIndex&#44;**itemContent&#93;</tt>")  |  Set a list item
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lslice" data="**sliceSpec&#44;****listName&#44;****targetList**&#93;</tt>")  |  slice listName to targetList
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lsub" data="\(sep=X&#44;\)**listName&#44;**content&#93;</tt>")  |  list of form AsepB, A=B in content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ls&#93;</tt>" data="")  |  left squiggly bracket
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ltol" data="**listName** content&#93;</tt>")  |  convert lines of content to list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;lv" data="**varName**&#93;</tt>")  |  local variable
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;max" data="**value1** **value2**&#93;</tt>")  |  maximum of two numbers
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;min" data="**value1** **value2**&#93;</tt>")  |  minimum of two numbers
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;mode" data="**3.2&#124;4.01s**&#93;</tt>")  |  set HTML mode
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;mul" data="**value** **multiplier**&#93;</tt>")  |  multiply two numbers
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ne" data="**value&#44;**content&#93;</tt>")  |  if value is empty&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;odd" data="**value** content&#93;</tt>")  |  if value is odd&#44; then content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ol" data="\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt>")  |  HTML ordered list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ord" data="**character**&#93;</tt>")  |  return ASCII code value in decimal
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;otodec" data="**value**&#93;</tt>")  |  octal to decimal conversion
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;p" data="content&#93;</tt>")  |  HTML paragraph
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;parm" data="**value**&#93;</tt>")  |  returns results of &#91;split&#93;
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;pop&#93;</tt>" data="")  |  Pop an item off the top of the general stack
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;push" data="content&#93;</tt>")  |  Push an item on to the general stack
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;rb&#93;</tt>" data="")  |  right square bracket
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;repeat" data="**value&#44;**content&#93;</tt>")  |  repeat content&#44; evaluating content <i>each time</i>
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;replace" data="\(sep=X&#44;\)**targetXreplacementXcontent**&#93;</tt>")  |  target replaced with replacement in content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;resolve" data="**lable&#44;**content&#93;</tt>")  |  resolve reference
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;rjust" data="**width&#44;****padChar&#44;**content&#93;</tt>")  |  right justify
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;roman" data="**value**&#93;</tt>")  |  returns lower case roman numeral
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;row" data="\(options&#44;\)content&#93;</tt>")  |  HTML table row
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;rs&#93;</tt>" data="")  |  right squiggly bracket
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;s" data="**stylename**\( styleParameters\)&#93;</tt>")  |  invoke style&#44; local&#44; if no local&#44; then global
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;sisort" data="content&#93;</tt>")  |  case-insensitive sort of lines
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;slice" data="**sliceSpec&#44;content**&#93;</tt>")  |  slice content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;soundex" data="\(len=N&#44;\)content&#93;</tt>")  |  return soundex value of content
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;spage&#93;</tt>" data="")  |  reset local styles to <i>none</i>
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;split" data="**X&#44;**content\(Xcontent\)&#93;</tt>")  |  split for use with &#91;parm&#93;
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;splitcount" data="**value**&#93;</tt>")  |  Maximum number of splits to perform in next &#91;split&#93;
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;sp&#93;</tt>" data="")  |  space
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ssort" data="content&#93;</tt>")  |  case-sensitive sort of lines
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;strip" data="content&#93;</tt>")  |  strip HTML tags out
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;style" data="**styleName** **styleContent**&#93;</tt>")  |  local style
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;sub" data="**value** **subtrahend**&#93;</tt>")  |  subtract two numbers
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;sys" data="**shellCommand**&#93;</tt>")  |  invoke an operating system command. Output is captured
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;t" data="\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt>")  |  style wrap around item(s)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;table" data="\(options&#44;\)content&#93;</tt>")  |  HTML table
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;time&#93;</tt>" data="")  |  The time of macro() processing (use CGI for live time in HTML)
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;translate" data="**listName&#44;**content&#93;</tt>")  |  translate content using character map formatted list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;u" data="content&#93;</tt>")  |  HTML underline
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;ul" data="\(wrap=style&#44;\)\(sep=X&#44;\)itemContent\(XitemContent\)&#93;</tt>")  |  HTML unordered list
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;upper" data="content&#93;</tt>")  |  convert to uppercase
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;v" data="**varName**&#93;</tt>")  |  local/global variable
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;vs" data="**varName** varContent&#93;</tt>")  |  local variable definition
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;wc" data="content&#93;</tt>")  |  return length of content in words
  (Unknown Built-in or Squiggly:  tag="<tt>&#91;wwrap" data="\(wrap=style&#44;\)**value&#44;**content&#93;</tt>")  |  word wrap content at column value


