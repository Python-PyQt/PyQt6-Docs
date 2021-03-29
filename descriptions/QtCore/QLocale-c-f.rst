.. sip:method-description::
    :status: todo
    :pysig: beae116e6e30ff65b5adb869b565e847
    :realsig: ()
    :digest: fd725abf6902d9eb7a5b088c7c758bc4

Returns a :sip:ref:`~PyQt6.QtCore.QLocale` object initialized to the "C" locale.

This locale is based on en_US but with various quirks of its own, such as simplified number formatting and its own date formatting. It implements the POSIX standards that describe the behavior of standard library functions of the "C" programming language.

Among other things, this means its collation order is based on the ASCII values of letters, so that (for case-sensitive sorting) all upper-case letters sort before any lower-case one (rather than each letter's upper- and lower-case forms sorting adjacent to one another, before the next letter's two forms).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLocale.system`.
