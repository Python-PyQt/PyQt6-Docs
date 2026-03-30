.. sip:class-description::
    :status: todo
    :brief: Widget which presents video produced by a media object
    :digest: af7d64e483d4722e61df210af6919072

The :sip:ref:`~PyQt6.QtMultimediaWidgets.QVideoWidget` class provides a widget which presents video produced by a media object.

Attaching a :sip:ref:`~PyQt6.QtMultimediaWidgets.QVideoWidget` to a :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer` or :sip:ref:`~PyQt6.QtMultimedia.QCamera` allows it to display the video or image output of that object.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-video.py
    :lines: 106-113

**Note**: Only a single display output can be attached to a media object at one time.

**Warning:** :sip:ref:`~PyQt6.QtMultimediaWidgets.QVideoWidget` is not supported on the ``eglfs`` platform plugin.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QCamera`, :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer`, :sip:ref:`~PyQt6.QtMultimediaWidgets.QGraphicsVideoItem`.
