.. sip:class-description::
    :status: todo
    :brief: Access to widgets reusable to integrate fulltext search as well as to index and search documentation
    :digest: e54a0e2039c12391f39cd1b4551cad16

The :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngine` class provides access to widgets reusable to integrate fulltext search as well as to index and search documentation.

Before the search engine can be used, one has to instantiate at least a :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore` object that needs to be passed to the search engines constructor. This is required as the search engine needs to be connected to the help engines setupFinished() signal to know when it can start to index documentation.

After starting the indexing process the signal :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngine.indexingStarted` is emitted and on the end of the indexing process the :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngine.indexingFinished` is emitted. To stop the indexing one can call :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngine.cancelIndexing`.

When the indexing process has finished, the search engine can be used to search through the index for a given term using the search() function. When the search input is passed to the search engine, the :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngine.searchingStarted` signal is emitted. When the search finishes, the :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngine.searchingFinished` signal is emitted. The search process can be stopped by calling :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngine.cancelSearching`.

If the search succeeds, :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngine.searchingFinished` is called with the search result count to fetch the search results from the search engine. Calling the :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngine.searchResults` function with a range returns a list of :sip:ref:`~PyQt6.QtHelp.QHelpSearchResult` objects within the range. The results consist of the document title and URL, as well as a snippet from the document that contains the best match for the search input.

To display the given search results use the :sip:ref:`~PyQt6.QtHelp.QHelpSearchResultWidget` or build up your own one if you need more advanced functionality. Note that the :sip:ref:`~PyQt6.QtHelp.QHelpSearchResultWidget` can not be instantiated directly, you must retrieve the widget from the search engine in use as all connections will be established for you by the widget itself.
