.. sip:enum-member-description::
    :status: todo
    :value: 0x02
    :realname: QEventLoop::ProcessEventsFlag::ExcludeSocketNotifiers
    :digest: 0baa95f1abeb87143cd477c9120b3764

Do not process socket notifier events. Note that the events are not discarded; they will be delivered the next time :sip:ref:`~PyQt6.QtCore.QEventLoop.processEvents` is called without the  flag.
