.. sip:method-description::
    :status: todo
    :pysig: 9071bc43c9f302c872dcc5a79cd4031c
    :realsig: (QTreeWidgetItem*,int,const QMimeData*,Qt::DropAction)
    :digest: 2499a2b7c33513f3ff6d7475bf8d0613

Handles the *data* supplied by a drag and drop operation that ended with the given *action* in the *index* in the given *parent* item.

The default implementation returns ``true`` if the drop was successfully handled by decoding the mime data and inserting it into the model; otherwise it returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeWidget.supportedDropActions`.
