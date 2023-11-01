.. sip:method-description::
    :status: todo
    :pysig: 25c81b0cee53121776a81212fbcf1663
    :realsig: (QSettings::Format, QSettings::Scope, const QString&, const QString&, QObject*)
    :digest: 39eab241cc6ab824d8eb9d44d0c0ab31

Constructs a :sip:ref:`~PyQt6.QtCore.QSettings` object for accessing settings of the application called *application* from the organization called *organization*, and with parent *parent*.

If *scope* is :sip:ref:`~PyQt6.QtCore.QSettings.Scope.UserScope`, the :sip:ref:`~PyQt6.QtCore.QSettings` object searches user-specific settings first, before it searches system-wide settings as a fallback. If *scope* is :sip:ref:`~PyQt6.QtCore.QSettings.Scope.SystemScope`, the :sip:ref:`~PyQt6.QtCore.QSettings` object ignores user-specific settings and provides access to system-wide settings.

If *format* is :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat`, the native API is used for storing settings. If *format* is :sip:ref:`~PyQt6.QtCore.QSettings.Format.IniFormat`, the INI format is used.

If no application name is given, the :sip:ref:`~PyQt6.QtCore.QSettings` object will only access the organization-wide :ref:`qsettings-fallback-mechanism`.
