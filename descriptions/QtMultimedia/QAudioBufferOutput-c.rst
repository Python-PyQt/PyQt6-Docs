.. sip:class-description::
    :status: todo
    :brief: Used for capturing audio data provided by QMediaPlayer
    :digest: cd057585c90b15ab2476cd73ef53d0ff

The :sip:ref:`~PyQt6.QtMultimedia.QAudioBufferOutput` class is used for capturing audio data provided by :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer`.

:sip:ref:`~PyQt6.QtMultimedia.QAudioBufferOutput` can be set to :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer` in order to receive audio buffers decoded by the media player. The received audio data can be used for any processing or visualization.

:sip:ref:`~PyQt6.QtMultimedia.QAudioBufferOutput` is only supported with the FFmpeg backend.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer`, :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.setAudioBufferOutput`, :sip:ref:`~PyQt6.QtMultimedia.QAudioBuffer`.
