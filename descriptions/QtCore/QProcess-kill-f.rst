.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 1629350b584152720cca3e3abbb936eb

Kills the current process, causing it to exit immediately.

On Windows, kill() uses TerminateProcess, and on Unix and macOS, the SIGKILL signal is sent to the process.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.terminate`.
