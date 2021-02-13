.. sip:class-description::
    :status: todo
    :brief: Proxies its source model unmodified
    :digest: c1fadb9baa0542cb98d552c7a6b844cc

The :sip:ref:`~PyQt6.QtCore.QIdentityProxyModel` class proxies its source model unmodified.

:sip:ref:`~PyQt6.QtCore.QIdentityProxyModel` can be used to forward the structure of a source model exactly, with no sorting, filtering or other transformation. This is similar in concept to an identity matrix where A.I = A.

Because it does no sorting or filtering, this class is most suitable to proxy models which transform the data() of the source model. For example, a proxy model could be created to define the font used, or the background colour, or the tooltip etc. This removes the need to implement all data handling in the same class that creates the structure of the model, and can also be used to create re-usable components.

This also provides a way to change the data in the case where a source model is supplied by a third party which cannot be modified.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_gui_itemviews_qidentityproxymodel.py
    :lines: 54-75

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractProxyModel`, `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`.
