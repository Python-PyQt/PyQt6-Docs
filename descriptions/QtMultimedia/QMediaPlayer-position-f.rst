.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: bc0ab3cf6d6ee774bb22c1d512d4940f

Returns the current position inside the media being played back in ms.

Returns 0 if the media player doesn't have a valid media file or stream. For live streams, the duration usually changes during playback as more data becomes available.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.setPosition`.
