.. sip:class-description::
    :status: todo
    :brief: Manages information about selected items in a model
    :digest: 5b7aa4972523b7223ed03e3b87e319af

The :sip:ref:`~PyQt6.QtCore.QItemSelection` class manages information about selected items in a model.

A :sip:ref:`~PyQt6.QtCore.QItemSelection` describes the items in a model that have been selected by the user. A :sip:ref:`~PyQt6.QtCore.QItemSelection` is basically a list of selection ranges, see :sip:ref:`~PyQt6.QtCore.QItemSelectionRange`. It provides functions for creating and manipulating selections, and selecting a range of items from a model.

The :sip:ref:`~PyQt6.QtCore.QItemSelection` class is one of the `Model/View Classes <https://doc.qt.io/qt-6/model-view-programming.html#model-view-classes>`_ and is part of Qt's `model/view framework <https://doc.qt.io/qt-6/model-view-programming.html>`_.

An item selection can be constructed and initialized to contain a range of items from an existing model. The following example constructs a selection that contains a range of items from the given ``model``, beginning at the ``topLeft``, and ending at the ``bottomRight``.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_gui_itemviews_qitemselectionmodel.py
    :lines: 54-54

An empty item selection can be constructed, and later populated as required. So, if the model is going to be unavailable when we construct the item selection, we can rewrite the above code in the following way:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_gui_itemviews_qitemselectionmodel.py
    :lines: 59-61

:sip:ref:`~PyQt6.QtCore.QItemSelection` saves memory, and avoids unnecessary work, by working with selection ranges rather than recording the model item index for each item in the selection. Generally, an instance of this class will contain a list of non-overlapping selection ranges.

Use :sip:ref:`~PyQt6.QtCore.QItemSelection.merge` to merge one item selection into another without making overlapping ranges. Use :sip:ref:`~PyQt6.QtCore.QItemSelection.split` to split one selection range into smaller ranges based on a another selection range.

.. seealso:: `Model/View Programming <https://doc.qt.io/qt-6/model-view-programming.html>`_, :sip:ref:`~PyQt6.QtCore.QItemSelectionModel`.
