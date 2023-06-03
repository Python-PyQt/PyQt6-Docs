.. sip:class-description::
    :status: todo
    :brief: Access the user's location
    :digest: 79d939545be8212edfe0fafb74c66730

Access the user's location.

By default the request is for approximate accuracy, and only while the application is in use. Use :sip:ref:`~PyQt6.QtCore.QLocationPermission.setAccuracy` and/or :sip:ref:`~PyQt6.QtCore.QLocationPermission.setAvailability` to override the default.

.. _qlocationpermission-requirements:

Requirements
------------

To request this permission at runtime, the following platform specific usage declarations have to be made at build time:

+----------+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Platform | Type                                                                                                           |                                                                                                                                                                                                                                                                                           |
+==========+================================================================================================================+===========================================================================================================================================================================================================================================================================================+
| macOS    | `Usage description <https://doc.qt.io/qt-6/permissions.html#apple-usage-description>`_                         | ``NSLocationUsageDescription``                                                                                                                                                                                                                                                            |
+----------+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| iOS      | `Usage description <https://doc.qt.io/qt-6/permissions.html#apple-usage-description>`_                         | ``NSLocationWhenInUseUsageDescription``, and ``NSLocationAlwaysAndWhenInUseUsageDescription`` if requesting :sip:ref:`~PyQt6.QtCore.QLocationPermission.Availability.Always`                                                                                                              |
+----------+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Android  | `
                                         <https://doc.qt.io/qt-6/permissions.html#android-uses-permission>`_ | * ``android.permission.ACCESS_FINE_LOCATION`` for :sip:ref:`~PyQt6.QtCore.QLocationPermission.Accuracy.Precise`                                                                                                                                                                           |
|          |                                                                                                                |                                                                                                                                                                                                                                                                                           |
|          |                                                                                                                | * ``android.permission.ACCESS_COARSE_LOCATION`` for :sip:ref:`~PyQt6.QtCore.QLocationPermission.Accuracy.Approximate`                                                                                                                                                                     |
|          |                                                                                                                |                                                                                                                                                                                                                                                                                           |
|          |                                                                                                                | * ``android.permission.ACCESS_BACKGROUND_LOCATION`` for :sip:ref:`~PyQt6.QtCore.QLocationPermission.Availability.Always`                                                                                                                                                                  |
|          |                                                                                                                |                                                                                                                                                                                                                                                                                           |
|          |                                                                                                                | **Note:** :sip:ref:`~PyQt6.QtCore.QLocationPermission.Availability.Always` ``uses-permission`` string has to be combined with one or both of :sip:ref:`~PyQt6.QtCore.QLocationPermission.Accuracy.Precise` and :sip:ref:`~PyQt6.QtCore.QLocationPermission.Accuracy.Approximate` strings. |
+----------+----------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Please see the individual usage declaration types for how to add them to your project.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.checkPermission`, `Application Permissions <https://doc.qt.io/qt-6/permissions.html>`_.
