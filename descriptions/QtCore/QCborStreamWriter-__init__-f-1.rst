.. sip:method-description::
    :status: todo
    :pysig: a5704e7d57089c440a7d83c72d987b9e
    :realsig: (QByteArray*)
    :digest: ab841f4c7d46e713780e59c66c2260c1

Creates a :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` object that will append the stream to *data*. All streaming is done immediately to the byte array, without the need for flushing any buffers.

The following example writes a number to a byte array then returns it.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 85-91

:sip:ref:`~PyQt6.QtCore.QCborStreamWriter` does not take ownership of *data*.
