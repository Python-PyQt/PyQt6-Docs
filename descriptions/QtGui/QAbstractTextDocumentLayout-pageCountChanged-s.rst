.. sip:signal-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: (int)
    :digest: f488547f29cd1eefb7cadaf4a6c82ea5

This signal is emitted when the number of pages in the layout changes; *newPages* is the updated page count.

Subclasses of :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout` should emit this signal when the number of pages in the layout has changed. Changes to the page count are caused by changes to the layout or the document content itself.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAbstractTextDocumentLayout.pageCount`.
