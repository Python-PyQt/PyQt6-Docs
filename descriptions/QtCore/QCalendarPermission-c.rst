.. sip:class-description::
    :status: todo
    :brief: Access the user's calendar
    :digest: 165b8ccbadaa579b1d1d5678def35850

Access the user's calendar.

By default the request is for read-only access. Use :sip:ref:`~PyQt6.QtCore.QCalendarPermission.setAccessMode` to override the default.

.. _qcalendarpermission-requirements:

Requirements
------------

To request this permission at runtime, the following platform specific usage declarations have to be made at build time:

+----------+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Platform | Type                                                                                                           |                                                                                                                                                                         |
+==========+================================================================================================================+=========================================================================================================================================================================+
| Apple    | `Usage description <https://doc.qt.io/qt-6/permissions.html#apple-usage-description>`_                         | ``NSCalendarsUsageDescription``                                                                                                                                         |
+----------+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Android  | `
                                         <https://doc.qt.io/qt-6/permissions.html#android-uses-permission>`_ | ``android.permission.READ_CALENDAR``. ``android.permission.WRITE_CALENDAR`` if :sip:ref:`~PyQt6.QtCore.QCalendarPermission.accessMode` is set to AccessMode::ReadWrite. |
+----------+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Please see the individual usage declaration types for how to add them to your project.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.checkPermission`, `Application Permissions <https://doc.qt.io/qt-6/permissions.html>`_.
