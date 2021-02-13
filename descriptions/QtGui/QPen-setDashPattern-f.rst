.. sip:method-description::
    :status: todo
    :pysig: 13ab3c5e77307569196120fd7ddfef82
    :realsig: (const QList<qreal>&)
    :digest: 95c4d8bfe6cb49eb75c4c23a294cf9f3

Sets the dash pattern for this pen to the given *pattern*. This implicitly converts the style of the pen to :sip:ref:`~PyQt6.QtCore.Qt.PenStyle.CustomDashLine`.

The pattern must be specified as an even number of positive entries where the entries 1, 3, 5... are the dashes and 2, 4, 6... are the spaces. For example:

+-------------------------+-------------------------------------------------------------------------------------------------+
| |image-qpen-custom-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpen.py |
|                         |     :lines: 111-116                                                                             |
+-------------------------+-------------------------------------------------------------------------------------------------+

The dash pattern is specified in units of the pens width; e.g. a dash of length 5 in width 10 is 50 pixels long. Note that a pen with zero width is equivalent to a cosmetic pen with a width of 1 pixel.

Each dash is also subject to cap styles so a dash of 1 with square cap set will extend 0.5 pixels out in each direction resulting in a total width of 2.

Note that the default cap style is :sip:ref:`~PyQt6.QtCore.Qt.PenCapStyle.SquareCap`, meaning that a square line end covers the end point and extends beyond it by half the line width.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPen.setStyle`, :sip:ref:`~PyQt6.QtGui.QPen.dashPattern`, :sip:ref:`~PyQt6.QtGui.QPen.setCapStyle`, :sip:ref:`~PyQt6.QtGui.QPen.setCosmetic`.

.. |image-qpen-custom-png| image:: ../../../images/qpen-custom.png
