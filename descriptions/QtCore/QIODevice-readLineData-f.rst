.. sip:method-description::
    :status: todo
    :pysig: 35be435d5eb927e68aeed4ae67cd8a52
    :realsig: (char*,qint64)
    :digest: 7aa17e657a197e7e437d00e9f33dac91

Reads up to *maxSize* characters into *data* and returns the number of characters read.

This function is called by :sip:ref:`~PyQt6.QtCore.QIODevice.readLine`, and provides its base implementation, using :sip:ref:`~PyQt6.QtCore.QIODevice.getChar`. Buffered devices can improve the performance of :sip:ref:`~PyQt6.QtCore.QIODevice.readLine` by reimplementing this function.

:sip:ref:`~PyQt6.QtCore.QIODevice.readLine` appends a '\\0' byte to *data*;  does not need to do this.

If you reimplement this function, be careful to return the correct value: it should return the number of bytes read in this line, including the terminating newline, or 0 if there is no line to be read at this point. If an error occurs, it should return -1 if and only if no bytes were read. Reading past EOF is considered an error.
