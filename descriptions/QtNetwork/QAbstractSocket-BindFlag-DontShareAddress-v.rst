.. sip:enum-member-description::
    :status: todo
    :value: 0x2
    :digest: 8cebddb121d577cf13dbad203634c55e

Bind the address and port exclusively, so that no other services are allowed to rebind. By passing this option to :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket.bind`, you are guaranteed that on successs, your service is the only one that listens to the address and port. No services are allowed to rebind, even if they pass . This option provides more security than , but on certain operating systems, it requires you to run the server with administrator privileges. On Unix and macOS, not sharing is the default behavior for binding an address and port, so this option is ignored. On Windows, this option uses the SO_EXCLUSIVEADDRUSE socket option.
