.. sip:enum-member-description::
    :status: todo
    :value: 0x01
    :digest: b73fab6edc20f47d4c076e0ec97b29d7

Do not process user input events, such as ButtonPress and KeyPress. Note that the events are not discarded; they will be delivered the next time :sip:ref:`~PyQt6.QtCore.QEventLoop.processEvents` is called without the  flag.
