.. sip:class-description::
    :status: todo
    :brief: Graphics item which display video produced by a QMediaPlayer or QCamera
    :digest: 8dd004f949ac6eeece14fbc98eb0f8b0

The :sip:ref:`~PyQt6.QtMultimediaWidgets.QGraphicsVideoItem` class provides a graphics item which display video produced by a :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer` or :sip:ref:`~PyQt6.QtMultimedia.QCamera`.

Attaching a :sip:ref:`~PyQt6.QtMultimediaWidgets.QGraphicsVideoItem` to a :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer` or :sip:ref:`~PyQt6.QtMultimedia.QCamera` allows it to display the video or image output of that media object.

.. literalinclude:: ../../../snippets/qtmultimedia-src-multimedia-doc-snippets-multimedia-snippets-video.py
    :lines: 146-154

**Note**: Only a single display output can be attached to a media object at one time.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QMediaPlayer`, :sip:ref:`~PyQt6.QtMultimediaWidgets.QVideoWidget`, :sip:ref:`~PyQt6.QtMultimedia.QCamera`.
