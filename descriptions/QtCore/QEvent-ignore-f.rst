.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 035afde4c61be5a252ecac7f148e0c8a

Clears the accept flag parameter of the event object, the equivalent of calling :sip:ref:`~PyQt6.QtCore.QEvent.setAccepted`\ (false).

Clearing the accept parameter indicates that the event receiver does not want the event. Unwanted events might be propagated to the parent widget.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QEvent.accept`.
