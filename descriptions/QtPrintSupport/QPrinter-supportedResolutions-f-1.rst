.. sip:method-description::
    :status: todo
    :pysig: 2e0b8f22613494b44c9678f7b212141a
    :realsig: () const
    :digest: bc7d09241f8c3d18bd28ce016e442880

Returns a list of the resolutions (a list of dots-per-inch integers) that the printer says it supports.

For X11 where all printing is directly to PDF, this function will always return a one item list containing only the PDF resolution, i.e., 72 (72 dpi – but see :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.PrinterMode.PrinterMode`).
