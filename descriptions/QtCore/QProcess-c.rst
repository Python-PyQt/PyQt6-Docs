.. sip:class-description::
    :status: todo
    :brief: Used to start external programs and to communicate with them
    :digest: 227f5986d9f3c1a1174896521915f1d0

The :sip:ref:`~PyQt6.QtCore.QProcess` class is used to start external programs and to communicate with them.

.. _qprocess-running-a-process:

Running a Process
-----------------

To start a process, pass the name and command line arguments of the program you want to run as arguments to :sip:ref:`~PyQt6.QtCore.QProcess.start`. Arguments are supplied as individual strings in a QStringList.

Alternatively, you can set the program to run with :sip:ref:`~PyQt6.QtCore.QProcess.setProgram` and :sip:ref:`~PyQt6.QtCore.QProcess.setArguments`, and then call :sip:ref:`~PyQt6.QtCore.QProcess.start` or :sip:ref:`~PyQt6.QtCore.QProcess.open`.

For example, the following code snippet runs the analog clock example in the Fusion style on X11 platforms by passing strings containing "-style" and "fusion" as two items in the list of arguments:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qprocess-qprocess-simpleexecution.py
    :lines: 60-60

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qprocess-qprocess-simpleexecution.py
    :lines: 65-65

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qprocess-qprocess-simpleexecution.py
    :lines: 70-74

:sip:ref:`~PyQt6.QtCore.QProcess` then enters the :sip:ref:`~PyQt6.QtCore.QProcess.ProcessState.Starting` state, and when the program has started, :sip:ref:`~PyQt6.QtCore.QProcess` enters the :sip:ref:`~PyQt6.QtCore.QProcess.ProcessState.Running` state and emits :sip:ref:`~PyQt6.QtCore.QProcess.started`.

:sip:ref:`~PyQt6.QtCore.QProcess` allows you to treat a process as a sequential I/O device. You can write to and read from the process just as you would access a network connection using :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`. You can then write to the process's standard input by calling write(), and read the standard output by calling read(), readLine(), and getChar(). Because it inherits :sip:ref:`~PyQt6.QtCore.QIODevice`, :sip:ref:`~PyQt6.QtCore.QProcess` can also be used as an input source for QXmlReader, or for generating data to be uploaded using :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager`.

When the process exits, :sip:ref:`~PyQt6.QtCore.QProcess` reenters the :sip:ref:`~PyQt6.QtCore.QProcess.ProcessState.NotRunning` state (the initial state), and emits :sip:ref:`~PyQt6.QtCore.QProcess.finished`.

The :sip:ref:`~PyQt6.QtCore.QProcess.finished` signal provides the exit code and exit status of the process as arguments, and you can also call :sip:ref:`~PyQt6.QtCore.QProcess.exitCode` to obtain the exit code of the last process that finished, and :sip:ref:`~PyQt6.QtCore.QProcess.exitStatus` to obtain its exit status. If an error occurs at any point in time, :sip:ref:`~PyQt6.QtCore.QProcess` will emit the :sip:ref:`~PyQt6.QtCore.QProcess.errorOccurred` signal. You can also call :sip:ref:`~PyQt6.QtCore.QProcess.error` to find the type of error that occurred last, and :sip:ref:`~PyQt6.QtCore.QProcess.state` to find the current process state.

**Note:** :sip:ref:`~PyQt6.QtCore.QProcess` is not supported on VxWorks, iOS, tvOS, or watchOS.

.. _qprocess-finding-the-executable:

Finding the Executable
----------------------

The program to be run can be set either by calling :sip:ref:`~PyQt6.QtCore.QProcess.setProgram` or directly in the :sip:ref:`~PyQt6.QtCore.QProcess.start` call. The effect of calling :sip:ref:`~PyQt6.QtCore.QProcess.start` with the program name and arguments is equivalent to calling :sip:ref:`~PyQt6.QtCore.QProcess.setProgram` and :sip:ref:`~PyQt6.QtCore.QProcess.setArguments` before that function and then calling the overload without those parameters.

:sip:ref:`~PyQt6.QtCore.QProcess` interprets the program name in one of three different ways, similar to how Unix shells and the Windows command interpreter operate in their own command-lines:

* If the program name is an absolute path, then that is the exact executable that will be launched and :sip:ref:`~PyQt6.QtCore.QProcess` performs no searching.

* If the program name is a relative path with more than one path component (that is, it contains at least one slash), the starting directory where that relative path is searched is OS-dependent: on Windows, it's the parent process' current working dir, while on Unix it's the one set with :sip:ref:`~PyQt6.QtCore.QProcess.setWorkingDirectory`.

* If the program name is a plain file name with no slashes, the behavior is operating-system dependent. On Unix systems, :sip:ref:`~PyQt6.QtCore.QProcess` will search the ``PATH`` environment variable; on Windows, the search is performed by the OS and will first the parent process' current directory before the ``PATH`` environment variable (see the documentation for CreateProcess for the full list).

To avoid platform-dependent behavior or any issues with how the current application was launched, it is adviseable to always pass an absolute path to the executable to be launched. For auxiliary binaries shipped with the application, one can construct such a path starting with :sip:ref:`~PyQt6.QtCore.QCoreApplication.applicationDirPath`. Similarly, to explicitly run an executable that is to be found relative to the directory set with :sip:ref:`~PyQt6.QtCore.QProcess.setWorkingDirectory`, use a program path starting with "./" or "../" as the case may be.

