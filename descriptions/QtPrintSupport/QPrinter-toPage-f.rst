.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 08edf8fee629870ee30f87a623295cfa

Returns the number of the last page in a range of pages to be printed (the "to page" setting). Pages in a document are numbered according to the convention that the first page is page 1.

By default, this function returns a special value of 0, meaning that the "to page" setting is unset.

**Note:** If :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.fromPage` and  both return 0, this indicates that *the whole document will be printed*.

The programmer is responsible for reading this setting and printing accordingly.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setFromTo`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.fromPage`, pageRanges().
