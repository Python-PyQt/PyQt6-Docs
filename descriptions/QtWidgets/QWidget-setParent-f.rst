.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 07680f7581f38988aab0819339bd1dfa

Sets the parent of the widget to *parent*, and resets the window flags. The widget is moved to position (0, 0) in its new parent.

If the new parent widget is in a different window, the reparented widget and its children are appended to the end of the :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocusPolicy` of the new parent widget, in the same internal order as before. If one of the moved widgets had keyboard focus,  calls :sip:ref:`~PyQt6.QtWidgets.QWidget.clearFocus` for that widget.

If the new parent widget is in the same window as the old parent, setting the parent doesn't change the tab order or keyboard focus.

If the "new" parent widget is the old parent widget, this function does nothing.

**Note:** The widget becomes invisible as part of changing its parent, even if it was previously visible. You must call :sip:ref:`~PyQt6.QtWidgets.QWidget.show` to make the widget visible again.

**Warning:** It is very unlikely that you will ever need this function. If you have a widget that changes its content dynamically, it is far easier to use :sip:ref:`~PyQt6.QtWidgets.QStackedWidget`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.setWindowFlags`.
