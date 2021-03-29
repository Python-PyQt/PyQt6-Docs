.. sip:method-description::
    :status: todo
    :pysig: 9382005ba3dfa636040567651d1db432
    :realsig: (const QList<QTreeWidgetItem*>&) const
    :digest: daafc0199635558d42ca4e2c24237629

Returns an object that contains a serialized description of the specified *items*. The format used to describe the items is obtained from the :sip:ref:`~PyQt6.QtWidgets.QTreeWidget.mimeTypes` function.

If the list of items is empty, ``nullptr`` is returned rather than a serialized empty list.
