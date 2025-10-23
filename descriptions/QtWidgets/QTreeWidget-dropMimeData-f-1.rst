.. sip:method-description::
    :status: todo
    :pysig: b0b6718665a05be006be14f6d3877ce3
    :realsig: (QTreeWidgetItem*,int,const QMimeData*,Qt::DropAction)
    :digest: 97798364ff4c426d35a71bc31695fbf9

Handles the *data* supplied by a drag and drop operation that ended with the given *action* in the *index* in the given *parent* item.

The default implementation returns ``true`` if the drop was successfully handled by decoding the mime data and inserting it into the model; otherwise it returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeWidget.supportedDropActions`, :sip:ref:`~PyQt6.QtWidgets.QTreeWidget.supportedDragActions`.
