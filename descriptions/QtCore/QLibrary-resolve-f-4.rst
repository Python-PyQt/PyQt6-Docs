.. sip:method-description::
    :status: todo
    :pysig: 8d3de76612916220c4a61ea492435575
    :realsig: (const char*)
    :digest: 3fbc24df6df1294623378498d97d5216

Returns the address of the exported symbol *symbol*. The library is loaded if necessary. The function returns ``nullptr`` if the symbol could not be resolved or if the library could not be loaded.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_plugin_qlibrary.py
    :lines: 72-78

The symbol must be exported as a C function from the library. This means that the function must be wrapped in an ``extern "C"`` if the library is compiled with a C++ compiler. On Windows you must also explicitly export the function from the DLL using the ``__declspec(dllexport)`` compiler directive, for example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_plugin_qlibrary.py
    :lines: 83-86

with ``MY_EXPORT`` defined as

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_plugin_qlibrary.py
    :lines: 91-95
