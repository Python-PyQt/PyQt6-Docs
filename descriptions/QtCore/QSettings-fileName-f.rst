.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: 958878a30fde75bb3cd342dde138e623

Returns the path where settings written using this :sip:ref:`~PyQt6.QtCore.QSettings` object are stored.

On Windows, if the format is :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat`, the return value is a system registry path, not a file path.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.isWritable`, :sip:ref:`~PyQt6.QtCore.QSettings.format`.
