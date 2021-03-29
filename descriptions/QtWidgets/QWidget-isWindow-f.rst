.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ff35eacef81a9e502f6e8c285de1a64d

Returns ``true`` if the widget is an independent window, otherwise returns ``false``.

A window is a widget that isn't visually the child of any other widget and that usually has a frame and a :sip:ref:`~PyQt6.QtWidgets.QWidget.setWindowTitle`.

A window can have a :sip:ref:`~PyQt6.QtWidgets.QWidget.parentWidget`. It will then be grouped with its parent and deleted when the parent is deleted, minimized when the parent is minimized etc. If supported by the window manager, it will also have a common taskbar entry with its parent.

:sip:ref:`~PyQt6.QtWidgets.QDialog` and :sip:ref:`~PyQt6.QtWidgets.QMainWindow` widgets are by default windows, even if a parent widget is specified in the constructor. This behavior is specified by the :sip:ref:`~PyQt6.QtCore.Qt.WindowFlags.Window` flag.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.window`, :sip:ref:`~PyQt6.QtWidgets.QWidget.isModal`, :sip:ref:`~PyQt6.QtWidgets.QWidget.parentWidget`.
