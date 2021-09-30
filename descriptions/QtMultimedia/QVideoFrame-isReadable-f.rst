.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 6b435ac19827fc3a4165a9110d851561

Identifies if the mapped contents of a video frame were read from the frame when it was mapped.

This is a convenience function which checks if the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.MapMode` contains the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.MapMode.WriteOnly` flag.

Returns true if the contents of the mapped memory were read from the video frame, and false otherwise.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.mapMode`, :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.MapMode`.
