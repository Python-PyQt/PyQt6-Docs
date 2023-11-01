.. sip:method-description::
    :status: todo
    :pysig: 8f073a1e029f8e4468adbec9c15c25e0
    :realsig: (const QString&)
    :digest: 1114ef1367183b5edaa6424c4ef7922c

Capture the image and save it to *file*. This operation is asynchronous in majority of cases, followed by signals :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageExposed`, :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageCaptured`, :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageSaved` or :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.error`.

If an empty *file* is passed, the camera back end chooses the default location and naming scheme for photos on the system, if only file name without full path is specified, the image will be saved to the default directory, with a full path reported with :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageCaptured` and :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageSaved` signals.

:sip:ref:`~PyQt6.QtMultimedia.QCamera` saves all the capture parameters like exposure settings or image processing parameters, so changes to camera parameters after :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.capture` is called do not affect previous capture requests.

:sip:ref:`~PyQt6.QtMultimedia.QImageCapture.capture` returns the capture Id parameter, used with :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageExposed`, :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageCaptured` and :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.imageSaved` signals.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QImageCapture.isReadyForCapture`.
