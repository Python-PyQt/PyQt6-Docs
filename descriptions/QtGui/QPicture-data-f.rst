.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 22dcb99fae4eb006800ce54103ada7a3

Returns a pointer to the picture data. The pointer is only valid until the next non-const function is called on this picture. The returned pointer is 0 if the picture contains no data.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPicture.setData`, :sip:ref:`~PyQt6.QtGui.QPicture.size`, :sip:ref:`~PyQt6.QtGui.QPicture.isNull`.
