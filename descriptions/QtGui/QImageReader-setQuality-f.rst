.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 4593d62aa68a93ffb30844dc7550543b

Sets the quality setting of the image format to *quality*.

Some image formats, in particular lossy ones, entail a tradeoff between a) visual quality of the resulting image, and b) decoding execution time. This function sets the level of that tradeoff for image formats that support it.

In case of scaled image reading, the quality setting may also influence the tradeoff level between visual quality and execution speed of the scaling algorithm.

The value range of *quality* depends on the image format. For example, the "jpeg" format supports a quality range from 0 (low visual quality) to 100 (high visual quality).

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImageReader.quality`, :sip:ref:`~PyQt6.QtGui.QImageReader.setScaledSize`.
