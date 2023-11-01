.. sip:method-description::
    :status: todo
    :pysig: 464feb29a6e2310a3236b0544eca8b36
    :realsig: (QSettings::Format, QSettings::Scope, const QString&)
    :digest: 65ba8f72be8fa1f4713e0be8fb46cf1a

Sets the path used for storing settings for the given *format* and *scope*, to *path*. The *format* can be a custom format.

The table below summarizes the default values:

+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------+-----------------------------+
| Platform                                             | Format                                                                                                      | Scope                                              | Path                        |
+======================================================+=============================================================================================================+====================================================+=============================+
| Windows                                              | :sip:ref:`~PyQt6.QtCore.QSettings.Format.IniFormat`                                                         | :sip:ref:`~PyQt6.QtCore.QSettings.Scope.UserScope` | ``FOLDERID_RoamingAppData`` |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------+-----------------------------+
| :sip:ref:`~PyQt6.QtCore.QSettings.Scope.SystemScope` | ``FOLDERID_ProgramData``                                                                                    |                                                    |                             |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------+-----------------------------+
| Unix                                                 | :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat`, :sip:ref:`~PyQt6.QtCore.QSettings.Format.IniFormat` | :sip:ref:`~PyQt6.QtCore.QSettings.Scope.UserScope` | ``$HOME/.config``           |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------+-----------------------------+
| :sip:ref:`~PyQt6.QtCore.QSettings.Scope.SystemScope` | ``/etc/xdg``                                                                                                |                                                    |                             |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------+-----------------------------+
| macOS and iOS                                        | :sip:ref:`~PyQt6.QtCore.QSettings.Format.IniFormat`                                                         | :sip:ref:`~PyQt6.QtCore.QSettings.Scope.UserScope` | ``$HOME/.config``           |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------+-----------------------------+
| :sip:ref:`~PyQt6.QtCore.QSettings.Scope.SystemScope` | ``/etc/xdg``                                                                                                |                                                    |                             |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------+-----------------------------+

The default :sip:ref:`~PyQt6.QtCore.QSettings.Scope.UserScope` paths on Unix, macOS, and iOS (``$HOME/.config`` or $HOME/Settings) can be overridden by the user by setting the ``XDG_CONFIG_HOME`` environment variable. The default :sip:ref:`~PyQt6.QtCore.QSettings.Scope.SystemScope` paths on Unix, macOS, and iOS (``/etc/xdg``) can be overridden when building the Qt library using the ``configure`` script's ``-sysconfdir`` flag (see :sip:ref:`~PyQt6.QtCore.QLibraryInfo` for details).

Setting the :sip:ref:`~PyQt6.QtCore.QSettings.Format.NativeFormat` paths on Windows, macOS, and iOS has no effect.

**Warning:** This function doesn't affect existing :sip:ref:`~PyQt6.QtCore.QSettings` objects.

.. seealso:: registerFormat().
