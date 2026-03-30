.. sip:class-description::
    :status: todo
    :brief: Access the user's contacts
    :digest: e41e1d48e447b5b4dde6b0b65eb0674d

Access the user's contacts.

By default the request is for read-only access. Use :sip:ref:`~PyQt6.QtCore.QContactsPermission.setAccessMode` to override the default.

.. _qcontactspermission-requirements:

Requirements
------------

To request this permission at runtime, the following platform specific usage declarations have to be made at build time:

+----------+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Platform | Type                                                                                                           |                                                                                                                                                                                                                     |
+==========+================================================================================================================+=====================================================================================================================================================================================================================+
| Apple    | `Usage description <https://doc.qt.io/qt-6/permissions.html#apple-usage-description>`_                         | ``NSContactsUsageDescription``                                                                                                                                                                                      |
+----------+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Android  | `
                                         <https://doc.qt.io/qt-6/permissions.html#android-uses-permission>`_ | ``android.permission.READ_CONTACTS``. ``android.permission.WRITE_CONTACTS`` if :sip:ref:`~PyQt6.QtCore.QContactsPermission.accessMode` is set to :sip:ref:`~PyQt6.QtCore.QContactsPermission.AccessMode.ReadWrite`. |
+----------+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Please see the individual usage declaration types for how to add them to your project.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.checkPermission`, `Application Permissions <https://doc.qt.io/qt-6/permissions.html>`_.
