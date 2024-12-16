.. sip:method-description::
    :status: todo
    :pysig: 364191bc772363d61cf96ad3eac70cf9
    :realsig: (const QSize&)
    :digest: 6021f6904b6a2b38a1c6065ea4f2b2ff

Sets the scaled size of the image to *size*. The scaling is performed after the initial clip rect, but before the scaled clip rect is applied. The algorithm used for scaling depends on the image format. By default (i.e., if the image format does not support scaling), :sip:ref:`~PyQt6.QtGui.QImageReader` will use QImage::scale() with Qt::SmoothScaling.

If only one dimension is set in *size*, the other one will be computed from the image's :sip:ref:`~PyQt6.QtGui.QImageReader.size` so as to maintain the aspect ratio.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.scaledSize`, :sip:ref:`~PyQt6.QtGui.QImageReader.setClipRect`, :sip:ref:`~PyQt6.QtGui.QImageReader.setScaledClipRect`.
