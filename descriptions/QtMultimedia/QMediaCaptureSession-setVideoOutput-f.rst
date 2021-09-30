.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: (QObject*)
    :digest: 2ab748bc03e97fbea01d7518be53c503

Sets a :sip:ref:`~PyQt6.QtCore.QObject`, (\ *output*), to a video preview for the capture session.

A :sip:ref:`~PyQt6.QtCore.QObject` based preview is expected to have an invokable  method that returns a :sip:ref:`~PyQt6.QtMultimedia.QVideoSink`.

The previously set preview is detached.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.videoOutput`.
