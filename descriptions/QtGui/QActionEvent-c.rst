.. sip:class-description::
    :status: todo
    :brief: Event that is generated when a QAction is added, removed, or changed
    :digest: 923e968bb4b6916b8d1d4f49340d42ec

The :sip:ref:`~PyQt6.QtGui.QActionEvent` class provides an event that is generated when a :sip:ref:`~PyQt6.QtGui.QAction` is added, removed, or changed.

Actions can be added to controls, for example by using QWidget::addAction(). This generates an :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActionAdded` event, which you can handle to provide custom behavior. For example, QToolBar reimplements QWidget::actionEvent() to create QToolButtons for the actions.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAction`.
