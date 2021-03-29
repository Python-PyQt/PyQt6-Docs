.. sip:method-description::
    :status: todo
    :pysig: bca95ea0372c08db22e1bf9f44c09c0d
    :realsig: (const QIcon&,const QString&,QListWidget*,int)
    :digest: d4a25dbf9cfacfd85f6386c9b5676528

Constructs an empty list widget item of the specified *type* with the given *icon*, *text* and *parent*. If the parent is not specified, the item will need to be inserted into a list widget with :sip:ref:`~PyQt6.QtWidgets.QListWidget.insertItem`.

This constructor inserts the item into the model of the parent that is passed to the constructor. If the model is sorted then the behavior of the insert is undetermined since the model will call the ``'<'`` operator method on the item which, at this point, is not yet constructed. To avoid the undetermined behavior, we recommend not to specify the parent and use :sip:ref:`~PyQt6.QtWidgets.QListWidget.insertItem` instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.type`.
