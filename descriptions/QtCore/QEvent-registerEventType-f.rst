.. sip:method-description::
    :status: todo
    :pysig: 100a2fed4a941c3f59e618d994698b09
    :realsig: (int)
    :digest: 9e7a3844e3d8e6e086e127a21233e58a

Registers and returns a custom event type. The *hint* provided will be used if it is available, otherwise it will return a value between :sip:ref:`~PyQt6.QtCore.QEvent.Type.User` and :sip:ref:`~PyQt6.QtCore.QEvent.Type.MaxUser` that has not yet been registered. The *hint* is ignored if its value is not between :sip:ref:`~PyQt6.QtCore.QEvent.Type.User` and :sip:ref:`~PyQt6.QtCore.QEvent.Type.MaxUser`.

Returns -1 if all available values are already taken or the program is shutting down.
