.. sip:method-description::
    :status: todo
    :pysig: 72e2cafa091a7d38d145ec5a6e8cba39
    :realsig: (QWindow*)
    :digest: 37cb810f2700d6a1c77c6b1f42c1a53a

Constructs a :sip:ref:`~PyQt6.QtMultimedia.QCapturableWindow` instance that maps to the given window.

The description of the :sip:ref:`~PyQt6.QtMultimedia.QCapturableWindow` will match the title of the given :sip:ref:`~PyQt6.QtGui.QWindow`.

Note, the constructor may create an invalid instance if the specified ``QWindow`` has not been presented yet. Thus, if the Qt application is not running, an invalid ``QCapturableWindow`` instance is expected. The validity of the instance can be tracked by querying :sip:ref:`~PyQt6.QtMultimedia.QCapturableWindow.isValid` over time.

If given a nullptr as input, this method will return an instance that will never become valid.

If given a window that is not top-level, this method will return an instance will never become valid.
