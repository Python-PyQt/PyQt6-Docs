.. sip:class-description::
    :status: todo
    :brief: Dialog for specifying the printer's configuration
    :digest: 56a3b9685c316db4cdfdf0f27101870d

The :sip:ref:`~PyQt6.QtPrintSupport.QPrintDialog` class provides a dialog for specifying the printer's configuration.

The dialog allows users to change document-related settings, such as the paper size and orientation, type of print (color or grayscale), range of pages, and number of copies to print.

Controls are also provided to enable users to choose from the printers available, including any configured network printers.

Typically, :sip:ref:`~PyQt6.QtPrintSupport.QPrintDialog` objects are constructed with a :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` object, and executed using the :sip:ref:`~PyQt6.QtPrintSupport.QPrintDialog.exec` function.

.. literalinclude:: ../../../snippets/qtbase-src-printsupport-doc-snippets-code-src_gui_dialogs_qabstractprintdialog.py
    :lines: 54-57

If the dialog is accepted by the user, the :sip:ref:`~PyQt6.QtPrintSupport.QPrinter` object is correctly configured for printing.

+-----------------------------------+----------------------------------------------+
| |image-plastique-printdialog-png| | |image-plastique-printdialog-properties-png| |
+-----------------------------------+----------------------------------------------+

The printer dialog (shown above in Plastique style) enables access to common printing properties. On X11 platforms that use the CUPS printing system, the settings for each available printer can be modified via the dialog's Properties push button.

On Windows and macOS, the native print dialog is used, which means that some :sip:ref:`~PyQt6.QtWidgets.QWidget` and :sip:ref:`~PyQt6.QtWidgets.QDialog` properties set on the dialog won't be respected. The native print dialog on macOS does not support setting printer options, i.e. :sip:ref:`~PyQt6.QtPrintSupport.QPrintDialog.setOptions` and :sip:ref:`~PyQt6.QtPrintSupport.QPrintDialog.setOption` have no effect.

In Qt 4.4, it was possible to use the static functions to show a sheet on macOS. This is no longer supported in Qt 4.5. If you want this functionality, use :sip:ref:`~PyQt6.QtPrintSupport.QPrintDialog.open`.

.. seealso:: :sip:ref:`~PyQt6.QtPrintSupport.QPageSetupDialog`, :sip:ref:`~PyQt6.QtPrintSupport.QPrinter`.

.. |image-plastique-printdialog-png| image:: ../../../images/plastique-printdialog.png
.. |image-plastique-printdialog-properties-png| image:: ../../../images/plastique-printdialog-properties.png
