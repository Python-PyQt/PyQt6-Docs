.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 21eef4e9880a3cc8f8b0b224f58b9090

Returns the architecture of the CPU that Qt was compiled for, in text format. Note that this may not match the actual CPU that the application is running on if there's an emulation layer or if the CPU supports multiple architectures (like x86-64 processors supporting i386 applications). To detect that, use :sip:ref:`~PyQt6.QtCore.QSysInfo.currentCpuArchitecture`.

Values returned by this function are stable and will not change over time, so applications can rely on the returned value as an identifier, except that new CPU types may be added over time.

Typical returned values are (note: list not exhaustive):

* "arm"

* "arm64"

* "i386"

* "ia64"

* "mips"

* "mips64"

* "power"

* "power64"

* "sparc"

* "sparcv9"

* "x86_64"

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSysInfo.buildAbi`, :sip:ref:`~PyQt6.QtCore.QSysInfo.currentCpuArchitecture`.
