.. sip:method-description::
    :status: todo
    :pysig: 128bb55d27fc765f89944a64fae19162
    :realsig: (qsizetype,qsizetype)
    :digest: 6794b895c2265d21bbee351ad5dcddf5

Removes *len* bytes from the array, starting at index position *pos*, and returns a reference to the array.

If *pos* is out of range, nothing happens. If *pos* is valid, but *pos* + *len* is larger than the size of the array, the array is truncated at position *pos*.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_text_qbytearray.py
    :lines: 206-208

Element removal will preserve the array's capacity and not reduce the amount of allocated memory. To shed extra capacity and free as much memory as possible, call :sip:ref:`~PyQt6.QtCore.QByteArray.squeeze` after the last change to the array's size.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray.insert`, :sip:ref:`~PyQt6.QtCore.QByteArray.replace`, :sip:ref:`~PyQt6.QtCore.QByteArray.squeeze`.
