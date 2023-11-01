.. sip:method-description::
    :status: todo
    :pysig: fcd8306d3f99f603963b2e2c5bd9e516
    :realsig: (const QSize&,const uchar*,QImage::Format)
    :digest: 062d559c9f24e36e25a438e3934b77c0

Constructs a bitmap with the given *size*, and sets the contents to the *bits* supplied.

The bitmap data has to be byte aligned and provided in the bit order specified by *monoFormat*. The mono format must be either :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_Mono` or :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_MonoLSB`. Use :sip:ref:`~PyQt6.QtGui.QImage.Format.Format_Mono` to specify data on the XBM format.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QBitmap.fromImage`.
