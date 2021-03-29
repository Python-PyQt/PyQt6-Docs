.. sip:signal-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 26d800823f0c03b6b935718dd48e1b7f

This signal is emitted whenever the content of the document changes in a way that affects the modification state. If *changed* is true, the document has been modified; otherwise it is false.

For example, calling :sip:ref:`~PyQt6.QtGui.QTextDocument.setModified`\ (false) on a document and then inserting text causes the signal to get emitted. If you undo that operation, causing the document to return to its original unmodified state, the signal will get emitted again.
