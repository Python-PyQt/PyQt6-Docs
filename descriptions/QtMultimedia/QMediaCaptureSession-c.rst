.. sip:class-description::
    :status: todo
    :brief: Allows capturing of audio and video content
    :digest: a5d33f7990bdebe0be22b0a5cbdad12e

The :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession` class allows capturing of audio and video content.

The :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession` is the central class that manages capturing of media on the local device.

You can connect a video input to :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession` using :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.setCamera`, :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.setScreenCapture` or :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.setWindowCapture`. A preview of the captured media can be seen by setting a :sip:ref:`~PyQt6.QtMultimediaWidgets.QVideoWidget` or :sip:ref:`~PyQt6.QtMultimediaWidgets.QGraphicsVideoItem` using :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.setVideoOutput`.

You can connect a microphone to :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession` using :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.setAudioInput`. The captured sound can be heard by routing the audio to an output device using :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession.setAudioOutput`.

You can capture still images from a camera by setting a :sip:ref:`~PyQt6.QtMultimedia.QImageCapture` object on the capture session, and record audio/video using a :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder`.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QCamera`, :sip:ref:`~PyQt6.QtMultimedia.QAudioDevice`, :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder`, :sip:ref:`~PyQt6.QtMultimedia.QImageCapture`, :sip:ref:`~PyQt6.QtMultimedia.QScreenCapture`, :sip:ref:`~PyQt6.QtMultimedia.QWindowCapture`, :sip:ref:`~PyQt6.QtMultimedia.QMediaRecorder`, :sip:ref:`~PyQt6.QtMultimediaWidgets.QGraphicsVideoItem`.
