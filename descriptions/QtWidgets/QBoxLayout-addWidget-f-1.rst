.. sip:method-description::
    :status: todo
    :pysig: 769ac2d2f06a76c32e657c3194614d9c
    :realsig: (QWidget*,int,Qt::Alignment)
    :digest: 8c35fa6adb1df7da2a5c76fca65713f5

Adds *widget* to the end of this box layout, with a stretch factor of *stretch* and alignment *alignment*.

The stretch factor applies only in the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.direction` of the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout`, and is relative to the other boxes and widgets in this :sip:ref:`~PyQt6.QtWidgets.QBoxLayout`. Widgets and boxes with higher stretch factors grow more.

If the stretch factor is 0 and nothing else in the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout` has a stretch factor greater than zero, the space is distributed according to the :sip:ref:`~PyQt6.QtWidgets.QWidget`:sizePolicy() of each widget that's involved.

The alignment is specified by *alignment*. The default alignment is 0, which means that the widget fills the entire cell.

*widget* becomes a child of the :sip:ref:`~PyQt6.QtWidgets.QLayout.parentWidget`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertWidget`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addItem`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addLayout`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addStretch`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addSpacing`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addStrut`.
