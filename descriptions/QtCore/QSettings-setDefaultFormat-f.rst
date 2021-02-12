.. sip:method-description::
    :status: todo
    :pysig: 4f2b6a13ac43a66ef8c0e92a8ef2fa0f
    :realsig: (QSettings::Format)
    :digest: 1f52298c0cba66526b28bfdd8fd994b1

Sets the default file format to the given *format*, which is used for storing settings for the :sip:ref:`~PyQt6.QtCore.QSettings`\ (\ :sip:ref:`~PyQt6.QtCore.QObject` \*) constructor.

If no default format is set, :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat` is used. See the documentation for the :sip:ref:`~PyQt6.QtCore.QSettings` constructor you are using to see if that constructor will ignore this function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.defaultFormat`, :sip:ref:`~PyQt6.QtCore.QSettings.format`.
