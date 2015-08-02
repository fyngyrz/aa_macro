# To-do

## Markdown-to-macro() Filter

Under development

### Done:

* headers
* images
* formatted links
* unformatted links
* blockquotes
* paragraphs
* line breaks
* markdown escapes
* emphasis: `*`, `**`, `_`, `__`
* lists
  * ordered
  * unordered
    * sub 1
    * sub 2
      * subsub 1
      * subsub 2

### To Do:

Generally complete to description at (Github's Cheatsheet)[https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf)

## Future: re-definition of escapes and "putbacks"

To allow special characters to be used via escapes, then to restore them
at the output stage so that HTML entities are *not* used. This, in
combination with styles, will expand the system beyond the limits of
HTML processing into general text processing quite handily.

## Github markdown processing

### Done:

* code
* fenced code blocks
* four-leading-space code lines

### To do:

* tables
* task lists

### Punting unless use *on* Gitub seems possible:

* username mentions \(Only useful as stands on Github\)
* issue references \(Only useful on stands Github\)

#### Alternate Filter for Github?

Be nice if, when this is all said and done, I could have macro\(\) accepted
as one of Github's supported filters. Somehow I doubt it, as they really
lock down their HTML, but you never know.
