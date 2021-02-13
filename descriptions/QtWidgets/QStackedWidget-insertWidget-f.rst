.. sip:method-description::
    :status: todo
    :pysig: 41ccc95225270c5eb34597a532ee0512
    :realsig: (int,QWidget*)
    :digest: 32f5c89daba095c5047f04e04e47efea

Inserts the given *widget* at the given *index* in the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget`. Ownership of *widget* is passed on to the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget`. If *index* is out of range, the *widget* is appended (in which case it is the actual index of the *widget* that is returned).

If the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget` was empty before this function is called, the given *widget* becomes the current widget.

Inserting a new widget at an index less than or equal to the current index will increment the current index, but keep the current widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.addWidget`, :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.removeWidget`, :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.setCurrentWidget`.
