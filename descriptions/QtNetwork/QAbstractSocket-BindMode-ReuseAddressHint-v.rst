.. sip:enum-member-description::
    :status: todo
    :value: 0x4
    :realname: QAbstractSocket::BindFlag::ReuseAddressHint
    :digest: 044bc7da57cbafc9302bb323415df235

Provides a hint to :sip:ref:`~PyQt6.QtNetwork.QAbstractSocket` that it should try to rebind the service even if the address and port are already bound by another socket. On Windows and Unix, this is equivalent to the SO_REUSEADDR socket option.
