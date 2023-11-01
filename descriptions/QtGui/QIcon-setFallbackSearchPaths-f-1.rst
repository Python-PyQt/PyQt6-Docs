.. sip:method-description::
    :status: todo
    :pysig: e086f7c3dd1fce31f5eda08ab7ea2590
    :realsig: (const QStringList&)
    :digest: e30be16c98b726f1c3d02e3445a9a9ab

Sets the fallback search paths for icons to *paths*.

The fallback search paths are consulted for standalone icon files if the current icon theme or fallback icon theme do not provide results for an icon lookup.

For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qicon.py
    :lines: 109-109

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.fallbackSearchPaths`, :sip:ref:`~PyQt6.QtGui.QIcon.setThemeSearchPaths`.
