.. sip:method-description::
    :status: todo
    :pysig: 979133a6ad75e1e466b96dcf38cc04b4
    :realsig: (const QString&,const QString&) const
    :digest: 0af59e36fdc512f27842762fa06c9486

Returns a list of the document links found for the *id*, filtered by *filterName*. The returned list contents depend on the passed filter, and therefore only the keywords registered for this filter will be returned. If you want to get all results unfiltered, pass empty string as *filterName*.
