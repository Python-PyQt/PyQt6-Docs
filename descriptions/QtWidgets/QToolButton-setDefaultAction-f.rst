.. sip:method-description::
    :status: todo
    :pysig: f8ca99b6c748ea427923a2f5f071f05b
    :realsig: (QAction*)
    :digest: 826ee1b1adad70f4f8690373bda37b75

Sets the default action to *action*.

If a tool button has a default action, the action defines the following properties of the button:

* checkable

* checked

* enabled

* :sip:ref:`~PyQt6.QtWidgets.QWidget.font`

* :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.icon`

* :sip:ref:`~PyQt6.QtWidgets.QToolButton.popupMode` (assuming the action has a menu)

* :sip:ref:`~PyQt6.QtWidgets.QWidget.statusTip`

* :sip:ref:`~PyQt6.QtWidgets.QAbstractButton.text`

* :sip:ref:`~PyQt6.QtWidgets.QWidget.toolTip`

* :sip:ref:`~PyQt6.QtWidgets.QWidget.whatsThis`

Other properties, such as autoRepeat, are not affected by actions.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QToolButton.defaultAction`.
