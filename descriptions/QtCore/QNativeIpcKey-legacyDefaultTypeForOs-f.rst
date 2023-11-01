.. sip:method-description::
    :status: todo
    :pysig: 11ae019ed640eb0466c0531e54cf81eb
    :realsig: ()
    :digest: af5472e5c251c7c21721efa7bb958fa9

Returns the :sip:ref:`~PyQt6.QtCore.QNativeIpcKey.Type.Type` that corresponds to the native IPC key that :sip:ref:`~PyQt6.QtCore.QSharedMemory` and :sip:ref:`~PyQt6.QtCore.QSystemSemaphore` used to use prior to Qt 6.6. Applications and libraries that must retain compatibility with code using either class that was compiled with Qt prior to version 6.6 can use this function to determine what IPC type the other applications may be using.

Note that this function relies on Qt having been built with identical configure-time options.
