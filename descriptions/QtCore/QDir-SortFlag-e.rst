.. sip:enum-description::
    :status: todo
    :digest: 0c426702650045154ebddadc8cda30c7

This enum describes the sort options available to :sip:ref:`~PyQt6.QtCore.QDir`, e.g. for :sip:ref:`~PyQt6.QtCore.QDir.entryList` and :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList`. The sort value is specified by OR-ing together values from the following list:

You can only specify one of the first four.

If you specify both DirsFirst and Reversed, directories are still put first, but in reverse order; the files will be listed after the directories, again in reverse order.
