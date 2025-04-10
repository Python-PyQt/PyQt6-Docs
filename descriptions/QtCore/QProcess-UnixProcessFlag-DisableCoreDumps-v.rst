.. sip:enum-member-description::
    :status: todo
    :value: 0x0200
    :digest: f26499ecc78caa1dc09875645ff08668

Requests that :sip:ref:`~PyQt6.QtCore.QProcess` disable core dumps in the child process. This is useful if the executable being run is likely to crash but users and maintainers are going to be uninterested in generating bug reports for those conditions (for example, the executable is a test process). This setting does not affect the :sip:ref:`~PyQt6.QtCore.QProcess.exitStatus` of the crashed process. It is implemented by setting the core dump size resource soft limit to zero, meaning the application can still reverse this change by raising it to a value up to the hard limit.
