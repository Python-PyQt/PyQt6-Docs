.. sip:method-description::
    :status: todo
    :pysig: 2a38832352a50ffc5e738fd2b818b613
    :realsig: (QWidget*)
    :digest: 8939bdc1137000b8e10b33c57f1e2671

Appends the given *widget* to the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget` and returns the index position. Ownership of *widget* is passed on to the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget`.

If the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget` is empty before this function is called, *widget* becomes the current widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.insertWidget`, :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.removeWidget`, :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.setCurrentWidget`.
