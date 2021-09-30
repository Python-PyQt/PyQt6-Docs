.. sip:class-description::
    :status: todo
    :brief: Encapsulates the result of a string search on a page
    :digest: b26b0e8747bd7ddddeeb69be76886ad1

The :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFindTextResult` class encapsulates the result of a string search on a page.

The string search can be initiated by the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.findText` or WebEngineView.findText() method. The results of the search are highlighted in the view. The details of this result are passed as a :sip:ref:`~PyQt6.QtWebEngineCore.QWebEngineFindTextResult` object that can be used to show a status message, such as "2 of 2 matches". For example:

::

    QObject::connect(view.page(), &QWebEnginePage::findTextFinished, [](const QWebEngineFindTextResult &result) {
        qInfo() << result.activeMatch() << "of" << result.numberOfMatches() << "matches";
    });

Results are passed to the user in the :sip:ref:`~PyQt6.QtWebEngineCore.QWebEnginePage.findTextFinished` and WebEngineView.findTextFinished() signals.
