.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: b701ad5d846b024bc8aa4ec2b2360936

Enters the array or map that is the current item and prepares for iterating the elements contained in the container. Returns true if entering the container succeeded, false otherwise (usually, a parsing error). Each call to  must be paired with a call to :sip:ref:`~PyQt6.QtCore.QCborStreamReader.leaveContainer`.

This function may only be called if the current item is an array or a map (that is, if :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isMap` or :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isContainer` is true). Calling it in any other condition is an error.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.leaveContainer`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isContainer`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isMap`.
