.. sip:method-description::
    :status: todo
    :pysig: c65fa2f2b93dd25ddbccea8a7ca6a8b7
    :realsig: (QGraphicsItem*)
    :digest: d75e9da197d3fa7efbc2c009ba003ee6

If the :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem` represents a :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem`, and it wants to take advantage of the automatic reparenting capabilities of `QGraphicsLayout <https://doc.qt.io/qt-6/graphicsview.html#qgraphicslayout>`_ it should set this value. Note that if you delete *item* and not delete the layout item, you are responsible of calling (``nullptr``) in order to avoid having a dangling pointer.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsLayoutItem.graphicsItem`.
