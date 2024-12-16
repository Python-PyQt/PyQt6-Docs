.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 32014a620f8ea11e3372fa7687c9018d

Signals that a new frame can be sent to the video frame input. After receiving the signal, if you have frames to be sent, invoke :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameInput.sendVideoFrame` once or in a loop until it returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameInput.sendVideoFrame`.
