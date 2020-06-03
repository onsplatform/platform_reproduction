import json

from settings import *
from platform_sdk.queue import ProcessQueue
from platform_sdk.domain.schema.api import SchemaApi
from platform_sdk.event_manager import EventManager


class ReproductionExecutor:

    def __init__(self, schema, event_manager, solution, settings):
        self.solution = solution
        self.settings = settings
        self.schema = schema
        self.event_manager = event_manager
        self.reproduction_check = ProcessQueue(reproduction_queue, solution, settings)
        self.reproduction_exec = ProcessQueue(reproduction_queue, solution, settings)

    def reproduce(self, solution):
        import pdb;pdb.set_trace()
        method_frame, header_frame, body = self.reproduction_check.check_next_message()
        if body:
            print(" [ ] Can it reproduce? %r" % body)
            event = json.loads(body)
            if not self.schema.is_reproducing(solution['id']):
                self.reproduction_check.close()
                method_frame, header_frame, body = self.reproduction_exec.dequeue()
                event = json.loads(body)
                self.event_manager.send_event(event['event'])
                print(" [x] Reproducing %r" % event)
        else:
            print('Nothing to do...')


schema = SchemaApi(SCHEMA)
event_manager = EventManager(EVENT_MANAGER)
print(f'Checking solutions...')
solutions = schema.get_solutions()
print(f'Solutions: {solutions}')
for solution in solutions:
    print(f'Checking reproduction to: {solution}')
    executor = ReproductionExecutor(schema, event_manager, solution['name'], PROCESS_SETTINGS)
    executor.reproduce(solution)
