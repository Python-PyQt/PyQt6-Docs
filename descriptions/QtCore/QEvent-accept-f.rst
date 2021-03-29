.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 0a47650414e54f1f1bb16540bbff9b4c

Sets the accept flag of the event object, the equivalent of calling :sip:ref:`~PyQt6.QtCore.QEvent.setAccepted`\ (true).

Setting the accept parameter indicates that the event receiver wants the event. Unwanted events might be propagated to the parent widget.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QEvent.ignore`.
