.. sip:method-description::
    :status: todo
    :pysig: 59bf221f290b7b3c761aac45fcfb19c8
    :realsig: (const QSize&,Qt::AspectRatioMode,Qt::TransformationMode) const
    :digest: 1afd2492e1ed9d2bee13fb6627abaf61

Returns a copy of the image scaled to a rectangle defined by the given *size* according to the given *aspectRatioMode* and *transformMode*.

.. image:: ../../../images/qimage-scaling.png

* If *aspectRatioMode* is :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio`, the image is scaled to *size*.

* If *aspectRatioMode* is :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.KeepAspectRatio`, the image is scaled to a rectangle as large as possible inside *size*, preserving the aspect ratio.

* If *aspectRatioMode* is :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding`, the image is scaled to a rectangle as small as possible outside *size*, preserving the aspect ratio.

If the given *size* is empty, this function returns a null image.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.isNull`, Image Transformations.
