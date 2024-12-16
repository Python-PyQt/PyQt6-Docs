.. sip:class-description::
    :status: todo
    :brief: Access to index and search documentation
    :digest: 71bd168b57e8f7057b25e84ded2aad11

The :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngineCore` class provides access to index and search documentation.

Before the search engine can be used, one has to instantiate at least a :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore` object that needs to be passed to the search engines constructor. This is required as the search engine needs to be connected to the help engines setupFinished() signal to know when it can start to index documentation.

After starting the indexing process the signal :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngineCore.indexingStarted` is emitted and on the end of the indexing process the :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngineCore.indexingFinished` is emitted. To stop the indexing one can call :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngineCore.cancelIndexing`.

When the indexing process has finished, the search engine can be used to search through the index for a given term using the :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngineCore.search` function. When the search input is passed to the search engine, the :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngineCore.searchingStarted` signal is emitted. When the search finishes, the :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngineCore.searchingFinished` signal is emitted. The search process can be stopped by calling :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngineCore.cancelSearching`.

If the search succeeds, :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngineCore.searchingFinished` is called with the search result count to fetch the search results from the search engine. Calling the :sip:ref:`~PyQt6.QtHelp.QHelpSearchEngineCore.searchResults` function with a range returns a list of :sip:ref:`~PyQt6.QtHelp.QHelpSearchResult` objects within the range. The results consist of the document title and URL, as well as a snippet from the document that contains the best match for the search input.
