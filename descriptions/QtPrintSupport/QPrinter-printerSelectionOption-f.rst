.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 440707605180a7960775195b6c6f4d4c

Returns the printer options selection string. This is useful only if the print command has been explicitly set.

The default value (an empty string) implies that the printer should be selected in a system-dependent manner.

Any other value implies that the given value should be used.

This function always returns an empty string on Windows and Mac.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setPrinterSelectionOption`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setPrintProgram`.
