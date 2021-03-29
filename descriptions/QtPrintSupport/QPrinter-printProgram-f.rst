.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: a16f284cb814c2a821f79fbc61be06b0

Returns the name of the program that sends the print output to the printer.

The default is to return an empty string; meaning that :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` will try to be smart in a system-dependent way. On X11 only, you can set it to something different to use a specific print program. On the other platforms, this returns an empty string.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setPrintProgram`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setPrinterSelectionOption`.
