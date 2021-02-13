.. sip:method-description::
    :status: todo
    :pysig: 47bc384ef78158df7bdc68df0f06aef9
    :realsig: (int)
    :digest: 9818e52f065bf07eb3bdfb288ce2ef4a

For image formats that support animation, this function jumps to the image whose sequence number is *imageNumber*. The next call to :sip:ref:`~PyQt6.QtGui.QImageIOHandler.read` will attempt to read this image.

The default implementation does nothing, and returns ``false``.
