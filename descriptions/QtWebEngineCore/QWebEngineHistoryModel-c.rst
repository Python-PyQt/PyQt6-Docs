.. sip:class-description::
    :status: todo
    :brief: A data model that represents the history of a web engine page
    :digest: f009f9e2d7d810b437aaec4b672db7f0

A data model that represents the history of a web engine page.

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistoryModel` type exposes the *title*, *url*, *icon*, and *offset* roles. The *title*, *url* and *icon* specify the title, URL, and favicon of the visited page. The *offset* specifies the position of the page in respect to the current page (0). A positive number indicates that the page was visited after the current page, whereas a negative number indicates that the page was visited before the current page.

This type is uncreatable, but it can be accessed by using the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory.itemsModel`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory.backItemsModel`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory.forwardItemsModel` methods.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory`.
