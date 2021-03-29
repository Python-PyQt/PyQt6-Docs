.. sip:method-description::
    :status: todo
    :pysig: b53f1d5b1a4365230bd1d8ab3bf9ddec
    :realsig: (const QSize&,Qt::AspectRatioMode,Qt::TransformationMode) const
    :digest: 7fc9363c69a2c6240e727d94c4c1c219

Scales the pixmap to the given *size*, using the aspect ratio and transformation modes specified by *aspectRatioMode* and *transformMode*.

.. image:: ../../../images/qimage-scaling.png

* If *aspectRatioMode* is :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.IgnoreAspectRatio`, the pixmap is scaled to *size*.

* If *aspectRatioMode* is :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.KeepAspectRatio`, the pixmap is scaled to a rectangle as large as possible inside *size*, preserving the aspect ratio.

* If *aspectRatioMode* is :sip:ref:`~PyQt6.QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding`, the pixmap is scaled to a rectangle as small as possible outside *size*, preserving the aspect ratio.

If the given *size* is empty, this function returns a null pixmap.

In some cases it can be more beneficial to draw the pixmap to a painter with a scale set rather than scaling the pixmap. This is the case when the painter is for instance based on OpenGL or when the scale factor changes rapidly.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPixmap.isNull`, Pixmap Transformations.
