.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 85ed18781da9df3bab02967cb046be58

This is an image format specific function that set the compression of an image. For image formats that do not support setting the compression, this value is ignored.

The value range of *compression* depends on the image format. For example, the "tiff" format supports two values, 0(no compression) and 1(LZW-compression).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageWriter.compression`.
