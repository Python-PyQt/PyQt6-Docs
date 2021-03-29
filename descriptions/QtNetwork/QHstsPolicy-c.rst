.. sip:class-description::
    :status: todo
    :brief: Specifies that a host supports HTTP Strict Transport Security policy (HSTS)
    :digest: 749ce11474fc7e8fde48f9156e7edf82

The :sip:ref:`~PyQt6.QtNetwork.QHstsPolicy` class specifies that a host supports HTTP Strict Transport Security policy (HSTS).

HSTS policy defines a period of time during which :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` should only access a host in a secure fashion. HSTS policy is defined by RFC6797.

You can set expiry time and host name for this policy, and control whether it applies to subdomains, either in the constructor or by calling :sip:ref:`~PyQt6.QtNetwork.QHstsPolicy.setExpiry`, :sip:ref:`~PyQt6.QtNetwork.QHstsPolicy.setHost` and setIncludesSubdomains().

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setStrictTransportSecurityEnabled`.
