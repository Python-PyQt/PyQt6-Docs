.. sip:class-description::
    :status: todo
    :brief: Contains color groups for each widget state
    :digest: 5dce2d7c81330baad5b92ff8be66bbf8

The :sip:ref:`~PyQt6.QtGui.QPalette` class contains color groups for each widget state.

A palette consists of three color groups: *Active*, *Disabled*, and *Inactive*. All widgets in Qt contain a palette and use their palette to draw themselves. This makes the user interface easily configurable and easier to keep consistent.

If you create a new widget we strongly recommend that you use the colors in the palette rather than hard-coding specific colors.

The color groups:

* The Active group is used for the window that has keyboard focus.

* The Inactive group is used for other windows.

* The Disabled group is used for widgets (not windows) that are disabled for some reason.

Both active and inactive windows can contain disabled widgets. (Disabled widgets are often called *inaccessible* or *grayed out*.)

In most styles, Active and Inactive look the same.

Colors and brushes can be set for particular roles in any of a palette's color groups with :sip:ref:`~PyQt6.QtGui.QPalette.setColor` and :sip:ref:`~PyQt6.QtGui.QPalette.setBrush`. A color group contains a group of colors used by widgets for drawing themselves. We recommend that widgets use color group roles from the palette such as "foreground" and "base" rather than literal colors like "red" or "turquoise". The color roles are enumerated and defined in the :sip:ref:`~PyQt6.QtGui.QPalette.ColorRole.ColorRole` documentation.

We strongly recommend that you use the default palette of the current style (returned by QGuiApplication::palette()) and modify that as necessary. This is done by Qt's widgets when they are drawn.

To modify a color group you call the functions :sip:ref:`~PyQt6.QtGui.QPalette.setColor` and :sip:ref:`~PyQt6.QtGui.QPalette.setBrush`, depending on whether you want a pure color or a pixmap pattern.

There are also corresponding :sip:ref:`~PyQt6.QtGui.QPalette.color` and :sip:ref:`~PyQt6.QtGui.QPalette.brush` getters, and a commonly used convenience function to get the :sip:ref:`~PyQt6.QtGui.QPalette.ColorRole.ColorRole` for the current :sip:ref:`~PyQt6.QtGui.QPalette.ColorGroup.ColorGroup`: :sip:ref:`~PyQt6.QtGui.QPalette.window`, :sip:ref:`~PyQt6.QtGui.QPalette.windowText`, :sip:ref:`~PyQt6.QtGui.QPalette.base`, etc.

You can copy a palette using the copy constructor and test to see if two palettes are *identical* using :sip:ref:`~PyQt6.QtGui.QPalette.isCopyOf`.

:sip:ref:`~PyQt6.QtGui.QPalette` is optimized by the use of `implicit sharing <https://doc.qt.io/qt-6/implicit-sharing.html>`_, so it is very efficient to pass :sip:ref:`~PyQt6.QtGui.QPalette` objects as arguments.

**Warning:** Some styles do not use the palette for all drawing, for instance, if they make use of native theme engines. This is the case for both the Windows Vista and the macOS styles.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QApplication.setPalette`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setPalette`, :sip:ref:`~PyQt6.QtGui.QColor`.
