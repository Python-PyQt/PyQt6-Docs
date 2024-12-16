.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: (const QImage&)
    :digest: b8ab0d990c6b7d641575fc5ce042f366

Constructs a :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame` from a :sip:ref:`~PyQt6.QtGui.QImage`.

If the :sip:ref:`~PyQt6.QtGui.QImage.Format` matches one of the formats in :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat.PixelFormat`, the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame` will hold an instance of the *image* and use that format without any pixel format conversion. In this case, pixel data will be copied only if you call :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame.map` with ``WriteOnly`` flag while keeping the original image.

Otherwise, if the :sip:ref:`~PyQt6.QtGui.QImage.Format` matches none of video formats, the image is first converted to a supported (A)RGB format using :sip:ref:`~PyQt6.QtGui.QImage.convertedTo` with the :sip:ref:`~PyQt6.QtCore.Qt.ImageConversionFlag.AutoColor` flag. This may incur a performance penalty.

If :sip:ref:`~PyQt6.QtGui.QImage.isNull` evaluates to true for the input :sip:ref:`~PyQt6.QtGui.QImage`, the :sip:ref:`~PyQt6.QtMultimedia.QVideoFrame` will be invalid and :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat.isValid` will return false.

.. seealso:: :sip:ref:`~PyQt6.QtMultimedia.QVideoFrameFormat.pixelFormatFromImageFormat`, :sip:ref:`~PyQt6.QtGui.QImage.convertedTo`, :sip:ref:`~PyQt6.QtGui.QImage.isNull`.
