AA Macro
========

Note that () designate optional parameters, `a|b` designates alternate parameter `a` or `b`

Text Styling
------------

    [b bold text]
    [i italic text]
    [u underlined text]
    [color HEX3|HEX6 colored text]    # HEX3 example: f09 (which means FF0099) HEX6 example: fe7842

Linking
-------

    [web URL (text)]        # If you don't provide text, you get "On the web"
    [link URL (text)]       # If you don't provide text, you get the URL as the text

Images
------

    [img URL]

Lists
-----

    [ul item1(,item2,item3...)]         # where item1 can be wrap=STYLE
    [ol item1(,item2,item3...)]         # where item1 can be wrap=STYLE
    [iful item1(,item2,item3...)]       # where item1 can be wrap=STYLE
    [ifol item1(,item2,item3...)]       # where item1 can be wrap=STYLE
    [t item1(,item2,item3...)]          # where item1 may be wrap=STYLE

Tables
------

    [table (options,)CONTENT]           # HTML table
    [row (options,)CONTENT]             # table ROW
    [header (options,)CONTENT]          # table header cell
    [cell (options,)CONTENT]            # table cell

Variables
---------

    [local variableName value]      # define a variable in the local environment
    [vs variableName value]         # ditto - same as local
    [global variableName value]     # define a variable in the global environment
    [v variableName]                # use a variable (local, if not local, then global)
    [gv variableName]               # use the global variable and ignore the local
    [lv variableName]               # use the local variable and ignore the global
    [page]                          # reset local environment

Stack
-----

    [push (N,)CONTENT]      # push CONTENT N deep onto stack. 1 is the same as no N.
    [pop]                   # pop stack. If stack empty, does nothing.
    [fetch (N)]             # get element N from stack but no pop. 0 is top, no N = 0
    [flush]                 # toss out entire stack

Math
----

    [add value addend]                  # add a number to a number
    [sub value subtrahend]              # subtract a number from a number
    [mul value multiplier]              # multiply a number by a number
    [div value divisor]                 # divide a number by a number
    [inc value]                         # add one to a number
    [dec value]                         # subtract one from a number

Conditionals
------------

    [even value conditionalContent]       # use conditional content if value is even
    [odd value conditionalContent]        # use conditional content if value is odd
    [if value match conditionalContent]   # use conditional content if value == match
    [else value match conditionalContent] # use conditional content if value != match
    [ne value,conditionalContent]         # use conditional content if value Not Empty

Misc
----

    [repeat count content]                # repeat content count times

Escape Codes:
-------------

    [co]                                # produces HTML ',' as &#44;
    [sp]                                # produces HTML ' ' as &#32;
    [lb]                                # produces HTML '[' as &#91;
    [rb]                                # produces HTML ']' as &#93;
    [ls]                                # produces HTML '{' as &#123;
    [rs]                                # produces HTML '}' as &#125;

Styles
------

    [style styleName Style]             # Defines a local style. Use [b] for body of style (see [s] tag, next)
    [gstyle styleName]                  # Defines a global style. Use [b] for body of style (see [s] tag, next)
    [s styleName contentToStyle]        # contentToStyle goes where [b] tag(s) is/are in style...
    [glos styleName contentToStyle]     # contentToStyle goes where [b] tag(s) is/are in style...
    [locs styleName contentToStyle]     # contentToStyle goes where [b] tag(s) is/are in style...
    {styleName contentToStyle}          # ...same thing, but simplified "squiggly" syntax

More on styles:
---------------

Styles give you ultimate power in creating your own text processing tool.

Styles are pretty easy to understand. You can have as many as you want, and they
can contain other styles, presets and so on. There are two components to styles;
defining them, and using them.

Here's a simple style definition:

    +-- DEFINE a style
    |     +-- name of style
    |     |      +-- beginning of style
    |     |      |       +-- where the body of the style will go
    |     |      |       |  +-- rest of pre-defined style
    |     |      |       |  |       +-- end of style
    |     |      |       |  |       |
    [style strike <strike>[b]</strike>]

So now to use that, you do this:

    +-- USE a style
    | +-- name of style to use
    | |      +-- the body that goes where the [b] tag(s) is/are in the style
    | |      |
    [s strike me out]

Which will come out of object.do() as:

    <strike>me out</strike>

You can nest more or less indefinitely:

    [b bold text [s strike [i bold and italic text]]]

### The Rules:

- Do not attempt to define one style inside another.
- repeat gets a number or a variable parameter. Nothing else. No nesting in the parameter!
(but you can use anything in what you want it to repeat)
- Give me a space or a newline. One space or newline only, Vasily.
Between the tag and any parameters, that is
- observe the format for tags. Some require spaces, some commas, to separate items.
or suffer the consequences, which will be aborted macros. :)
FYI: Generally commas are used for variable numbers of parameters.
- You can use [co] for literal commas, likewise `[lb]` `[rb]` `[ls]` and `[rs]` for literal braces.

