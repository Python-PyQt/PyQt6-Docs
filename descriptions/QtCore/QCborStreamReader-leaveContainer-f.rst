.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 7a4491fe52f8ac1019746ca76dd516f1

Leaves the array or map whose items were being processed and positions the decoder at the next item after the end of the container. Returns true if leaving the container succeeded, false otherwise (usually, a parsing error). Each call to :sip:ref:`~PyQt6.QtCore.QCborStreamReader.enterContainer` must be paired with a call to .

This function may only be called if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.hasNext` has returned false and :sip:ref:`~PyQt6.QtCore.QCborStreamReader.containerDepth` is not zero. Calling it in any other condition is an error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.enterContainer`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.parentContainerType`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.containerDepth`.
