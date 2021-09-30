.. sip:class-description::
    :status: todo
    :brief: Represents a custom URL request
    :digest: 794c257bb3c7c6ee7ab6a51e56185934

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob` class represents a custom URL request.

A :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob` is given to :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlSchemeHandler.requestStarted` and must be handled by the derived implementations of the class. The job can be handled by calling either :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.reply`, :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.redirect`, or :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineUrlRequestJob.fail`.

The class is owned by the web engine and does not need to be deleted. However, the web engine may delete the job when it is no longer needed, and therefore the signal :sip:ref:`~PyQt6.QtCore.QObject.destroyed` must be monitored if a pointer to the object is stored.
