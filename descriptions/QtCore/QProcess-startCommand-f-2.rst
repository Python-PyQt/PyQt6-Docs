.. sip:method-description::
    :status: todo
    :pysig: db9e987ef4095603eb9a90fba7ad8846
    :realsig: (const QString&, QIODeviceBase::OpenMode)
    :digest: c528fcab1e0ce90dcbd5d6cbb6bb1a75

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

On operating systems where the system API for passing command line arguments to a subprocess natively uses a single string (Windows), one can conceive command lines which cannot be passed via :sip:ref:`~PyQt6.QtCore.QProcess`'s portable list-based API. In these rare cases you need to use :sip:ref:`~PyQt6.QtCore.QProcess.setProgram` and setNativeArguments() instead of this function.

.. seealso:: splitCommand(), :sip:ref:`~PyQt6.QtCore.QProcess.start`.
