.. sip:class-description::
    :status: todo
    :brief: Object to store the settings used by QWebEnginePage
    :digest: 56386a070f7f079965022c0af5d870cc

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineSettings` class provides an object to store the settings used by :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage`.

:sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineSettings` allows configuration of browser properties, such as font sizes and families, and generic attributes, such as JavaScript support. Individual attributes are set using the setAttribute() function. The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineSettings.WebAttribute` enum further describes each attribute.

Each :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage` object has its own :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineSettings` object, which configures the settings for that page. If a setting is not configured for a web engine page, it is looked up in the settings of the profile the page belongs to.

.. seealso:: QWebEnginePage::settings()QWebEngineView::settings().
