.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (qreal)
    :digest: 030ba6862f27ddf24e265bf4af789d1c

Sets the dash offset (the starting point on the dash pattern) for this pen to the *offset* specified. The offset is measured in terms of the units used to specify the dash pattern.

+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| |image-qpen-dashpattern-png| | For example, a pattern where each stroke is four units long, followed by a gap of two units, will begin with the stroke when drawn as a line.                                                                                                                      |
|                              |                                                                                                                                                                                                                                                                    |
|                              | However, if the dash offset is set to 4.0, any line drawn will begin with the gap. Values of the offset up to 4.0 will cause part of the stroke to be drawn first, and values of the offset between 4.0 and 6.0 will cause the line to begin with part of the gap. |
+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Note:** This implicitly converts the style of the pen to :sip:ref:`~PyQt6.QtCore.Qt.PenStyle.CustomDashLine`.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPen.dashOffset`.

.. |image-qpen-dashpattern-png| image:: ../../../images/qpen-dashpattern.png
