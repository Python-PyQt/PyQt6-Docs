.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 437c793869080bc391a9aec0b678551c

Sets the document name to *name*.

On X11, the document name is for example used as the default output filename in :sip:ref:`~PyQt6.QtPrintSupport.QPrintDialog`. Note that the document name does not affect the file name if the printer is printing to a file. Use the setOutputFile() function for this.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.docName`, :sip:ref:`~PyQt6.QtPrintSupport.QPrintEngine.PrintEnginePropertyKey`.
