.. sip:method-description::
    :status: todo
    :pysig: 22b7f5463612f0c82a57f286edaa8749
    :realsig: (const QByteArray&, const QString&)
    :digest: 9c129313399bb243fe59404ddd259a12

This is a convenience static function that saves *fileContent* to a file, using a file name and location chosen by the user. *fileNameHint* can be provided to suggest a file name to the user.

This function is used to save files to the local file system on Qt for WebAssembly, where the web sandbox places restrictions on how such access may happen. Its implementation will make the browser display a native file dialog, where the user makes the file selection.

It can also be used on other platforms, where it will fall back to using :sip:ref:`~PyQt6.QtWidgets.QFileDialog`.

The function is asynchronous and returns immediately.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 161-162
