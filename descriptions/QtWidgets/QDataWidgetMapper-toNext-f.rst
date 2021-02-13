.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: abbfa664324019051bb66b80686acb4c

Populates the widgets with data from the next row of the model if the orientation is horizontal (the default), otherwise with data from the next column.

Calls :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.setCurrentIndex` internally. Does nothing if there is no next row in the model.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.toPrevious`, :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.setCurrentIndex`.
