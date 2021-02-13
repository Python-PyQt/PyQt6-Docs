.. sip:method-description::
    :status: todo
    :pysig: 61569f2965b7a369eb10b6d75d410d11
    :realsig: (int,int)
    :digest: e4aa81d0bca69f1e10260df983a58fed

Sets the range of pages to be printed to cover the pages with numbers specified by *from* and *to*, where *from* corresponds to the first page in the range and *to* corresponds to the last.

**Note:** Pages in a document are numbered according to the convention that the first page is page 1. However, if *from* and *to* are both set to 0, the *whole document will be printed*.

This function is mostly used to set a default value that the user can override in the print dialog when you call setup().

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.fromPage`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.toPage`, pageRanges().
