.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 56c88a46acb877edd63ec05bf9c3f842

Sets the auto start flag to *enable*. This flag only makes sense for method call messages, where it tells the D-Bus server to either auto start the service responsible for the service name, or not to auto start it.

By default this flag is true, i.e. a service is autostarted. This means:

When the service that this method call is sent to is already running, the method call is sent to it. If the service is not running yet, the D-Bus daemon is requested to autostart the service that is assigned to this service name. This is handled by .service files that are placed in a directory known to the D-Bus server. These files then each contain a service name and the path to a program that should be executed when this service name is requested.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusMessage.autoStartService`.
