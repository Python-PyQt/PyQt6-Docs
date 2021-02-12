.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: c9df7ca15ed3d881eab440dae891d2c9

``-abc`` is interpreted as ``--abc``, i.e. as the long option named ``abc``. This is how Qt's own tools (uic, rcc...) have always been parsing arguments. This mode should be used for preserving compatibility in applications that were parsing arguments in such a way. There is an exception if the ``a`` option has the :sip:ref:`~PyQt6.QtCore.QCommandLineOption.Flags.ShortOptionStyle` flag set, in which case it is still interpreted as ``-a bc``.
