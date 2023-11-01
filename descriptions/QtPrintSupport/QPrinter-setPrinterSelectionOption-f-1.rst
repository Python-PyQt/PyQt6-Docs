.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: aea446669da489e842523ca28a5d9b1e

Sets the printer to use *option* to select the printer. *option* is null by default (which implies that Qt should be smart enough to guess correctly), but it can be set to other values to use a specific printer selection option.

If the printer selection option is changed while the printer is active, the current print job may or may not be affected.

This function has no effect on Windows or Mac.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.printerSelectionOption`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setPrintProgram`.
