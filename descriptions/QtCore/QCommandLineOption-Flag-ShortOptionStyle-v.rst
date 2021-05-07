.. sip:enum-member-description::
    :status: todo
    :value: 0x2
    :digest: f06071adacc5501d7e691cb89608dad0

The option will always be understood as a short option, regardless of what was set by :sip:ref:`~PyQt6.QtCore.QCommandLineParser.setSingleDashWordOptionMode`. This allows flags such as ``-DDEFINE=VALUE`` or ``-I/include/path`` to be interpreted as short flags even when the parser is in :sip:ref:`~PyQt6.QtCore.QCommandLineParser.SingleDashWordOptionMode.ParseAsLongOptions` mode.
