.. sip:class-description::
    :status: done
    :brief: Encapsulate a Python object as a sequence range

:sip:ref:`~PyQt6.QtCore.QPySequenceRange` encapsulates a Python object that
implements a sequence range so that it can be used by
:sip:ref:`~PyQt6.QtCore.QRangeModel`.  A :sip:ref:`~PyQt6.QtCore.QRangeModel`
instance can then be passed to an appropriate Qt view (usually
:sip:ref:`~PyQt6.QtWidgets.QListView`) for the underlying Python object to be
displayed or edited.
