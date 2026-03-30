.. sip:method-description::
    :status: todo
    :pysig: 3be1a9e6b661cb52907ee3c598581baa
    :realsig: (const QString&, const QString&, const char*)
    :digest: 7230348c4b2da0e72dfa235c339ba9ca

Loads the library *fileName* with full version number *version* and returns the address of the exported symbol *symbol*. Note that *fileName* should not include the platform-specific file suffix; (see :sip:ref:`~PyQt6.QtCore.QLibrary.fileName`). The library remains loaded until the application exits. *version* is ignored on Windows.

The function returns ``nullptr`` if the symbol could not be resolved or if the library could not be loaded.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLibrary.resolve`.
