.. sip:method-description::
    :status: todo
    :pysig: 1d557afd38e9b10837d8f94f0b85c942
    :realsig: (int)
    :digest: ac7b4eae9ed6fa66fa02e4a0f2769837

Returns a pointer to the start of the frame data buffer for a *plane*.

This value is only valid while the frame data is :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.map`.

Changes made to data accessed via this pointer (when mapped with write access) are only guaranteed to have been persisted when :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.unmap` is called and when the buffer has been mapped for writing.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.map`, :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.mappedBytes`, :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.bytesPerLine`, :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.planeCount`.
