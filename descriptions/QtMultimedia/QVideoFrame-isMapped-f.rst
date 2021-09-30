.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: d34f3781f43b3826ecd979934f6f96f7

Identifies if a video frame's contents are currently mapped to system memory.

This is a convenience function which checks that the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.MapMode` of the frame is not equal to :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.MapMode.NotMapped`.

Returns true if the contents of the video frame are mapped to system memory, and false otherwise.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.mapMode`, :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.MapMode`.
