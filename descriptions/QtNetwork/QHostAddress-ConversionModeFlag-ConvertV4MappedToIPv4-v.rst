.. sip:enum-member-description::
    :status: todo
    :value: 1
    :digest: 7aba53596ebd9261d36f238b1745c70c

Convert IPv4-mapped IPv6 addresses (RFC 4291 sect. 2.5.5.2) when comparing. Therefore :sip:ref:`~PyQt6.QtNetwork.QHostAddress`\ ("::ffff:192.168.1.1") will compare equal to :sip:ref:`~PyQt6.QtNetwork.QHostAddress`\ ("192.168.1.1").
