.. sip:enum-description::
    :status: todo
    :realname: QDir::SortFlag
    :digest: 3359c9abb40670cccd7ea765dffcfc2c

This enum describes the sort options available to :sip:ref:`~PyQt6.QtCore.QDir`, e.g. for :sip:ref:`~PyQt6.QtCore.QDir.entryList` and :sip:ref:`~PyQt6.QtCore.QDir.entryInfoList`. The sort value is specified by OR-ing together values from the following list:

You can only specify one of the first four.

If you specify both  and Reversed, directories are still put first, but in reverse order; the files will be listed after the directories, again in reverse order.
