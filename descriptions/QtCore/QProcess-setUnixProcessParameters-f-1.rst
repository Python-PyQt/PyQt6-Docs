.. sip:method-description::
    :status: todo
    :pysig: 42b8222959261f51991b73c451e86c90
    :realsig: (const QProcess::UnixProcessParameters&)
    :digest: fc9e9df5a2da3db647901af8c658f2f8

Sets the extra settings and parameters for the child process on Unix systems to be *params*. This function can be used to ask :sip:ref:`~PyQt6.QtCore.QProcess` to modify the child process before launching the target executable.

This function can be used to change certain properties of the child process, such as closing all extraneous file descriptors, changing the nice level of the child, or disconnecting from the controlling TTY. For more fine-grained control of the child process or to modify it in other ways, use the setChildProcessModifier() function. If both a child process modifier and Unix process parameters are set, the modifier is run before these parameters are applied.

**Note:** This function is only available on Unix platforms.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.unixProcessParameters`, setChildProcessModifier().
