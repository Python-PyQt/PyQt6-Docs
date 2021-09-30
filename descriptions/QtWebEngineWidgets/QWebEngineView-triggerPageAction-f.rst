.. sip:method-description::
    :status: todo
    :pysig: cab115ff4ad25a8d87b0ebc0343e607b
    :realsig: (QWebEnginePage::WebAction,bool)
    :digest: a94b9f9438c37252ebf2ad22fa0a5bda

Triggers the specified *action*. If it is a checkable action, the specified *checked* state is assumed.

The following example triggers the copy action and therefore copies any selected text to the clipboard.

.. literalinclude:: ../../../snippets/qtwebengine-src-webenginewidgets-doc-snippets-qtwebengine_qwebengineview_snippet.py
    :lines: 44-44

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineWidgets.QWebEngineView.pageAction`.
