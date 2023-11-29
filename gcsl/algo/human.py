import keyboard
import time

class HumanExpert(object):

    def __init__(self) -> None:
        self.human_action = None
        self.mode = 0
    
    def get_key_state(self, key):
        try:
            # Check if the key is pressed
            return keyboard.is_pressed(key)
        except AttributeError:
            # Handle special keys
            return False
    
    def get_action(self, action):
        human_action = None
        if self.get_key_state('down') and self.get_key_state('left'):
            human_action = 0
        elif self.get_key_state('down'):
            human_action = 1
        elif self.get_key_state('down') and self.get_key_state('right'):
            human_action = 2
        elif self.get_key_state('left'):
            human_action = 3
        elif self.get_key_state('right'):
            human_action = 5
        elif self.get_key_state('up') and self.get_key_state('left'):
            human_action = 6
        elif self.get_key_state('up'):
            human_action = 7
        elif self.get_key_state('up') and self.get_key_state('right'):
            human_action = 8
        
        if human_action is not None:
            return human_action
        return action

# if __name__ == "__main__":
#     policy = HumanExpert()

#     while True:
#         print(policy.get_action(-1))
#         time.sleep(0.1)
