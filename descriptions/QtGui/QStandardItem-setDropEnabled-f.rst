.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 5ab85b10d77216500240954e619d7d74

Sets whether the item is drop enabled. If *dropEnabled* is true, the item can be used as a drop target; otherwise, it cannot.

Note that you also need to ensure that drops are enabled in the view; see QWidget::acceptDrops(); and that the model supports the desired drop actions; see :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.supportedDropActions`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStandardItem.isDropEnabled`, :sip:ref:`~PyQt6.QtGui.QStandardItem.setDragEnabled`, :sip:ref:`~PyQt6.QtGui.QStandardItem.setFlags`.
