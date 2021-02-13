.. sip:class-description::
    :status: todo
    :brief: Paint device that paints on a printer
    :digest: 5ac81c7bd66de007793c23565b624c42

The :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` class is a paint device that paints on a printer.

This device represents a series of pages of printed output, and is used in almost exactly the same way as other paint devices such as `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ and :sip:ref:`~PyQt6.QtGui.QPixmap`. A set of additional functions are provided to manage device-specific features, such as orientation and resolution, and to step through the pages in a document as it is generated.

When printing directly to a printer on Windows or macOS, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` uses the built-in printer drivers. On X11, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` uses the Common Unix Printing System (CUPS) to send PDF output to the printer. As an alternative, the :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.printProgram` function can be used to specify the command or utility to use instead of the system default.

Note that setting parameters like paper size and resolution on an invalid printer is undefined. You can use :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.isValid` to verify this before changing any parameters.

:sip:ref:`~PyQt6.QtPrintSupport.QPrinter` supports a number of parameters, most of which can be changed by the end user through a :sip:ref:`~PyQt6.QtPrintSupport.QPrintDialog`. In general, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` passes these functions onto the underlying :sip:ref:`~PyQt6.QtPrintSupport.QPrintEngine`.

The most important parameters are:

* setPageLayout() tells :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` which page orientation to use, and what size to expect from the printer.

* :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setResolution` tells :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` what resolution you wish the printer to provide, in dots per inch (DPI).

* :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setFullPage` tells :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` whether you want to deal with the full page or just with the part the printer can draw on.

* :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.setCopyCount` tells :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` how many copies of the document it should print.

Many of these functions can only be called before the actual printing begins (i.e., before :sip:ref:`~PyQt6.QtGui.QPainter.begin` is called). This usually makes sense because, for example, it's not possible to change the number of copies when you are halfway through printing. There are also some settings that the user sets (through the printer dialog) and that applications are expected to obey. See :sip:ref:`~PyQt6.QtPrintSupport.QAbstractPrintDialog`'s documentation for more details.

When :sip:ref:`~PyQt6.QtGui.QPainter.begin` is called, the :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` it operates on is prepared for a new page, enabling the :sip:ref:`~PyQt6.QtGui.QPainter` to be used immediately to paint the first page in a document. Once the first page has been painted, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.newPage` can be called to request a new blank page to paint on, or :sip:ref:`~PyQt6.QtGui.QPainter.end` can be called to finish printing. The second page and all following pages are prepared using a call to :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.newPage` before they are painted.

The first page in a document does not need to be preceded by a call to :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.newPage`. You only need to calling :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.newPage` after :sip:ref:`~PyQt6.QtGui.QPainter.begin` if you need to insert a blank page at the beginning of a printed document. Similarly, calling :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.newPage` after the last page in a document is painted will result in a trailing blank page appended to the end of the printed document.

If you want to abort the print job, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter.abort` will try its best to stop printing. It may cancel the entire job or just part of it.

Since :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` can print to any :sip:ref:`~PyQt6.QtPrintSupport.QPrintEngine` subclass, it is possible to extend printing support to cover new types of printing subsystem by subclassing :sip:ref:`~PyQt6.QtPrintSupport.QPrintEngine` and reimplementing its interface.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrintDialog`, `Qt Print Support <https://doc.qt.io/qt-6/qtprintsupport-index.html>`_.
