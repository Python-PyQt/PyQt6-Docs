.. sip:method-description::
    :status: todo
    :pysig: 3bab94b6398a4d48acc3dbcf33b0e84c
    :realsig: (double,char,int)
    :digest: 722e8a400a5d6183c70acf5c44797071

This is an overloaded function.

Returns a byte-array representing the floating-point number *n* as text.

Returns a byte array containing a string representing *n*, with a given *format* and *precision*, with the same meanings as for QString::number(double, char, int). For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 402-403

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.toDouble`, :sip:ref:`~PyQt6.QtCore.QLocale.FloatingPointPrecisionOption`.
