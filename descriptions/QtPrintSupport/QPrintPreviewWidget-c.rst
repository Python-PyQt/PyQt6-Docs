.. sip:class-description::
    :status: todo
    :brief: Widget for previewing page layouts for printer output
    :digest: cb54db21b7548bd908447d8764c88b9a

The :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget` class provides a widget for previewing page layouts for printer output.

:sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewDialog` uses a :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget` internally, and the purpose of :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget` is to make it possible to embed the preview into other widgets. It also makes it possible to build a different user interface around it than the default one provided with :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewDialog`.

Using :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget` is straightforward:

#. Create the :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget`

   Construct the :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget` either by passing in an existing :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` object, or have :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget` create a default constructed :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` object for you.

#. Connect the :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget.paintRequested` signal to a slot.

   When the widget needs to generate a set of preview pages, a :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewWidget.paintRequested` signal will be emitted from the widget. Connect a slot to this signal, and draw onto the :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` passed in as a signal parameter. Call :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.newPage`, to start a new page in the preview.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`, :sip:ref:`~PyQt6.QtPrintSupport.QPrintDialog`, :sip:ref:`~PyQt6.QtPrintSupport.QPageSetupDialog`, :sip:ref:`~PyQt6.QtPrintSupport.QPrintPreviewDialog`.
