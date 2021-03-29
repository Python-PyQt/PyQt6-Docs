.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: b2172401b38ec9465fee7c331f80890b

Kills the current process, causing it to exit immediately.

On Windows,  uses TerminateProcess, and on Unix and macOS, the SIGKILL signal is sent to the process.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.terminate`.
