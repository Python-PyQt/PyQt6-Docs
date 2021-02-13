.. sip:class-description::
    :status: todo
    :brief: Used to start external programs and to communicate with them
    :digest: be9fb8cf8f70ab3f22fbb2e2c059e939

The `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ class is used to start external programs and to communicate with them.

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

`QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ then enters the :sip:ref:`~PyQt6.QtCore.QProcess.ProcessState.Starting` state, and when the program has started, `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ enters the :sip:ref:`~PyQt6.QtCore.QProcess.ProcessState.Running` state and emits :sip:ref:`~PyQt6.QtCore.QProcess.started`.

`QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ allows you to treat a process as a sequential I/O device. You can write to and read from the process just as you would access a network connection using QTcpSocket. You can then write to the process's standard input by calling write(), and read the standard output by calling read(), readLine(), and getChar(). Because it inherits :sip:ref:`~PyQt6.QtCore.QIODevice`, `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ can also be used as an input source for QXmlReader, or for generating data to be uploaded using QNetworkAccessManager.

When the process exits, `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ reenters the :sip:ref:`~PyQt6.QtCore.QProcess.ProcessState.NotRunning` state (the initial state), and emits :sip:ref:`~PyQt6.QtCore.QProcess.finished`.

The :sip:ref:`~PyQt6.QtCore.QProcess.finished` signal provides the exit code and exit status of the process as arguments, and you can also call :sip:ref:`~PyQt6.QtCore.QProcess.exitCode` to obtain the exit code of the last process that finished, and :sip:ref:`~PyQt6.QtCore.QProcess.exitStatus` to obtain its exit status. If an error occurs at any point in time, `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ will emit the :sip:ref:`~PyQt6.QtCore.QProcess.errorOccurred` signal. You can also call :sip:ref:`~PyQt6.QtCore.QProcess.error` to find the type of error that occurred last, and :sip:ref:`~PyQt6.QtCore.QProcess.state` to find the current process state.

**Note:** `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ is not supported on VxWorks, iOS, tvOS, or watchOS.

.. _qprocess-communicating-via-channels:

Communicating via Channels
--------------------------

Processes have two predefined output channels: The standard output channel (``stdout``) supplies regular console output, and the standard error channel (``stderr``) usually supplies the errors that are printed by the process. These channels represent two separate streams of data. You can toggle between them by calling :sip:ref:`~PyQt6.QtCore.QProcess.setReadChannel`. `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ emits readyRead() when data is available on the current read channel. It also emits :sip:ref:`~PyQt6.QtCore.QProcess.readyReadStandardOutput` when new standard output data is available, and when new standard error data is available, :sip:ref:`~PyQt6.QtCore.QProcess.readyReadStandardError` is emitted. Instead of calling read(), readLine(), or getChar(), you can explicitly read all data from either of the two channels by calling :sip:ref:`~PyQt6.QtCore.QProcess.readAllStandardOutput` or :sip:ref:`~PyQt6.QtCore.QProcess.readAllStandardError`.

The terminology for the channels can be misleading. Be aware that the process's output channels correspond to `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_'s *read* channels, whereas the process's input channels correspond to `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_'s *write* channels. This is because what we read using `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ is the process's output, and what we write becomes the process's input.

`QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ can merge the two output channels, so that standard output and standard error data from the running process both use the standard output channel. Call :sip:ref:`~PyQt6.QtCore.QProcess.setProcessChannelMode` with :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannelMode.MergedChannels` before starting the process to activate this feature. You also have the option of forwarding the output of the running process to the calling, main process, by passing :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannelMode.ForwardedChannels` as the argument. It is also possible to forward only one of the output channels - typically one would use :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannelMode.ForwardedErrorChannel`, but :sip:ref:`~PyQt6.QtCore.QProcess.ProcessChannelMode.ForwardedOutputChannel` also exists. Note that using channel forwarding is typically a bad idea in GUI applications - you should present errors graphically instead.

Certain processes need special environment settings in order to operate. You can set environment variables for your process by calling :sip:ref:`~PyQt6.QtCore.QProcess.setProcessEnvironment`. To set a working directory, call :sip:ref:`~PyQt6.QtCore.QProcess.setWorkingDirectory`. By default, processes are run in the current working directory of the calling process.

The positioning and the screen Z-order of windows belonging to GUI applications started with `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ are controlled by the underlying windowing system. For Qt 5 applications, the positioning can be specified using the ``-qwindowgeometry`` command line option; X11 applications generally accept a ``-geometry`` command line option.

**Note:** On QNX, setting the working directory may cause all application threads, with the exception of the `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ caller thread, to temporarily freeze during the spawning process, owing to a limitation in the operating system.

.. _qprocess-synchronous-process-api:

Synchronous Process API
-----------------------

`QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ provides a set of functions which allow it to be used without an event loop, by suspending the calling thread until certain signals are emitted:

* :sip:ref:`~PyQt6.QtCore.QProcess.waitForStarted` blocks until the process has started.

* :sip:ref:`~PyQt6.QtCore.QProcess.waitForReadyRead` blocks until new data is available for reading on the current read channel.

* :sip:ref:`~PyQt6.QtCore.QProcess.waitForBytesWritten` blocks until one payload of data has been written to the process.

* :sip:ref:`~PyQt6.QtCore.QProcess.waitForFinished` blocks until the process has finished.

Calling these functions from the main thread (the thread that calls :sip:ref:`~PyQt6.QtWidgets.QApplication.exec`) may cause your user interface to freeze.

The following example runs ``gzip`` to compress the string "Qt rocks!", without an event loop:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-process-process.py
    :lines: 58-69

.. _qprocess-notes-for-windows-users:

Notes for Windows Users
-----------------------

Some Windows commands (for example, ``dir``) are not provided by separate applications, but by the command interpreter itself. If you attempt to use `QProcess <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qprocess>`_ to execute these commands directly, it won't work. One possible solution is to execute the command interpreter itself (``cmd.exe`` on some Windows systems), and ask the interpreter to execute the desired command.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBuffer`, :sip:ref:`~PyQt6.QtCore.QFile`.
