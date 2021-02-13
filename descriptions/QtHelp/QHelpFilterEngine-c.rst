.. sip:class-description::
    :status: todo
    :brief: Filtered view of the help contents
    :digest: bb96693ef8b2df2339d29c3749077633

The :sip:ref:`~PyQt6.QtHelp.QHelpFilterEngine` class provides a filtered view of the help contents.

The filter engine allows the management of filters associated with a :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore` instance. The help engine internally creates an instance of the filter engine, which can be accessed by calling :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.filterEngine`. Therefore, the public constructor of this class is disabled.

The filters are identified by a filter name string. Filter details are described by the :sip:ref:`~PyQt6.QtHelp.QHelpFilterData` class.

The filter engine allows for adding new filters and changing the existing filters' data through the :sip:ref:`~PyQt6.QtHelp.QHelpFilterEngine.setFilterData` method. An existing filter can be removed through the :sip:ref:`~PyQt6.QtHelp.QHelpFilterEngine.removeFilter` method.

Out of the registered filters one can be marked as the active one. The active filter will be used by the associated help engine for returning filtered results of many different functions, such as content, index, or search results. If no filter is marked active, the help engine returns the full results list available.

The active filter is returned by :sip:ref:`~PyQt6.QtHelp.QHelpFilterEngine.activeFilter` and it can be changed by :sip:ref:`~PyQt6.QtHelp.QHelpFilterEngine.setActiveFilter`.

.. seealso:: :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore`.
