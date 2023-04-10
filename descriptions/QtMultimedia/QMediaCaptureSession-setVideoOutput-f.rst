.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: (QObject*)
    :digest: 50d33c394ce03596fd8bec8c2a64248b

Sets a :sip:ref:`~PyQt6.QtCore.QObject`, (\ *output*), to a video preview for the capture session.

A :sip:ref:`~PyQt6.QtCore.QObject` based preview is expected to have an invokable :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.videoSink` method that returns a :sip:ref:`~PyQt6.QtMultimedia.QVideoSink`.

The previously set preview is detached.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.videoOutput`.