On Windows, the ".exe" suffix is not required for most uses, except those outlined in the CreateProcess documentation. Additionally, :sip:ref:`~PyQt6.QtCore.QProcess` will convert the Unix-style forward slashes to Windows path backslashes for the program name. This allows code using :sip:ref:`~PyQt6.QtCore.QProcess` to be written in a cross-platform manner, as shown in the examples above.

:sip:ref:`~PyQt6.QtCore.QProcess` does not support directly executing Unix shell or Windows command interpreter built-in functions, such as ``cmd.exe``'s ``dir`` command or the Bourne shell's ``export``. On Unix, even though many shell built-ins are also provided as separate executables, their behavior may differ from those implemented as built-ins. To run those commands, one should explicitly execute the interpreter with suitable options. For Unix systems, launch "/bin/sh" with two arguments: "-c" and a string with the command-line to be run. For Windows, due to the non-standard way ``cmd.exe`` parses its command-line, use setNativeArguments() (for example, "/c dir d:").

.. _qprocess-communicating-via-channels:

Communicating via Channels
--------------------------

Processes have two predefined output channels: The standard output channel (``stdout``) supplies regular console output, and the standard error channel (``stderr``) usually supplies the errors that are printed by the process. These channels represent two separate streams of data. You can toggle between them by calling :sip:ref:`~PyQt6.QtCore.QProcess.setReadChannel`. :sip:ref:`~PyQt6.QtCore.QProcess` emits readyRead() when data is available on the current read channel. It also emits :sip:ref:`~PyQt6.QtCore.QProcess.readyReadStandardOutput` when new standard output data is available, and when new standard error data is available, :sip:ref:`~PyQt6.QtCore.QProcess.readyReadStandardError` is emitted. Instead of calling read(), readLine(), or getChar(), you can explicitly read all data from either of the two channels by calling :sip:ref:`~PyQt6.QtCore.QProcess.readAllStandardOutput` or :sip:ref:`~PyQt6.QtCore.QProcess.readAllStandardError`.

The terminology for the channels can be misleading. Be aware that the process's output channels correspond to :sip:ref:`~PyQt6.QtCore.QProcess`'s *read* channels, whereas the process's input channels correspond to :sip:ref:`~PyQt6.QtCore.QProcess`'s *write* channels. This is because what we read using :sip:ref:`~PyQt6.QtCore.QProcess` is the process's output, and what we write becomes the process's input.

:sip:ref:`~PyQt6.QtCore.QProcess` can merge the two output channels, so that standard output and standard error data from the running process both use the standard output channel. Call :sip:ref:`~PyQt6.QtCore.QProcess.setProcessChannelMode` with :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannelMode.MergedChannels` before starting the process to activate this feature. You also have the option of forwarding the output of the running process to the calling, main process, by passing :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannelMode.ForwardedChannels` as the argument. It is also possible to forward only one of the output channels - typically one would use :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannelMode.ForwardedErrorChannel`, but :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannelMode.ForwardedOutputChannel` also exists. Note that using channel forwarding is typically a bad idea in GUI applications - you should present errors graphically instead.

Certain processes need special environment settings in order to operate. You can set environment variables for your process by calling :sip:ref:`~PyQt6.QtCore.QProcess.setProcessEnvironment`. To set a working directory, call :sip:ref:`~PyQt6.QtCore.QProcess.setWorkingDirectory`. By default, processes are run in the current working directory of the calling process.

The positioning and the screen Z-order of windows belonging to GUI applications started with :sip:ref:`~PyQt6.QtCore.QProcess` are controlled by the underlying windowing system. For Qt 5 applications, the positioning can be specified using the ``-qwindowgeometry`` command line option; X11 applications generally accept a ``-geometry`` command line option.

**Note:** On QNX, setting the working directory may cause all application threads, with the exception of the :sip:ref:`~PyQt6.QtCore.QProcess` caller thread, to temporarily freeze during the spawning process, owing to a limitation in the operating system.

.. _qprocess-synchronous-process-api:

Synchronous Process API
-----------------------

:sip:ref:`~PyQt6.QtCore.QProcess` provides a set of functions which allow it to be used without an event loop, by suspending the calling thread until certain signals are emitted:

* :sip:ref:`~PyQt6.QtCore.QProcess.waitForStarted` blocks until the process has started.

* :sip:ref:`~PyQt6.QtCore.QProcess.waitForReadyRead` blocks until new data is available for reading on the current read channel.

* :sip:ref:`~PyQt6.QtCore.QProcess.waitForBytesWritten` blocks until one payload of data has been written to the process.

* :sip:ref:`~PyQt6.QtCore.QProcess.waitForFinished` blocks until the process has finished.

Calling these functions from the main thread (the thread that calls :sip:ref:`~PyQt6.QtWidgets.QApplication.exec`) may cause your user interface to freeze.

The following example runs ``gzip`` to compress the string "Qt rocks!", without an event loop:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-process-process.py
    :lines: 58-69

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBuffer`, :sip:ref:`~PyQt6.QtCore.QFile`, :sip:ref:`~PyQt6.QtNetwork.QTcpSocket`.
