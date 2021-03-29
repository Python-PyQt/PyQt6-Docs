.. sip:method-description::
    :status: todo
    :pysig: 00224bcd83be5529a3de8e5e1e638c36
    :realsig: (const QList<QListWidgetItem*>&) const
    :digest: daafc0199635558d42ca4e2c24237629

Returns an object that contains a serialized description of the specified *items*. The format used to describe the items is obtained from the :sip:ref:`~PyQt6.QtWidgets.QListWidget.mimeTypes` function.

If the list of items is empty, ``nullptr`` is returned instead of a serialized empty list.
