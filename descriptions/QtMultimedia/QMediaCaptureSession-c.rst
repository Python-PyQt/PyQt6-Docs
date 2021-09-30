.. sip:class-description::
    :status: todo
    :brief: Allows capturing of audio and video content
    :digest: 6eab3bddd6d847164222eb8cc3f90a65

The :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession` class allows capturing of audio and video content.

The :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession` is the central class that manages capturing of media on the local device.

You can connect a camera and a microphone to :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession` using :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.setCamera` and :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.setAudioInput`. A preview of the captured media can be seen by setting a :sip:ref:`~PyQt6.QtMultimedia.QVideoSink` of :sip:ref:`~PyQt6.QtMultimediaWidgets.QVideoWidget` using :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.setVideoOutput` and heard by routing the audio to an output device using :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.setAudioOutput`.

You can capture still images from a camera by setting a :sip:ref:`~PyQt6.QtMultimedia.QImageCapture` object on the capture session, and record audio/video using a :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder`.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QCamera`, :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice`, :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder`, :sip:ref:`~PyQt6.QtMultimedia.QImageCapture`, :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder`.
