# aa_macro

No to-dos at this time.

Stable, occasionally receiving additional built-ins as the need arises.

# Markdown-to-macro\(\) Filter

Under development. Aiming primarily at github extensions and standard markdown

### To Do for Github's extensions:

Generally complete to description at (Github's Cheatsheet)[https://enterprise.github.com/downloads/en/markdown-cheatsheet.pdf]

## To Do for standard markdown processing

* markdown doesn't specify image sizes, but we COULD if we can find them
* hrules: `--- - - - *** * * * ___ _ _ _`
* `&quot;` should be untouched! don't entity-up amps in entities, but otherwise, do
* <> only converted if not as a tag or thrown out in link-link syntax
* `*` or `_` surround by spaces are literal
* On header lines, all closing # must be stripped
* Blockquotes can be nested (ugh)
* \`\`-defined code spans
* Literal backticks are allowed in \`\`-defined code spans
* angle-links:
  *	`<URL>` -- `<a href="URL">URL</a>` ... also works for email addresses
* email entity encoding to fool some spambots
*reference-style links:
  * [text][id] or [text] [id]   <<< that's how you USE em
  * [id][]                          or implicit notation uses id for text
  * [id]: URL "optional title" <<< that's how you DEFINE them
    * link may be surrounded by optional <>
    * optional indent may be up to three spaces
    * single quotes, double quotes, or parens for title
    * these occur on single lines, or, title can be on next line
* reference-style images:
  * ![alt/title text][id]     <<< USE
  * [id]: URL 
* lists can use \* OR \+ OR \-
* markdown uses 1\. NOT 1\)
* lists are valid with up to three spaces of indent
* code blocks supported within list items
  * (done by indenting 8sp or 2t)
* blockquotes supported inside list items
  * (done by indenting after list item 4sp or 1t)
* paragraphs supported within list items
  * (done by separating list items with a blank line,
  * then indenting four space to start new paras)

## Github markdown processing

### Done:

* code
* fenced code blocks
* four-leading-space code lines
* tables

### To do:

* task lists

### Punting unless use *on* Gitub seems possible:

* username mentions \(Only useful as stands on Github\)
* issue references \(Only useful on stands Github\)

#### Alternate Filter for Github?

Be nice if, when this is all said and done, I could have macro\(\) accepted
as one of Github's supported filters. Somehow I doubt it, as they really
lock down their HTML, but you never know.
