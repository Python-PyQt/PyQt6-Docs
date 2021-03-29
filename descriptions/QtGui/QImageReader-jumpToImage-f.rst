.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int)
    :digest: 9a807f9fe0b02b92cdcd0ec13221b1cf

For image formats that support animation, this function skips to the image whose sequence number is *imageNumber*, returning true if successful or false if the corresponding image cannot be found.

The next call to :sip:ref:`~PyQt6.QtGui.QImageReader.read` will attempt to read this image.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.jumpToNextImage`, :sip:ref:`~PyQt6.QtGui.QImageIOHandler.jumpToImage`.
