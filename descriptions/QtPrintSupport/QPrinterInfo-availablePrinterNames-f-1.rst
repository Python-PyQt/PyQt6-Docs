.. sip:method-description::
    :status: todo
    :pysig: d409847c33b4369753f8b837c22758e9
    :realsig: ()
    :digest: 71cf259b6f785d11f92cb624081661f2

Returns a list of all the available Printer Names on this system.

It is recommended to use this instead of :sip:ref:`~PyQt6.QtPrintSupport.QPrinterInfo.availablePrinters` as it will be faster on most systems.

Note that the list may become outdated if changes are made on the local system or remote print server. Only instantiate required :sip:ref:`~PyQt6.QtPrintSupport.QPrinterInfo` instances when needed, and always check for validity before calling.
