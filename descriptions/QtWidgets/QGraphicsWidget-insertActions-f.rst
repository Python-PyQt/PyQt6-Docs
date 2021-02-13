.. sip:method-description::
    :status: todo
    :pysig: 1f8ceb8889a8af6d95af5e04a432e1c9
    :realsig: (QAction*,const QList<QAction*>&)
    :digest: 21e09046c54935d4d35691b411da29ec

Inserts the actions *actions* to this widget's list of actions, before the action *before*. It appends the action if *before* is ``nullptr`` or *before* is not a valid action for this widget.

A `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ can have at most one of each action.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.removeAction`, :sip:ref:`~PyQt6.QtWidgets.QMenu`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.insertAction`, :sip:ref:`~PyQt6.QtWidgets.QWidget.insertActions`.
