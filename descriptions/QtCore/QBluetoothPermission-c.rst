.. sip:class-description::
    :status: todo
    :brief: Access Bluetooth peripherals
    :digest: 602d102f8aece50b19878bf6d66cd120

Access Bluetooth peripherals.

.. _qbluetoothpermission-requirements:

Requirements
------------

To request this permission at runtime, the following platform specific usage declarations have to be made at build time:

+----------+----------------------------------------------------------------------------------------------------------------+---------------------------------------+
| Platform | Type                                                                                                           |                                       |
+==========+================================================================================================================+=======================================+
| Apple    | `Usage description <https://doc.qt.io/qt-6/permissions.html#apple-usage-description>`_                         | ``NSBluetoothAlwaysUsageDescription`` |
+----------+----------------------------------------------------------------------------------------------------------------+---------------------------------------+
| Android  | `
                                         <https://doc.qt.io/qt-6/permissions.html#android-uses-permission>`_ | ``android.permission.BLUETOOTH``      |
+----------+----------------------------------------------------------------------------------------------------------------+---------------------------------------+

Please see the individual usage declaration types for how to add them to your project.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.checkPermission`, `Application Permissions <https://doc.qt.io/qt-6/permissions.html>`_.
