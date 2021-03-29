.. sip:method-description::
    :status: todo
    :pysig: b056f1c5be1b349bfa1af179ed091c87
    :realsig: (const QString&,QListWidget*,int)
    :digest: 81097900587776e025c299ae2df8bd18

Constructs an empty list widget item of the specified *type* with the given *text* and *parent*. If the parent is not specified, the item will need to be inserted into a list widget with :sip:ref:`~PyQt6.QtWidgets.QListWidget.insertItem`.

This constructor inserts the item into the model of the parent that is passed to the constructor. If the model is sorted then the behavior of the insert is undetermined since the model will call the ``'<'`` operator method on the item which, at this point, is not yet constructed. To avoid the undetermined behavior, we recommend not to specify the parent and use :sip:ref:`~PyQt6.QtWidgets.QListWidget.insertItem` instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.type`.
