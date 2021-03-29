.. sip:method-description::
    :status: todo
    :pysig: 44853ba04dc108304654af48758a7c9a
    :realsig: (QPrinter::OutputFormat)
    :digest: 308de31e7580af64aab62289c9d74106

Sets the output format for this printer to *format*.

If *format* is the same value as currently set then no change will be made.

If *format* is :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.OutputFormat.NativeFormat` then the :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.printerName` will be set to the default printer. If there are no valid printers configured then no change will be made. If you want to set :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.OutputFormat.NativeFormat` with a specific :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.printerName` then use :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setPrinterName`.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.outputFormat`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setPrinterName`.
