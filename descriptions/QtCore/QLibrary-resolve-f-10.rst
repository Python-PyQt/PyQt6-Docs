.. sip:method-description::
    :status: todo
    :pysig: 4df4c96fc29805659ff9c02f59c037a5
    :realsig: (const QString&, const QString&, const char*)
    :digest: 255f2e74b543cf365e72062580720f61

This is an overloaded function.

Loads the library *fileName* with full version number *version* and returns the address of the exported symbol *symbol*. Note that *fileName* should not include the platform-specific file suffix; (see :sip:ref:`~PyQt6.QtCore.QLibrary.fileName`). The library remains loaded until the application exits. *version* is ignored on Windows.

The function returns ``nullptr`` if the symbol could not be resolved or if the library could not be loaded.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLibrary.resolve`.
