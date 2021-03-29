.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 882f1f47f582d440e2f2009d65bed3ab

Sets the quality setting of the image format to *quality*.

Some image formats, in particular lossy ones, entail a tradeoff between a) visual quality of the resulting image, and b) encoding execution time and compression level. This function sets the level of that tradeoff for image formats that support it. For other formats, this value is ignored.

The value range of *quality* depends on the image format. For example, the "jpeg" format supports a quality range from 0 (low visual quality, high compression) to 100 (high visual quality, low compression).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageWriter.quality`.
