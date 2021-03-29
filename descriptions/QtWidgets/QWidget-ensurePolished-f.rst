.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: () const
    :digest: 50a2a1b31db83e6d8dbff856616803d7

Ensures that the widget and its children have been polished by :sip:ref:`~PyQt6.QtWidgets.QStyle` (i.e., have a proper font and palette).

`QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ calls this function after it has been fully constructed but before it is shown the very first time. You can call this function if you want to ensure that the widget is polished before doing an operation, e.g., the correct font size might be needed in the widget's :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint` reimplementation. Note that this function *is* called from the default implementation of :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint`.

Polishing is useful for final initialization that must happen after all constructors (from base classes as well as from subclasses) have been called.

If you need to change some settings when a widget is polished, reimplement :sip:ref:`~PyQt6.QtWidgets.QWidget.event` and handle the :sip:ref:`~PyQt6.QtCore.QEvent.Type.Polish` event type.

**Note:** The function is declared const so that it can be called from other const functions (e.g., :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint`).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.event`.
