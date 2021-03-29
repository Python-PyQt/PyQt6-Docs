.. sip:method-description::
    :status: todo
    :pysig: 364191bc772363d61cf96ad3eac70cf9
    :realsig: (const QSize&)
    :digest: 46bd2f18c3f7143718740a5c3914e521

Sets the scaled size of the image to *size*. The scaling is performed after the initial clip rect, but before the scaled clip rect is applied. The algorithm used for scaling depends on the image format. By default (i.e., if the image format does not support scaling), :sip:ref:`~PyQt6.QtGui.QImageReader` will use QImage::scale() with Qt::SmoothScaling.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.scaledSize`, :sip:ref:`~PyQt6.QtGui.QImageReader.setClipRect`, :sip:ref:`~PyQt6.QtGui.QImageReader.setScaledClipRect`.
