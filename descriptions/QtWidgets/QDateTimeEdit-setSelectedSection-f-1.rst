.. sip:method-description::
    :status: todo
    :pysig: e42cf3ed58fd9515976e3e43bf0a7379
    :realsig: (QDateTimeEdit::Section)
    :digest: 90458faca5f90fa562b18d6b59d81970

Selects *section*. If *section* doesn't exist in the currently displayed sections, this function does nothing. If *section* is :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.Section.NoSection`, this function will unselect all text in the editor. Otherwise, this function will move the cursor and the current section to the selected section.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.currentSection`.
