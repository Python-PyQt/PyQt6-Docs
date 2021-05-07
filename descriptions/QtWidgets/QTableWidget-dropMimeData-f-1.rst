.. sip:method-description::
    :status: todo
    :pysig: f0b909230760c0f56a106db962e0c0be
    :realsig: (int,int,const QMimeData*,Qt::DropAction)
    :digest: cfdce83c6b40d63ff86b70521d26dd63

Handles the *data* supplied by a drag and drop operation that ended with the given *action* in the given *row* and *column*. Returns ``true`` if the data and action can be handled by the model; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTableWidget.supportedDropActions`.
