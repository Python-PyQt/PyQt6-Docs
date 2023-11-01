.. sip:enum-member-description::
    :status: todo
    :value: 0x0020
    :digest: 0732c7a19dffc10fa0119790fac21f9f

Requests that :sip:ref:`~PyQt6.QtCore.QProcess` use ``vfork(2)`` to start the child process. Use this flag to indicate that the callback function set with setChildProcessModifier() is safe to execute in the child side of a ``vfork(2)``; that is, the callback does not modify any non-local variables (directly or through any function it calls), nor attempts to communicate with the parent process. It is implementation-defined if :sip:ref:`~PyQt6.QtCore.QProcess` will actually use ``vfork(2)`` and if ``vfork(2)`` is different from standard ``fork(2)``.
