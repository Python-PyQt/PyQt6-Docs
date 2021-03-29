.. sip:method-description::
    :status: todo
    :pysig: 8c8087fd493f0f74ea1c4101775fe081
    :realsig: ()
    :digest: b35b9ec45f1931e991fa520d51f62af6

Returns the default printer on the system.

The return value should be checked using :sip:ref:`~PyQt6.QtPrintSupport.QPrinterInfo.isNull` before being used, in case there is no default printer.

On some systems it is possible for there to be available printers but none of them set to be the default printer.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinterInfo.isNull`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinterInfo.isDefault`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinterInfo.availablePrinters`.
