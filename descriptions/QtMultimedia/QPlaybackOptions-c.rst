.. sip:class-description::
    :status: todo
    :brief: Enables low-level control of media playback options
    :digest: ed035da269db4f4e6fb2cc90eaa25278

The :sip:ref:`~PyQt6.QtMultimedia.QPlaybackOptions` class enables low-level control of media playback options.

:sip:ref:`~PyQt6.QtMultimedia.QPlaybackOptions` gives low-level control of media playback options. Although we strongly recommend to rely on the default settings of :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer`, :sip:ref:`~PyQt6.QtMultimedia.QPlaybackOptions` can be used to optimize media playback to specific use cases where the default options are not ideal.

Note that options are hints to the media backend, and may be ignored if they are not supported by the current media format or codec.

Playback options rely on support in the media backend. Availability is documented per option.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer`.
