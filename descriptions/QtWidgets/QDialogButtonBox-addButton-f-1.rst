.. sip:method-description::
    :status: todo
    :pysig: d6f01c85cd55af55511b4892de479de0
    :realsig: (QAbstractButton*,QDialogButtonBox::ButtonRole)
    :digest: f6724ac018525678ba6180f93c5836ad

Adds the given *button* to the button box with the specified *role*. If the role is invalid, the button is not added.

If the button has already been added, it is removed and added again with the new role.

**Note:** The button box takes ownership of the button.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.removeButton`, :sip:ref:`~PyQt6.QtWidgets.QDialogButtonBox.clear`.
