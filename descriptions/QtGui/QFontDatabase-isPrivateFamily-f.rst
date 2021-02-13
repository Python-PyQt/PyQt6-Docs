.. sip:method-description::
    :status: todo
    :pysig: 787ad3d0f6e2063950bbbf6e050908f3
    :realsig: (const QString&)
    :digest: 24d39099f73fdae35b5b40e9a14d9f42

Returns ``true`` if and only if the *family* font family is private.

This happens, for instance, on macOS and iOS, where the system UI fonts are not accessible to the user. For completeness, :sip:ref:`~PyQt6.QtGui.QFontDatabase.families` returns all font families, including the private ones. You should use this function if you are developing a font selection control in order to keep private fonts hidden.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QFontDatabase.families`.
