.. sip:enum-member-description::
    :status: todo
    :value: 0x0002
    :digest: 01290dab823ffc89d702cad1744d52cb

Always sets the ``SIGPIPE`` signal to ignored (``SIG_IGN``), even if the ``ResetSignalHandlers`` flag was set. By default, if the child attempts to write to its standard output or standard error after the respective channel was closed with :sip:ref:`~PyQt6.QtCore.QProcess.closeReadChannel`, it would get the ``SIGPIPE`` signal and terminate immediately; with this flag, the write operation fails without a signal and the child may continue executing.
