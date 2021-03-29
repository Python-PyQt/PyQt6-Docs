.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: faa9884400657da5b239887ee38a5188

This virtual function discards any cached size hint information. You should always call this function if you change the return value of the :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.sizeHint` function. Subclasses must always call the base implementation when reimplementing this function.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.effectiveSizeHint`.
