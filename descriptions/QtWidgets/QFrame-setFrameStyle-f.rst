.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: 8d02ba8d980bd3ac17bcca082163257c

Sets the frame style to *style*.

The *style* is the bitwise OR between a frame shape and a frame shadow style. See the picture of the frames in the main class documentation.

The frame shapes are given in :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape` and the shadow styles in :sip:ref:`~PyQt6.QtWidgets.QFrame.Shadow`.

If a mid-line width greater than 0 is specified, an additional line is drawn for :sip:ref:`~PyQt6.QtWidgets.QFrame.Shadow.Raised` or :sip:ref:`~PyQt6.QtWidgets.QFrame.Shadow.Sunken` :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape.Box`, :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape.HLine`, and :sip:ref:`~PyQt6.QtWidgets.QFrame.Shape.VLine` frames. The mid-color of the current color group is used for drawing middle lines.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QFrame.frameStyle`.
