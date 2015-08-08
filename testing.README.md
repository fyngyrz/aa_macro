Testing
-------

Testing requires the presence of the following files:

```
aa_ansiicolor.py
expected.html
mactest.txt
test.gif
test.jpg
test.png
test_aa_macro.py
```

Testing requires that the directory with the test files be the
current directory.

Testing requires that the user executing the test posses
write permission for the directory within which the test
is performed.

All tests are in [test_aa_macro.py](test_aa_macro.py), and can be run with:

    python test_aa_macro.py

On success, this will have a zero exit status, and the output will look like the following:

    .
    ----------------------------------------------------------------------
    Ran 1 test in 0.000s

    OK

On failure, error messages will be presented, and a list of the differences
between what was expected from the test, and the output of the test.

Lines that begin with a \- indicate that this information was expected, but was
missing in the output.

Lines that begin with a \+ indicate that this information was not expected,
but was present in the output.
