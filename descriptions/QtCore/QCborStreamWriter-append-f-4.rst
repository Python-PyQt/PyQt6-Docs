.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 823c89f3f18b7a74b4b237ffac3587a8

Appends the boolean value *b* to the stream, creating either a CBOR False value or a CBOR True value. This function is equivalent to (and implemented as):

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 197-197

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.appendNull`, :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.appendUndefined`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isBool`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toBool`.
