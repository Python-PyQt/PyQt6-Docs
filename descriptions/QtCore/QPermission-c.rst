.. sip:class-description::
    :status: todo
    :brief: An opaque wrapper of a typed permission
    :digest: a087ad971ee367910ee7c915b091a9c0

An opaque wrapper of a typed permission.

The :sip:ref:`~PyQt6.QtCore.QPermission` class is an opaque wrapper of a :ref:`typed permission<qpermission-typed-permissions>`, used when checking or requesting permissions. You do not need to construct this type explicitly, as the type is automatically used when checking or requesting permissions:

::

    qApp->checkPermission(QCameraPermission{});

When requesting permissions, the given functor will be passed an instance of a :sip:ref:`~PyQt6.QtCore.QPermission`, which can be used to check the result of the request:

::

    qApp->requestPermission(QCameraPermission{}, [](const QPermission &permission) {
        if (permission.status() == Qt::PermissionStatus::Granted)
            takePhoto();
    });

To inspect the properties of the original, typed permission, use the :sip:ref:`~PyQt6.QtCore.QPermission.value` function:

::

    QLocationPermission locationPermission;
    locationPermission.setAccuracy(QLocationPermission::Precise);
    qApp->requestPermission(locationPermission, this, &LocationWidget::permissionUpdated);

::

    void LocationWidget::permissionUpdated(const QPermission &permission)
    {
        if (permission.status() != Qt::PermissionStatus::Granted)
            return;
        auto locationPermission = permission.value<QLocationPermission>();
        if (!locationPermission || locationPermission->accuracy() != QLocationPermission::Precise)
            return;
        updatePreciseLocation();
    }

.. _qpermission-typed-permission:

.. _qpermission-typed-permissions:

Typed Permissions
.................

The following permissions are available:

+------------------------------------------------+----------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QCameraPermission`     | Access the camera for taking pictures or videos.         |
+------------------------------------------------+----------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QMicrophonePermission` | Access the microphone for monitoring or recording sound. |
+------------------------------------------------+----------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QBluetoothPermission`  | Access Bluetooth peripherals.                            |
+------------------------------------------------+----------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QLocationPermission`   | Access the user's location.                              |
+------------------------------------------------+----------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QContactsPermission`   | Access the user's contacts.                              |
+------------------------------------------------+----------------------------------------------------------+
| :sip:ref:`~PyQt6.QtCore.QCalendarPermission`   | Access the user's calendar.                              |
+------------------------------------------------+----------------------------------------------------------+

.. seealso:: `Application Permissions <https://doc.qt.io/qt-6/permissions.html>`_.
