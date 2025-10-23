.. sip:method-description::
    :status: todo
    :pysig: 61c2d0ea3a2a9d22ea4dda2c8dd7a516
    :realsig: (int,QWidget*,int,Qt::Alignment)
    :digest: 1bb298a1dd442782b988c15d56d8abbd

Inserts *widget* at position *index*, with stretch factor *stretch* and alignment *alignment*. If *index* is negative, the widget is added at the end.

The stretch factor applies only in the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.direction` of the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout`, and is relative to the other boxes and widgets in this :sip:ref:`~PyQt6.QtWidgets.QBoxLayout`. Widgets and boxes with higher stretch factors grow more.

If the stretch factor is 0 and nothing else in the :sip:ref:`~PyQt6.QtWidgets.QBoxLayout` has a stretch factor greater than zero, the space is distributed according to the :sip:ref:`~PyQt6.QtWidgets.QWidget`:sizePolicy() of each widget that's involved.

The alignment is specified by *alignment*. The default alignment is 0, which means that the widget fills the entire cell.

*widget* becomes a child of the :sip:ref:`~PyQt6.QtWidgets.QLayout.parentWidget`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.addWidget`, :sip:ref:`~PyQt6.QtWidgets.QBoxLayout.insertItem`.
