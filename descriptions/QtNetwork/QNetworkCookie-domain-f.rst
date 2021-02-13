.. sip:method-description::
    :status: todo
    :pysig: 341be97d9aff90c9978347f66f945b77
    :realsig: () const
    :digest: eec2527509eff96914a989f443cbe2da

Returns the domain this cookie is associated with. This corresponds to the "domain" field of the cookie string.

Note that the domain here may start with a dot, which is not a valid hostname. However, it means this cookie matches all hostnames ending with that domain name.

.. seealso:: :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.setDomain`.
