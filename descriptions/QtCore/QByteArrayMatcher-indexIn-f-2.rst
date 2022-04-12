.. sip:method-description::
    :status: todo
    :pysig: 155689fb3ea0161afa7a8b8a4e0992c8
    :realsig: (QByteArrayView,qsizetype) const
    :digest: 8c4f6d5ed412bb668839476309b9becf

This is an overloaded function.

Searches the byte array *data*, from byte position *from* (default 0, i.e. from the first byte), for the byte array :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.pattern` that was set in the constructor or in the most recent call to :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.setPattern`. Returns the position where the :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.pattern` matched in *data*, or -1 if no match was found.
