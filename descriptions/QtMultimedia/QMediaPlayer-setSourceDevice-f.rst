.. sip:method-description::
    :status: todo
    :pysig: ffb2152c2a168b538539159fe3c3aec2
    :realsig: (QIODevice*,const QUrl&)
    :digest: 5e59e0e344acbc86ac6436a7cb9e1f1e

Sets the current source *device*.

The media data will be read from *device*. The *sourceUrl* can be provided to resolve additional information about the media, mime type etc. The *device* must be open and readable.

For macOS the *device* should also be seek-able.

**Note:** This function returns immediately after recording the specified source of the media. It does not wait for the media to finish loading and does not check for errors. Listen for the :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.mediaStatusChanged` and :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.error` signals to be notified when the media is loaded, and if an error occurs during loading.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer.sourceDevice`.
