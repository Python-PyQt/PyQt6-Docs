.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (qsizetype)
    :digest: a51d9b07419144964b469609b9aac010

Inverts the value of the bit at index position *i*, returning the previous value of that bit as either true (if it was set) or false (if it was unset).

If the previous value was 0, the new value will be 1. If the previous value was 1, the new value will be 0.

*i* must be a valid index position in the bit array (i.e., 0 <= *i* < :sip:ref:`~PyQt6.QtCore.QBitArray.size`).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBitArray.setBit`, :sip:ref:`~PyQt6.QtCore.QBitArray.clearBit`.
