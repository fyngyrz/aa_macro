# [aagen](aagen)

[aagen](aagen) is a command line tool to take a source input file
formatted for the `macro()` processor, and generate the results to a
file or to the stdout stream.

[aagen](aagen) requires aa_macro.py

[aagen](aagen) can use aa_ansiicolor.py if it is present to do syntax
highlighting on its errors and usage outputs. If this import library is
not present, [aagen](aagen) simply won't use color.

Invocation; use `aagen` if aagen is in the current path but not the
current directory, or `./aagen` if aagen is in the current directory.

An example file is provided:

    aagen-example.txt

You can utilize the example file this way:

    aagen aagen-example.txt
	aagen aagen-example.txt -f aagen-example.html

...or...

    ./aagen  aagen-example.txt
	./aagen aagen-example.txt -f aagen-example.html

Type `aagen` or `./aagen` by itself for a listing of the available options.
