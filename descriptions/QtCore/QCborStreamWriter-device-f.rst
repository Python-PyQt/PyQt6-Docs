.. sip:method-description::
    :status: todo
    :pysig: 7f3af5685d06b3c562a73c51e37f2a3f
    :realsig: () const
    :digest: 3da1b10bda16cb97aea520cdb56c0469

Returns the :sip:ref:`~PyQt6.QtCore.QIODevice` that this :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` object is writing to. The device must have previously been set with either the constructor or with :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.setDevice`.

If this object was created by writing to a :sip:ref:`~PyQt6.QtCore.QByteArray`, this function will return an internal instance of :sip:ref:`~PyQt6.QtCore.QBuffer`, which is owned by :sip:ref:`~PyQt6.QtCore.QCborStreamWriter`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.setDevice`.
