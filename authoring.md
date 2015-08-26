# Authoring in Macro\(\)

This is a collection of ideas and approaches that may be interesting with
regard to authoring using `Macro()`.

## Style definition

### Making a Style Definition Disappear Completely

It aids clarity to place each style on its own line. However,
conceptually, the newline at the end of the line is *outside*
the style, and so ends up in the resulting output. The way to
avoid this is to add two spaces to the end of any line that
closes a style definition. `macro()` will see this and "eat"
both the two spaces and the subsequent newline.

### Defining Styles Over Multiple Lines

You can define a style over multiple lines by placing two spaces at the
end of each line. Here's a fun use of styles, where one of the styles is 
built over four lines for clarity, with interspersed lines used to
separate the styles and content. The interspersed lines are simply two
spaces and a newline; consequently, they are stripped out so they make
perfect spacers.

This is a set of styles that provides a way to created ordered lists
with reference labels. The reason to do this is that later
back-references to the list will always be to the correctly numbered
item in the list, even if you add other items later.

Style | Function
----- | --------
\{oostyle\} | the list style, in this case number, colon, space, item.
\{oo\} | instantiates the list, setting the list ordinal to zero.
\{oi\} | manages the numbering and association with the item lable.
\{oref\} | emplaces the actual number of the lable-referenced list item.

```
[style oo [local lcount 0]]  
  
[style oostyle [v lcount]: [b]]  
  
[style oi [local lcount [add [v lcount] 1]]  
[splitcount 1][split [co],[b]]  
[dset lmem,[parm 0]:[v lcount]]  
{oostyle [parm 1]}]  
  
[style oref #[d lmem,[b]]]  
  
Foodieness

{oo}
{oi nut,line of nuttiness}
{oi fruit,fruity line}
{oi rock,stone-age line}

Referring to item {oref fruit}, I prefer cherries.
```

The output of the above is:

```
Foodiness

1: line of nuttiness
2: fruity line
3: stone-age line

Referring to item #2, I prefer cherries.
```

This type of list generation also allows list splitting around content,
as the list context does not end until the next list is instantiated.

```
Foodiness

{oo}
{oi nut,line of nuttiness}
{oi fruit,fruity line}
{oi rock,stone-age line}

Referring to item {oref fruit}, I prefer cherries. However...

{oi spag,spaghetti}
{oi shel,shells}
{oi ling,linguini}

...when it comes to pasta, I prefer {oref lconv} over the others.
```

The output of that is:

```
Foodiness

1: line of nuttiness
2: fruity line
3: stone-age line

Referring to item #2, I prefer cherries. However...

4: spaghetti
5: shells
6: linguini

...when it comes to pasta, I prefer #4 over the others.
```

### Back-Referencing and Order of Definition

Styles are not evaluated until they are used. This means that as long as all
the styles involved are defined before they are invoked, either directly or
within another style, they can be defined in any order. The allows you to
create alphabetic-ordered style sets that in turn make it easier to find the
style you are looking for.

So:

 * Define styles in any order
 * Styles must be defined only before they are actually used
 * It's ok to reference one style within another before it is defined
as long as the outermost style isn't actually invoked prior to any inner styles
being defined.

## Namespaces

Built-ins and styles have separate namespaces. As `{styleName` actually
resolves to `[s styleName` in the processor, there's no conflict at all.
So you can define finger-twisters like `[style b [b [b]]]` without any
conflicts.

Generally what this means in actual practice is:

 * you define your styles with `[s styleName]`
 * then, within your text
   * you use `{styleName}` to access your styles
   * you use `[builtInName]` to access built-ins

