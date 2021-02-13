.. sip:method-description::
    :status: todo
    :pysig: f8ca99b6c748ea427923a2f5f071f05b
    :realsig: (QAction*)
    :digest: 5db45065638e680531176bd0006c6296

Appends the action *action* to this widget's list of actions.

All QGraphicsWidgets have a list of :sip:ref:`~PyQt6.QtGui.QAction`\ s, however they can be represented graphically in many different ways. The default use of the :sip:ref:`~PyQt6.QtGui.QAction` list (as returned by :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.actions`) is to create a context :sip:ref:`~PyQt6.QtWidgets.QMenu`.

A `QGraphicsWidget <https://doc.qt.io/qt-6/graphicsview.html#qgraphicswidget>`_ should only have one of each action and adding an action it already has will not cause the same action to be in the widget twice.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.removeAction`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.insertAction`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsWidget.actions`, :sip:ref:`~PyQt6.QtWidgets.QWidget.addAction`.
