.. sip:method-description::
    :status: todo
    :pysig: 2f7af7ab5abbd13c008452f651acb447
    :realsig: (int)
    :digest: ac7b4eae9ed6fa66fa02e4a0f2769837

Returns a pointer to the start of the frame data buffer for a *plane*.

This value is only valid while the frame data is :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.map`.

Changes made to data accessed via this pointer (when mapped with write access) are only guaranteed to have been persisted when :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.unmap` is called and when the buffer has been mapped for writing.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.map`, :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.mappedBytes`, :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.bytesPerLine`, :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.planeCount`.
