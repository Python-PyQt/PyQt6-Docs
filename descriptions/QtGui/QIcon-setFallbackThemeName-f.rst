.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: (const QString&)
    :digest: 47bea2d292838ac067c0c2d19ef06da5

Sets the fallback icon theme to *name*.

The fallback icon theme is consulted for icons not provided by the :sip:ref:`~PyQt6.QtGui.QIcon.themeName`, or if the :sip:ref:`~PyQt6.QtGui.QIcon.themeName` does not exist.

The *name* should correspond to theme in the same format as documented by :sip:ref:`~PyQt6.QtGui.QIcon.setThemeName`, and will be looked up in :sip:ref:`~PyQt6.QtGui.QIcon.themeSearchPaths`.

**Note:** Fallback icon themes should be set before creating :sip:ref:`~PyQt6.QtGui.QGuiApplication`, to ensure correct initialization.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.fallbackThemeName`, :sip:ref:`~PyQt6.QtGui.QIcon.themeSearchPaths`, :sip:ref:`~PyQt6.QtGui.QIcon.themeName`.
