.. sip:method-description::
    :status: todo
    :pysig: 3492941b7185ab01b7b322b81d6a6906
    :realsig: (const QRectF&, int, const QString&, QRectF*)
    :digest: 957ea6778ca59bf0277a440fbe89f783

Draws the given *text* within the provided *rectangle*. The *rectangle* along with alignment *flags* defines the anchors for the *text*.

+---------------------------+-----------------------------------------------------------------------------------------------------+
| |image-qpainter-text-png| | .. literalinclude:: ../../../snippets/qtbase-src-gui-doc-snippets-code-src_gui_painting_qpainter.py |
|                           |     :lines: 323-324                                                                                 |
+---------------------------+-----------------------------------------------------------------------------------------------------+

The *boundingRect* (if not null) is set to what the bounding rectangle should be in order to enclose the whole text. For example, in the following image, the dotted line represents *boundingRect* as calculated by the function, and the dashed line represents *rectangle*:

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

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextDontClip`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextSingleLine`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextExpandTabs`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextShowMnemonic`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextWordWrap`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextIncludeTrailingSpaces`

By default, :sip:ref:`~PyQt6.QtGui.QPainter` draws text anti-aliased.

**Note:** The y-coordinate of *rectangle* is used as the top of the font.

.. seealso:: :sip:ref:`~PyQt6.QtCore.Qt.AlignmentFlag`, :sip:ref:`~PyQt6.QtCore.Qt.TextFlag`, :sip:ref:`~PyQt6.QtGui.QPainter.boundingRect`, :sip:ref:`~PyQt6.QtGui.QPainter.layoutDirection`.

.. |image-qpainter-text-png| image:: ../../../images/qpainter-text.png
.. |image-qpainter-text-bounds-png| image:: ../../../images/qpainter-text-bounds.png
