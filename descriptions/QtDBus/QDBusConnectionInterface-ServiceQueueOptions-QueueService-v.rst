.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: fd03a2d3d56a9fc6250572382699376a

Attempts to register the requested service, but do not try to replace it if another application already has it registered. Instead, simply put this application in queue, until it is given up. The :sip:ref:`~PyQt6.QtDBus.QDBusConnectionInterface.serviceRegistered` signal will be emitted when that happens.
