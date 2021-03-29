.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: f7fb5a8e9c961c88dd4a5ae4dcea9c01

Sets the number of pixels that fit vertically in a physical meter, to *y*.

Together with :sip:ref:`~PyQt6.QtGui.QImage.dotsPerMeterX`, this number defines the intended scale and aspect ratio of the image, and determines the scale at which :sip:ref:`~PyQt6.QtGui.QPainter` will draw graphics on the image. It does not change the scale or aspect ratio of the image when it is rendered on other paint devices.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QImage.dotsPerMeterY`, Image Information.
