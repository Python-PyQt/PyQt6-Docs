.. sip:method-description::
    :status: todo
    :pysig: eb0f4268c69bb1945f0c5fae1eaa4f44
    :realsig: (const QString&, const QStringList&)
    :digest: eadc83d74c023392796749a35ff9d255

Starts the program *program* with the arguments *arguments* in a new process, waits for it to finish, and then returns the exit code of the process. Any data the new process writes to the console is forwarded to the calling process.

The environment and working directory are inherited from the calling process.

Argument handling is identical to the respective :sip:ref:`~PyQt6.QtCore.QProcess.start` overload.

If the process cannot be started, -2 is returned. If the process crashes, -1 is returned. Otherwise, the process' exit code is returned.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.start`.
