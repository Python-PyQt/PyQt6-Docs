.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 959e5743cea4e5eb7894928f55d040de

Returns ``true`` if the printer supports printing multiple copies of the same document in one job; otherwise false is returned.

On most systems this function will return true. However, on X11 systems that do not support CUPS, this function will return false. That means the application has to handle the number of copies by printing the same document the required number of times.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setCopyCount`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.copyCount`.
