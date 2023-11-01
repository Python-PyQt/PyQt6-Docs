.. sip:method-description::
    :status: todo
    :pysig: 343bada708610e255929d9e8bde01fd7
    :realsig: (int, int, int, int, int, const QString&, QRect*)
    :digest: 03051bf5ad53d77dc7a4bb9e761d995e

This is an overloaded function.

Draws the given *text* within the rectangle with origin (\ *x*, *y*), *width* and *height*.

The *boundingRect* (if not null) is set to the what the bounding rectangle should be in order to enclose the whole text. For example, in the following image, the dotted line represents *boundingRect* as calculated by the function, and the dashed line represents the rectangle defined by *x*, *y*, *width* and *height*:

+----------------------------------+-----------------------------------------------------------------------------------------------------+
| |image-qpainter-text-bounds-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|                                  |     :lines: 395-411                                                                                 |
+----------------------------------+-----------------------------------------------------------------------------------------------------+

The *flags* argument is a bitwise OR of the following flags:

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignLeft`

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignRight`

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignHCenter`

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignJustify`

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignTop`

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignBottom`

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignVCenter`

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignCenter`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextSingleLine`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextExpandTabs`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextShowMnemonic`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextWordWrap`

By default, :sip:ref:`~PyQt6.QtGui.QPainter` draws text anti-aliased.

**Note:** The y-position is used as the top of the font.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.Alignment`, :sip:ref:`~PyQt6.QtCore.Qt.TextFlag`, :sip:ref:`~PyQt6.QtGui.QPainter.setFont`, :sip:ref:`~PyQt6.QtGui.QPainter.setPen`.

.. |image-qpainter-text-bounds-png| image:: ../../../images/qpainter-text-bounds.png
