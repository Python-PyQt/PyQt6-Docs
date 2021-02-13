.. sip:method-description::
    :status: todo
    :pysig: 48e0b7b7211368d7fe37ab6bd3de75d6
    :realsig: (QAction*,QAction*)
    :digest: a8cad1ea41e8e52d2e884cebb975bb75

Inserts the action *action* to this widget's list of actions, before the action *before*. It appends the action if *before* is ``nullptr`` or *before* is not a valid action for this widget.

A `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ should only have one of each action.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.removeAction`, :sip:ref:`~PyQt6.QtWidgets.QWidget.addAction`, :sip:ref:`~PyQt6.QtWidgets.QMenu`, :sip:ref:`~PyQt6.QtWidgets.QWidget.contextMenuPolicy`, :sip:ref:`~PyQt6.QtWidgets.QWidget.actions`.
