.. sip:class-description::
    :status: todo
    :brief: Rich text browser with hypertext navigation
    :digest: 85058070013d4880c5f81296be5bc983

The :sip:ref:`~PyQt6.QtWidgets.QTextBrowser` class provides a rich text browser with hypertext navigation.

This class extends :sip:ref:`~PyQt6.QtWidgets.QTextEdit` (in read-only mode), adding some navigation functionality so that users can follow links in hypertext documents.

If you want to provide your users with an editable rich text editor, use :sip:ref:`~PyQt6.QtWidgets.QTextEdit`. If you want a text browser without hypertext navigation use :sip:ref:`~PyQt6.QtWidgets.QTextEdit`, and use :sip:ref:`~PyQt6.QtWidgets.QTextEdit.setReadOnly` to disable editing. If you just need to display a small piece of rich text use :sip:ref:`~PyQt6.QtWidgets.QLabel`.

.. _qtextbrowser-document-source-and-contents:

Document Source and Contents
----------------------------

The contents of :sip:ref:`~PyQt6.QtWidgets.QTextEdit` are set with setHtml() or setPlainText(), but :sip:ref:`~PyQt6.QtWidgets.QTextBrowser` also implements the :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.setSource` function, making it possible to use a named document as the source text. The name is looked up in a list of search paths and in the directory of the current document factory.

If a document name ends with an anchor (for example, "``#anchor"``), the text browser automatically scrolls to that position (using scrollToAnchor()). When the user clicks on a hyperlink, the browser will call :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.setSource` itself with the link's ``href`` value as argument. You can track the current source by connecting to the :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.sourceChanged` signal.

.. _qtextbrowser-navigation:

Navigation
----------

:sip:ref:`~PyQt6.QtWidgets.QTextBrowser` provides :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.backward` and :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.forward` slots which you can use to implement Back and Forward buttons. The :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.home` slot sets the text to the very first document displayed. The :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.anchorClicked` signal is emitted when the user clicks an anchor. To override the default navigation behavior of the browser, call the :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.setSource` function to supply new document text in a slot connected to this signal.

If you want to load documents stored in the Qt resource system use ``qrc`` as the scheme in the URL to load. For example, for the document resource path ``:/docs/index.html`` use ``qrc:/docs/index.html`` as the URL with :sip:ref:`~PyQt6.QtWidgets.QTextBrowser.setSource`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTextEdit`, :sip:ref:`~PyQt6.QtGui.QTextDocument`.
