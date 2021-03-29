.. sip:method-description::
    :status: todo
    :pysig: c57c4dcf862b70ffa7fe16635a87b1b0
    :realsig: (QPrinter::PageOrder)
    :digest: 842825f910bcbdaeda03929f05bb0c37

Sets the page order to *pageOrder*.

The page order can be :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.PageOrder.FirstPageFirst` or :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.PageOrder.LastPageFirst`. The application is responsible for reading the page order and printing accordingly.

This function is mostly useful for setting a default value that the user can override in the print dialog.

This function is only supported under X11.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.pageOrder`.
