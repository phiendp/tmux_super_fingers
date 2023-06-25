import os
from .action import Action
from ..targets.target_payload import EditorOpenable


class SendToVsCodeAction(Action):
    def __init__(self, target_payload: EditorOpenable):
        self.target_payload = target_payload

    def perform(self):
        path = self.target_payload.file_path

        if self.target_payload.line_number:
            path += f':{self.target_payload.line_number}'

        os.system(f'code -g {path}')
