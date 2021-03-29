.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: eaf2c2d87992d909684397ac60ea5f2f

Returns ``true`` if collation is turned on when multiple copies is selected. Returns ``false`` if it is turned off when multiple copies is selected. When collating is turned off the printing of each individual page will be repeated the numCopies() amount before the next page is started. With collating turned on all pages are printed before the next copy of those pages is started.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setCollateCopies`.
