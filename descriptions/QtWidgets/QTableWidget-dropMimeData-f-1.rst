.. sip:method-description::
    :status: todo
    :pysig: f0b909230760c0f56a106db962e0c0be
    :realsig: (int,int,const QMimeData*,Qt::DropAction)
    :digest: 50dab9025d59da480e16c9748067ef2d

Handles the *data* supplied by a drag and drop operation that ended with the given *action* in the given *row* and *column*. Returns ``true`` if the data and action can be handled by the model; otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTableWidget.supportedDropActions`, :sip:ref:`~PyQt6.QtWidgets.QTableWidget.supportedDragActions`.
