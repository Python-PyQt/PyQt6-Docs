.. sip:method-description::
    :status: todo
    :pysig: 57c21b050608123aa7787aab4357c0dd
    :realsig: (int,int,const QMimeData*,Qt::DropAction)
    :digest: cfdce83c6b40d63ff86b70521d26dd63

Handles the *data* supplied by a drag and drop operation that ended with the given *action* in the given *row* and *column*. Returns ``true`` if the data and action can be handled by the model; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTableWidget.supportedDropActions`.
