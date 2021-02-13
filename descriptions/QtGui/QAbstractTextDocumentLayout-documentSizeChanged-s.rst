.. sip:signal-description::
    :status: todo
    :pysig: c5d6e3115e754b395283dc1c09f54493
    :realsig: (const QSizeF&)
    :digest: d1526f8bf0ae20f15964a57d3b4dbb63

This signal is emitted when the size of the document layout changes to *newSize*.

Subclasses of :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout` should emit this signal when the document's entire layout size changes. This signal is useful for widgets that display text documents since it enables them to update their scroll bars correctly.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout.documentSize`.
