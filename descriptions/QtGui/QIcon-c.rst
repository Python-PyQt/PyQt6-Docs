.. sip:class-description::
    :status: todo
    :brief: Scalable icons in different modes and states
    :digest: d39946f7d981a3029f94773fa210450b

The :sip:ref:`~PyQt6.QtGui.QIcon` class provides scalable icons in different modes and states.

A :sip:ref:`~PyQt6.QtGui.QIcon` can generate smaller, larger, active, and disabled pixmaps from the set of pixmaps it is given. Such pixmaps are used by Qt widgets to show an icon representing a particular action.

The simplest use of :sip:ref:`~PyQt6.QtGui.QIcon` is to create one from a :sip:ref:`~PyQt6.QtGui.QPixmap` file or resource, and then use it, allowing Qt to work out all the required icon styles and sizes. For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qicon.py
    :lines: 68-69

To undo a :sip:ref:`~PyQt6.QtGui.QIcon`, simply set a null icon in its place:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qicon.py
    :lines: 74-74

Use the :sip:ref:`~PyQt6.QtGui.QImageReader.supportedImageFormats` and :sip:ref:`~PyQt6.QtGui.QImageWriter.supportedImageFormats` functions to retrieve a complete list of the supported file formats.

When you retrieve a pixmap using pixmap(\ :sip:ref:`~PyQt6.QtCore.QSize`, Mode, State), and no pixmap for this given size, mode and state has been added with :sip:ref:`~PyQt6.QtGui.QIcon.addFile` or :sip:ref:`~PyQt6.QtGui.QIcon.addPixmap`, then :sip:ref:`~PyQt6.QtGui.QIcon` will generate one on the fly. This pixmap generation happens in a :sip:ref:`~PyQt6.QtGui.QIconEngine`. The default engine scales pixmaps down if required, but never up, and it uses the current style to calculate a disabled appearance. By using custom icon engines, you can customize every aspect of generated icons. With QIconEnginePlugin it is possible to register different icon engines for different file suffixes, making it possible for third parties to provide additional icon engines to those included with Qt.

**Note:** Since Qt 4.2, an icon engine that supports SVG is included.

.. _qicon-making-classes-that-use-qicon:

Making Classes that Use QIcon
-----------------------------

If you write your own widgets that have an option to set a small pixmap, consider allowing a :sip:ref:`~PyQt6.QtGui.QIcon` to be set for that pixmap. The Qt class :sip:ref:`~PyQt6.QtWidgets.QToolButton` is an example of such a widget.

Provide a method to set a :sip:ref:`~PyQt6.QtGui.QIcon`, and when you draw the icon, choose whichever pixmap is appropriate for the current state of your widget. For example:

.. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_image_qicon.py
    :lines: 81-89

You might also make use of the ``Active`` mode, perhaps making your widget ``Active`` when the mouse is over the widget (see :sip:ref:`~PyQt6.QtWidgets.QWidget.enterEvent`), while the mouse is pressed pending the release that will activate the function, or when it is the currently selected item. If the widget can be toggled, the "On" mode might be used to draw a different icon.

.. image:: ../../../images/icon.png

**Note:** :sip:ref:`~PyQt6.QtGui.QIcon` needs a :sip:ref:`~PyQt6.QtGui.QGuiApplication` instance before the icon is created.

.. _qicon-high-dpi-icons:

High DPI Icons
--------------

There are two ways that :sip:ref:`~PyQt6.QtGui.QIcon` supports high DPI icons: via :sip:ref:`~PyQt6.QtGui.QIcon.addFile` and :sip:ref:`~PyQt6.QtGui.QIcon.fromTheme`.

:sip:ref:`~PyQt6.QtGui.QIcon.addFile` is useful if you have your own custom directory structure and do not need to use the `freedesktop.org Icon Theme Specification <https://doc.qt.io/qt-6/https://standards.freedesktop.org/icon-theme-spec/icon-theme-spec-latest.html>`_. Icons created via this approach use Qt's "@nx" high DPI syntax.

Using :sip:ref:`~PyQt6.QtGui.QIcon.fromTheme` is necessary if you plan on following the Icon Theme Specification. To make :sip:ref:`~PyQt6.QtGui.QIcon` use the high DPI version of an image, add an additional entry to the appropriate ``index.theme`` file:

::

    [Icon Theme]
    Name=Test
    Comment=Test Theme

    Directories=32x32/actions,32x32@2/actions

    [32x32/actions]
    Size=32
    Context=Actions
    Type=Fixed

    # High DPI version of the entry above.
    [32x32@2/actions]
    Size=32
    Scale=2
    Type=Fixed

Your icon theme directory would then look something like this:

::

    ├── 32x32
    │   └── actions
    │       └── appointment-new.png
    ├── 32x32@2
    │   └── actions
    │       └── appointment-new.png
    └── index.theme
