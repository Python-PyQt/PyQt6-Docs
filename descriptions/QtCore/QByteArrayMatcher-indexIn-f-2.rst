.. sip:method-description::
    :status: todo
    :pysig: 155689fb3ea0161afa7a8b8a4e0992c8
    :realsig: (QByteArrayView,qsizetype) const
    :digest: 9e437f100d20464970475a5c9b4a6194

Searches the byte array *data*, from byte position *from* (default 0, i.e. from the first byte), for the byte array :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.pattern` that was set in the constructor or in the most recent call to :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.setPattern`. Returns the position where the :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.pattern` matched in *data*, or -1 if no match was found.
