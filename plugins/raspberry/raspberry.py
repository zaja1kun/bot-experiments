'''Module contains commands for Raspberry Pi device control.'''
from errbot import BotPlugin, botcmd


class RaspberryStatus(BotPlugin):
    '''Raspberry device connected commands.'''

    @botcmd
    def echo(self, msg, args):
        '''Echo command.'''
        self.send(msg.frm, args)
        return '/echo command finished.'

    @botcmd
    def card(self, msg, _):
        '''Card command.'''
        card_params = {
            'body': 'body',
            'to': msg.frm,
            'summary': 'summary',
            'title': 'title',
            'image': 'https://getuikit.com/v2/docs/images/placeholder_600x400.svg',
        }
        self.send_card(**card_params)

    @botcmd
    def poll(self, msg, _):
        '''Poll command.'''
        self.start_poller(interval=1, method=self.send, times=3, args=(msg.frm, '*poll*'))
