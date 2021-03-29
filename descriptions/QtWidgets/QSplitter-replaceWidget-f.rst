.. sip:method-description::
    :status: todo
    :pysig: 86852f587188911de9b839ef12320e46
    :realsig: (int,QWidget*)
    :digest: 5eaaebc5775fc088ebe51ac58de8a04d

Replaces the widget in the splitter's layout at the given *index* by *widget*.

Returns the widget that has just been replaced if *index* is valid and *widget* is not already a child of the splitter. Otherwise, it returns null and no replacement or addition is made.

The geometry of the newly inserted widget will be the same as the widget it replaces. Its visible and collapsed states are also inherited.

**Note:** The splitter takes ownership of *widget* and sets the parent of the replaced widget to null.

**Note:** Because *widget* gets :sip:ref:`~PyQt6.QtWidgets.QWidget.setParent` into the splitter, its :sip:ref:`~PyQt6.QtWidgets.QWidget.geometry` may not be set right away, but only after *widget* will receive the appropriate events.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.insertWidget`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.indexOf`.
