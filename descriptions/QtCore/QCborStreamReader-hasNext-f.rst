.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 9599049b27ea91cc818fdd33617af6c1

Returns true if there are more items to be decoded in the current container or false of we've reached its end. If we're parsing the root element,  returning false indicates the parsing is complete; otherwise, if the container depth is non-zero, then the outer code needs to call :sip:ref:`~PyQt6.QtCore.QCborStreamReader.leaveContainer`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.parentContainerType`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.containerDepth`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.leaveContainer`.
