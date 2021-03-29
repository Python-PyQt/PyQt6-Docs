.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 4498b3ab06b8eb15fcc1c5a765acb2d4

Reparses the current element. This function must be called when more data becomes available in the source :sip:ref:`~PyQt6.QtCore.QIODevice` after parsing failed due to reaching the end of the input data before the end of the CBOR stream.

When reading from QByteArray(), the :sip:ref:`~PyQt6.QtCore.QCborStreamReader.addData` function automatically calls this function. Calling it when the reading had not failed is a no-op.
