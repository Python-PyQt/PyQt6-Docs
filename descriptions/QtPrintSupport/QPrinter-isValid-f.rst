.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ca42791717e7ca3fc07be6ccb729ae98

Returns ``true`` if the printer currently selected is a valid printer in the system, or a pure PDF printer; otherwise returns ``false``.

To detect other failures check the output of :sip:ref:`~PyQt6.QtGui.QPainter.begin` or :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.newPage`.

.. literalinclude:: ../../../snippets/qtbase-src-printsupport-doc-snippets-printing-qprinter-errors.py
    :lines: 64-78

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setPrinterName`.
