.. sip:method-description::
    :status: todo
    :pysig: ac63555edfbb8c463d188d49f0cd2497
    :realsig: (int)
    :digest: 09ae12df8b6179a77cf8bce824b12f91

Advance the CBOR stream decoding one element. You should usually call this function when parsing fixed-width basic elements (that is, integers, simple values, tags and floating point values). But this function can be called when the current item is a string, array or map too and it will skip over that entire element, including all contained elements.

This function returns true if advancing was successful, false otherwise. It may fail if the stream is corrupt, incomplete or if the nesting level of arrays and maps exceeds *maxRecursion*. Calling this function when :sip:ref:`~PyQt6.QtCore.QCborStreamReader.hasNext` has returned false is also an error. If this function returns false, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.lastError` will return the error code detailing what the failure was.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.lastError`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isValid`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.hasNext`.
