.. sip:method-description::
    :status: todo
    :pysig: 979133a6ad75e1e466b96dcf38cc04b4
    :realsig: (const QString&,const QString&) const
    :digest: 928a7ebd7d1753b906e231209db1acf6

Returns a list of the document links found for the *keyword*, filtered by *filterName*. The returned list contents depend on the passed filter, and therefore only the keywords registered for this filter will be returned. If you want to get all results unfiltered, pass empty string as *filterName*.
