# Markdown-to-macro() Filter

## Paragraphs, escapes, empty parens

Might be nice to be able to take a file that's been written in markdown format
and output it as compatible source for macro()

This would allow someone who has previously created some number of documents
to convert them easily, while making available to them the many advantages
that macro() has to offer. \(This is not a link\) and \[I am not square\]

Linking
=======

This line has a link next [My Link](http://fyngyrz.com) and then more text.

### Sort-of linking: Images

Whereas this line has an image next ![My Image](http://fyngyrz.com/images/beachflag.png) and then additional text

### Raw URL

And this is a raw url http://datapipe-blackbeltsystems.com right back there

## Emphasis

Here comes **some bold text** and then *italic text* followed
by some more __bold text__ and another bit of _italic text_.
Which, not being modest, we will follow with some **bold _and italic_ text**
and in fact, we'll **do it _twice_.** And then **_there is this,_** quite seriously.
Now we'll **break across
two lines** and _then do
it again_ as we are just that kind of line-breaker.

## Lists

Unordered:

* single level
* very simple
* hopefully, anyway

Ordered:

1) one
2) dos
3) III

Unordered with unordered sublist

* line one
* line two
  * subline 1
  * subline 2
* line three

## Code

### Fenced code:

```
 org $0100
toport lda 0,x++
 sta >ioport
 bne toport
 rts
```

Now for some HTML fenced code:

```
<p>
paragraph content goes here
</p>
```

### In-line code:

Here is some code: `macro()` and that's the end of it,
or at least, hopefully.

This stuff has tags: `<pre>foo</pre>`

### Four-space indent code:

This is not indented four spaces.
Neither is this

    But this is
    as is this
    and this

But not this.

## Tables

header 1 | header two
-------- | ----------
cell a | cell B
cell III | cell quatro
