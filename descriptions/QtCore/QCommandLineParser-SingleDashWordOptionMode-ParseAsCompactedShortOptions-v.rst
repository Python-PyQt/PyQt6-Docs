.. sip:enum-member-description::
    :status: todo
    :value: 0
    :digest: 2c51faed0a8191c8c1f8eb95f0a69860

``-abc`` is interpreted as ``-a -b -c``, i.e. as three short options that have been compacted on the command-line, if none of the options take a value. If ``a`` takes a value, then it is interpreted as ``-a bc``, i.e. the short option ``a`` followed by the value ``bc``. This is typically used in tools that behave like compilers, in order to handle options such as ``-DDEFINE=VALUE`` or ``-I/include/path``. This is the default parsing mode. New applications are recommended to use this mode.
