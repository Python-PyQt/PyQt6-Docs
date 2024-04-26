.. sip:method-description::
    :status: todo
    :pysig: e086f7c3dd1fce31f5eda08ab7ea2590
    :realsig: (const QStringList&)
    :digest: 9f07e27ab5a6e789593ff7d7652ef4a2

Sets the fallback search paths for icons to *paths*.

The fallback search paths are consulted for standalone icon files if the :sip:ref:`~PyQt6.QtGui.QIcon.themeName` or :sip:ref:`~PyQt6.QtGui.QIcon.fallbackThemeName` do not provide results for an icon lookup.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qicon.py
    :lines: 109-109

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.fallbackSearchPaths`, :sip:ref:`~PyQt6.QtGui.QIcon.setThemeSearchPaths`.
