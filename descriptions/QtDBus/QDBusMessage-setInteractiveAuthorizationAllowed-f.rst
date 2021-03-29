.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: cf17172fbcf127072b5cc09526e96402

Sets the interactive authorization flag to *enable*. This flag only makes sense for method call messages, where it tells the D-Bus server that the caller of the method is prepared to wait for interactive authorization to take place (for instance via Polkit) before the actual method is processed.

By default this flag is false and the other end is expected to make any authorization decisions non-interactively and promptly.

The ``org.freedesktop.DBus.Error.InteractiveAuthorizationRequired`` error indicates that authorization failed, but could have succeeded if this flag had been set.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusMessage.isInteractiveAuthorizationAllowed`.
