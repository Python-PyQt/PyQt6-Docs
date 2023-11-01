.. sip:class-description::
    :status: todo
    :brief: Access the microphone for monitoring or recording sound
    :digest: 9c268910be29a3fd3786aa93f96f9002

Access the microphone for monitoring or recording sound.

.. _qmicrophonepermission-requirements:

Requirements
------------

To request this permission at runtime, the following platform specific usage declarations have to be made at build time:

+----------+----------------------------------------------------------------------------------------------------------------+-------------------------------------+
| Platform | Type                                                                                                           |                                     |
+==========+================================================================================================================+=====================================+
| Apple    | `Usage description <https://doc.qt.io/qt-6/permissions.html#apple-usage-description>`_                         | ``NSMicrophoneUsageDescription``    |
+----------+----------------------------------------------------------------------------------------------------------------+-------------------------------------+
| Android  | `
                                         <https://doc.qt.io/qt-6/permissions.html#android-uses-permission>`_ | ``android.permission.RECORD_AUDIO`` |
+----------+----------------------------------------------------------------------------------------------------------------+-------------------------------------+

Please see the individual usage declaration types for how to add them to your project.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.requestPermission`, :sip:ref:`~PyQt6.QtCore.QCoreApplication.checkPermission`, `Application Permissions <https://doc.qt.io/qt-6/permissions.html>`_.
