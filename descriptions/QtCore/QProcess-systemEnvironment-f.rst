.. sip:method-description::
    :status: todo
    :pysig: 2959872364c7b497ae5baab9d50a0314
    :realsig: ()
    :digest: c2d2bccb3b06b028a3ce5d95a10eed7b

Returns the environment of the calling process as a list of key=value pairs. Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qprocess.py
    :lines: 135-137

This function does not cache the system environment. Therefore, it's possible to obtain an updated version of the environment if low-level C library functions like ``setenv`` or ``putenv`` have been called.

However, note that repeated calls to this function will recreate the list of environment variables, which is a non-trivial operation.

**Note:** For new code, it is recommended to use :sip:ref:`~PyQt6.QtCore.QProcessEnvironment.systemEnvironment`

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcessEnvironment.systemEnvironment`, :sip:ref:`~PyQt6.QtCore.QProcess.setProcessEnvironment`.
