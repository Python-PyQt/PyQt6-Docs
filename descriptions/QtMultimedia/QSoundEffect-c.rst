.. sip:class-description::
    :status: todo
    :brief: Way to play low latency sound effects
    :digest: 0a2d04abe93330032d3dd4661572241c

The :sip:ref:`~PyQt6.QtMultimedia.QSoundEffect` class provides a way to play low latency sound effects.

This class allows you to play uncompressed audio files (typically WAV files) in a generally lower latency way, and is suitable for "feedback" type sounds in response to user actions (e.g. virtual keyboard sounds, positive or negative feedback for popup dialogs, or game sounds). If low latency is not important, consider using the :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer` class instead, since it supports a wider variety of media formats and is less resource intensive.

This example shows how a looping, somewhat quiet sound effect can be played:

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-qsound.py
    :lines: 58-62

Typically the sound effect should be reused, which allows all the parsing and preparation to be done ahead of time, and only triggered when necessary. This assists with lower latency audio playback.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-qsound.py
    :lines: 72-82

Since :sip:ref:`~PyQt6.QtMultimedia.QSoundEffect` requires slightly more resources to achieve lower latency playback, the platform may limit the number of simultaneously playing sound effects.
