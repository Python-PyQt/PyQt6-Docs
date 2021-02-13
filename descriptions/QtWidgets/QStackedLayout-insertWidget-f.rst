.. sip:method-description::
    :status: todo
    :pysig: 41ccc95225270c5eb34597a532ee0512
    :realsig: (int,QWidget*)
    :digest: 0c0e554e4dd18597340bf3cae082c3d0

Inserts the given *widget* at the given *index* in this :sip:ref:`~PyQt6.QtWidgets.QStackedLayout`. If *index* is out of range, the widget is appended (in which case it is the actual index of the *widget* that is returned).

If the :sip:ref:`~PyQt6.QtWidgets.QStackedLayout` is empty before this function is called, the given *widget* becomes the current widget.

Inserting a new widget at an index less than or equal to the current index will increment the current index, but keep the current widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.addWidget`, removeWidget(), :sip:ref:`~PyQt6.QtWidgets.QStackedLayout.setCurrentWidget`.
