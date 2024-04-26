.. sip:method-description::
    :status: todo
    :pysig: 00dca10a992e5fc5a830adddcd7ced48
    :realsig: (QPointF, QTextDocument*, int, int)
    :digest: 405d1fffbc2bd01d36a3fa16b9cba0ed

Adds the contents of *document* to the text node at *position*. If *selectionStart* is >= 0, then this marks the first character in a selected area of *selectionCount* number of characters. The selection is represented as a background fill with the :sip:ref:`~PyQt6.QtQuick.QSGTextNode.selectionColor` and the selected text is rendered in the :sip:ref:`~PyQt6.QtQuick.QSGTextNode.selectionTextColor`.

This function forwards its arguments to the virtual function doAddTextDocument().

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGTextNode.clear`.
