.. sip:method-description::
    :status: todo
    :pysig: 343bada708610e255929d9e8bde01fd7
    :realsig: (int, int, int, int, int, const QString&, QRect*)
    :digest: f2a7d417123056e67a89e9cb49db4681

Draws the given *text* within the rectangle with origin (\ *x*, *y*), *width* and *height*.

The *boundingRect* (if not null) is set to the what the bounding rectangle should be in order to enclose the whole text. For example, in the following image, the dotted line represents *boundingRect* as calculated by the function, and the dashed line represents the rectangle defined by *x*, *y*, *width* and *height*:

+----------------------------------+-----------------------------------------------------------------------------------------------------+
| |image-qpainter-text-bounds-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|                                  |     :lines: 395-411                                                                                 |
+----------------------------------+-----------------------------------------------------------------------------------------------------+

The *flags* argument is a bitwise OR of the following flags:

* :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag.AlignLeft`

* :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag.AlignRight`

* :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag.AlignHCenter`

* :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag.AlignJustify`

* :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag.AlignTop`

* :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag.AlignBottom`

* :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag.AlignVCenter`

* :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag.AlignCenter`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextSingleLine`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextExpandTabs`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextShowMnemonic`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextWordWrap`

By default, :sip:ref:`~PyQt6.QtGui.QPainter` draws text anti-aliased.

**Note:** The y-position is used as the top of the font.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`, :sip:ref:`~PyQt6.QtCore.Qt.TextFlag`, :sip:ref:`~PyQt6.QtGui.QPainter.setFont`, :sip:ref:`~PyQt6.QtGui.QPainter.setPen`.

.. |image-qpainter-text-bounds-png| image:: ../../../images/qpainter-text-bounds.png
