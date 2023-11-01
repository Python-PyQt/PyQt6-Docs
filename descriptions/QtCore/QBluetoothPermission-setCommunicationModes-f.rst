.. sip:method-description::
    :status: todo
    :pysig: 2cd7aded590d3a93e16b5c5fb33d3170
    :realsig: (QBluetoothPermission::CommunicationModes)
    :digest: c5edb8b6017d549e80494eff06a72d4e

Sets the allowed Bluetooth communication modes to *modes*.

**Note:** A default-constructed instance of CommunicationModes has no sense, so an attempt to set such a mode will raise a ``qWarning()`` and fall back to using the :sip:ref:`~PyQt6.QtCore.QBluetoothPermission.CommunicationMode.Default` mode.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QBluetoothPermission.communicationModes`.
