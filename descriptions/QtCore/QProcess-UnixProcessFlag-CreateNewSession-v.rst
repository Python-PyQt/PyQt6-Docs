.. sip:enum-member-description::
    :status: todo
    :value: 0x0040
    :digest: 41fdd0ed765146f898b4dd137802cae3

Starts a new process session, by calling ``setsid(2)``. This allows the child process to outlive the session the current process is in. This is one of the steps that :sip:ref:`~PyQt6.QtCore.QProcess.startDetached` takes to allow the process to detach, and is also one of the steps to daemonize a process.
