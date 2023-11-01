.. sip:class-description::
    :status: todo
    :brief: Access the camera for taking pictures or videos
    :digest: 046d3c2f451095c08d3bbdfa418354d7

Access the camera for taking pictures or videos.

.. _qcamerapermission-requirements:

Requirements
------------

To request this permission at runtime, the following platform specific usage declarations have to be made at build time:

+----------+----------------------------------------------------------------------------------------------------------------+-------------------------------+
| Platform | Type                                                                                                           |                               |
+==========+================================================================================================================+===============================+
| Apple    | `Usage description <https://doc.qt.io/qt-6/permissions.html#apple-usage-description>`_                         | ``NSCameraUsageDescription``  |
+----------+----------------------------------------------------------------------------------------------------------------+-------------------------------+
| Android  | `
                                         <https://doc.qt.io/qt-6/permissions.html#android-uses-permission>`_ | ``android.permission.CAMERA`` |
+----------+----------------------------------------------------------------------------------------------------------------+-------------------------------+

Please see the individual usage declaration types for how to add them to your project.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.checkPermission`, `Application Permissions <https://doc.qt.io/qt-6/permissions.html>`_.
