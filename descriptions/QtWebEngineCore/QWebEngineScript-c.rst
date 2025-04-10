.. sip:class-description::
    :status: todo
    :brief: Encapsulates a JavaScript program
    :digest: 1e232e772968c8ba259120ad4adfe496

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineScript` class encapsulates a JavaScript program.

:sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineScript` enables the programmatic injection of so called *user scripts* in the JavaScript engine at different points, determined by :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineScript.injectionPoint`, during the loading of web contents.

Scripts can be executed either in the main JavaScript *world*, along with the rest of the JavaScript coming from the web contents, or in their own isolated world. While the DOM of the page can be accessed from any world, JavaScript variables of a function defined in one world are not accessible from a different one. :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineScript.ScriptWorldId.ScriptWorldId` provides some predefined IDs for this purpose.

The following `Greasemonkey <https://doc.qt.io/qt-6/https://wiki.greasespot.net/Metadata_Block>`_ attributes are supported since Qt 5.8: ``@exclude``, ``@include``, ``@name``, ``@match``, and ``@run-at``.

Use QWebEnginePage::scripts() and QWebEngineProfile::scripts() to access the collection of scripts associated with a single page or a number of pages sharing the same profile.

.. seealso:: `Script Injection <https://doc.qt.io/qt-6/qtwebengine-overview.html#script-injection>`_.
