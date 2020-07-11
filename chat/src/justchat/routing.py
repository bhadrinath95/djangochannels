"""
A Channels routing configuration is similar to a Django URLconf
It tells Channels what code to run when an HTTP request is received by the Channels server.
"""

from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    # (http->django views is added by default)
})