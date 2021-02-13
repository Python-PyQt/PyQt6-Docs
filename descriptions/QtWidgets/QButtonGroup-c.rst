.. sip:class-description::
    :status: todo
    :brief: Container to organize groups of button widgets
    :digest: 463d3e5076ba30d28be766d75fa23ced

The :sip:ref:`~PyQt6.QtWidgets.QButtonGroup` class provides a container to organize groups of button widgets.

:sip:ref:`~PyQt6.QtWidgets.QButtonGroup` provides an abstract container into which button widgets can be placed. It does not provide a visual representation of this container (see :sip:ref:`~PyQt6.QtWidgets.QGroupBox` for a container widget), but instead manages the states of each of the buttons in the group.

An :sip:ref:`~PyQt6.QtWidgets.QButtonGroup.exclusive` button group switches off all checkable (toggle) buttons except the one that has been clicked. By default, a button group is exclusive. The buttons in a button group are usually checkable :sip:ref:`~PyQt6.QtWidgets.QPushButton`\ s, :sip:ref:`~PyQt6.QtWidgets.QCheckBox`\ es (normally for non-exclusive button groups), or :sip:ref:`~PyQt6.QtWidgets.QRadioButton`\ s. If you create an exclusive button group, you should ensure that one of the buttons in the group is initially checked; otherwise, the group will initially be in a state where no buttons are checked.

A button can be added to the group with :sip:ref:`~PyQt6.QtWidgets.QButtonGroup.addButton` and removed with :sip:ref:`~PyQt6.QtWidgets.QButtonGroup.removeButton`. If the group is exclusive, the currently checked button is available with :sip:ref:`~PyQt6.QtWidgets.QButtonGroup.checkedButton`. If a button is clicked, the :sip:ref:`~PyQt6.QtWidgets.QButtonGroup.buttonClicked` signal is emitted; for a checkable button in an exclusive group this means that the button has been checked. The list of buttons in the group is returned by :sip:ref:`~PyQt6.QtWidgets.QButtonGroup.buttons`.

In addition, :sip:ref:`~PyQt6.QtWidgets.QButtonGroup` can map between integers and buttons. You can assign an integer id to a button with :sip:ref:`~PyQt6.QtWidgets.QButtonGroup.setId`, and retrieve it with :sip:ref:`~PyQt6.QtWidgets.QButtonGroup.id`. The id of the currently checked button is available with :sip:ref:`~PyQt6.QtWidgets.QButtonGroup.checkedId`, and there is an overloaded signal :sip:ref:`~PyQt6.QtWidgets.QButtonGroup.buttonClicked` which emits the id of the button. The id ``-1`` is reserved by :sip:ref:`~PyQt6.QtWidgets.QButtonGroup` to mean "no such button". The purpose of the mapping mechanism is to simplify the representation of enum values in a user interface.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QGroupBox`, :sip:ref:`~PyQt6.QtWidgets.QPushButton`, :sip:ref:`~PyQt6.QtWidgets.QCheckBox`, :sip:ref:`~PyQt6.QtWidgets.QRadioButton`.
