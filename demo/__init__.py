
from otree.api import *
c = cu

doc = ''

class C(BaseConstants):
    NAME_IN_URL = 'cal_score_now'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    q1 = models.IntegerField(
        choices=[1,2,3,4,5], 
        label='Question 1', widget=widgets.RadioSelectHorizontal)
    q2 = models.IntegerField(
        choices=[1,2,3,4,5],                
        label='Question 2', 
        widget=widgets.RadioSelectHorizontal)

class calculate(Page):
    form_model = 'player'
    form_fields = ['q1', 'q2',]

page_sequence = [calculate]
