 
# Macro() Quick Reference
## Functional Groupings


**key:** built-in \(options\) required content



HTML Text Styling | &nbsp;
----------------- | ----
 &#91;p content&#93; |  HTML paragraph
 &#91;bq content&#93; |  HTML blockquote
 &#91;b content&#93; |  HTML bold
 &#91;i content&#93; |  HTML italics
 &#91;u content&#93; |  HTML underline
 &#91;color HEX3&#124;HEX6 content&#93; |  HTML text color

HTML Linking | &nbsp;
------------ | ----
 &#91;a \(tab&#44;\)URL\(&#44;linkedContent\)&#93; |  HTML link

HTML Images | &nbsp;
----------- | ----
 &#91;img \(imageTitle&#44;\)imageURL \(linkURL\)&#93; |  HTML image
 &#91;locimg \(imageTitle&#44;\)imageURL \(linkURL\)&#93; |  HTML image, with size (uses &#91;lipath&#93;)
 &#91;lipath pathToImages&#93; |  path for &#91;locimg&#93;

HTML Lists | &nbsp;
---------- | ----
 &#91;ul \(wrap=style&#44;\(sep=X&#44;\)\)itemContent\(XitemContent\)&#93; |  HTML unordered list
 &#91;ol \(wrap=style&#44;\(sep=X&#44;\)\)itemContent\(XitemContent\)&#93; |  HTML ordered list
 &#91;iful \(wrap=style&#44;\(sep=X&#44;\)\)itemContent\(XitemContent\)&#93; |  HTML unordered list IF &gt; one item
 &#91;ifol \(wrap=style&#44;\(sep=X&#44;\)\)itemContent\(XitemContent\)&#93; |  HTML ordered list IF &gt; one item
 &#91;t \(wrap=style&#44;\(sep=X&#44;\)\)itemContent\(XitemContent\)&#93; |  style wrap around item(s)

HTML Tables | &nbsp;
----------- | ----
 &#91;table \(options&#44;\)content&#93; |  HTML table
 &#91;row \(options&#44;\)content&#93; |  HTML table row
 &#91;header \(options&#44;\)content&#93; |  HTML table header cell
 &#91;cell \(options&#44;\)content&#93; |  HTML table data cell

Variables | &nbsp;
--------- | ----
 &#91;local varname varContent&#93; |  local variable definition
 &#91;vs varName varContent&#93; |  local variable definition
 &#91;global varName varContent&#93; |  global variable definition
 &#91;v varName&#93; |  local/global variable
 &#91;gv varName&#93; |  global variable
 &#91;lv varName&#93; |  local variable

Data Lists | &nbsp;
---------- | ----
 &#91;list \(sep=X&#44;\)listname&#44;itemContent\(XitemContent\)&#93; |  create or overwrite a list
 &#91;lcopy sourceList destinationList&#93; |  copy list to new or existing list
 &#91;ltol listName content&#93; |  convert lines of content to list
 &#91;append listName&#44;itemContent&#93; |  append an item to a list (can create new list)
 &#91;lpush listName&#44;itemContent&#93; |  append an item to a list (can create new list)
 &#91;lpop listName&#44;\(listIndex\)&#93; |  pop an item out of a list at top, or at listIndex
 &#91;lset listName&#44;listIndex&#44;itemContent&#93; |  Set a list item
 &#91;llen listName&#93; |  returns length of list
 &#91;lslice sliceSpec&#44;listName&#44;targetList&#93; |  slice listName to targetList
 &#91;dlist \(wrap=styleName&#44;\)\(parms=PRE&#44;\)\(posts=PST&#44;\)listName&#93; |  dump a list
 &#91;e listName&#44;listIndex&#93; |  output item from list of length n (listIndex = 0 to n-1)
 &#91;lcc listOne&#44;listTwo&#44;listResult&#93; |  list concatenate
 &#91;lsub \(sep=X&#44;\)listName&#44;content&#93; |  list of form AsepB, A=B in content
 &#91;asort listName&#93; |  ASCII alphabetic sort of list&#44; in place
 &#91;aisort listName&#93; |  ASCII case-insensitive sofr of list&#44; in place
 &#91;isort \(sep=X&#44;\)listName&#93; |  sort by leading integer&#44; sep defaults to &quot;&#44;&quot;
 &#91;lhsort listName&#93; |  sort list by leading amateur radio callsign&#44;, any non-alphanumeric sep
 &#91;cmap listName&#93; |  create 1:1 character map
 &#91;translate listName&#44;content&#93; |  translate content using character map formatted list

