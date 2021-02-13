.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 5a9e00d0624ff5643789b4ee3f463eab

Sets the miter limit of this pen to the given *limit*.

.. image:: ../../../images/qpen-miterlimit.png

The miter limit describes how far a miter join can extend from the join point. This is used to reduce artifacts between line joins where the lines are close to parallel.

This value does only have effect when the pen style is set to :sip:ref:`~PyQt6.QtCore.Qt.PenJoinStyle.MiterJoin`. The value is specified in units of the pen's width, e.g. a miter limit of 5 in width 10 is 50 pixels long. The default miter limit is 2, i.e. twice the pen width in pixels.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPen.miterLimit`, :sip:ref:`~PyQt6.QtGui.QPen.setJoinStyle`, Join Style.
