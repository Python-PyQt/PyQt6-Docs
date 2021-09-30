.. sip:method-description::
    :status: todo
    :pysig: cab115ff4ad25a8d87b0ebc0343e607b
    :realsig: (QWebEnginePage::WebAction,bool)
    :digest: cd5bc1019dc7326347e5c609cb54f0ec

This function can be called to trigger the specified *action*. It is also called by Qt WebEngine if the user triggers the action, for example through a context menu item.

If *action* is a checkable action, then *checked* specifies whether the action is toggled or not.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.action`.
