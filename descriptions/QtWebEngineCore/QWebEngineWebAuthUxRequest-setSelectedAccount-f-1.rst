.. sip:method-description::
    :status: todo
    :pysig: 464116456943d857ef223b2d24ec328b
    :realsig: (const QString&)
    :digest: 35ad6bae1efae0b9971ff05f2ccc277f

Sends the *selectedAccount* name to the authenticator. This is needed when the current WebAuth request's UX state is :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState.SelectAccount`. The WebAuth request is blocked until the user selects an account and invokes this method.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.userNames`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState.SelectAccount`.
