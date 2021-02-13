.. sip:class-description::
    :status: todo
    :brief: Holds one Unix file descriptor
    :digest: ffd30a0296b0272176dd3139ea7d6b90

The :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` class holds one Unix file descriptor.

The :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` class is used to hold one Unix file descriptor for use with the Qt D-Bus module. This allows applications to send and receive Unix file descriptors over the D-Bus connection, mapping automatically to the D-Bus type 'h'.

Objects of type QDBusUnixFileDescriptors can be used also as parameters in signals and slots that get exported to D-Bus by registering with :sip:ref:`~PyQt6.QtDBus.QDBusConnection.registerObject`.

:sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` does not take ownership of the file descriptor. Instead, it will use the Unix system call ``dup(2)`` to make a copy of the file descriptor. This file descriptor belongs to the :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` object and should not be stored or closed by the user. Instead, you should make your own copy if you need that.

.. _qdbusunixfiledescriptor-availability:

Availability
............

Unix file descriptor passing is not available in all D-Bus connections. This feature is present with D-Bus library and bus daemon version 1.4 and upwards on Unix systems. Qt D-Bus automatically enables the feature if such a version was found at compile-time and run-time.

To verify that your connection does support passing file descriptors, check if the :sip:ref:`~PyQt6.QtDBus.QDBusConnection.ConnectionCapabilities.UnixFileDescriptorPassing` capability is set with :sip:ref:`~PyQt6.QtDBus.QDBusConnection.connectionCapabilities`. If the flag is not active, then you will not be able to make calls to methods that have :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` as arguments or even embed such a type in a variant. You will also not receive calls containing that type.

Note also that remote applications may not have support for Unix file descriptor passing. If you make a D-Bus to a remote application that cannot receive such a type, you will receive an error reply. If you try to send a signal containing a D-Bus file descriptor or return one from a method call, the message will be silently dropped.

Even if the feature is not available, :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` will continue to operate, so code need not have compile-time checks for the availability of this feature.

On non-Unix systems, :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor` will always report an invalid state and :sip:ref:`~PyQt6.QtDBus.QDBusUnixFileDescriptor.isSupported` will return false.

.. seealso:: QDBusConnection::ConnectionCapabilities, :sip:ref:`~PyQt6.QtDBus.QDBusConnection.connectionCapabilities`.
