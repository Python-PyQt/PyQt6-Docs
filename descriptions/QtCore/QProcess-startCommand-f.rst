.. sip:method-description::
    :status: todo
    :pysig: 524b1a5c9d574fa2c581bf621b6c99c5
    :realsig: (const QString&,QIODeviceBase::OpenMode)
    :digest: f964f39f0d949c90a4f1af2af4a87ade

Starts the command *command* in a new process. The OpenMode is set to *mode*.

*command* is a single string of text containing both the program name and its arguments. The arguments are separated by one or more spaces. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qprocess.py
    :lines: 115-118

Arguments containing spaces must be quoted to be correctly supplied to the new process. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qprocess.py
    :lines: 123-124

Literal quotes in the *command* string are represented by triple quotes. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qprocess.py
    :lines: 129-130

After the *command* string has been split and unquoted, this function behaves like :sip:ref:`~PyQt6.QtCore.QProcess.start`.

On operating systems where the system API for passing command line arguments to a subprocess natively uses a single string (Windows), one can conceive command lines which cannot be passed via `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_'s portable list-based API. In these rare cases you need to use :sip:ref:`~PyQt6.QtCore.QProcess.setProgram` and setNativeArguments() instead of this function.

.. seealso:: splitCommand(), :sip:ref:`~PyQt6.QtCore.QProcess.start`.
