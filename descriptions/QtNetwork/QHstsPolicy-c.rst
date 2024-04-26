.. sip:class-description::
    :status: todo
    :brief: Specifies that a host supports HTTP Strict Transport Security policy (HSTS)
    :digest: 08068e364890e3368856d4a7f4aa9eb0

The :sip:ref:`~PyQt6.QtNetwork.QHstsPolicy` class specifies that a host supports HTTP Strict Transport Security policy (HSTS).

HSTS policy defines a period of time during which :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager` should only access a host in a secure fashion. HSTS policy is defined by RFC6797.

You can set expiry time and host name for this policy, and control whether it applies to subdomains, either in the constructor or by calling :sip:ref:`~PyQt6.QtNetwork.QHstsPolicy.setExpiry`, :sip:ref:`~PyQt6.QtNetwork.QHstsPolicy.setHost` and :sip:ref:`~PyQt6.QtNetwork.QHstsPolicy.setIncludesSubDomains`.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkAccessManager.setStrictTransportSecurityEnabled`.
