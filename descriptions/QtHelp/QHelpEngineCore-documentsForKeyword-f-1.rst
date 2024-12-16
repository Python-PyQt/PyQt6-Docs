.. sip:method-description::
    :status: todo
    :pysig: e642e1005c1d89b5747431d0b4689ff2
    :realsig: (const QString&, const QString&) const
    :digest: 928a7ebd7d1753b906e231209db1acf6

Returns a list of the document links found for the *keyword*, filtered by *filterName*. The returned list contents depend on the passed filter, and therefore only the keywords registered for this filter will be returned. If you want to get all results unfiltered, pass empty string as *filterName*.
