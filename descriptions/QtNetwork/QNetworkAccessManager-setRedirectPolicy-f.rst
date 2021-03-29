.. sip:method-description::
    :status: todo
    :pysig: d81136b64693beb8b40f3a663e2b34d8
    :realsig: (QNetworkRequest::RedirectPolicy)
    :digest: 1c91bb0e86d6ad295c165efd9402031b

Sets the manager's redirect policy to be the *policy* specified. This policy will affect all subsequent requests created by the manager.

Use this function to enable or disable HTTP redirects on the manager's level.

**Note:** When creating a request QNetworkRequest::RedirectAttributePolicy has the highest priority, next by priority the manager's policy.

The default value is :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.RedirectPolicy.NoLessSafeRedirectPolicy`. Clients relying on manual redirect handling are encouraged to set this policy explicitly in their code.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.redirectPolicy`, :sip:ref:`~PyQt6.QtNetwork.QNetworkRequest.RedirectPolicy`.
