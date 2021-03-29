.. sip:class-description::
    :status: todo
    :brief: Configuration dialog for the page-related options on a printer
    :digest: 38f2a186776a0fb42241e584c4d209af

The :sip:ref:`~PyQt6.QtPrintSupport.QPageSetupDialog` class provides a configuration dialog for the page-related options on a printer.

On Windows and macOS the page setup dialog is implemented using the native page setup dialogs.

Note that on Windows and macOS custom paper sizes won't be reflected in the native page setup dialogs. Additionally, custom page margins set on a :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` won't show in the native macOS page setup dialog.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`, :sip:ref:`~PyQt6.QtPrintSupport.QPrintDialog`.
