.. sip:method-description::
    :status: todo
    :pysig: 7cbecee60901b4e5a54925e8bb5e282a
    :realsig: (const QString&, const QStringList&, QIODeviceBase::OpenMode)
    :digest: e190a3564142e0b5fe13ad04f97092bf

Starts the given *program* in a new process, passing the command line arguments in *arguments*. See :sip:ref:`~PyQt6.QtCore.QProcess.setProgram` for information about how :sip:ref:`~PyQt6.QtCore.QProcess` searches for the executable to be run. The OpenMode is set to *mode*. No further splitting of the arguments is performed.

The :sip:ref:`~PyQt6.QtCore.QProcess` object will immediately enter the Starting state. If the process starts successfully, :sip:ref:`~PyQt6.QtCore.QProcess` will emit :sip:ref:`~PyQt6.QtCore.QProcess.started`; otherwise, :sip:ref:`~PyQt6.QtCore.QProcess.errorOccurred` will be emitted. Do note that on platforms that are able to start child processes synchronously (notably Windows), those signals will be emitted before this function returns and this :sip:ref:`~PyQt6.QtCore.QProcess` object will transition to either :sip:ref:`~PyQt6.QtCore.QProcess.ProcessState.Running` or :sip:ref:`~PyQt6.QtCore.QProcess.ProcessState.NotRunning` state, respectively. On others paltforms, the :sip:ref:`~PyQt6.QtCore.QProcess.started` and :sip:ref:`~PyQt6.QtCore.QProcess.errorOccurred` signals will be delayed.

Call :sip:ref:`~PyQt6.QtCore.QProcess.waitForStarted` to make sure the process has started (or has failed to start) and those signals have been emitted. It is safe to call that function even if the process starting state is already known, though the signal will not be emitted again.

**Windows:** The arguments are quoted and joined into a command line that is compatible with the ``CommandLineToArgvW()`` Windows function. For programs that have different command line quoting requirements, you need to use setNativeArguments(). One notable program that does not follow the ``CommandLineToArgvW()`` rules is cmd.exe and, by consequence, all batch scripts.

If the :sip:ref:`~PyQt6.QtCore.QProcess` object is already running a process, a warning may be printed at the console, and the existing process will continue running unaffected.

**Note:** Success at starting the child process only implies the operating system has successfully created the process and assigned the resources every process has, such as its process ID. The child process may crash or otherwise fail very early and thus not produce its expected output. On most operating systems, this may include dynamic linking errors.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.processId`, :sip:ref:`~PyQt6.QtCore.QProcess.started`, :sip:ref:`~PyQt6.QtCore.QProcess.waitForStarted`, setNativeArguments().
