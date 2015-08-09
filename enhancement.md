# Enhancing class `macro()`

Have an idea for a cool built-in? It can be very easy to do.

A minimum of two tasks are typically involved. This is the 'hard"
(cough) one:

 * In aa\_macro.py, search for the first occurance of `p_fn`
 * This is the "paragraph" built in. Look at it. All two lines of it.

```python
def p_fn(self,tag,data):
return '<p>'+data+'</p>'
```

 * Incoming parameter **self**: obvious, or if not, put it in yours anyway
 * Incoming parameter **tag**: the tag that got you here, in this case `p`
 * Incoming parameter **data**: everything to the right of `p` until the
closing `]`. In other words, if the input to macro.do\(\) is `[p foo bar]`,
then data = `foo bar`
 * Do something to the data. In this case, it wraps it with `<p></p>`
 * Return the result.

This is the easy one:

 * In aa\_macro.py, from the beginning or from `p_fn` search for `'p'`

```python
'p'     : self.p_fn,
```

 * That's an entry in a function table. :\)
 * In the table put the tag string (`'p'` in this case) See `p_fn` entry for howto.
The tag string must not contain spaces or newlines.
 * After the tag string, put a colon \( ':' \) See `p_fn` entry for howto.
 * Put the name of your function, preceded by `self.` See `p_fn` entry for howto.
 * Add a trailing comma

Lastly, the function table is broken up into functional groups for my
\(okay, and your\) convenience and no other reason. I would suggest that you
put your function in the most appropriate group just for sanity's sake,
but it's your barbecue, so whatever. Note that if you *don't* do so, but
I accept a patch because I like your idea, I'm going to move it if I think
it was poorly placed. :\)

Of course, if no group really matches what you're doing, and you don't
like the "misc" portion of the table, feel free to create a new section.

## A walk through the addition process

Suppose we want to be able to number a list with roman numerals. First
thing that might occur to you to ask is, well, uppercase roman numerals
or lowercase? My answer would be, clearly, it'd be nice to have both.
But two sets of code to generate them that way? Silly. So, the need for
case conversion arises, and we have our first target. Which we will
solve in about one minute, like this. First task, implement the actual
function:

```python
def upper_fn(self,tag,data):
    return data.upper()
```

Second task, add the function and its tag to the function table:

```python
    'upper'  : self.upper_fn,
```

Ok, that's done. But hey, while we're thinking this way, we should
certainly do this; first task, implement
the actual function:

```python
    def lower_fn(self,tag,data):
        return data.lower()
```

Second task, add the function and its tag to the function table:

```python
    'lower'  : self.lower_fn,
```

Now, we'll be able to do `[upper i]` and get `I` out. Or `[lower I]` and get
`i` out. Spiffy. It's almost too easy, isn't it? Sure. Well, making roman numerals
is a little more challenging.

As numbers are handled in the usual decimal fashion within `aa_macro()`, we'll
do all the work of producing, counting, etc. just as we usually would, and concentrate instead
on simply converting from decimal to roman. First task, the function:

```python
def roman_fn(self,tag,data):
    o = ''
    try:    number = int(data)
    except: pass
    else:
        if number > -1 and number < 4001:
            romans = ['m','cm','d','cd','c','xc','l','xl','x','ix','v','iv','i']
		    integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
            for v in range(0,13):
                ct = int(number / integers[v])
                o += romans[v] * ct
                number -= integers[v] * ct
	return o
```

Second task, add the function and its tag to the function table:

    'roman' : roman_fn,

Then we can do this:

feed in: `[roman 12]`  
results: `xii`  

And we can do this...

    [style uroman [upper [roman [b]]]]

feed in: `{uroman 4}`  
results: `IV`  

So, that's that, eh? \(Keeping in mind `macro()` can already count\)

Well, no. Shouldn't be, anyway. See, that algorithm runs every time we
convert a number. So it initializes those arrays every time, too. Naughty.
So let's put them in the class globally, so that they only get set up once
per object. This is super-simple. Just move them to the front of `macro()`,
in the `__init__()` function, like so...

    self.romans = ['m','cm','d','cd','c','xc','l','xl','x','ix','v','iv','i']
    self.integers = [1000,900,500,400,100,90,50,40,10,9,5,4,1]

...and then alter `roman_fn()` accordingly:

```python
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
```

So, great, right? One more thing... roman numerals look best in a monospaced, serif font,
because you need to be able to tell the difference between the letter L and the letter I.
Normally, that's what the &lt;tt&gt;&lt;/tt&gt; tags produce in HTML, assuming they
haven't been disrupted by CSS, so then we can just wrap the roman numerals in those tags.
If your CSS changes &lt;tt&gt; such that it uses a sans-serif font, then you would use either a &lt;font&gt; tag or an
appropriate CSS style instead (neither of which work in Github's markdown, by the way),
but for this walk-through, &lt;tt&gt; will do:

    [style roman <tt>[roman [b]]</tt>]
    [style uroman <tt>[upper [roman [b]]]</tt>]

Which allows:

feed in: `{roman 15}`  
results: &lt;tt&gt;xv&lt;tt&gt;  

feed in: `{uroman 17}`  
results: &lt;tt&gt;XVII&lt;tt&gt;  

Now we're cooking.

I guess now I have to go and add this to `macro()`, as it's pretty cool. But I assure you, it
wasn't in the class prior to my writing this little howto. But that's the process
in general, and as you can see, it's pretty open-ended. And fun.

# You should understand that:

Text is generally processed left to right and inside out based on bracketing.
For example:

    [p [i foo] [b bar] [u blurgh]]

Order of processing is: `i`, `b`, `u`, then `p` so internally, it goes through
the following stages in exactly this order:

    [p [i foo] [b bar] [u blurgh]]
    [p <i>foo</i> [b bar] [u blurgh]]
    [p <i>foo</i> <b>bar</b> [u blurgh]]
    [p <i>foo</i> <b>bar</b> <u>blurgh</u>]
    <p><i>foo</i> <b>bar</b> <u>blurgh</u></p>

Generally this won't bite you, especially in the case of a simple
tag similar to `b`, but if you try to do anything tricky where one
tag depends upon the result of another tag, make sure you have this
processing order firmly in mind.

There are some other, more complicated things in there, of course, and
I'd be no less than delighted if you added things of similar complexity.
In aid of this, you can ask me questions if you need to. My email address is in
aa_macro.py so it's pretty easy to do. I will answer any even remotely
reasonable question that isn't of the "how do I write Python" variety. I also
take interesting suggestions under consideration.

Thanks for taking a look at my macro() class. Time is the most valuable thing
we have. I truly appreciate you spending some of yours on this, and that
includes casual glances.

Cheers!

--Ben
