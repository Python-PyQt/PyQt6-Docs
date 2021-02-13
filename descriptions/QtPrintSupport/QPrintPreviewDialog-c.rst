.. sip:class-description::
    :status: todo
    :brief: Dialog for previewing and configuring page layouts for printer output
    :digest: 073379db4e80720e04982ed68f36ca06

The :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewDialog` class provides a dialog for previewing and configuring page layouts for printer output.

Using :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewDialog` in your existing application is straightforward:

#. Create the :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewDialog`.

   You can construct a :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewDialog` with an existing :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` object, or you can have :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewDialog` create one for you, which will be the system default printer.

#. Connect the :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewDialog.paintRequested` signal to a slot.

   When the dialog needs to generate a set of preview pages, the :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewDialog.paintRequested` signal will be emitted. You can use the exact same code for the actual printing as for having the preview generated, including calling :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.newPage` to start a new page in the preview. Connect a slot to the :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewDialog.paintRequested` signal, where you draw onto the :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` object that is passed into the slot.

#. Call exec().

   Call QPrintPreviewDialog::exec() to show the preview dialog.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`, :sip:ref:`~PyQt6.QtPrintSupport.QPrintDialog`, :sip:ref:`~PyQt6.QtPrintSupport.QPageSetupDialog`, :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget`.
