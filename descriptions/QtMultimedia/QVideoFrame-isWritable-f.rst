.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 2f6de57a9c47be281d09a01af54ab905

Identifies if the mapped contents of a video frame will be persisted when the frame is unmapped.

This is a convenience function which checks if the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.MapMode` contains the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.MapMode.WriteOnly` flag.

Returns true if the video frame will be updated when unmapped, and false otherwise.

**Note:** The result of altering the data of a frame that is mapped in read-only mode is undefined. Depending on the buffer implementation the changes may be persisted, or worse alter a shared buffer.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.mapMode`, :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.MapMode`.
