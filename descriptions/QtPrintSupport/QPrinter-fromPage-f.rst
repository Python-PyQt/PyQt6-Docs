.. sip:method-description::
    :status: todo
    :pysig: fa7153f7ed1cb6c0fcf2ffb2fac21748
    :realsig: () const
    :digest: 56abb649bd1c7361886d8595bbab4c41

Returns the number of the first page in a range of pages to be printed (the "from page" setting). Pages in a document are numbered according to the convention that the first page is page 1.

By default, this function returns a special value of 0, meaning that the "from page" setting is unset.

**Note:** If  and :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.toPage` both return 0, this indicates that *the whole document will be printed*.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setFromTo`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.toPage`, pageRanges().
