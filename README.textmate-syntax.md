# Textmate \(and presumably Github\) compatible syntax definition

[textmate-syntax.txt](textmate-syntax.txt) is what you need to
put in a Textmate bundle in order to display `macro()` source
with syntax highlighting.

Keep in mind that what this does is set up some of textmate's
pre-defined classes to go along with `macro()` syntax; the coloring
itself is matched to those classes in Textmate's preferences,
under "Fonts and Colors."

Here's how I have mine set up:

![Textmate Syntax](textmate-syntax.png)

## Environment

These are the circumstances under which I developed this syntax file:

<tt>OS X 10.6.8, Mac Pro Dual Xeon 8-core, Textmate Version 1.5.11 (1635)</tt>

Note there are later versions of both Textmate and OS X, and using those may require
some additional work.

Sadly, Apple broke the Mac operating system so badly as of OS X 10.9 that Textmate 1.x will no longer work, so your only option there is to go with 2.x. Gotta love Apple, charging directly into the future &mdash;
right over your software investment. Sheesh.
