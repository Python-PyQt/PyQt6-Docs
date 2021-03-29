.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 389ab7c9171dbc58156bf43b489175d8

Clears the tree widget by removing all of its items and selections.

**Note:** Since each item is removed from the tree widget before being deleted, the return value of :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.treeWidget` will be invalid when called from an item's destructor.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeWidget.takeTopLevelItem`, :sip:ref:`~PyQt6.QtWidgets.QTreeWidget.topLevelItemCount`, :sip:ref:`~PyQt6.QtWidgets.QTreeWidget.columnCount`.