Data Dictionaries | &nbsp;
----------------- | ----
 &#91;dict \(sep=X&#44;\)\(keysep=Y&#44;\)dictName&#44;keyYvalue\(XkeyYvalue\)&#93; |  create/replace dictionary
 &#91;dcopy sourceDictionary&#44;destinationDictionary&#93; |  copy/replace destination with source
 &#91;dkeys sourceDictionary&#44;destinationList&#93; |  create a <b>list</b> of keys from source
 &#91;dset \(keysep=Y&#44;\)dictName&#44;keyYvalue&#93; |  create/replace dictionary item
 &#91;d dictName&#44;key&#93; |  retrieve a dictionary value using key

General Stack | &nbsp;
------------- | ----
 &#91;push content&#93; |  Push an item on to the general stack
 &#91;pop&#93; |  Pop an item off the top of the general stack
 &#91;fetch itemIndex&#93; |  fetch any item from stack - 0 is top of stack
 &#91;flush&#93; |  delete stack contents

Math | &nbsp;
---- | ----
 &#91;add value addend&#93; |  add two numbers
 &#91;sub value subtrahend&#93; |  subtract two numbers
 &#91;mul value multiplier&#93; |  multiply two numbers
 &#91;div value divisor&#93; |  divide two numbers
 &#91;max value1 value2&#93; |  maximum of two numbers
 &#91;min value1 value2&#93; |  minimum of two numbers
 &#91;inc value&#93; |  add one to value
 &#91;dec value&#93; |  subtract one from value

Conditional Content | &nbsp;
------------------- | ----
 &#91;even value content&#93; |  if value is even&#44; then content
 &#91;odd value content&#93; |  if value is odd&#44; then content
 &#91;if value match content&#93; |  if match&#44; then content
 &#91;else value match content&#93; |  if <b>not</b> match&#44; then content
 &#91;ne value&#44;content&#93; |  if value is empty&#44; then content
 &#91;eq value&#44;content&#93; |  if value is <b>not</b> empty&#44; then content
 &#91;ifle value1&#44;value2 &#44;content&#93; |  if value1 &lt;= value2&#44; then content
 &#91;ifge value1&#44;value2 &#44;content&#93; |  if value1 &gt;= value2&#44; then content

Text Processing | &nbsp;
--------------- | ----
 &#91;slice sliceSpec&#44;content&#93; |  slice content
 &#91;splitcount value&#93; |  Maximum number of splits to perform in next &#91;split&#93;
 &#91;split X&#44;content\(Xcontent\)&#93; |  split for use with &#91;parm&#93;
 &#91;parm value&#93; |  returns results of &#91;split&#93;
 &#91;upper content&#93; |  convert to uppercase
 &#91;lower content&#93; |  convert to lowercase
 &#91;soundex \(len=N&#44;\)content&#93; |  return soundex value of content
 &#91;strip content&#93; |  strip HTML tags out
 &#91;roman value&#93; |  returns lower case roman numeral
 &#91;dtohex value&#93; |  decimal to hexadecimal conversion
 &#91;dtooct value&#93; |  decimal to octal conversion
 &#91;dtobin value&#93; |  decimal to binary conversion
 &#91;htodec value&#93; |  hexadecimal to decimal conversion
 &#91;otodec value&#93; |  octal to decimal conversion
 &#91;btodec value&#93; |  binary to decimal conversion
 &#91;wwrap \(wrap=style&#44;\)value&#44;content&#93; |  word wrap content at column value
 &#91;len content&#93; |  return length of content in characters
 &#91;wc content&#93; |  return length of content in words
 &#91;lc content&#93; |  return length of content in lines
 &#91;chr value&#93; |  return ASCII character of code=value
 &#91;ord character&#93; |  return ASCII code value in decimal
 &#91;csep value&#93; |  comma-separate an integer
 &#91;fcsep value&#93; |  comma-separate a floating point number
 &#91;dup value&#44;content&#93; |  duplicate content <i>after</i> evaluation (also see &#91;repeat&#93;)
 &#91;find \(sep=X&#44;\)stringXcontent&#93; |  find string in content&#44; sep default = &quot;&#44;&quot;
 &#91;replace \(sep=X&#44;\)targetXreplacementXcontent&#93; |  target replaced with replacement in content
 &#91;count \(sep=X&#44;\)\(overlaps=yes&#44;\)\(casesens=yes&#44;\)patternXcontent&#93; |  count incidences
 &#91;caps content&#93; |  sentence case
 &#91;capw content&#93; |  word case
 &#91;capt content&#93; |  title case
 &#91;expand dictName&#44;content&#93; |  dictionary based keyword expansion with leading cap forwarding
 &#91;ssort content&#93; |  case-sensitive sort of lines
 &#91;sisort content&#93; |  case-insensitive sort of lines
 &#91;issort content&#93; |  sort of lines by integer followed by a comma
 &#91;hsort content&#93; |  sort of lines by amatuer radio callsign followed by non-alphanumeric
 &#91;inter iStr&#44;L&#124;R&#44;value&#44;content&#93; |  intersperse iStr every value in content
 &#91;rjust width&#44;padChar&#44;content&#93; |  right justify
 &#91;ljust width&#44;padChar&#44;content&#93; |  left justify
 &#91;center width&#44;padChar&#44;content&#93; |  center (neg width indicates pad both sides)

