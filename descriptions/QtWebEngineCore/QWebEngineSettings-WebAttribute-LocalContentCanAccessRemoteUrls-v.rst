.. sip:enum-member-description::
    :status: todo
    :value: 6
    :digest: 186df561f7446013192c46eb4571b33f

Allows locally loaded documents to ignore cross-origin rules so that they can access remote resources that would normally be blocked, because all remote resources are considered cross-origin for a local file. Remote access that would not be blocked by cross-origin rules is still possible when this setting is disabled (default). Note that disabling this setting does not stop XMLHttpRequests or media elements in local files from accessing remote content. Basically, it only stops some HTML subresources, such as scripts, and therefore disabling this setting is not a safety mechanism.
