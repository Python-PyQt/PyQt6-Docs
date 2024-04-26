.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: bbf66e387265895d4fd5e6f6ccc13cea

Configures whether, for asynchronous calls, the caller is prepared to wait for interactive authorization.

If *enable* is set to ``true``, the D-Bus messages generated for asynchronous calls via this interface will set the ``ALLOW_INTERACTIVE_AUTHORIZATION`` flag.

This flag is only useful when unprivileged code calls a more privileged method call, and an authorization framework is deployed that allows possibly interactive authorization.

The default is ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtDBus.QDBusAbstractInterface.isInteractiveAuthorizationAllowed`, :sip:ref:`~PyQt6.QtDBus.QDBusMessage.setInteractiveAuthorizationAllowed`.
