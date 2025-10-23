.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 9fd010e59faa52f4a3209bd4acce6834

Sets additional native command line *arguments* for the program.

On operating systems where the system API for passing command line *arguments* to a subprocess natively uses a single string, one can conceive command lines which cannot be passed via :sip:ref:`~PyQt6.QtCore.QProcess`'s portable list-based API. In such cases this function must be used to set a string which is *appended* to the string composed from the usual argument list, with a delimiting space.

**Note:** This function is available only on the Windows platform.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QProcess.nativeArguments`.
