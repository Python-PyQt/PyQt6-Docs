.. sip:signal-description::
    :status: todo
    :pysig: 3a0fae09897386430d798813ccc2a251
    :realsig: (const QUrl&, const QString&, const QUrl&)
    :digest: 3fd224f4bac041117466a701a0fc4b40

This signal is emitted when user should complete the authorization.

If authorization server has provided *completeVerificationUrl*, user can navigate to that URL. The URL contains the needed *userCode* and any other needed parameters.

Alternatively, the user needs to navigate to *verificationUrl* and enter *userCode* manually.

.. seealso:: :ref:`qoauth2deviceauthorizationflow-device-flow-usage`.
