.. sip:method-description::
    :status: todo
    :pysig: 7375d14f211a1abcabd1aa11c540c3f9
    :realsig: ()
    :digest: 1704093a1c9b7a57b76adc78c7df33d5

The systemEnvironment function returns the environment of the calling process.

It is returned as a :sip:ref:`~PyQt6.QtCore.QProcessEnvironment`. This function does not cache the system environment. Therefore, it's possible to obtain an updated version of the environment if low-level C library functions like ``setenv`` or ``putenv`` have been called.

However, note that repeated calls to this function will recreate the :sip:ref:`~PyQt6.QtCore.QProcessEnvironment` object, which is a non-trivial operation.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.systemEnvironment`.
