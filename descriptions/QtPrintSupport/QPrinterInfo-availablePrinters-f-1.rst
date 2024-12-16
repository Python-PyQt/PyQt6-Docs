.. sip:method-description::
    :status: todo
    :pysig: f6ee93f7338ad6c56fcaee1ce07e2cd3
    :realsig: ()
    :digest: b6b515ca6664dc142005b3112237e64d

Returns a list of :sip:ref:`~PyQt6.QtPrintSupport.QPrinterInfo` objects for all the available printers on this system.

It is NOT recommended to use this as creating each printer instance may take a long time, especially if there are remote networked printers, and retained instances may become outdated if changes are made on the local system or remote print server. Use :sip:ref:`~PyQt6.QtPrintSupport.QPrinterInfo.availablePrinterNames` instead and only instantiate printer instances as you need them.
