.. sip:method-description::
    :status: todo
    :pysig: be19219e980ca570e4d111e6320872f1
    :realsig: (const QString&)
    :digest: cdc37d4d76c1955e22decaeec77eb654

Returns the :sip:ref:`~PyQt6.QtGui.QIcon` corresponding to *name* in the current icon theme.

The latest version of the freedesktop icon specification and naming specification can be obtained here:

* `http://standards.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html <http://standards.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html>`_

* `http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html <http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html>`_

To fetch an icon from the current icon theme:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qicon.py
    :lines: 96-96

**Note:** By default, only X11 will support themed icons. In order to use themed icons on Mac and Windows, you will have to bundle a compliant theme in one of your :sip:ref:`~PyQt6.QtGui.QIcon.themeSearchPaths` and set the appropriate :sip:ref:`~PyQt6.QtGui.QIcon.themeName`.

**Note:** Qt will make use of GTK's icon-theme.cache if present to speed up the lookup. These caches can be generated using gtk-update-icon-cache: `https://developer.gnome.org/gtk3/stable/gtk-update-icon-cache.html <https://developer.gnome.org/gtk3/stable/gtk-update-icon-cache.html>`_.

**Note:** If an icon can't be found in the current theme, then it will be searched in :sip:ref:`~PyQt6.QtGui.QIcon.fallbackSearchPaths` as an unthemed icon.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QIcon.themeName`, :sip:ref:`~PyQt6.QtGui.QIcon.setThemeName`, :sip:ref:`~PyQt6.QtGui.QIcon.themeSearchPaths`, :sip:ref:`~PyQt6.QtGui.QIcon.fallbackSearchPaths`.
