.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: a98941446a9731d6c2abaa81041b5ad3

Returns true if the type of the current element is either an unsigned integer or a negative one (that is, if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type` returns :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type.UnsignedInteger` or :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type.NegativeInteger`). If this function returns true, you may call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toInteger` to read that value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toInteger`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toUnsignedInteger`, toNegativeInteger(), :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isUnsignedInteger`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isNegativeInteger`.
