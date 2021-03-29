.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 8aa8e351009b172db8ce67abe4e82f03

Returns the length of the string or byte array, or the number of items in an array or the number, of item pairs in a map, if known. This function must not be called if the length is unknown (that is, if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown` returned false). It is an error to do that and it will cause :sip:ref:`~PyQt6.QtCore.QCborStreamReader` to stop parsing the input stream.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown`, :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startMap`.
