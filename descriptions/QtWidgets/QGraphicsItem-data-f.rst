.. sip:method-description::
    :status: todo
    :pysig: 929edda6a97571ebce7151ff0802751f
    :realsig: (int) const
    :digest: a7db7b237930032770a353e1cbe2a3e4

Returns this item's custom data for the key *key* as a `QVariant <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qvariant>`_.

Custom item data is useful for storing arbitrary properties in any item. Example:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_graphicsview_qgraphicsitem.py
    :lines: 172-178

Qt does not use this feature for storing data; it is provided solely for the convenience of the user.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.setData`.
