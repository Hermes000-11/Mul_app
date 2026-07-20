import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
    # Method which is called when consumer establish websocket connection
    # async is pointing that this fucntion is a coroutine(a function which can pause and start again while remaining all info)
        
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # self.scope is a dictionary which contains info about current websocket connection(like request in Django)
        # url_route, kwargs, room_name are infos which we want to have an access to
        
        self.group_name = f'room_{self.room_name}'
        # groups are used in channels layers for communication between two different websocket connections(users)
        # the 'room_' is pointing to  an exact purpose of the group

        await self.channel_layer.group_add(
            self.group_name, self.channel_name
        )
        # 'self.channel_layer' is an object which gives us an access to the system of the groups and channels('redis' in our case)
        # group_add adds current channel to a group
        # await is waiting for function finishing, when it is finished, 
        # if we have await in our async function, the async function wont proceed with executing while await is not done
        
        await self.accept()
        # self.accept is confirming a websocket connection, Warning! without it the connection will be closed
        # after this accept method, consumer will be able to send and reveive messages

    async def disconnect(self, close_code):
        # disconnect method is called automaticaly when websocket connection is closed(for example user close the window or quit the app)
        # 'close_code' is showing us the reason why connection was closed(like 404, or 1000 for normal disconnection)
        
        await self.channel_layer.group_discard(
            self.group_name, self.channel_name
        )
        # the same as group_add function but for removing the channels from the group

    
    async def receive(self, text_data):
        # receive function is called when consumer is sending the message
        # text_data usually a JSON string with info about the data sended by user 
        
        data = json.loads(text_data)
        # json.loads method is turning a JSON string into python dictionary
        # we need it cause websocket is able to process only strings and bytes
        
        message = data['message']
        # data['message'] takes the value from the dictionary with 'message' key

        await self.channel_layer.group_send(
            # group_send method sends the message to channels in group
            self.group_name,
            {
                'type': 'chat_message',
                'message': message,
            }
            # first arg - a group name, second arg - dictionary with the data,
            
            # 'type' is telling us which function will be called in consumers.py(this file)
            # the '_' is replaced with dot, chat.message = chat_message

            # 'message' the text which we received from our dictionary
        )
    async def chat_message(self, event):
        # this method is called automatically when group receive a message('type': 'chat.message')
        # 'event' is dictionary which we used in group_send
        
        await self.send(text_data=json.dumps({
            # self.send is sending the message back to this exact user(who called this method)
            # text_data=json.dumps turn python dictionary back to JSON to let websocket process it
            'message': event['message'], 
            # a message which user will receive
        }))
        