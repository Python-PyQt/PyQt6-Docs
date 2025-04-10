.. sip:method-description::
    :status: todo
    :pysig: c5283bf81cad04335531dd6931c2734d
    :realsig: (const QString&)
    :digest: d7109319e31fabf2252b94b6543b3a7a

Sets the current icon theme to *name*.

If the theme matches the name of an installed font that provides named glyphs, then :sip:ref:`~PyQt6.QtGui.QIcon.fromTheme` calls that match one of the glyphs will produce an icon for that glyph.

Otherwise, the theme will be looked up in :sip:ref:`~PyQt6.QtGui.QIcon.themeSearchPaths`. At the moment the only supported icon theme format is the `Freedesktop Icon Theme Specification <https://doc.qt.io/qt-6/https://standards.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html>`_. The *name* should correspond to a directory name in the themeSearchPath() containing an ``index.theme`` file describing its contents.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.themeSearchPaths`, :sip:ref:`~PyQt6.QtGui.QIcon.themeName`, `Freedesktop Icon Theme Specification <https://doc.qt.io/qt-6/https://standards.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html>`_.
