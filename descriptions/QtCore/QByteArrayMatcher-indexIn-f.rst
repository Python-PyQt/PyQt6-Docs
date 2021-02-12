.. sip:method-description::
    :status: todo
    :pysig: 3999d77b17884fbcff0c5b402b16be9a
    :realsig: (const QByteArray&,qsizetype) const
    :digest: 4aa7a4c8a1e23cb41459eea5f4e57be6

Searches the byte array *ba*, from byte position *from* (default 0, i.e. from the first byte), for the byte array :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.pattern` that was set in the constructor or in the most recent call to :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.setPattern`. Returns the position where the :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.pattern` matched in *ba*, or -1 if no match was found.
