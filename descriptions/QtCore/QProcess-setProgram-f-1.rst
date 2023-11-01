.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 9d0338a2aa49dab7d56886fb4e6b38bd

Set the *program* to use when starting the process. This function must be called before :sip:ref:`~PyQt6.QtCore.QProcess.start`.

If *program* is an absolute path, it specifies the exact executable that will be launched. Relative paths will be resolved in a platform-specific manner, which includes searching the ``PATH`` environment variable (see :ref:`qprocess-finding-the-executable` for details).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.start`, :sip:ref:`~PyQt6.QtCore.QProcess.setArguments`, :sip:ref:`~PyQt6.QtCore.QProcess.program`, :sip:ref:`~PyQt6.QtCore.QStandardPaths.findExecutable`.
