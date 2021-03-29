.. sip:method-description::
    :status: todo
    :pysig: f8ca99b6c748ea427923a2f5f071f05b
    :realsig: (QAction*)
    :digest: 2655b8a0c4543439f415b1d47f67f9df

Appends the action *action* to this widget's list of actions.

All QWidgets have a list of :sip:ref:`~PyQt6.QtGui.QAction`\ s, however they can be represented graphically in many different ways. The default use of the :sip:ref:`~PyQt6.QtGui.QAction` list (as returned by :sip:ref:`~PyQt6.QtWidgets.QWidget.actions`) is to create a context :sip:ref:`~PyQt6.QtWidgets.QMenu`.

A `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ should only have one of each action and adding an action it already has will not cause the same action to be in the widget twice.

The ownership of *action* is not transferred to this `QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.removeAction`, :sip:ref:`~PyQt6.QtWidgets.QWidget.insertAction`, :sip:ref:`~PyQt6.QtWidgets.QWidget.actions`, :sip:ref:`~PyQt6.QtWidgets.QMenu`.
