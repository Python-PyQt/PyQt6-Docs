.. sip:method-description::
    :status: todo
    :pysig: 8df747f14ef8054a8aeecb93fe4f1471
    :realsig: (QWidget*,Qt::WindowFlags)
    :digest: fd330e90b26c155d2ae1c29f322d9dc5

Constructs a dialog with parent *parent*.

A dialog is always a top-level widget, but if it has a parent, its default location is centered on top of the parent. It will also share the parent's taskbar entry.

The widget flags *f* are passed on to the `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ constructor. If, for example, you don't want a What's This button in the title bar of the dialog, pass :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.WindowTitleHint` | :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.WindowSystemMenuHint` in *f*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.setWindowFlags`.
