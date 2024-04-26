.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: (const QString&)
    :digest: 514904f1eb4ef39b67b8bf8cf4356cc2

Sets the current icon theme to *name*.

The theme will be will be looked up in :sip:ref:`~PyQt6.QtGui.QIcon.themeSearchPaths`.

At the moment the only supported icon theme format is the `Freedesktop Icon Theme Specification <https://doc.qt.io/qt-6/https://standards.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html>`_. The *name* should correspond to a directory name in the themeSearchPath() containing an ``index.theme`` file describing its contents.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.themeSearchPaths`, :sip:ref:`~PyQt6.QtGui.QIcon.themeName`, `Freedesktop Icon Theme Specification <https://doc.qt.io/qt-6/https://standards.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html>`_.
