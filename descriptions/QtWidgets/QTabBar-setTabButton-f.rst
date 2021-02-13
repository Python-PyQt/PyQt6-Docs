.. sip:method-description::
    :status: todo
    :pysig: e71124f01daa0fa0f5f52781de839cd8
    :realsig: (int,QTabBar::ButtonPosition,QWidget*)
    :digest: 2cb9e014a8be2415c8280a2b13dd0725

Sets *widget* on the tab *index*. The widget is placed on the left or right hand side depending upon the *position*.

Any previously set widget in *position* is hidden.

The tab bar will take ownership of the widget and so all widgets set here will be deleted by the tab bar when it is destroyed unless you separately reparent the widget after setting some other widget (or ``nullptr``).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTabBar.tabButton`, :sip:ref:`~PyQt6.QtWidgets.QTabBar.tabsClosable`.
