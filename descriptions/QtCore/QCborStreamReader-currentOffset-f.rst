.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: d05e1a0cd7a0c127d6f0c0662e2721c9

Returns the offset in the input stream of the item currently being decoded. The current offset is the number of decoded bytes so far only if the source data is a :sip:ref:`~PyQt6.QtCore.QByteArray` or it is a :sip:ref:`~PyQt6.QtCore.QIODevice` that was positioned at its beginning when decoding started.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.reset`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.clear`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.device`.
