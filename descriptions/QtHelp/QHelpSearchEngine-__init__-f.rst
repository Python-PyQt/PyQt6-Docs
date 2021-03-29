.. sip:method-description::
    :status: todo
    :pysig: af0a14db1cc6ee10081e3cfbac0a34ae
    :realsig: (QHelpEngineCore*,QObject*)
    :digest: 7e61f57d35c802563055063ac74d72e9

Constructs a new search engine with the given *parent*. The search engine uses the given *helpEngine* to access the documentation that needs to be indexed. The :sip:ref:`~PyQt6.QtHelp.QHelpEngine`'s setupFinished() signal is automatically connected to the :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngine`'s indexing function, so that new documentation will be indexed after the signal is emitted.
