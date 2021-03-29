.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ef0ed4686a0a30bd62a725e6f5d96fed

Returns true if the type of the current element is an IEEE 754 single-precision floating point (that is, if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type` returns :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type.Float`). If this function returns true, you may call toFloat() to read that data.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, toFloat(), :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isFloat16`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isDouble`.
