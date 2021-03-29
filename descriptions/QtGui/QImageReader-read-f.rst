.. sip:method-description::
    :status: todo
    :pysig: fb51eb2740812f4466a824231ed4bce3
    :realsig: ()
    :digest: e884fc11d68dcb680f1112960c6059e2

Reads an image from the device. On success, the image that was read is returned; otherwise, a null :sip:ref:`~PyQt6.QtGui.QImage` is returned. You can then call :sip:ref:`~PyQt6.QtGui.QImageReader.error` to find the type of error that occurred, or :sip:ref:`~PyQt6.QtGui.QImageReader.errorString` to get a human readable description of the error.

For image formats that support animation, calling  repeatedly will return the next frame. When all frames have been read, a null image will be returned.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.canRead`, :sip:ref:`~PyQt6.QtGui.QImageReader.supportedImageFormats`, :sip:ref:`~PyQt6.QtGui.QImageReader.supportsAnimation`, :sip:ref:`~PyQt6.QtGui.QMovie`.
