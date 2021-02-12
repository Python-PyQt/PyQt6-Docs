.. sip:enum-description::
    :status: todo
    :digest: a7d86a6ec51e664e65e4d05de3f5df58

This enum describes the process output channel modes of `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_. Pass one of these values to :sip:ref:`~PyQt6.QtCore.QProcess.setProcessChannelMode` to set the current read channel mode.

**Note:** Windows intentionally suppresses output from GUI-only applications to inherited consoles. This does *not* apply to output redirected to files or pipes. To forward the output of GUI-only applications on the console nonetheless, you must use  and do the forwarding yourself by reading the output and writing it to the appropriate output channels.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.setProcessChannelMode`.