Miscellanea | &nbsp;
----------- | ----
 &#91;sys shellCommand&#93; |  invoke an operating system command. Output is captured
 &#91;date&#93; |  The date of macro() processing (use CGI for live date in HTML)
 &#91;time&#93; |  The time of macro() processing (use CGI for live time in HTML)
 &#91;include fileName&#93; |  include macro() source file
 &#91;embrace moduleName&#93; |  add&#44; extend&#44; or replace macro() functionality
 &#91;repeat value&#44;content&#93; |  repeat content&#44; evaluating content <i>each time</i>
 &#91;comment content&#93; |  suppress output. <i>note: non-content operations still process</i>
 &#91;back HEX3&#124;HEX6&#93; |  HTML background text color for HTML 4.01s mode <i>only</i>
 &#91;mode 3.2&#124;4.01s&#93; |  set HTML mode

Escapes | &nbsp;
------- | ----
 &#91;co&#93; |  comma
 &#91;sp&#93; |  space
 &#91;lb&#93; |  left square bracket
 &#91;rb&#93; |  right square bracket
 &#91;ls&#93; |  left squiggly bracket
 &#91;rs&#93; |  right squiggly bracket
 &#91;lf&#124;nl&#93; |  new line

Styles | &nbsp;
------ | ----
 &#91;style styleName styleContent&#93; |  local style
 &#91;gstyle styleName styleContent&#93; |  global style
 &#91;s stylename\(styleParameters\)&#93; |  invoke style&#44; local&#44; if no local&#44; then global
 &#91;glos stylename\(styleParameters\)&#93; |  invoke global style
 &#91;locs stylename\(styleParameters\)&#93; |  invoke local style
 &#91;spage&#93; |  reset local styles to <i>none</i>
 &#91;ghost \(source=global&#124;local&#44;\)stylename&#93; |  output style without processing it
 &#91;fref lable&#93; |  forward (or backward) reference
 &#91;resolve lable&#44;content&#93; |  resolve reference


## Alphabetical Order

**key:** built-in \(options\) required content


