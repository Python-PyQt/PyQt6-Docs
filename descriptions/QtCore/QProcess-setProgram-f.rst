.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: (const QString&)
    :digest: 9d0338a2aa49dab7d56886fb4e6b38bd

Set the *program* to use when starting the process. This function must be called before :sip:ref:`~PyQt6.QtCore.QProcess.start`.

If *program* is an absolute path, it specifies the exact executable that will be launched. Relative paths will be resolved in a platform-specific manner, which includes searching the ``PATH`` environment variable (see :ref:`qprocess-finding-the-executable` for details).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.start`, :sip:ref:`~PyQt6.QtCore.QProcess.setArguments`, :sip:ref:`~PyQt6.QtCore.QProcess.program`, :sip:ref:`~PyQt6.QtCore.QStandardPaths.findExecutable`.
