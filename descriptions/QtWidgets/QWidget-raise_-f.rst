.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realname: QWidget::raise
    :realsig: ()
    :digest: a5c6dcdc553ecf348194fb2f5d89e9d3

Raises this widget to the top of the parent widget's stack.

After this call the widget will be visually in front of any overlapping sibling widgets.

**Note:** When using :sip:ref:`~PyQt6.QtWidgets.QWidget.activateWindow`, you can call this function to ensure that the window is stacked on top.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.lower`, :sip:ref:`~PyQt6.QtWidgets.QWidget.stackUnder`.
