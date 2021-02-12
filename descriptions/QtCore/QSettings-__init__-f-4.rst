.. sip:method-description::
    :status: todo
    :pysig: 17e0f5a066ea321e122e788cafab95c3
    :realsig: (QSettings::Scope,const QString&,const QString&,QObject*)
    :digest: 841e8f6ec3d1377a320891a79b1024d2

Constructs a :sip:ref:`~PyQt6.QtCore.QSettings` object for accessing settings of the application called *application* from the organization called *organization*, and with parent *parent*.

If *scope* is :sip:ref:`~PyQt6.QtCore.QSettings.Scope.UserScope`, the :sip:ref:`~PyQt6.QtCore.QSettings` object searches user-specific settings first, before it searches system-wide settings as a fallback. If *scope* is :sip:ref:`~PyQt6.QtCore.QSettings.Scope.SystemScope`, the :sip:ref:`~PyQt6.QtCore.QSettings` object ignores user-specific settings and provides access to system-wide settings.

The storage format is set to :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat` (i.e. calling :sip:ref:`~PyQt6.QtCore.QSettings.setDefaultFormat` before calling this constructor has no effect).

If no application name is given, the :sip:ref:`~PyQt6.QtCore.QSettings` object will only access the organization-wide :ref:`qsettings-fallback-mechanism`.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.setDefaultFormat`.
