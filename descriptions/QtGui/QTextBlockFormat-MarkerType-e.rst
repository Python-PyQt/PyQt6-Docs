.. sip:enum-description::
    :status: todo
    :digest: e320e749d2d51265b34d81eb565ace31

This enum describes the types of markers a list item can have. If a list item (a paragraph for which :sip:ref:`~PyQt6.QtGui.QTextBlock.textList` returns the list) has a marker, it is rendered instead of the normal bullet. In this way, checkable list items can be mixed with plain list items in the same list, overriding the type of bullet specified by the :sip:ref:`~PyQt6.QtGui.QTextListFormat.style` for the entire list.

In the future, this may be extended to specify other types of paragraph decorations.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextListFormat.style`.
