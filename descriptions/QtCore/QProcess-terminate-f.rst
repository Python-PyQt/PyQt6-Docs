.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 2060de7f0158ec03eea9d06152016545

Attempts to terminate the process.

The process may not exit as a result of calling this function (it is given the chance to prompt the user for any unsaved files, etc).

On Windows,  posts a WM_CLOSE message to all top-level windows of the process and then to the main thread of the process itself. On Unix and macOS the ``SIGTERM`` signal is sent.

Console applications on Windows that do not run an event loop, or whose event loop does not handle the WM_CLOSE message, can only be terminated by calling :sip:ref:`~PyQt6.QtCore.QProcess.kill`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.kill`.
