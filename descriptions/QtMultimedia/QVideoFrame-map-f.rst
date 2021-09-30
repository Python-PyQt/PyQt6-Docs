.. sip:method-description::
    :status: todo
    :pysig: b995a8d85d438be327377aa5944f9af0
    :realsig: (QVideoFrame::MapMode)
    :digest: 6b81e74b9873966d1f5fa344aecd77b7

Maps the contents of a video frame to system (CPU addressable) memory.

In some cases the video frame data might be stored in video memory or otherwise inaccessible memory, so it is necessary to map a frame before accessing the pixel data. This may involve copying the contents around, so avoid mapping and unmapping unless required.

The map *mode* indicates whether the contents of the mapped memory should be read from and/or written to the frame. If the map mode includes the ``QVideoFrame::ReadOnly`` flag the mapped memory will be populated with the content of the video frame when initially mapped. If the map mode includes the ``QVideoFrame::WriteOnly`` flag the content of the possibly modified mapped memory will be written back to the frame when unmapped.

While mapped the contents of a video frame can be accessed directly through the pointer returned by the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.bits` function.

When access to the data is no longer needed, be sure to call the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.unmap` function to release the mapped memory and possibly update the video frame contents.

If the video frame has been mapped in read only mode, it is permissible to map it multiple times in read only mode (and unmap it a corresponding number of times). In all other cases it is necessary to unmap the frame first before mapping a second time.

**Note:** Writing to memory that is mapped as read-only is undefined, and may result in changes to shared data or crashes.

Returns true if the frame was mapped to memory in the given *mode* and false otherwise.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.unmap`, :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.mapMode`, :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.bits`.
