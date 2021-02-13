.. sip:method-description::
    :status: todo
    :pysig: 859b584ee9160de6e8abf8204cd34b1d
    :realsig: (int,QWidget*,int,Qt::Alignment)
    :digest: 966cf9e9c8bb47155bf5b5ce6818468a

Inserts *widget* at position *index*, with stretch factor *stretch* and alignment *alignment*. If *index* is negative, the widget is added at the end.

The stretch factor applies only in the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.direction` of the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout`, and is relative to the other boxes and widgets in this :sip:ref:`~PyQt6.QtWidgets.QBoxLayout`. Widgets and boxes with higher stretch factors grow more.

If the stretch factor is 0 and nothing else in the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout` has a stretch factor greater than zero, the space is distributed according to the `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_:sizePolicy() of each widget that's involved.

The alignment is specified by *alignment*. The default alignment is 0, which means that the widget fills the entire cell.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addWidget`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertItem`.
