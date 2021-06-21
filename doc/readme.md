# Divio documentation for developers

For instructions on installation, building the documentation, and guidelines for
contributing to SymPy's documentation, please read the `SymPy Documentation
Style Guide <https://docs.sympy.org/dev/documentation-style-guide.html>`_.
The SymPy Documentation Style Guide can also be read at
src/documentation-style-guide.rst.

## Build the documentation locally

You'll need the [enchant](https://www.abisource.com/projects/enchant/) library,
used by ``pyenchant`` for spelling.

Install with ``brew install enchant`` (macOS) or the appropriate command for
your system.

Then:

    git clone git@github.com:sympy/sympy.git  # clone
    cd sympy/doc
    make install
    make run
    open http://localhost:9001