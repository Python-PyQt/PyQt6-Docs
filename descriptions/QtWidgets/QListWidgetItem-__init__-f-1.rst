.. sip:method-description::
    :status: todo
    :pysig: 90194a95a79fa38d0bd20733c80dec24
    :realsig: (QListWidget*,int)
    :digest: a6e5b35120c4d7efa8ba7718fbbbb219

Constructs an empty list widget item of the specified *type* with the given *parent*. If *parent* is not specified, the item will need to be inserted into a list widget with :sip:ref:`~PyQt6.QtWidgets.QListWidget.insertItem`.

This constructor inserts the item into the model of the parent that is passed to the constructor. If the model is sorted then the behavior of the insert is undetermined since the model will call the ``'<'`` operator method on the item which, at this point, is not yet constructed. To avoid the undetermined behavior, we recommend not to specify the parent and use :sip:ref:`~PyQt6.QtWidgets.QListWidget.insertItem` instead.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QListWidgetItem.type`.
