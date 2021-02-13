.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 5df25c0028eec6bcf5d50dc6c5b2301c

Sets the name of the output file to *fileName*.

Setting a null or empty name (0 or "") disables printing to a file. Setting a non-empty name enables printing to a file.

This can change the value of :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.outputFormat`. If the file name has the ".pdf" suffix PDF is generated. If the file name has a suffix other than ".pdf", the output format used is the one set with :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setOutputFormat`.

:sip:ref:`~PyQt6.QtPrintSupport.QPrinter` uses Qt's cross-platform PDF print engines respectively. If you can produce this format natively, for example macOS can generate PDF's from its print engine, set the output format back to :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.OutputFormat.NativeFormat`.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.outputFileName`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setOutputFormat`.
