.. sip:method-description::
    :status: todo
    :pysig: f6a258d8f3ee5206d682d799316314b1
    :realsig: (bool)
    :digest: ef600b9ef03ebb077fa0e3678952056c

Finds a new widget to give the keyboard focus to, as appropriate for Tab and Shift+Tab, and returns ``true`` if it can find a new widget, or false if it can't.

If *next* is true, this function searches forward, if *next* is false, it searches backward.

Sometimes, you will want to reimplement this function. For example, a web browser might reimplement it to move its "current active link" forward or backward, and call focusNextPrevChild() only when it reaches the last or first link on the "page".

Child widgets call focusNextPrevChild() on their parent widgets, but only the window that contains the child widgets decides where to redirect focus. By reimplementing this function for an object, you thus gain control of focus traversal for all child widgets.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.focusNextChild`, :sip:ref:`~PyQt6.QtWidgets.QWidget.focusPreviousChild`.
