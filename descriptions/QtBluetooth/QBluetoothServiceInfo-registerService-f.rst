.. sip:method-description::
    :status: todo
    :pysig: bc05139c1ad0fda2ae2f6483b542eb8a
    :realsig: (const QBluetoothAddress&)
    :digest: d23143c841d5a1c197d8e0422edb09f4

Registers this service with the platform's Service Discovery Protocol (SDP) implementation, making it findable by other devices when they perform service discovery. Returns true if the service is successfully registered, otherwise returns false. Once registered changes to the record cannot be made. The service must be unregistered and registered again with the changes.

The *localAdapter* parameter determines the local Bluetooth adapter under which the service should be registered. If *localAdapter* is ``null`` the default Bluetooth adapter will be used. If this service info object is already registered via a local adapter and this is function is called using a different local adapter, the previous registration is removed and the service reregistered using the new adapter.
