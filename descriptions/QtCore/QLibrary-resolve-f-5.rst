.. sip:method-description::
    :status: todo
    :pysig: 59e83915e0ec58b791717c7a6fdb653e
    :realsig: (const QString&,const char*)
    :digest: f6cb1d32effd4007070f76a6145a5cad

This is an overloaded function.

Loads the library *fileName* and returns the address of the exported symbol *symbol*. Note that *fileName* should not include the platform-specific file suffix; (see :sip:ref:`~PyQt6.QtCore.QLibrary.fileName`). The library remains loaded until the application exits.

The function returns ``nullptr`` if the symbol could not be resolved or if the library could not be loaded.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLibrary.resolve`.
