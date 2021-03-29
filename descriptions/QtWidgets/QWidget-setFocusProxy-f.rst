.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 3a72f064512ec904dca3a903357a1215

Sets the widget's focus proxy to widget *w*. If *w* is ``nullptr``, the function resets this widget to have no focus proxy.

Some widgets can "have focus", but create a child widget, such as :sip:ref:`~PyQt6.QtWidgets.QLineEdit`, to actually handle the focus. In this case, the widget can set the line edit to be its focus proxy.

sets the widget which will actually get focus when "this widget" gets it. If there is a focus proxy, :sip:ref:`~PyQt6.QtWidgets.QWidget.setFocus` and :sip:ref:`~PyQt6.QtWidgets.QWidget.hasFocus` operate on the focus proxy. If "this widget" is the focus widget, then  moves focus to the new focus proxy.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.focusProxy`.