&#91;a \(tab&#44;\)URL\(&#44;linkedContent\)&#93; |  HTML link
&#91;add value addend&#93; |  add two numbers
&#91;aisort listName&#93; |  ASCII case-insensitive sofr of list&#44; in place
&#91;append listName&#44;itemContent&#93; |  append an item to a list (can create new list)
&#91;asort listName&#93; |  ASCII alphabetic sort of list&#44; in place
&#91;b content&#93; |  HTML bold
&#91;back HEX3&#124;HEX6&#93; |  HTML background text color for HTML 4.01s mode <i>only</i>
&#91;bq content&#93; |  HTML blockquote
&#91;btodec value&#93; |  binary to decimal conversion
&#91;caps content&#93; |  sentence case
&#91;capt content&#93; |  title case
&#91;capw content&#93; |  word case
&#91;cell \(options&#44;\)content&#93; |  HTML table data cell
&#91;center width&#44;padChar&#44;content&#93; |  center (neg width indicates pad both sides)
&#91;chr value&#93; |  return ASCII character of code=value
&#91;cmap listName&#93; |  create 1:1 character map
&#91;color HEX3&#124;HEX6 content&#93; |  HTML text color
&#91;comment content&#93; |  suppress output. <i>note: non-content operations still process</i>
&#91;count \(sep=X&#44;\)\(overlaps=yes&#44;\)\(casesens=yes&#44;\)patternXcontent&#93; |  count incidences
&#91;co&#93; |  comma
&#91;csep value&#93; |  comma-separate an integer
&#91;d dictName&#44;key&#93; |  retrieve a dictionary value using key
&#91;date&#93; |  The date of macro() processing (use CGI for live date in HTML)
&#91;dcopy sourceDictionary&#44;destinationDictionary&#93; |  copy/replace destination with source
&#91;dec value&#93; |  subtract one from value
&#91;dict \(sep=X&#44;\)\(keysep=Y&#44;\)dictName&#44;keyYvalue\(XkeyYvalue\)&#93; |  create/replace dictionary
&#91;div value divisor&#93; |  divide two numbers
&#91;dkeys sourceDictionary&#44;destinationList&#93; |  create a <b>list</b> of keys from source
&#91;dlist \(wrap=styleName&#44;\)\(parms=PRE&#44;\)\(posts=PST&#44;\)listName&#93; |  dump a list
&#91;dset \(keysep=Y&#44;\)dictName&#44;keyYvalue&#93; |  create/replace dictionary item
&#91;dtobin value&#93; |  decimal to binary conversion
&#91;dtohex value&#93; |  decimal to hexadecimal conversion
&#91;dtooct value&#93; |  decimal to octal conversion
&#91;dup value&#44;content&#93; |  duplicate content <i>after</i> evaluation (also see &#91;repeat&#93;)
&#91;e listName&#44;listIndex&#93; |  output item from list of length n (listIndex = 0 to n-1)
&#91;else value match content&#93; |  if <b>not</b> match&#44; then content
&#91;embrace moduleName&#93; |  add&#44; extend&#44; or replace macro() functionality
&#91;eq value&#44;content&#93; |  if value is <b>not</b> empty&#44; then content
&#91;even value content&#93; |  if value is even&#44; then content
&#91;expand dictName&#44;content&#93; |  dictionary based keyword expansion with leading cap forwarding
&#91;fcsep value&#93; |  comma-separate a floating point number
&#91;fetch itemIndex&#93; |  fetch any item from stack - 0 is top of stack
&#91;find \(sep=X&#44;\)stringXcontent&#93; |  find string in content&#44; sep default = &quot;&#44;&quot;
&#91;flush&#93; |  delete stack contents
&#91;fref lable&#93; |  forward (or backward) reference
&#91;ghost \(source=global&#124;local&#44;\)stylename&#93; |  output style without processing it
&#91;global varName varContent&#93; |  global variable definition
&#91;glos stylename\(styleParameters\)&#93; |  invoke global style
&#91;gstyle styleName styleContent&#93; |  global style
&#91;gv varName&#93; |  global variable
&#91;header \(options&#44;\)content&#93; |  HTML table header cell
&#91;hsort content&#93; |  sort of lines by amatuer radio callsign followed by non-alphanumeric
&#91;htodec value&#93; |  hexadecimal to decimal conversion
&#91;i content&#93; |  HTML italics
&#91;if value match content&#93; |  if match&#44; then content
&#91;ifge value1&#44;value2 &#44;content&#93; |  if value1 &gt;= value2&#44; then content
&#91;ifle value1&#44;value2 &#44;content&#93; |  if value1 &lt;= value2&#44; then content
&#91;ifol \(wrap=style&#44;\(sep=X&#44;\)\)itemContent\(XitemContent\)&#93; |  HTML ordered list IF &gt; one item
&#91;iful \(wrap=style&#44;\(sep=X&#44;\)\)itemContent\(XitemContent\)&#93; |  HTML unordered list IF &gt; one item
&#91;img \(imageTitle&#44;\)imageURL \(linkURL\)&#93; |  HTML image
&#91;inc value&#93; |  add one to value
&#91;include fileName&#93; |  include macro() source file
&#91;inter iStr&#44;L&#124;R&#44;value&#44;content&#93; |  intersperse iStr every value in content
&#91;isort \(sep=X&#44;\)listName&#93; |  sort by leading integer&#44; sep defaults to &quot;&#44;&quot;
&#91;issort content&#93; |  sort of lines by integer followed by a comma
&#91;lb&#93; |  left square bracket
&#91;lc content&#93; |  return length of content in lines
&#91;lcc listOne&#44;listTwo&#44;listResult&#93; |  list concatenate
&#91;lcopy sourceList destinationList&#93; |  copy list to new or existing list
&#91;len content&#93; |  return length of content in characters
&#91;lf&#124;nl&#93; |  new line
&#91;lhsort listName&#93; |  sort list by leading amateur radio callsign&#44;, any non-alphanumeric sep
&#91;lipath pathToImages&#93; |  path for &#91;locimg&#93;
&#91;list \(sep=X&#44;\)listname&#44;itemContent\(XitemContent\)&#93; |  create or overwrite a list
&#91;ljust width&#44;padChar&#44;content&#93; |  left justify
&#91;llen listName&#93; |  returns length of list
&#91;local varname varContent&#93; |  local variable definition
&#91;locimg \(imageTitle&#44;\)imageURL \(linkURL\)&#93; |  HTML image, with size (uses &#91;lipath&#93;)
&#91;locs stylename\(styleParameters\)&#93; |  invoke local style
&#91;lower content&#93; |  convert to lowercase
&#91;lpop listName&#44;\(listIndex\)&#93; |  pop an item out of a list at top, or at listIndex
&#91;lpush listName&#44;itemContent&#93; |  append an item to a list (can create new list)
&#91;lset listName&#44;listIndex&#44;itemContent&#93; |  Set a list item
&#91;lslice sliceSpec&#44;listName&#44;targetList&#93; |  slice listName to targetList
&#91;lsub \(sep=X&#44;\)listName&#44;content&#93; |  list of form AsepB, A=B in content
&#91;ls&#93; |  left squiggly bracket
&#91;ltol listName content&#93; |  convert lines of content to list
&#91;lv varName&#93; |  local variable
&#91;max value1 value2&#93; |  maximum of two numbers
&#91;min value1 value2&#93; |  minimum of two numbers
&#91;mode 3.2&#124;4.01s&#93; |  set HTML mode
&#91;mul value multiplier&#93; |  multiply two numbers
&#91;ne value&#44;content&#93; |  if value is empty&#44; then content
&#91;odd value content&#93; |  if value is odd&#44; then content
&#91;ol \(wrap=style&#44;\(sep=X&#44;\)\)itemContent\(XitemContent\)&#93; |  HTML ordered list
&#91;ord character&#93; |  return ASCII code value in decimal
&#91;otodec value&#93; |  octal to decimal conversion
&#91;p content&#93; |  HTML paragraph
&#91;parm value&#93; |  returns results of &#91;split&#93;
&#91;pop&#93; |  Pop an item off the top of the general stack
&#91;push content&#93; |  Push an item on to the general stack
&#91;rb&#93; |  right square bracket
&#91;repeat value&#44;content&#93; |  repeat content&#44; evaluating content <i>each time</i>
&#91;replace \(sep=X&#44;\)targetXreplacementXcontent&#93; |  target replaced with replacement in content
&#91;resolve lable&#44;content&#93; |  resolve reference
&#91;rjust width&#44;padChar&#44;content&#93; |  right justify
&#91;roman value&#93; |  returns lower case roman numeral
&#91;row \(options&#44;\)content&#93; |  HTML table row
&#91;rs&#93; |  right squiggly bracket
&#91;s stylename\(styleParameters\)&#93; |  invoke style&#44; local&#44; if no local&#44; then global
&#91;sisort content&#93; |  case-insensitive sort of lines
&#91;slice sliceSpec&#44;content&#93; |  slice content
&#91;soundex \(len=N&#44;\)content&#93; |  return soundex value of content
&#91;spage&#93; |  reset local styles to <i>none</i>
&#91;split X&#44;content\(Xcontent\)&#93; |  split for use with &#91;parm&#93;
&#91;splitcount value&#93; |  Maximum number of splits to perform in next &#91;split&#93;
&#91;sp&#93; |  space
&#91;ssort content&#93; |  case-sensitive sort of lines
&#91;strip content&#93; |  strip HTML tags out
&#91;style styleName styleContent&#93; |  local style
&#91;sub value subtrahend&#93; |  subtract two numbers
&#91;sys shellCommand&#93; |  invoke an operating system command. Output is captured
&#91;t \(wrap=style&#44;\(sep=X&#44;\)\)itemContent\(XitemContent\)&#93; |  style wrap around item(s)
&#91;table \(options&#44;\)content&#93; |  HTML table
&#91;time&#93; |  The time of macro() processing (use CGI for live time in HTML)
&#91;translate listName&#44;content&#93; |  translate content using character map formatted list
&#91;u content&#93; |  HTML underline
&#91;ul \(wrap=style&#44;\(sep=X&#44;\)\)itemContent\(XitemContent\)&#93; |  HTML unordered list
&#91;upper content&#93; |  convert to uppercase
&#91;v varName&#93; |  local/global variable
&#91;vs varName varContent&#93; |  local variable definition
&#91;wc content&#93; |  return length of content in words
&#91;wwrap \(wrap=style&#44;\)value&#44;content&#93; |  word wrap content at column value


