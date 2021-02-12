.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 8b971cf74ffc7f9f1967a08425848dfc

Returns true if the current element is a container (that is, an array or a map), false if it is anything else. If the current element is a container, the :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown` function may be used to find out if the container's size is explicit in the stream and, if so, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.length` can be used to get that size.

More importantly, for a container, the :sip:ref:`~PyQt6.QtCore.QCborStreamReader.enterContainer` function is available to begin iterating through the elements contained therein.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader.type`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isArray`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isMap`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.isLengthKnown`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.length`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.enterContainer`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.leaveContainer`, :sip:ref:`~PyQt6.QtCore.QCborStreamReader.containerDepth`.
