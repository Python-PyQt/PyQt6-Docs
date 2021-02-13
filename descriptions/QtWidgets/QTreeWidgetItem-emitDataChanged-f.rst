.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 102e678b407da97af27dfdcc99b83cc3

Causes the model associated with this item to emit a :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dataChanged`\ () signal for this item.

You normally only need to call this function if you have subclassed :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem` and reimplemented :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.data` and/or :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.setData`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.setData`.
