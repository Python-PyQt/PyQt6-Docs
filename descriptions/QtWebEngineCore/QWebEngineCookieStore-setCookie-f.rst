.. sip:method-description::
    :status: todo
    :pysig: 803f2f04c2fef6303cb714d29f977625
    :realsig: (const QNetworkCookie&,const QUrl&)
    :digest: b828b588a452d0ec2f58bcfc8f199f9e

Adds *cookie* to the cookie store.

**Note:** If *cookie* specifies a :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.domain` that does not start with a dot, a dot is automatically prepended. To limit the cookie to the exact server, omit :sip:ref:`~PyQt6.QtNetwork.QNetworkCookie.domain` and set *origin* instead.

The provided URL should also include the scheme.

**Note:** This operation is asynchronous.
