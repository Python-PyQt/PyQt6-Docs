.. sip:method-description::
    :status: todo
    :pysig: 2f1ecde80dab8a5c9d0a1483850077ec
    :realsig: (QPointF, QTextLayout*, int, int, int, int)
    :digest: 33b3568badcc558b7dfe16864fa45583

Adds the contents of *layout* to the text node at *position*. If *selectionStart* is >= 0, then this marks the first character in a selected area of *selectionCount* number of characters. The selection is represented as a background fill with the :sip:ref:`~PyQt6.QtQuick.QSGTextNode.selectionColor` and the selected text is rendered in the :sip:ref:`~PyQt6.QtQuick.QSGTextNode.selectionTextColor`.

For convenience, *lineStart* and *lineCount* can be used to select the range of :sip:ref:`~PyQt6.QtGui.QTextLine` objects to include from the layout. This can be useful, for instance, when creating elided layouts. If *lineCount* is < 0, then the the node will include the lines from *lineStart* to the end of the layout.

This function forwards its arguments to the virtual function doAddTextLayout().

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGTextNode.clear`.
