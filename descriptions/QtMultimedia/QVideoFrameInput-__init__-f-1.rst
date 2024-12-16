.. sip:method-description::
    :status: todo
    :pysig: b738456af15f52b98bb158cc98294cb7
    :realsig: (const QVideoFrameFormat&, QObject*)
    :digest: 90dd88f12ec3320b22f01a80aec91d17

Constructs a new :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameInput` object with video frame *format* and *parent*.

The specified *format* will work as a hint for the initialization of the matching video encoder upon invoking :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder.record`. If the format is not specified or not valid, the video encoder will be initialized upon sending the first frame. Sending of video frames with another pixel format and size after initialization of the matching video encoder might cause a performance penalty during recording.

We recommend specifying the format if you know in advance what kind of frames you're going to send.
