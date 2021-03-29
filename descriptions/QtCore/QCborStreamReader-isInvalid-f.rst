.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: dbc503495c8309584528e8296043a06f

Returns true if the current element is invalid, false otherwise. The current element may be invalid if there was a decoding error or we've just parsed the last element in an array or map.

**Note:** This function is not to be confused with :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isNull`. Null is a normal CBOR type that must be handled by the application.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isValid`.
