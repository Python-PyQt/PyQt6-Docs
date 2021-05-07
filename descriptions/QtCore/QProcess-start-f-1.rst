.. sip:method-description::
    :status: todo
    :pysig: 58231f3216b3f0a281a1edb4716b0c0a
    :realsig: (const QString&,const QStringList&,QIODeviceBase::OpenMode)
    :digest: b1369382858ae117d2dfd08f6f88709c

Starts the given *program* in a new process, passing the command line arguments in *arguments*.

The :sip:ref:`~PyQt6.QtCore.QProcess` object will immediately enter the Starting state. If the process starts successfully, :sip:ref:`~PyQt6.QtCore.QProcess` will emit :sip:ref:`~PyQt6.QtCore.QProcess.started`; otherwise, :sip:ref:`~PyQt6.QtCore.QProcess.errorOccurred` will be emitted.

**Note:** Processes are started asynchronously, which means the :sip:ref:`~PyQt6.QtCore.QProcess.started` and :sip:ref:`~PyQt6.QtCore.QProcess.errorOccurred` signals may be delayed. Call :sip:ref:`~PyQt6.QtCore.QProcess.waitForStarted` to make sure the process has started (or has failed to start) and those signals have been emitted.

**Note:** No further splitting of the arguments is performed.

**Windows:** The arguments are quoted and joined into a command line that is compatible with the ``CommandLineToArgvW()`` Windows function. For programs that have different command line quoting requirements, you need to use setNativeArguments(). One notable program that does not follow the ``CommandLineToArgvW()`` rules is cmd.exe and, by consequence, all batch scripts.

The OpenMode is set to *mode*.

If the :sip:ref:`~PyQt6.QtCore.QProcess` object is already running a process, a warning may be printed at the console, and the existing process will continue running unaffected.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.processId`, :sip:ref:`~PyQt6.QtCore.QProcess.started`, :sip:ref:`~PyQt6.QtCore.QProcess.waitForStarted`, setNativeArguments().
