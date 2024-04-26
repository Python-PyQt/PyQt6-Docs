.. sip:method-description::
    :status: todo
    :pysig: db2496c2cb0381bcccab30a3cf43ffbf
    :realsig: (const QByteArray&, const QString&, QWidget*)
    :digest: 5c0c4e8b92fe9108d23126f88f1c4a12

This is a convenience static function that saves *fileContent* to a file, using a file name and location chosen by the user. *fileNameHint* can be provided to suggest a file name to the user.

Use this function to save content to local files on Qt for WebAssembly, if the web sandbox restricts file access. Its implementation enables displaying a native file dialog in the browser, where the user specifies an output file based on the *fileNameHint* argument.

*parent* is ignored on Qt for WebAssembly. Pass *parent* on other platforms, to make the popup a child of another widget. If the platform doesn't support native file dialogs, the function falls back to :sip:ref:`~PyQt6.QtWidgets.QFileDialog`.

The function is asynchronous and returns immediately.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_dialogs_qfiledialog.py
    :lines: 161-162
