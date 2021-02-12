.. sip:signal-description::
    :status: todo
    :pysig: 53e4f9a237b22c12cd30ad51ffae0af0
    :realsig: (int,QProcess::ExitStatus)
    :digest: 0a37e9faaebe57666ee1dca159af9019

This signal is emitted when the process finishes. *exitCode* is the exit code of the process (only valid for normal exits), and *exitStatus* is the exit status. After the process has finished, the buffers in `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ are still intact. You can still read any data that the process may have written before it finished.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.exitStatus`.
