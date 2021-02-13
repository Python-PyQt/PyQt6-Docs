.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: afba070fbe5609c3b48790544e944f41

Sets the number of pixels that fit horizontally in a physical meter, to *x*.

Together with :sip:ref:`~PyQt6.QtGui.QImage.dotsPerMeterY`, this number defines the intended scale and aspect ratio of the image, and determines the scale at which :sip:ref:`~PyQt6.QtGui.QPainter` will draw graphics on the image. It does not change the scale or aspect ratio of the image when it is rendered on other paint devices.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.dotsPerMeterX`, Image Information.
