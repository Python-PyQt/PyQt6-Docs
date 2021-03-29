.. sip:class-description::
    :status: todo
    :brief:  TODO
    :digest: 8a05bed013ac204f314b3dd9f0e7e0dd

Represents a handle to a signal-slot (or signal-functor) connection.

It can be used to check if the connection is valid and to disconnect it using :sip:ref:`~PyQt6.QtCore.QObject.disconnect`. For a signal-functor connection without a context object, it is the only way to selectively disconnect that connection.

As Connection is just a handle, the underlying signal-slot connection is unaffected when Connection is destroyed or reassigned.
