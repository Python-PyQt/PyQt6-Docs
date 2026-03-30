.. sip:signal-description::
    :status: todo
    :pysig: 2d9a1447e87954f62ae3dd085bb1217d
    :realsig: (const QUrl&, const QString&, const QUrl&)
    :digest: 3fd224f4bac041117466a701a0fc4b40

This signal is emitted when user should complete the authorization.

If authorization server has provided *completeVerificationUrl*, user can navigate to that URL. The URL contains the needed *userCode* and any other needed parameters.

Alternatively, the user needs to navigate to *verificationUrl* and enter *userCode* manually.

.. seealso:: :ref:`qoauth2deviceauthorizationflow-device-flow-usage`.
