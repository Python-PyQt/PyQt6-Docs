.. sip:method-description::
    :status: todo
    :pysig: 0281bb2a03f8f3624f862e1826a39fe8
    :realsig: (QObject*)
    :digest: 2db6cbe751c4ce9aee6c9c3c278050eb

Constructs a new off-the-record profile with the parent *parent*.

An off-the-record profile leaves no record on the local machine, and has no persistent data or cache. Thus, the HTTP cache can only be in memory and the cookies can only be non-persistent. Trying to change these settings will have no effect.

.. seealso:: :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineProfile.isOffTheRecord`.
