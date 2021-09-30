.. sip:class-description::
    :status: todo
    :brief: Widget that can be docked inside a QMainWindow or floated as a top-level window on the desktop
    :digest: 19506d4a9a05163a402642dd161c57b3

The :sip:ref:`~PyQt6.QtWidgets.QDockWidget` class provides a widget that can be docked inside a :sip:ref:`~PyQt6.QtWidgets.QMainWindow` or floated as a top-level window on the desktop.

:sip:ref:`~PyQt6.QtWidgets.QDockWidget` provides the concept of dock widgets, also know as tool palettes or utility windows. Dock windows are secondary windows placed in the *dock widget area* around the :sip:ref:`~PyQt6.QtWidgets.QMainWindow.centralWidget` in a :sip:ref:`~PyQt6.QtWidgets.QMainWindow`.

.. image:: ../../../images/mainwindow-docks.png

Dock windows can be moved inside their current area, moved into new areas and floated (e.g., undocked) by the end-user. The :sip:ref:`~PyQt6.QtWidgets.QDockWidget` API allows the programmer to restrict the dock widgets ability to move, float and close, as well as the areas in which they can be placed.

.. _qdockwidget-appearance:

Appearance
----------

A :sip:ref:`~PyQt6.QtWidgets.QDockWidget` consists of a title bar and the content area. The title bar displays the dock widgets :sip:ref:`~PyQt6.QtWidgets.QWidget.windowTitle`, a *float* button and a *close* button. Depending on the state of the :sip:ref:`~PyQt6.QtWidgets.QDockWidget`, the *float* and *close* buttons may be either disabled or not shown at all.

The visual appearance of the title bar and buttons is dependent on the :sip:ref:`~PyQt6.QtWidgets.QStyle` in use.

A :sip:ref:`~PyQt6.QtWidgets.QDockWidget` acts as a wrapper for its child widget, set with :sip:ref:`~PyQt6.QtWidgets.QDockWidget.setWidget`. Custom size hints, minimum and maximum sizes and size policies should be implemented in the child widget. :sip:ref:`~PyQt6.QtWidgets.QDockWidget` will respect them, adjusting its own constraints to include the frame and title. Size constraints should not be set on the :sip:ref:`~PyQt6.QtWidgets.QDockWidget` itself, because they change depending on whether it is docked; a docked :sip:ref:`~PyQt6.QtWidgets.QDockWidget` has no frame and a smaller title bar.

**Note:** On macOS, if the :sip:ref:`~PyQt6.QtWidgets.QDockWidget` has a native window handle (for example, if winId() is called on it or the child widget), then due to a limitation it will not be possible to drag the dock widget when undocking. Starting the drag will undock the dock widget, but a second drag will be needed to move the dock widget itself.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMainWindow`, `Dock Widgets Example <https://doc.qt.io/qt-6/qtwidgets-mainwindows-dockwidgets-example.html>`_.
