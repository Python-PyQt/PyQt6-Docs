.. sip:method-description::
    :status: todo
    :pysig: 8de06b155d1d8e75153ed0d725f3f4fa
    :realsig: (const char*,QtMsgType)
    :digest: b94454145420b94990ac79984317017b

Constructs a :sip:ref:`~PyQt6.QtCore.QLoggingCategory` object with the provided *category* name, and enables all messages with types at least as verbose as *enableForLevel*, which defaults to :sip:ref:`~PyQt6.QtCore.QtMsgType.QtDebugMsg` (which enables all categories).

If *category* is ``nullptr``, the category name ``"default"`` is used.

**Note:** *category* must be kept valid during the lifetime of this object. Using a string literal for it is the usual way to achieve this.
