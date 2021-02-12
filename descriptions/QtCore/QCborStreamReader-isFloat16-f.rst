.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: b78ba2ea6eead101f7a6b69c48913d56

Returns true if the type of the current element is an IEEE 754 half-precision floating point (that is, if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type` returns :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type.Float16`). If this function returns true, you may call toFloat16() to read that data.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, toFloat16(), :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isFloat`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isDouble`.
