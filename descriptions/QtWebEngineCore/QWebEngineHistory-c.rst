.. sip:class-description::
    :status: todo
    :brief: Represents the history of a web engine page
    :digest: c452ac72050dedcd47d47ea4287a6d6b

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory` class represents the history of a web engine page.

Each web engine page contains a history of visited pages that can be accessed by :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.history`.

The history uses the concept of a *current item*, dividing the pages visited into those that can be visited by navigating *back* and *forward* using the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory.back` and :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory.forward` functions. The current item can be obtained by calling :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory.currentItem`, and an arbitrary item in the history can be made the current item by passing it to :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory.goToItem`.

A list of items describing the pages that can be visited by going back can be obtained by calling the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory.backItems` function; similarly, items describing the pages ahead of the current page can be obtained with the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory.forwardItems` function. The total list of items is obtained with the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory.items` function.

Also, the following :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistoryModel` data model objects are provided:

* ``backItemsModel()``, which contains the URLs of visited pages.

* ``forwardItemsModel()``, which contains the URLs of the pages that were visited after visiting the current page.

* ``itemsModel()``, which contains the URLs of the back and forward items, as well as the URL of the current page.

Just as with containers, functions are available to examine the history in terms of a list. Arbitrary items in the history can be obtained with :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory.itemAt`, the total number of items is given by :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory.count`, and the history can be cleared with the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory.clear` function.

:sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistory`'s state can be saved to a :sip:ref:`~PyQt6.QtCore.QDataStream` using the >> operator and loaded by using the << operator.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineHistoryItem`, `QWebEnginePage <https://doc.qt.io/qt-6/qtwebengine-changes-qt6.html#qwebenginepage>`_.
