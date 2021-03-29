.. sip:class-description::
    :status: todo
    :brief: Event that is generated when a QAction is added, removed, or changed
    :digest: 00ed583e32f11febe6b8b14413753a78

The :sip:ref:`~PyQt6.QtGui.QActionEvent` class provides an event that is generated when a :sip:ref:`~PyQt6.QtGui.QAction` is added, removed, or changed.

Actions can be added to controls, for example by using :sip:ref:`~PyQt6.QtWidgets.QWidget.addAction`. This generates an :sip:ref:`~PyQt6.QtCore.QEvent.Type.ActionAdded` event, which you can handle to provide custom behavior. For example, :sip:ref:`~PyQt6.QtWidgets.QToolBar` reimplements :sip:ref:`~PyQt6.QtWidgets.QWidget.actionEvent` to create :sip:ref:`~PyQt6.QtWidgets.QToolButton`\ s for the actions.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QAction`, :sip:ref:`~PyQt6.QtWidgets.QWidget.addAction`, :sip:ref:`~PyQt6.QtWidgets.QWidget.removeAction`, :sip:ref:`~PyQt6.QtWidgets.QWidget.actions`.
