.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 6e5add8b9360f51a722795912be376ac

Resets the source back to the beginning and clears the decoder state. If the source data was a :sip:ref:`~PyQt6.QtCore.QByteArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader` will restart from the beginning of the array.

If the source data is a :sip:ref:`~PyQt6.QtCore.QIODevice`, this function will call :sip:ref:`~PyQt6.QtCore.QIODevice.reset`, which will seek to byte position 0. If the CBOR stream is not found at the beginning of the device (e.g., beginning of a file), then this function will likely do the wrong thing. Instead, position the :sip:ref:`~PyQt6.QtCore.QIODevice` to the right offset and call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.setDevice`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.clear`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.setDevice`.
