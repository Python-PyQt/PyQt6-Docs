.. sip:method-description::
    :status: todo
    :pysig: c5c154cc8d665c929486168782c564eb
    :realsig: (const QString&,const char*)
    :digest: adf307dfe1dd6bcf9339b276ffd0f89e

Constructs a bitmap from the file specified by the given *fileName*. If the file does not exist, or has an unknown format, the bitmap becomes a null bitmap.

The *fileName* and *format* parameters are passed on to the :sip:ref:`~PyQt6.QtGui.QPixmap.load` function. If the file format uses more than 1 bit per pixel, the resulting bitmap will be dithered automatically.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.isNull`, :sip:ref:`~PyQt6.QtGui.QImageReader.imageFormat`.
