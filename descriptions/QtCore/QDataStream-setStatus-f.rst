.. sip:method-description::
    :status: todo
    :pysig: c61c69ee503135798ef5827bfbdd91c5
    :realsig: (QDataStream::Status)
    :digest: 941d9fe23fc04d6f34da47336396b6d9

Sets the status of the data stream to the *status* given.

Subsequent calls to setStatus() are ignored until :sip:ref:`~PyQt6.QtCore.QDataStream.resetStatus` is called.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QDataStream.Status.Status`, :sip:ref:`~PyQt6.QtCore.QDataStream.status`, :sip:ref:`~PyQt6.QtCore.QDataStream.resetStatus`.
