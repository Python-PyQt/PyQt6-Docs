.. sip:method-description::
    :status: todo
    :pysig: 49cd6c4846645627c7c8750fdcfb2bfd
    :realsig: ()
    :digest: 811c0fbc53de653604004b2579a656cb

Returns the architecture of the CPU that the application is running on, in text format. Note that this function depends on what the OS will report and may not detect the actual CPU architecture if the OS hides that information or is unable to provide it. For example, a 32-bit OS running on a 64-bit CPU is usually unable to determine the CPU is actually capable of running 64-bit programs.

Values returned by this function are mostly stable: an attempt will be made to ensure that they stay constant over time and match the values returned by :sip:ref:`~PyQt6.QtCore.QSysInfo.buildCpuArchitecture`. However, due to the nature of the operating system functions being used, there may be discrepancies.

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

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSysInfo.buildAbi`, :sip:ref:`~PyQt6.QtCore.QSysInfo.buildCpuArchitecture`.
