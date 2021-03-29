.. sip:method-description::
    :status: todo
    :pysig: ae312437ab869e371f300040bbe75a79
    :realsig: () const
    :digest: 63e76f87053651a0e5f17b296d374cbf

Returns the exit status of the last process that finished.

On Windows, if the process was terminated with TerminateProcess() from another application, this function will still return :sip:ref:`~PyQt6.QtCore.QProcess.ExitStatus.NormalExit` unless the exit code is less than 0.
