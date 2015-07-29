# Enhancing class macro()

Have an idea for a cool built-in? It can be very easy to do.

A minimmum of two tasks are typically involved. This is the 'hard"
(cough) one:

1. In aa\_macro.py, search for the first occurance of `p_fn`
2. This is the "paragraph" built in. Look at it. All two lines.
```python
    def p_fn(self,tag,data):
        return '<p>'+data+'</p>'
```
3. Incoming parameter self: obvious, or if not, put it in yours anyway
4. Incoming parameter tag: the tag that got you here, in this case `p`
5. Incoming parameter data: everything to the right of `p` until the
   closing `]`. In other words, if the input to macro() is `[p foo bar]`,
   then data = `foo bar`
6. Do something to the data. In this case, it wraps it with `<p></p>`
7. Return the result.

This is the easy one:

1. In aa\_macro.py, from the beginning or from `p_fn`search for `'p'`
```python
    'p'     : self.p_fn,
```
2. That's an entry in a function table. :\)
3. In the table put the tag string (`'p'` in this case) See `p_fn` entry for howto.
The tag string must not contain spaces or newlines.
4. After the tag string, put a colon \( ':' \) See `p_fn` entry for howto.
5. Put the name of your function, preceded by `self.` See `p_fn` entry for howto.
6. Add a trailing comma

Lastly, the function table is broken up into functional groups for my
\(okay, and your\) convenience and no other reason. I would suggest that you
put your function in the most appropriate group just for sanity's sake,
but it's your barbecue, so whatever. Note that if you *don't* do so, but
I accept a patch because I like your idea, I'm going to move it if I think
it was poorly placed. :\)

Of course, if no group really matches what you're doing, and you don't
like the "misc" portion of the table, feel free to create a new section.

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

Thanks for considering my macro() class. Time is the most valuable thing
we have. I truly appreciate you spending some of yours on this, and that
includes casual glances.

Cheers!

--Ben
