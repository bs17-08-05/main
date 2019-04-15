from channels.routing import ProtocolTypeRouter
import core.routing

application = ProtocolTypeRouter({
    'websocket': core.routing.channel_routing,
})