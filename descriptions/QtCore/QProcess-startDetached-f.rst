.. sip:method-description::
    :status: todo
    :pysig: 08c6ffc21d0a586000807b49fbade88c
    :realsig: (qint64*)
    :digest: 5825c26648bc79c31b2b6878a86d3b64

Starts the program set by :sip:ref:`~PyQt6.QtCore.QProcess.setProgram` with arguments set by :sip:ref:`~PyQt6.QtCore.QProcess.setArguments` in a new process, and detaches from it. Returns ``true`` on success; otherwise returns ``false``. If the calling process exits, the detached process will continue to run unaffected.

**Unix:** The started process will run in its own session and act like a daemon.

The process will be started in the directory set by :sip:ref:`~PyQt6.QtCore.QProcess.setWorkingDirectory`. If :sip:ref:`~PyQt6.QtCore.QProcess.workingDirectory` is empty, the working directory is inherited from the calling process.

**Note:** On QNX, this may cause all application threads to temporarily freeze.

If the function is successful then \*\ *pid* is set to the process identifier of the started process. Note that the child process may exit and the PID may become invalid without notice. Furthermore, after the child process exits, the same PID may be recycled and used by a completely different process. User code should be careful when using this variable, especially if one intends to forcibly terminate the process by operating system means.

Only the following property setters are supported by :

* :sip:ref:`~PyQt6.QtCore.QProcess.setArguments`

* setCreateProcessArgumentsModifier()

* setNativeArguments()

* :sip:ref:`~PyQt6.QtCore.QProcess.setProcessEnvironment`

* :sip:ref:`~PyQt6.QtCore.QProcess.setProgram`

* :sip:ref:`~PyQt6.QtCore.QProcess.setStandardErrorFile`

* :sip:ref:`~PyQt6.QtCore.QProcess.setStandardInputFile`

* :sip:ref:`~PyQt6.QtCore.QProcess.setStandardOutputFile`

* :sip:ref:`~PyQt6.QtCore.QProcess.setWorkingDirectory`

All other properties of the `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ object are ignored.

**Note:** The called process inherits the console window of the calling process. To suppress console output, redirect standard/error output to :sip:ref:`~PyQt6.QtCore.QProcess.nullDevice`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.start`, startDetached(const QString &program, const QStringList &arguments, const QString &workingDirectory, qint64 *pid).
