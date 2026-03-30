.. sip:method-description::
    :status: todo
    :pysig: 5be56581c2039583bba24d26602fd599
    :realsig: (const QString&) const
    :digest: c422503168662fc0bd5281391b0c8840

Returns a sorted list of available indices, filtered by *filterName*. The returned list contents depend on the passed filter, and therefore only the indices registered for this filter will be returned. If you want to get all available indices unfiltered, pass empty string as *filterName*.
