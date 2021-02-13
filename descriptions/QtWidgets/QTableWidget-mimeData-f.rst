.. sip:method-description::
    :status: todo
    :pysig: b0a47374b85eabdc71317dc88c39c4c6
    :realsig: (const QList<QTableWidgetItem*>&) const
    :digest: daafc0199635558d42ca4e2c24237629

Returns an object that contains a serialized description of the specified *items*. The format used to describe the items is obtained from the :sip:ref:`~PyQt6.QtWidgets.QTableWidget.mimeTypes` function.

If the list of items is empty, ``nullptr`` is returned rather than a serialized empty list.
