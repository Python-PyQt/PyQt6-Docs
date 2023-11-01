.. sip:attribute-description::
    :status: todo
    :digest: 8b9d7cf9d079603b99db52c167e7e68b

This constant expression variable holds the default native IPC type for the current OS. It will be :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.Type.Windows` for Windows systems and :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.Type.PosixRealtime` elsewhere. Note that this constant is different from what :sip:ref:`~PyQt6.QtCore.QSharedMemory` and :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` defaulted to on the majority of Unix systems prior to Qt 6.6; see :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.legacyDefaultTypeForOs` for more information.
