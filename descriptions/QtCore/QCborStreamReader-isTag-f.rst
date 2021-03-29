.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 2dfc019afb914f991fab63b9a4e4fd18

Returns true if the type of the current element is a CBOR tag (that is, if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type` returns :sip:ref:`~PyQt6.QtCore.QCborStreamReader.Type.Tag`). If this function returns true, you may call toTag() to read that data.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, toTag().
