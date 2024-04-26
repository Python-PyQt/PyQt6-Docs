.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: 95a804588413f5c2c8176a069cc227ec

Enables or disables the ``ALLOW_INTERACTIVE_AUTHORIZATION`` flag in a message.

This flag only makes sense for method call messages (\ :sip:ref:`~PyQt6.QtDBus.QDBusMessage.MessageType.MethodCallMessage`). If *enable* is set to ``true``, the flag indicates to the callee that the caller of the method is prepared to wait for interactive authorization to take place (for instance via Polkit) before the actual method is processed.

If *enable* is set to ``false``, the flag is not set, meaning that the other end is expected to make any authorization decisions non-interactively and promptly. This is the default.

The ``org.freedesktop.DBus.Error.InteractiveAuthorizationRequired`` error indicates that authorization failed, but could have succeeded if this flag had been set.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusMessage.isInteractiveAuthorizationAllowed`, :sip:ref:`~PyQt6.QtDBus.QDBusAbstractInterface.setInteractiveAuthorizationAllowed`.
