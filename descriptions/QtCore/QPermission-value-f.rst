.. sip:method-description::
    :status: todo
    :pysig: ed36a1ef76a59ee3f15180e0441188ad
    :realsig: () const
    :digest: 7a24d8d732512e881e4545e2b3f12049

Returns the :ref:`typed permission<qpermission-typed-permissions>` of type ``T``, or ``std::nullopt`` if this :sip:ref:`~PyQt6.QtCore.QPermission` object doesn't contain one.

Use :sip:ref:`~PyQt6.QtCore.QPermission.type` for dynamically choosing which typed permission to request.

Constraints
-----------

Participates in overload resolution only if ``T`` is one of the :ref:`typed permission<qpermission-typed-permissions>` classes:

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
