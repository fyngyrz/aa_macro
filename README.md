# [aa_macro.py](aa_macro.py) -- class macro()

This class provides a means for you to generate HTML using Python as
the intermediary engine.

The benefit is conceptually like markdown, but <tt>macro()</tt> is much, much
more powerful. It isn't meant to replace markdown, and cannot do so,
because markdown is built into so many things. For your own use,
however, <tt>macro()</tt> is a terrific solution to a very wide range of HTML
formatting tasks. You can do anything from format a simple paragraph to
generate a complete manual with indexes, table of contents, footnotes,
completely custom styles and more.

One of the reasons that <tt>macro()</tt> is more powerful is that although the
idea is similar in that it enables you to generate HTML easily and that
it can certainly be easily readable if used in the simple ways such as
one uses markdown, it does not embrace the idea that a text source file
should look like an unmarked file, or that functionality should be
sacrificed because complex functionality might not be as readable.

Consider: have you seen much markdown actually displayed as text?
Personally, I don't see that characteristic as valuable in and of
itself -- by far, based on how it is used, the more valuable characteristic is that it is *readable*, which
is not the same thing at all as "looks like unmarked text." You can
approach <tt>macro()</tt> the same way, aiming at the same types of markup,
and it'll be perfectly readable -- it just won't look like it is
unmarked.

Here are some comparisons relevant to markdown that demonstrate
the readability of basic markup:

Desired Result | Markdown | macro\(\)
-------------- | -------- | -------
Italics | <tt>\*verbiage\*</tt> | <tt>\[i verbiage\]</tt>
Bold | <tt>\*\*verbiage\*\*</tt> | <tt>\[b verbiage\]</tt>
Paragraph | <tt>verbiage</tt> | <tt>\[p verbiage\]</tt>
List | <tt>\* item1</tt><br><tt>\* item2</tt> | <tt>\[ul item1,item2\]</tt><br>or, if you prefer,<br><tt>\[ul</tt><br><tt>item1,</tt><br><tt>item2</tt><br><tt>\]</tt><br>

Use is trivial:

```python
from aa_macro import *
mod = macro()
textToProcess = '[b Boldly said]'	# [b contentToStyle] results in <b>contentToStyle</b>
processedText = mod.do(textToProcess)
```

That's really all there is to it.

Now I'll quickly introduce you to the concept of a style. You define a style by giving it a name,
and then filling it with... goodies. :) It has a *special* goodie, the <tt>[b]</tt> tag, which
fills in with the content you feed the style. Basically this is the idea:

    [style hello Why hello, [b], how are you?]

Which you use like this...

    {hello Ben}

...which would in turn result in:

    Why hello, Ben, how are you?

You can also pass multiple parameters; details on that are in the main documentation.

From here, we step into far more powerful (and interesting, I think)
areas of formatting and then some blatantly tricky use of styles as well.

I'll give one example (Okay, two examples, thanks a lot, Blake :metal:) here using several features;
but <tt>macro()</tt> offers a wide range of features beyond this, so don't
think for a moment that this in any way represents a limit on what you can do.

    [local chapter Introduction to the Work]
    [style h1 <h1>[v [b]]</h1>]
    
    {h1 chapter}

The first line sets a local variable named chapter to "Introduction to the Work"

The second line:

* creates a style that uses <tt>\[v \[b\]\]</tt> to produce the content of the variable
name which is provided as the body of the style.
* wraps that in <tt>&lt;h1&gt;</tt> and <tt>&lt;/h1&gt;</tt> tags

The third line invokes the style with the name of the variable.

This produces the following HTML:

    <h1>Introduction to the Work</h1>

The utility of such a thing is that first, the chapter name can now be referenced anywhere, and changed
at any time, because it is a variable (a local... globals are supported as well); while the h1 style shows
how you can wrap anything - in this case the content of the variable name passed in - in any other tags
or encodings you wish.

## A (much) more complex example

So, my friend looked at this readme, and he, in a fit of Perl-like cognition, says to me:

"...so rather than this: <tt>{h1 chapter}</tt> I'd like <tt>{h1 $chapter\}</tt>"

Personally, not my thing. However. Here's a style that distinguishes between <tt>$chapter</tt>
and <tt>chapter</tt>, treating the former as a variable name to resolve, and the latter as a literal (you can
break styles over multiple lines after the style name and/or within any content destined for output)...

<tt>[style v</tt>  
<tt>[if [slice :1,[b]] $ [v [slice 1:,[b]]]]</tt>  
<tt>[else [slice :1,[b]] $ [b]]]</tt>  

...so now you can do this...

<tt>{v chapter}</tt> which produces "chapter"  
...or this...  
<tt>{v $chapter}</tt> which produces "Introduction to the Work"

With style v in the can, so to speak, now we can write the h1 style this way:

    [style h1 <h1>{v [b]}</h1>]

So now to use h1 you could write:

<tt>{h1 $chapter}</tt> which would get you....

    <h1>Introduction to the Work</h1>
    
...as opposed to:

<tt>{h1 chapter}</tt> which gets you....

    <h1>chapter</h1>

And, now that you have the v style written, you can use it anywhere:

    [style italic [i {v [b]}]]
    
or, more concisely...

    [style i [i {v [b]}]]

...to be used like this (either style i or style italic work as of now):

<tt>{i chapter}</tt> which gets you "*chapter*"  
<tt>{i $chapter}</tt> which gets you "*Introduction to the Work*"  

Same friend: "So what if I want to feed in "$chapter" as a literal?"

One way is with an escape mechanism for $. Here's how to do
that using the HTML entity for "$":

    [style $ &#36;]
	{i {$}chapter}

## More

At the top of the class in the <tt>aa_macro.py</tt> file, all the various features are described. At the end
of the class, there are a series of examples that will execute if you simply type this at the command line:

    python aa_macro.py

Enjoy. :)
