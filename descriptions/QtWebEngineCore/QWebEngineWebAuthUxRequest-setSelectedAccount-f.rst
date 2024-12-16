.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: 35ad6bae1efae0b9971ff05f2ccc277f

Sends the *selectedAccount* name to the authenticator. This is needed when the current WebAuth request's UX state is :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState.SelectAccount`. The WebAuth request is blocked until the user selects an account and invokes this method.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.userNames`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState.SelectAccount`.
