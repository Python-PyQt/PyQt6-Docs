.. sip:method-description::
    :status: todo
    :pysig: 464116456943d857ef223b2d24ec328b
    :realsig: (const QString&)
    :digest: 83c25eb303f3b14cd6454c3cee1e333b

Sends the *pin* to the authenticator that prompts for a PIN. This is needed when the current WebAuth request's UX state is :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState.CollectPin`. The WebAuth request is blocked until the user responds with a PIN.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthPinRequest`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineWebAuthUxRequest.WebAuthUxState.CollectPin`.
