.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 560ffcf8c0cfa40019b1a6c973ba0032

Aborts the current print run. Returns ``true`` if the print run was successfully aborted and :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.printerState` will return :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.PrinterState.Aborted`; otherwise returns ``false``.

It is not always possible to abort a print job. For example, all the data has gone to the printer but the printer cannot or will not cancel the job when asked to.
