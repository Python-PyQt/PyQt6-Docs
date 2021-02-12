.. sip:method-description::
    :status: todo
    :pysig: 14cfca2ae20c9a1cdd63b7e4750587c1
    :realsig: (const QProcessEnvironment&)
    :digest: 647f9a9e0b23bc3de07ce32e0d3eddc5

Sets the *environment* that `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ will pass to the child process.

For example, the following code adds the environment variable ``TMPDIR``:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qprocess-environment-main.py
    :lines: 69-73

Note how, on Windows, environment variable names are case-insensitive.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.processEnvironment`, :sip:ref:`~PyQt6.QtCore.QProcessEnvironment.systemEnvironment`, setEnvironment().
