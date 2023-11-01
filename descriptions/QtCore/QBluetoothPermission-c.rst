.. sip:class-description::
    :status: todo
    :brief: Access Bluetooth peripherals
    :digest: 6fa246a6629afa51c4d8682dd172b051

Access Bluetooth peripherals.

.. _qbluetoothpermission-requirements:

Requirements
------------

To request this permission at runtime, the following platform specific usage declarations have to be made at build time:

+----------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| Platform | Type                                                                                                           |                                               |
+==========+================================================================================================================+===============================================+
| Apple    | `Usage description <https://doc.qt.io/qt-6/permissions.html#apple-usage-description>`_                         | ``NSBluetoothAlwaysUsageDescription``         |
+----------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
| Android  | `
                                         <https://doc.qt.io/qt-6/permissions.html#android-uses-permission>`_ | Up to Android 11 (API Level < 31):            |
|          |                                                                                                                |                                               |
|          |                                                                                                                | * ``android.permission.BLUETOOTH``            |
|          |                                                                                                                |                                               |
|          |                                                                                                                | * ``android.permission.ACCESS_FINE_LOCATION`` |
|          |                                                                                                                |                                               |
|          |                                                                                                                | Starting from Android 12 (API Level >= 31):   |
|          |                                                                                                                |                                               |
|          |                                                                                                                | * ``android.permission.BLUETOOTH_ADVERTISE``  |
|          |                                                                                                                |                                               |
|          |                                                                                                                | * ``android.permission.BLUETOOTH_CONNECT``    |
|          |                                                                                                                |                                               |
|          |                                                                                                                | * ``android.permission.BLUETOOTH_SCAN``       |
|          |                                                                                                                |                                               |
|          |                                                                                                                | * ``android.permission.ACCESS_FINE_LOCATION`` |
+----------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------+

Please see the individual usage declaration types for how to add them to your project.

**Note:** Currently on Android the ``android.permission.ACCESS_FINE_LOCATION`` permission is requested together with Bluetooth permissions. This is required for Bluetooth to work properly, unless the application provides a strong assertion in the application manifest that it does not use Bluetooth to derive a physical location. This permission coupling may change in future.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.checkPermission`, `Application Permissions <https://doc.qt.io/qt-6/permissions.html>`_.
