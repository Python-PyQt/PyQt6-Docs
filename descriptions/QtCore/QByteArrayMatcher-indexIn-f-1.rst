.. sip:method-description::
    :status: todo
    :pysig: d73d396ed9322fcaaa0e2b8f14f5ba74
    :realsig: (const char*,qsizetype,qsizetype) const
    :digest: fcff4f7385f2261ad09880d569258d6a

Searches the char string *str*, which has length *len*, from byte position *from* (default 0, i.e. from the first byte), for the byte array :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.pattern` that was set in the constructor or in the most recent call to :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.setPattern`. Returns the position where the :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.pattern` matched in *str*, or -1 if no match was found.
