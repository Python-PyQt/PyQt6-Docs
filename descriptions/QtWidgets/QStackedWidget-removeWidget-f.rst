.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: 02e56fc89f1514304bf2725a3debb4fd

Removes *widget* from the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget`. i.e., *widget* is *not* deleted but simply removed from the stacked layout, causing it to be hidden.

**Note:** Parent object and parent widget of *widget* will remain the :sip:ref:`~PyQt6.QtWidgets.QStackedWidget`. If the application wants to reuse the removed *widget*, then it is recommended to re-parent it.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.addWidget`, :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.insertWidget`, :sip:ref:`~PyQt6.QtWidgets.QStackedWidget.currentWidget`.
