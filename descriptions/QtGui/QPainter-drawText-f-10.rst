.. sip:method-description::
    :status: todo
    :pysig: daacd402103e83e3d5aac335b6a4f8ae
    :realsig: (const QRect&, int, const QString&, QRect*)
    :digest: ed49a133ee26cde86d1a73bb5d13e494

This is an overloaded function.

Draws the given *text* within the provided *rectangle* according to the specified *flags*.

The *boundingRect* (if not null) is set to the what the bounding rectangle should be in order to enclose the whole text. For example, in the following image, the dotted line represents *boundingRect* as calculated by the function, and the dashed line represents *rectangle*:

+----------------------------------+-----------------------------------------------------------------------------------------------------+
| |image-qpainter-text-bounds-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|                                  |     :lines: 395-411                                                                                 |
+----------------------------------+-----------------------------------------------------------------------------------------------------+

By default, :sip:ref:`~PyQt6.QtGui.QPainter` draws text anti-aliased.

**Note:** The y-coordinate of *rectangle* is used as the top of the font.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.setFont`, :sip:ref:`~PyQt6.QtGui.QPainter.setPen`.

.. |image-qpainter-text-bounds-png| image:: ../../../images/qpainter-text-bounds.png
