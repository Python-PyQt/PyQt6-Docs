.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: 958aa9eabe622059d1c51428da93ef64

Sets the current *source*.

Setting the media to a null :sip:ref:`~PyQt6.QtCore.QUrl` will cause the player to discard all information relating to the current media source and to cease all I/O operations related to that media. Setting the media will stop the playback.

**Note:** This function returns immediately after recording the specified source of the media. It does not wait for the media to finish loading and does not check for errors. Listen for the :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.mediaStatusChanged` and :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.error` signals to be notified when the media is loaded and when an error occurs during loading.

**Note:** FFmpeg, used by the FFmpeg media backend, restricts use of nested protocols for security reasons. In controlled environments where all inputs are trusted, the list of approved protocols can be overridden using the QT_FFMPEG_PROTOCOL_WHITELIST environment variable. This environment variable is Qt's private API and can change between patch releases without notice.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.source`.
