.. sip:method-description::
    :status: todo
    :pysig: 3bab94b6398a4d48acc3dbcf33b0e84c
    :realsig: (double,char,int)
    :digest: 4a3406b2769e49c9956ae094b24ecfd2

Returns a byte-array representing the floating-point number *n* as text.

Returns a byte array containing a string representing *n*, with a given *format* and *precision*, with the same meanings as for QString::number(double, char, int). For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 402-403

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.toDouble`, :sip:ref:`~PyQt6.QtCore.QLocale.FloatingPointPrecisionOption`.
