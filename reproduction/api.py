from flask import Blueprint, request, make_response
from reproduction.settings import PROCESS_SETTINGS, reproduction_queue
from platform_sdk.queue import ProcessQueue


def construct_blueprint(process_memory_api):
    reproduction_blueprint = Blueprint('reproduction', __name__, url_prefix='/reproduction')

    @reproduction_blueprint.route('/execute', methods=['POST'])
    def execute():
        reproduction_id = request.json['reproductionId']
        instances = request.json['instancesIds']
        solution = request.json['solution']
        process_queue = ProcessQueue(reproduction_queue, solution, PROCESS_SETTINGS)
        for instance in instances:
            event = process_memory_api.get_event(instance)
            event['scope'] = 'reproduction'
            event['reproduction'] = {
                'instanceId': instance,
                'reproduction_id': reproduction_id
            }
            process_queue.enqueue(reproduction_id, {
                'solution': solution,
                'event': event
            })

        return make_response('', 200)

    return reproduction_blueprint
