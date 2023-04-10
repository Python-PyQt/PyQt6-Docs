.. sip:method-description::
    :status: todo
    :pysig: 1a4e7c8fc571300d2677165954c38ec2
    :realsig: (QVideoSink*)
    :digest: 5978cc2781716fff24a3a5c421d7df89

Sets a :sip:ref:`~PyQt6.QtMultimedia.QVideoSink`, (\ *sink*), to a video preview for the capture session.

A :sip:ref:`~PyQt6.QtCore.QObject` based preview is expected to have an invokable :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.videoSink` method that returns a :sip:ref:`~PyQt6.QtMultimedia.QVideoSink`.

The previously set preview is detached.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.videoSink`.
