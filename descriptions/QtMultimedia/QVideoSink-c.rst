.. sip:class-description::
    :status: todo
    :brief: Represents a generic sink for video data
    :digest: 0d8fc6e5138353c21651489400f3a867

The :sip:ref:`~PyQt6.QtMultimedia.QVideoSink` class represents a generic sink for video data.

The :sip:ref:`~PyQt6.QtMultimedia.QVideoSink` class can be used to retrieve video data on a frame by frame basis from Qt Multimedia.

:sip:ref:`~PyQt6.QtMultimedia.QVideoSink` will provide individual video frames to the application developer through the :sip:ref:`~PyQt6.QtMultimedia.QVideoSink.videoFrameChanged` signal.

The video frame can then be used to read out the data of those frames and handle them further. When using :sip:ref:`~PyQt6.QtGui.QPainter`, the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame` can be drawing using the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.paint` method.

:sip:ref:`~PyQt6.QtMultimedia.QVideoFrame` objects can consume a significant amount of memory or system resources and should thus not be held for longer than required by the application.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer`, :sip:ref:`~PyQt6.QtMultimedia.QMediaCaptureSession`.
