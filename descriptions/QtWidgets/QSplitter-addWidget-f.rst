.. sip:method-description::
    :status: todo
    :pysig: 3d87b361e46af7a9d071f2e3463bbc7a
    :realsig: (QWidget*)
    :digest: cd7a201b5af90361d22d5621f261db96

Adds the given *widget* to the splitter's layout after all the other items.

If *widget* is already in the splitter, it will be moved to the new position.

**Note:** The splitter takes ownership of the widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.insertWidget`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.widget`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.indexOf`.
