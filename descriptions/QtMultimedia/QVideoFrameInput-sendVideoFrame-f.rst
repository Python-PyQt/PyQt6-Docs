.. sip:method-description::
    :status: todo
    :pysig: c495ab361a180691415869a992e12e23
    :realsig: (const QVideoFrame&)
    :digest: ace675fc5d34f5e162613569b91f4c31

Sends :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame` to :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder` or a video output through :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`.

Returns ``true`` if the specified *frame* has been sent successfully to the destination. Returns ``false``, if the frame hasn't been sent, which can happen if the instance is not assigned to :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`, the session doesn't have video outputs or a media recorder, the media recorder is not started or its queue is full. The signal :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameInput.readyToSendVideoFrame` will be sent as soon as the destination is able to handle a new frame.

Sending of an empty video frame is treated by :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder` as an end of the input stream. :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder` stops the recording automatically if :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.autoStop` is ``true`` and all the inputs have reported the end of the stream.
