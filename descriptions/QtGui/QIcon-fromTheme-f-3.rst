.. sip:method-description::
    :status: todo
    :pysig: 46df8864bd29c8b024ba416f1e8c75c2
    :realsig: (const QString&, const QIcon&)
    :digest: 7f631ff532adaece80f0062ea3e2faf4

This is an overloaded function.

Returns the :sip:ref:`~PyQt6.QtGui.QIcon` corresponding to *name* in the :sip:ref:`~PyQt6.QtGui.QIcon.themeName`.

If the current theme does not provide an icon for *name*, the :sip:ref:`~PyQt6.QtGui.QIcon.fallbackThemeName` is consulted, before falling back to looking up standalone icon files in the :sip:ref:`~PyQt6.QtGui.QIcon.fallbackSearchPaths`. Finally, the platform's native icon library is consulted.

If no icon is found *fallback* is returned.

This is useful to provide a guaranteed fallback, regardless of whether the current set of icon themes and fallbacks paths support the requested icon.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qicon.py
    :lines: 103-103

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.fallbackThemeName`, :sip:ref:`~PyQt6.QtGui.QIcon.fallbackSearchPaths`.
