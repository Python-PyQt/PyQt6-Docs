.. sip:method-description::
    :status: todo
    :pysig: be19219e980ca570e4d111e6320872f1
    :realsig: (const QString&)
    :digest: e1b57666c7b1fd4d45eda8b61e749fca

Returns the :sip:ref:`~PyQt6.QtGui.QIcon` corresponding to *name* in the :sip:ref:`~PyQt6.QtGui.QIcon.themeName`.

If the current theme does not provide an icon for *name*, the :sip:ref:`~PyQt6.QtGui.QIcon.fallbackThemeName` is consulted, before falling back to looking up standalone icon files in the :sip:ref:`~PyQt6.QtGui.QIcon.fallbackSearchPaths`. Finally, the platform's native icon library is consulted.

To fetch an icon from the current icon theme:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qicon.py

If an :sip:ref:`~PyQt6.QtGui.QIcon.themeName` has not been explicitly set via :sip:ref:`~PyQt6.QtGui.QIcon.setThemeName` a platform defined icon theme will be used.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.themeName`, :sip:ref:`~PyQt6.QtGui.QIcon.fallbackThemeName`, :sip:ref:`~PyQt6.QtGui.QIcon.setThemeName`, :sip:ref:`~PyQt6.QtGui.QIcon.themeSearchPaths`, :sip:ref:`~PyQt6.QtGui.QIcon.fallbackSearchPaths`, `Freedesktop Icon Naming Specification <https://doc.qt.io/qt-6/https://specifications.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html>`_.
