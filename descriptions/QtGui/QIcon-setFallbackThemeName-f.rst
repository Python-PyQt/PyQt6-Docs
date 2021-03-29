.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: (const QString&)
    :digest: 7d9e103c13357daf706e59f888608f82

Sets the fallback icon theme to *name*.

The *name* should correspond to a directory name in the themeSearchPath() containing an index.theme file describing its contents.

**Note:** This should be done before creating :sip:ref:`~PyQt6.QtGui.QGuiApplication`, to ensure correct initialization.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.fallbackThemeName`, :sip:ref:`~PyQt6.QtGui.QIcon.themeSearchPaths`, :sip:ref:`~PyQt6.QtGui.QIcon.themeName`.
