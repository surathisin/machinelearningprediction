from django.db import models
from boards.models import Board


class Topic(models.Model):
    # your other fields...
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    # In boards.Topic model
    board = models.ForeignKey(Board, related_name='boards_topics', on_delete=models.CASCADE)

# In accounts.Topic model (assuming you have a similar setup)
    board = models.ForeignKey(Board, related_name='accounts_topics', on_delete=models.CASCADE)

