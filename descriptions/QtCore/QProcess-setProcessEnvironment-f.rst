.. sip:method-description::
    :status: todo
    :pysig: 14cfca2ae20c9a1cdd63b7e4750587c1
    :realsig: (const QProcessEnvironment&)
    :digest: 712c32fa1f02c6dfe97ab4c27a4efc60

Sets the *environment* that :sip:ref:`~PyQt6.QtCore.QProcess` will pass to the child process.

For example, the following code adds the environment variable ``TMPDIR``:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qprocess-environment-main.py
    :lines: 69-73

Note how, on Windows, environment variable names are case-insensitive.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.processEnvironment`, :sip:ref:`~PyQt6.QtCore.QProcessEnvironment.systemEnvironment`, :ref:`qprocess-environment-variables`.
