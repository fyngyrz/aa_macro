# Authoring in Macro\(\)

This is a collection of ideas and approaches that are useful in
authoring using `Macro()`.

## Style definition

### Making a Style Defintion Disappear Completely

It aids clarity to place each style on its own line. However,
conceptually, the newline at the end of the line is *outside*
the style, and so ends up in the resulting output. The way to
avoid this is to add two spaces to the end of any line that
closes a style definition. `macro()` will see this and "eat"
both the two spaces and the subsequent newline.

### Defining Styles Over Multiple Lines

You can define a style over multiple lines by placing a
newline directly after the style name instead of a space.

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

