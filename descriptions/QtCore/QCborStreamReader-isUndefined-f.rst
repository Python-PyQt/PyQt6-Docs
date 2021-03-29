.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 146b86f4bbeb7c537e5d9500077d6d36

Returns true if the current element is the ``undefined`` value, false if it is anything else. Undefined values may be encoded to indicate that some conversion failed or was not possible when creating the stream. :sip:ref:`~PyQt6.QtCore.QCborStreamReader` never performs any replacement and this function will only return true if the stream contains an explicit undefined value.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isSimpleType`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.toSimpleType`.
