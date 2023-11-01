.. sip:method-description::
    :status: todo
    :pysig: 508e645b907c0825f330e8aa2b764b5b
    :realsig: (const QString&,const QIcon&)
    :digest: 28d0cc805f6f7072c87de2311ff8db8e

This is an overloaded function.

Returns the :sip:ref:`~PyQt6.QtGui.QIcon` corresponding to *name* in the current icon theme.

If the current theme does not provide an icon for *name*, the fallback icon theme is consulted, before falling back to looking up standalone icon files in the :sip:ref:`~PyQt6.QtGui.QIcon.fallbackSearchPaths`.

If no icon is found *fallback* is returned.

This is useful to provide a guaranteed fallback, regardless of whether the current set of icon themes and fallbacks paths support the requested icon.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qicon.py
    :lines: 103-103

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.fallbackSearchPaths`, fallbackIconTheme().
