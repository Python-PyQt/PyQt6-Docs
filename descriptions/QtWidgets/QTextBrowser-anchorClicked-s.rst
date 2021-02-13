.. sip:signal-description::
    :status: todo
    :pysig: 46a7bdf6ff0ff3a292573662f7d8a6a2
    :realsig: (const QUrl&)
    :digest: 54bada82723511358bd3032ddccaf9e3

This signal is emitted when the user clicks an anchor. The URL referred to by the anchor is passed in *link*.

Note that the browser will automatically handle navigation to the location specified by *link* unless the :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.openLinks` property is set to false or you call :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.setSource` in a slot connected. This mechanism is used to override the default navigation features of the browser.
