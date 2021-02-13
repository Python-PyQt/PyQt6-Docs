.. sip:enum-member-description::
    :status: todo
    :value: 8
    :realname: QHostAddress::ConversionModeFlag::ConvertLocalHost
    :digest: bcdb77db6d6a229e996a1f41ed5d6e9d

Convert the IPv6 loopback addresses to its IPv4 equivalent when comparing. Therefore e.g. :sip:ref:`~PyQt6.QtNetwork.QHostAddress`\ ("::1") will compare equal to :sip:ref:`~PyQt6.QtNetwork.QHostAddress`\ ("127.0.0.1").
