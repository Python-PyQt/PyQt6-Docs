.. sip:method-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: ccd10500a67e439e98eb35e749e5b8a0

Sets the current *source*.

Setting the media to a null :sip:ref:`~PyQt6.QtCore.QUrl` will cause the player to discard all information relating to the current media source and to cease all I/O operations related to that media.

**Note:** This function returns immediately after recording the specified source of the media. It does not wait for the media to finish loading and does not check for errors. Listen for the :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.mediaStatusChanged` and :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.error` signals to be notified when the media is loaded and when an error occurs during loading.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.source`.
