.. sip:method-description::
    :status: todo
    :pysig: 48e0b7b7211368d7fe37ab6bd3de75d6
    :realsig: (QAction*,QAction*)
    :digest: 12f3277eb6d4ad1aee7febbb0e7c42e5

Inserts the action *action* to this widget's list of actions, before the action *before*. It appends the action if *before* is ``nullptr`` or *before* is not a valid action for this widget.

A `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ should only have one of each action.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.removeAction`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.addAction`, :sip:ref:`~PyQt6.QtWidgets.QMenu`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.actions`, :sip:ref:`~PyQt6.QtWidgets.QWidget.insertActions`.
