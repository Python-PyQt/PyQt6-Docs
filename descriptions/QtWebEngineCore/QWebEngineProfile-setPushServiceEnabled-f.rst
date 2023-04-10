.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: (bool)
    :digest: b51d28d39f4105e34e7e644f1e572d27

Enables the push messaging service if *enable* is ``true``, otherwise disables it.

**Note:** Qt WebEngine uses `Firebase Cloud Messaging (FCM) <https://firebase.google.com>`_ as a browser push service. Therefore, all push messages will go through the Google push service and its respective servers.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.isPushServiceEnabled`.
