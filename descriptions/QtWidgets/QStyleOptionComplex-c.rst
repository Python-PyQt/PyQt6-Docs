.. sip:class-description::
    :status: todo
    :brief: Used to hold parameters that are common to all complex controls
    :digest: 6dcb56cfab1ccf3fe98dc827252d5031

The :sip:ref:`~PyQt6.QtWidgets.QStyleOptionComplex` class is used to hold parameters that are common to all complex controls.

This class is not used on its own. Instead it is used to derive other complex control options, for example :sip:ref:`~PyQt6.QtWidgets.QStyleOptionSlider` and :sip:ref:`~PyQt6.QtWidgets.QStyleOptionSpinBox`.

For performance reasons, there are few member functions and the access to the member variables is direct (i.e., using the ``.`` or ``->`` operator). This makes the structures straightforward to use and emphasizes that these are simply parameters used by the style functions.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QStyleOption`.
