.. sip:class-description::
    :status: todo
    :brief: Access Bluetooth peripherals
    :digest: cf0acdf29ee7fd877f07a0847651e46c

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
+----------+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------+

Please see the individual usage declaration types for how to add them to your project.

**Note:** Since Qt 6.8.1, the ACCESS_FINE_LOCATION permission is no longer requested if API Level >= 31. This `may limit some Bluetooth scan results <https://doc.qt.io/qt-6/https://developer.android.com/develop/connectivity/bluetooth/bt-permissions>`_. Users needing these results need to request the location permission separately (see :sip:ref:`~PyQt6.QtCore.QLocationPermission.Accuracy.Precise`) and ensure that ``BLUETOOTH_SCAN`` permission doesn't have the ``android:usesPermissionFlags="neverForLocation"`` attribute set. For setting and customizing permissions in the application manifest, `see this guide <https://doc.qt.io/qt-6/android-manifest-file-configuration.html#qt-permissions-and-features>`_.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.checkPermission`, `Application Permissions <https://doc.qt.io/qt-6/permissions.html>`_.
