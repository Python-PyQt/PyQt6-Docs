.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: bcfbd4a5a95e622094fbf60a89eaa5c9

Sets the printer name to *name*.

If the *name* is empty then the output format will be set to :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.OutputFormat.PdfFormat`.

If the *name* is not a valid printer then no change will be made.

If the *name* is a valid printer then the output format will be set to :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.OutputFormat.NativeFormat`.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.printerName`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.isValid`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setOutputFormat`.
