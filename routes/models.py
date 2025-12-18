from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError


class Airport(models.Model):
    code = models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            'unique': 'Airport code already exists.'
        }
    )

    def __str__(self):
        return self.code



class AirportRoute(models.Model):
    """
    Represents a route from one airport to another
    (Binary Tree: Left / Right)
    """

    POSITION_CHOICES = (
        ('left', 'Left'),
        ('right', 'Right'),
    )

    parent_airport = models.ForeignKey(
        Airport,
        related_name='child_routes',
        on_delete=models.CASCADE
    )
    child_airport = models.ForeignKey(
        Airport,
        related_name='parent_routes',
        on_delete=models.CASCADE
    )
    position = models.CharField(max_length=5, choices=POSITION_CHOICES)
    duration = models.PositiveIntegerField(help_text="Duration (KM or Minutes)")

    class Meta:
        unique_together = ('parent_airport', 'position')

    def __str__(self):
        return f"{self.parent_airport} -> {self.child_airport} ({self.position})"
    def clean(self):
        # Parent and child cannot be same
        if self.parent_airport == self.child_airport:
            raise ValidationError(
                "Parent airport and child airport cannot be the same."
            )

        # Duration must be greater than 0
        if self.duration <= 0:
            raise ValidationError(
                "Duration must be greater than zero."
            )
