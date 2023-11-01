.. sip:enum-description::
    :status: todo
    :digest: 57148afbceadf1a4c25c01627a1bf48c

This enum is used to control the allowed Bluetooth communication modes.

**Note:** The fine-grained permissions are currently supported only on Android 12 and newer. On older Android versions, as well as on Apple operating systems, any mode results in full Bluetooth access.

**Note:** For now the ``Access`` mode on Android also requests the :sip:ref:`~PyQt6.QtCore.QLocationPermission.Accuracy.Precise` permission. This permission coupling may change in the future.
