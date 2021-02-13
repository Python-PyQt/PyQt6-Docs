.. sip:method-description::
    :status: todo
    :pysig: 45c0a44fbe3abfe6ad732b8f51127c80
    :realsig: (QTime,QTime)
    :digest: 44d57c5d442a3bea98c3dd627d27bbeb

Set the range of allowed times for the date time edit.

This convenience function sets the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumTime` and :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumTime` properties.

Note that these only constrain the date time edit's value on, respectively, the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumDate` and :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumDate`. When these date properties do not coincide, times after *max* are allowed on dates before :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumDate` and times before *min* are allowed on dates after :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumDate`.

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qdatetimeedit.py
    :lines: 84-84

is analogous to:

.. literalinclude:: ../../../snippets/qtbase-src-widgets-doc-snippets-code-src_gui_widgets_qdatetimeedit.py
    :lines: 89-90

If either *min* or *max* is invalid, this function does nothing. This function preserves the :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumDate` and :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumDate` properties. If those properties coincide and *max* is less than *min*, *min* is used as *max*.

If the range is narrower then a time interval whose end it spans, for example the interval from ten to an hour to ten past the same hour, users can only edit the time to one in the later part of the range if keyboard-tracking is disabled.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.minimumTime`, :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.maximumTime`, :sip:ref:`~PyQt6.QtWidgets.QDateTimeEdit.setDateTimeRange`, :sip:ref:`~PyQt6.QtCore.QTime.isValid`, :ref:`qdatetimeedit-keyboard-tracking`.
