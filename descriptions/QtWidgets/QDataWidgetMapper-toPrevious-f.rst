.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 3731ec7edc577140cb1b0374bd6818e5

Populates the widgets with data from the previous row of the model if the orientation is horizontal (the default), otherwise with data from the previous column.

Calls :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.setCurrentIndex` internally. Does nothing if there is no previous row in the model.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.toNext`, :sip:ref:`~PyQt6.QtWidgets.QDataWidgetMapper.setCurrentIndex`.
