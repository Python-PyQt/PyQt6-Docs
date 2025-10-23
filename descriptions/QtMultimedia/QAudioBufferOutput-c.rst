.. sip:class-description::
    :status: todo
    :brief: Used for capturing audio data provided by QMediaPlayer
    :digest: e1485661f04ef908d56f953aeac80281

The :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferOutput` class is used for capturing audio data provided by :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer`.

:sip:ref:`~PyQt6.QtMultimedia.QAudioBufferOutput` can be set to :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer` in order to receive audio buffers decoded by the media player. The received audio data can be used for any processing or visualization. An audio level meter implementation can be seen in the widget based `Media Player Example <https://doc.qt.io/qt-6/qtmultimedia-player-example.html>`_.

:sip:ref:`~PyQt6.QtMultimedia.QAudioBufferOutput` is only supported with the FFmpeg backend.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer`, :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.setAudioBufferOutput`, :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer`.
