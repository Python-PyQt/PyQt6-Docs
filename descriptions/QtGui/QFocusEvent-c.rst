.. sip:class-description::
    :status: todo
    :brief: Contains event parameters for widget focus events
    :digest: 4a77bc50b92a185a951127bcfbe9e61c

The :sip:ref:`~PyQt6.QtGui.QFocusEvent` class contains event parameters for widget focus events.

Focus events are sent to widgets when the keyboard input focus changes. Focus events occur due to mouse actions, key presses (such as Tab or Backtab), the window system, popup menus, keyboard shortcuts, or other application-specific reasons. The reason for a particular focus event is returned by :sip:ref:`~PyQt6.QtGui.QFocusEvent.reason` in the appropriate event handler.

The event handlers :sip:ref:`~PyQt6.QtWidgets.QWidget.focusInEvent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.focusOutEvent`, :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.focusInEvent` and :sip:ref:`~PyQt6.QtWidgets.QGraphicsItem.focusOutEvent` receive focus events.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocus`, :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocusPolicy`, `Keyboard Focus in Widgets <https://doc.qt.io/qt-6/focus.html>`_.
