.. sip:method-description::
    :status: todo
    :pysig: 4093631cab0089e862b519097f2305e3
    :realsig: (int,QWidget*)
    :digest: 16be12d586a929a4e01924dc3c299c19

Inserts the *widget* specified into the splitter's layout at the given *index*.

If *widget* is already in the splitter, it will be moved to the new position.

If *index* is an invalid index, then the widget will be inserted at the end.

**Note:** The splitter takes ownership of the widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.addWidget`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.indexOf`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.widget`.
