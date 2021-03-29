.. sip:method-description::
    :status: todo
    :pysig: 1f8ceb8889a8af6d95af5e04a432e1c9
    :realsig: (QAction*,const QList<QAction*>&)
    :digest: 5b7fed4afb63917e9b4835079948b537

Inserts the actions *actions* to this widget's list of actions, before the action *before*. It appends the action if *before* is ``nullptr`` or *before* is not a valid action for this widget.

A `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ can have at most one of each action.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.removeAction`, :sip:ref:`~PyQt6.QtWidgets.QMenu`, :sip:ref:`~PyQt6.QtWidgets.QWidget.insertAction`, :sip:ref:`~PyQt6.QtWidgets.QWidget.contextMenuPolicy`.
