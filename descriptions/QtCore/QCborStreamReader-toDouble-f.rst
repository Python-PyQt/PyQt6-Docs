.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 90ca17c27b20f4182c5b4cace590bcf4

Returns the 64-bit double-precision floating point value of the current element.

This function does not perform any type conversions, including from other floating point types or from integer values. Therefore, it may only be called if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isDouble` is true; calling it in any other condition is an error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isDouble`, toFloat16(), toFloat().
